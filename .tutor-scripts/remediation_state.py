#!/usr/bin/env python3
"""
remediation_state.py — the missing cap on remediation-after-fail, and the
escalation path nothing in this plugin has ever had.

Before this script, course-runner.md's remediation step could cycle
indefinitely: remediate, retest, fail, remediate, retest, fail — forever,
with nothing routing "this isn't working" anywhere. That's a real cost
beyond one learner's frustration, because of how phase-convergence works:
an unresolved remediation stays the bottleneck for *all* of this learner's
other courses at the same academic level (convergence is scoped to one
learner's own same-level cohort_id, per course-runner — not other
students, but still a real stall on the learner's own progress).

The policy this script applies, per (course, stage):
  - attempt 1: same-framework re-explanation targeted at the classified
    cause (the model does the re-explaining; this script only counts and
    labels the attempt).
  - attempt 2: if the same cause recurs, switch to a genuinely different
    approach (different worked example or analogy) AND check whether this
    is really an earlier-stage or earlier-course gap (the routing gap
    tutor-core's scoping note names as (6) — `missing_prerequisite` as a
    `cause` is exactly the signal to check this against).
  - past attempt 2: `action: "escalate"`, never a silent third loop. The
    stage stays `test_pending_convergence`; the learner is told plainly
    this one is taking longer than expected; it's logged for
    course-auditor's cohort-wide rollup (a stage with a real escalation is
    a candidate for "this lesson is unclear," not "this learner is slow").
    `escalate` is not a dead end — the learner can keep working the stage
    informally, it just stops counting as a system-driven attempt, which is
    what actually gets a genuinely unclear lesson noticed and fixed instead
    of infinitely re-served.

State lives in subjects/<course_id>.json under a new `remediation` object,
keyed by stage_id — deliberately not folded into `error_patterns` (that's a
log of individual wrong answers; this is a counter and a policy decision
per stage, a different shape of state entirely):
  "remediation": {
    "S09": {"attempts": 2, "last_cause": "misconception", "escalated": true,
             "escalated_at_slot": 240}
  }

Subcommands:
    record <subjects.json> <stage_id> <cause> <current_slot>
        Increments the attempt counter for this stage and returns the
        action to take. Call this once, right when remediation actually
        starts for a fresh attempt — not on every turn of the remediation
        conversation itself.
    reset  <subjects.json> <stage_id>
        Clears the counter on a genuine re-pass. Call this from the same
        place course-runner already writes syllabus_status: "pass" after a
        remediated retest — a cleared counter is what lets a stage that
        struggled once still remediate cleanly if a *different* problem
        turns up two stages later.
    status <subjects.json> <stage_id>
        Read-only look at the current count/escalation state, e.g. for
        course-auditor's rollup or to decide whether to check the
        missing-prerequisite routing before attempt 2.

Usage:
    python3 remediation_state.py record <subjects.json> <stage_id> <cause> <current_slot>
    python3 remediation_state.py reset <subjects.json> <stage_id>
    python3 remediation_state.py status <subjects.json> <stage_id>

Output: JSON to stdout.
"""
import json
import sys
from tutorlib import atomic_io, consent, filelock

CAP = 2  # attempts before escalation — attempt 1 and attempt 2 are system-driven; attempt 3 never fires


def _load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(path, data):
    atomic_io.write_json(path, data)


@filelock.locked("subjects_path")
def record(subjects_path, stage_id, cause, current_slot):
    d = _load(subjects_path)
    rem = d.setdefault("remediation", {})
    if not isinstance(rem, dict):
        return {"error": "remediation field is not an object — needs migrate_schema.py first"}

    entry = rem.get(stage_id)
    if not isinstance(entry, dict):
        entry = {"attempts": 0, "last_cause": None, "escalated": False, "escalated_at_slot": None}

    if entry.get("escalated"):
        # already escalated — recording again doesn't re-trigger anything; report status, change nothing.
        rem[stage_id] = entry
        return {
            "action": "already_escalated",
            "stage_id": stage_id,
            "attempts": entry["attempts"],
            "detail": "this stage already escalated; the learner can keep working it informally, "
                      "but it no longer counts as a system-driven remediation attempt",
        }

    entry["attempts"] += 1
    entry["last_cause"] = cause

    if entry["attempts"] == 1:
        action = "same_framework_reexplain"
        detail = "attempt 1 — re-explain within the current framework, targeted at the classified cause"
    elif entry["attempts"] == 2:
        action = "different_approach_and_check_earlier_stage"
        detail = ("attempt 2 — switch to a genuinely different worked example or analogy, and check "
                   "whether this is really an earlier-stage or earlier-course gap (especially if cause "
                   "is 'missing_prerequisite')")
    else:
        entry["escalated"] = True
        entry["escalated_at_slot"] = int(current_slot)
        action = "escalate"
        detail = ("past attempt 2 — do not run a third system-driven remediation loop. Stage stays "
                  "test_pending_convergence. Tell the learner plainly this one is taking longer than "
                  "expected. Logged for course-auditor's cohort-wide rollup.")

    rem[stage_id] = entry
    allowed, cstatus = consent.check(subjects_path, consent.PROGRESS)
    if allowed:
        _save(subjects_path, d)

    return {
        **({} if allowed else consent.skipped(cstatus, consent.PROGRESS)),
        "action": action,
        "stage_id": stage_id,
        "attempts": entry["attempts"],
        "cap": CAP,
        "cause": cause,
        "escalated": entry["escalated"],
        "detail": detail,
    }


@filelock.locked("subjects_path")
def reset(subjects_path, stage_id):
    d = _load(subjects_path)
    rem = d.setdefault("remediation", {})
    had_entry = stage_id in rem
    if had_entry:
        rem.pop(stage_id, None)
        allowed, cstatus = consent.check(subjects_path, consent.PROGRESS)
        if not allowed:
            return {"action": "reset", "stage_id": stage_id, "had_entry": had_entry, **consent.skipped(cstatus, consent.PROGRESS)}
        _save(subjects_path, d)
    return {"action": "reset", "stage_id": stage_id, "had_entry": had_entry}


def status(subjects_path, stage_id):
    d = _load(subjects_path)
    rem = d.get("remediation", {})
    entry = rem.get(stage_id) if isinstance(rem, dict) else None
    if entry is None:
        return {"stage_id": stage_id, "attempts": 0, "escalated": False, "detail": "no remediation on record for this stage"}
    return {"stage_id": stage_id, **entry}


def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "usage: remediation_state.py record|reset|status <subjects.json> <stage_id> [cause] [current_slot]"}))
        sys.exit(2)
    cmd, subjects_path = sys.argv[1], sys.argv[2]
    try:
        if cmd == "record":
            if len(sys.argv) != 6:
                print(json.dumps({"error": "usage: remediation_state.py record <subjects.json> <stage_id> <cause> <current_slot>"}))
                sys.exit(2)
            result = record(subjects_path, sys.argv[3], sys.argv[4], sys.argv[5])
        elif cmd == "reset":
            if len(sys.argv) != 4:
                print(json.dumps({"error": "usage: remediation_state.py reset <subjects.json> <stage_id>"}))
                sys.exit(2)
            result = reset(subjects_path, sys.argv[3])
        elif cmd == "status":
            if len(sys.argv) != 4:
                print(json.dumps({"error": "usage: remediation_state.py status <subjects.json> <stage_id>"}))
                sys.exit(2)
            result = status(subjects_path, sys.argv[3])
        else:
            print(json.dumps({"error": f"unknown subcommand {cmd!r}, expected record|reset|status"}))
            sys.exit(2)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        sys.exit(1)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
