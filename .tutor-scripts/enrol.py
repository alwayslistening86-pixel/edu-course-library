#!/usr/bin/env python3
"""
enrol.py -- create a learner's progress file for a course (K-19 follow-up; the last hand-written whole-file state).

    python3 enrol.py <profile_dir> <courses_dir> <course_id> <active|dormant> <today YYYY-MM-DD>

Both /add-course paths (a freshly built course and an existing canonical one) and `course-runner`'s defensive create write the same
file; this makes them identical by construction. `<active|dormant>` is `candidate_state` from `roster_check.py <level>`: the caller
decides it, this script never does. Creates `<profile_dir>/subjects/<course_id>.json` (schema 5) with: `cohort_id` = the course's
`academic_level` (or "standalone:<course_id>"), every stage `unsat` (practical stages the learner has not declared the capability
for start `withheld`), `current_stage` = the first rung, phase `lesson`, confidence 0.5 and empty ledgers.

Refuses when: the course or its stage ladder is unreadable, the course is already enrolled (use the resume flow for a dropped one),
the roster is full (`roster_check.py`'s own `can_add_course`), or the learner's consent is revoked (nothing is persisted).
The new file is validated against the subjects schema before it is written. Atomic, locked, ledgered.
"""
import json
import os
import sys

import roster_check
from apply_capabilities import apply as apply_capabilities
from cohort_status import is_standalone, standalone_cohort_id
from tutorlib import cli, consent, filelock, ids, ledger, schema, state


def build(course_id, course, today_iso, state):
    ladder = course["stage_ladder"]
    return {
        "schema_version": 5, "course_id": course_id, "roster_state": state,
        "cohort_id": standalone_cohort_id(course_id) if is_standalone(course) else course.get("academic_level"),
        "syllabus_status": {s: "unsat" for s in ladder}, "notices_acknowledged": [], "current_stage": ladder[0], "current_phase": "lesson",
        "exam_status": "locked", "confidence": 0.5, "error_patterns": [], "item_mastery": {}, "remediation": {},
        "last_session_summary": "", "last_updated": today_iso,
    }


def enrol(profile_dir, courses_dir, course_id, roster_state, today_iso):
    ids.validate(course_id, "course id")
    if roster_state not in ("active", "dormant"):
        return {"error": f"state must be 'active' or 'dormant' (candidate_state from roster_check.py), got {roster_state!r}"}
    profile_path = os.path.join(profile_dir, "student_profile.json")
    subj_path = os.path.join(profile_dir, "subjects", f"{course_id}.json")
    course_path = os.path.join(courses_dir, course_id, "course.json")
    try:
        with open(course_path, encoding="utf-8") as f:
            course = json.load(f)
        with open(profile_path, encoding="utf-8") as f:
            profile = json.load(f)
    except (OSError, ValueError) as e:
        return {"error": f"FileNotFoundError: cannot read {course_path} or {profile_path}: {e}"}
    if not isinstance(course.get("stage_ladder"), list) or not course["stage_ladder"]:
        return {"error": f"{course_id} has no stage_ladder"}
    if not is_standalone(course) and not isinstance(course.get("academic_level"), int):
        return {"error": f"{course_id} has no academic_level and is not standalone: cannot choose a cohort"}
    allowed, cstatus = consent.check(subj_path, consent.PROGRESS)
    if not allowed:
        return {"action": "not_persisted", "course_id": course_id, **consent.skipped(cstatus, consent.PROGRESS)}
    os.makedirs(os.path.dirname(subj_path), exist_ok=True)
    with filelock.file_lock(profile_path):
        if os.path.exists(subj_path):
            return {"error": f"{course_id} is already enrolled (a dropped course is resumed, not re-enrolled)"}
        roster = roster_check.compute(profile_dir, courses_dir)
        if "error" not in roster and not roster.get("can_add_course", True):
            return {"error": f"the roster is full ({roster.get('roster_occupancy')} of {roster.get('max_incomplete_courses')}): complete or drop a course first"}
        subj = build(course_id, course, today_iso, roster_state)
        subj, report = apply_capabilities(profile, course, subj)
        problems = schema.validate(subj, "subjects")
        if problems:
            return {"error": "the new file would not match the subjects schema: " + "; ".join(problems[:3])}
        with filelock.file_lock(subj_path):
            state.save(subj_path, subj, "subjects")
    ledger.record(subj_path, "enrol.py", "enrol", course_id, True, None, {"state": roster_state})
    return {"action": "enrol", "course_id": course_id, "roster_state": roster_state, "cohort_id": subj["cohort_id"],
            "current_stage": subj["current_stage"], "theory_only": report["theory_only"], "withheld_stages": report["withheld_now"], "written": True}


def main(argv):
    if len(argv) != 5:
        print(json.dumps({"error": "usage: enrol.py <profile_dir> <courses_dir> <course_id> <active|dormant> <today YYYY-MM-DD>"}))
        return 2
    try:
        return cli.emit(enrol(*argv))
    except (cli.EXPECTED_ERRORS + (ids.InvalidId,)) as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
