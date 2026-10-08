#!/usr/bin/env python3
"""
record_stage_result.py — owns the write-back for the single most load-bearing
field in this whole system: a stage's pass/fail result and, on a genuine
pass, `current_stage` advancement.

**Why this exists (v1.11.0).** Every stage's `stages/<stage_id>/test.md` —
generated from `_template/stages/S1/test.md` and, before this version,
identical in every one of 1253 stage files across all 62 courses — told the
model to "Record `passed` or `not_passed`... into this course's micro-
profile." But `syllabus_status` has only ever meant `"pass"` / `"fail"` /
`"unsat"` / `"withheld"` — every script that reads it (`cohort_status.py`,
`gate_check.py`, `apply_capabilities.py`, `coverage_check.py`,
`resume_enrollment.py`) checks the literal string `"pass"`, and
`course-runner.md` itself has always said `"pass"`/`"fail"`, never
`"passed"`/`"not_passed"`. No script ever wrote `syllabus_status` or
`current_stage` at all — both were, like `confidence` and review-card
fields before v1.10.0, hand-write-back fields the calling skill was merely
told in prose to set correctly. This is the exact same failure shape
v1.10.0 closed for `confidence`/review cards, applied to the field that
actually gates course completion, cohort convergence, and the level ledger
— arguably the most consequential field in the whole system to get wrong
silently.

This script is the fix: it owns the write. `stages/<stage_id>/test.md` now
says `pass`/`fail` (see `_template` and every course's own copy, updated
alongside this script), and `course-runner.md` calls `apply` instead of
"record the result into syllabus_status" left as an unenforced instruction.

**What `apply` does, exactly matching course-runner.md's own rule
("Only advance current_stage on a genuine pass, then to the next ladder
stage that isn't withheld"):**
  1. Loads `subjects.json` and `course.json`.
  2. Sets `syllabus_status[stage_id]` to `"pass"` or `"fail"`.
  3. On `"fail"`: stops there. `current_stage`/`current_phase` are
     untouched — remediation happens within the same stage
     (`remediation_state.py` owns that separately), never here.
  4. On `"pass"`: walks `course.json`'s `stage_ladder` forward from this
     stage, skipping any stage currently marked `"withheld"` in
     `syllabus_status` (a practical stage this learner hasn't unlocked —
     see `apply_capabilities.py`), and sets `current_stage` to the first
     one that isn't. If nothing remains (the ladder is exhausted), leaves
     `current_stage` as-is — completion itself is derived elsewhere
     (`cohort_status.is_complete`), not decided by this script. Also resets
     `current_phase` to `"lesson"` for the new stage — a genuinely new
     stage always starts there, so this needs no judgment call.

This script never grades anything and never decides *whether* a test was
passed — that real judgment (was the method right, not just the final
answer; does the rubric's pass_threshold hold) stays entirely with the
model, exactly as `gate_check.py`/`error_log.py`/`review_math.py` never
decide the judgment call that precedes their own writes either. It only
gives that judgment, once made, a durable, code-enforced effect.

**A pass needs a grading record (B-04.5e, ADR 0012).** `apply ... pass` is refused unless `record_grading.py` has recorded this stage's test since the
last result was written for it (`grading_used` in the progress file remembers which attempt a result consumed, so one record cannot back two results), and,
when the stage's rubric entry carries a `pass_percent` (only where the issuing body publishes one), unless the recorded marks reach that percentage. A refusal
writes nothing and says what to do. The check is skipped, with the reason in `grading_check`, when it cannot apply: signal-class data is not being kept
(consent limited), the course has no rubric entry for the stage, or the history database cannot be read. Repeating a pass that is already recorded changes
nothing and is not re-checked. A `fail` is never refused; it consumes the latest record so it cannot later back a pass.

Usage:
    python3 record_stage_result.py apply <subjects.json> <course.json> \
        <stage_id> <pass|fail>

Output: JSON to stdout. Writes subjects.json in place on success.
"""
import json
import os
import sys

import sqlite_store
from cohort_status import TEST_PENDING
from tutorlib import cli, consent, filelock, ledger, state

RESULTS = ("pass", "fail")


def _load(path):
    return state.load(path, "subjects")


