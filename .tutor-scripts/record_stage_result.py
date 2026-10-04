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

Usage:
    python3 record_stage_result.py apply <subjects.json> <course.json> \
        <stage_id> <pass|fail>

Output: JSON to stdout. Writes subjects.json in place on success.
"""
import json
import sys
from tutorlib import atomic_io, cli, consent, filelock, state

RESULTS = ("pass", "fail")


def _load(path):
    return state.load(path, "subjects")


def _save(path, data):
    atomic_io.write_json(path, data)


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
    syllabus_status[stage_id] = result

    advanced_to = None
    if result == "pass":
        idx = ladder.index(stage_id)
        for candidate in ladder[idx + 1:]:
            if syllabus_status.get(candidate) != "withheld":
                advanced_to = candidate
                break
        if advanced_to is not None:
            d["current_stage"] = advanced_to
            d["current_phase"] = "lesson"

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
    main()
