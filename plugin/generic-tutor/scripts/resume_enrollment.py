#!/usr/bin/env python3
"""
resume_enrollment.py — flips a DROPPED enrollment back to live, and touches nothing else.

/drop preserves subjects/<course_id>.json exactly as it stood ("a pause, not a
deletion"), and gate_check.py now refuses to teach a dropped course - so
/add-course must be able to resume one. Without this, the compiler's dedupe branch
("create a new subjects file at all-unsat") would silently overwrite the preserved
progress. This script is the safe half of that branch: it changes ONLY
`roster_state` (and `last_updated`), and refuses unless the file really is
`dropped`, so progress, syllabus_status, current_stage/phase, confidence,
error_patterns and last_session_summary can never be reset by a resume. (The
review deck is a separate file and is never opened here.)

It does not decide the target state - course-compiler runs roster_check.py first
(roster cap, level-lock consequence) and passes `active`, or `dormant` if the lock
check says the course is locked.

Refuses (writes nothing) if:
  - the enrollment is not currently `dropped`
  - target_state is not `active` or `dormant`
  - syllabus_status keys no longer match the canonical course's stage_ladder
    (the course changed while dropped - that needs /audit, not a guess)

A COMPLETE course never reopens a level: if the enrolment is complete (every stage passed,
exam passed if enabled) the script still flips it out of `dropped` - so gate_check reports it as
complete rather than sending the learner round in a circle - but skips the ledger lowering even if
--reopen-* was passed, and says so (`already_complete: true`, `reopened_level: null`). Clearing only
fires when a course *becomes* complete, so lowering the ledger for an already-complete course would
leave the level open until some other course at it finished.

Reopening a cleared level: if the course being resumed is UNFINISHED and its level is at or
below highest_level_cleared (it was excluded from that level's clearing while dropped),
course-compiler passes --reopen-profile <student_profile.json> --reopen-to <level-1>, taken
from roster_check.py --resume's effective_highest_level_cleared, after the learner has
confirmed the re-lock. This script then also LOWERS highest_level_cleared to that value and
changes nothing else in the profile. It only ever lowers (a value >= the stored one is
refused), and it is the only place in the plugin that does; clearing is the only thing that
raises it (journey-planner).

Usage:
    python3 resume_enrollment.py <subjects_json> <course_json> <active|dormant> <today_iso_date> \
        [--reopen-profile <student_profile.json> --reopen-to <int>]
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cohort_status import is_complete  # noqa: E402
from tutorlib import atomic_io, cli, consent, filelock, ledger


@ledger.logged("resume_enrollment.py", "subjects_path")
@filelock.locked("subjects_path")
def resume(subjects_path, course_path, target_state, today_iso, reopen_profile=None, reopen_to=None):
    if target_state not in ("active", "dormant"):
        return {"resumed": False, "error": f"target_state must be active or dormant, got {target_state!r}"}
    with open(subjects_path, "r", encoding="utf-8") as f:
        subj = json.load(f)
    with open(course_path, "r", encoding="utf-8") as f:
        course = json.load(f)

    state = subj.get("roster_state")
    if state != "dropped":
        return {"resumed": False, "error": f"enrollment is {state!r}, not dropped - nothing to resume, nothing written"}

    ladder = set(course.get("stage_ladder", []))
    tracked = set((subj.get("syllabus_status") or {}).keys())
    if ladder != tracked:
        return {
            "resumed": False,
            "error": "syllabus_status no longer matches the course's stage_ladder - course changed while dropped; run /audit, nothing written",
            "only_in_course": sorted(ladder - tracked),
            "only_in_enrollment": sorted(tracked - ladder),
        }

    reopened = None
    profile = None
    already_complete = is_complete(course, subj)
    if (reopen_profile is None) != (reopen_to is None):
        return {"resumed": False, "error": "--reopen-profile and --reopen-to must be given together, nothing written"}
    if reopen_profile is not None and not already_complete:
        with open(reopen_profile, "r", encoding="utf-8") as f:
            profile = json.load(f)
        stored = int(profile.get("highest_level_cleared", 0))
        if int(reopen_to) >= stored or int(reopen_to) < 0:
            return {"resumed": False, "error": f"reopen_to {reopen_to} must be below the stored highest_level_cleared ({stored}) and >= 0, nothing written"}
        reopened = {"from": stored, "to": int(reopen_to)}

    subj["roster_state"] = target_state
    subj["last_updated"] = today_iso
    allowed, cstatus = consent.check(subjects_path, consent.PROGRESS)
    if not allowed:
        return {"resumed": False, **consent.skipped(cstatus, consent.PROGRESS)}
    atomic_io.write_json(subjects_path, subj)
    if profile is not None:
        profile["highest_level_cleared"] = reopened["to"]
        atomic_io.write_json(reopen_profile, profile)
    return {"resumed": True, "already_complete": already_complete, "reopened_level": reopened, "roster_state": target_state, "preserved_current_stage": subj.get("current_stage"),
            "preserved_pass_count": sum(1 for v in subj["syllabus_status"].values() if v == "pass")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("subjects_json")
    ap.add_argument("course_json")
    ap.add_argument("target_state")
    ap.add_argument("today_iso_date")
    ap.add_argument("--reopen-profile")
    ap.add_argument("--reopen-to", type=int)
    a = ap.parse_args()
    sys.exit(cli.emit(resume(a.subjects_json, a.course_json, a.target_state, a.today_iso_date,
                             a.reopen_profile, a.reopen_to)))


if __name__ == "__main__":
    main()