def _grading_gate(subjects_path, course_path, stage_id, used):
    """(refusal or None, evidence dict or None, note or None, attempt or None): may a pass for this stage be recorded now?"""
    allowed, _ = consent.check(subjects_path, consent.SIGNAL)
    if not allowed:
        return None, None, "not checked: grading records are not kept under this consent", None
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(course_path)), "rubric.json"), encoding="utf-8") as f:
            entry = (json.load(f).get("stage_rubrics") or {}).get(stage_id)
    except (OSError, ValueError):
        entry = None
    if not isinstance(entry, dict):
        return None, None, "not checked: the course has no rubric entry for this stage", None
    latest = sqlite_store.latest_grading(subjects_path, stage_id)
    if not latest.get("ok"):
        return None, None, f"not checked: the history database could not be read ({latest.get('error')})", None
    attempt = latest.get("attempt")
    if attempt is None:
        return f"stage {stage_id} has no grading record: grade its test and run record_grading.py first, then record the result", None, None, None
    if attempt <= used:
        return (f"the latest grading record for stage {stage_id} (attempt {attempt}) was already used for an earlier result: "
                "grade this test and run record_grading.py first"), None, None, None
    available = latest.get("available") or 0
    percent = round(100 * (latest.get("awarded") or 0) / available, 1) if available else None
    evidence = {"attempt": attempt, "awarded": latest.get("awarded"), "available": available, "percent": percent}
    need = entry.get("pass_percent")
    if isinstance(need, int) and (percent is None or percent < need):
        return f"the recorded marks for stage {stage_id} are {evidence['awarded']} of {available} ({percent}%), below the pass mark of {need}%", evidence, None, attempt
    return None, evidence, None, attempt


def _save(path, data):
    state.save(path, data, "subjects")


@ledger.logged("record_stage_result.py", "subjects_path")
@filelock.locked("subjects_path")
def apply(subjects_path, course_path, stage_id, result):
    if result not in RESULTS:
        return {"error": f"result must be one of {RESULTS}, got {result!r}"}

    d = _load(subjects_path)
    course = _load(course_path)

    ladder = course.get("stage_ladder", [])
    if not isinstance(ladder, list) or stage_id not in ladder:
        return {"error": f"stage_id {stage_id!r} not found in {course_path}'s stage_ladder"}

    syllabus_status = d.setdefault("syllabus_status", {})
    previous = syllabus_status.get(stage_id)

    evidence = check_note = grading_attempt = None
    grading_used = d.setdefault("grading_used", {})
    if result == "pass" and previous != "pass":
        refusal, evidence, check_note, grading_attempt = _grading_gate(subjects_path, course_path, stage_id, int(grading_used.get(stage_id) or 0))
        if refusal:
            return {"error": refusal}
    elif result == "fail":
        latest = sqlite_store.latest_grading(subjects_path, stage_id)
        grading_attempt = latest.get("attempt") if latest.get("ok") else None
    if grading_attempt:
        grading_used[stage_id] = max(int(grading_used.get(stage_id) or 0), grading_attempt)
    if not grading_used:
        d.pop("grading_used", None)
    syllabus_status[stage_id] = result

    advanced_to = None
    roster_reset = None
    if result == "pass":
        idx = ladder.index(stage_id)
        for candidate in ladder[idx + 1:]:
            if syllabus_status.get(candidate) != "withheld":
                advanced_to = candidate
                break
        current = d.get("current_stage")
        if advanced_to is not None and current in ladder and ladder.index(current) >= ladder.index(advanced_to):
            advanced_to = None      # replayed pass for an earlier stage: never move the learner backwards
        if advanced_to is not None:
            d["current_stage"] = advanced_to
            d["current_phase"] = "lesson"
        # A pass ends this course's wait: it starts its next stage's lesson. Left as test_pending_convergence it would count
        # as already "ready to test" for that next stage and defeat the cohort convergence rule (cohort_status test_ready).
        if d.get("roster_state") == TEST_PENDING:
            d["roster_state"] = "active"
            roster_reset = "active"

    allowed, cstatus = consent.check(subjects_path, consent.PROGRESS)
    if not allowed:
        return {"action": "not_persisted", "stage_id": stage_id, "result": result, **consent.skipped(cstatus, consent.PROGRESS)}
    _save(subjects_path, d)

    return {
        "stage_id": stage_id,
        "previous_status": previous,
        "result": result,
        "advanced_to": advanced_to,
        "current_stage": d.get("current_stage"),
        **({"roster_state_reset": roster_reset} if roster_reset else {}),
        **({"grading": evidence} if evidence else {}),
        **({"grading_check": check_note} if check_note else {}),
        "written": True,
    }


def main():
    if len(sys.argv) != 6 or sys.argv[1] != "apply":
        print(json.dumps({"error": "usage: record_stage_result.py apply <subjects.json> <course.json> <stage_id> <pass|fail>"}))
        sys.exit(2)
    _, _, subjects_path, course_path, stage_id, result = sys.argv
    try:
        out = apply(subjects_path, course_path, stage_id, result)
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        sys.exit(1)
    sys.exit(cli.emit(out))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
