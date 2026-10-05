#!/usr/bin/env python3
"""
status.py -- one-screen summary of where a learner stands (C-06, U-01 groundwork).

    python3 status.py <learner_dir> <courses_dir>

Read-only. Output:
  learner, session_slot, consent, roster{occupancy, max, can_add},
  courses[{course_id, name, roster_state, level|standalone, current_stage, current_phase,
           stages_passed, stages_total, complete, theory_only, confidence, due_reviews,
           unresolved_errors, coverage_status, grounding_status}],
  due_reviews_total, next_action{command, reason}

`next_action` is a plain suggestion, never a gate: due reviews first, then the live course with the most
stages left, otherwise a hint about what is blocking (dormant, suspended, nothing enrolled).
"""
import json
import os
import sys

import roster_check
from cohort_status import LIVE_STATES, is_complete, is_standalone, is_suspended, withheld_stages
from tutorlib import cli, consent


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def build(learner_dir, courses_dir):
    profile = _load(os.path.join(learner_dir, "student_profile.json"))
    if profile is None:
        return {"error": f"no readable student_profile.json in {learner_dir}"}
    slot = profile.get("session_slot", 0) if isinstance(profile.get("session_slot", 0), int) else 0
    sdir = os.path.join(learner_dir, "subjects")
    courses, due_total = [], 0
    for fn in sorted(os.listdir(sdir)) if os.path.isdir(sdir) else []:
        if not fn.endswith(".json") or fn.endswith("_review_deck.json"):
            continue
        subj = _load(os.path.join(sdir, fn))
        if not isinstance(subj, dict):
            continue
        cid = subj.get("course_id") or fn[:-5]
        course = _load(os.path.join(courses_dir, cid, "course.json")) or {}
        status = subj.get("syllabus_status") or {}
        ladder = course.get("stage_ladder") or list(status)
        deck = _load(os.path.join(sdir, f"{cid}_review_deck.json")) or {}
        due = sum(1 for c in deck.get("cards", []) if isinstance(c, dict) and isinstance(c.get("due_at_slot"), int) and c["due_at_slot"] <= slot)
        live = subj.get("roster_state") in LIVE_STATES and not is_suspended(course.get("grounding_status"))
        if live:
            due_total += due
        complete = bool(course) and is_complete(course, subj)
        courses.append({
            "course_id": cid, "name": course.get("name"), "roster_state": subj.get("roster_state"),
            "level": None if (course and is_standalone(course)) else course.get("academic_level"),
            "standalone": bool(course) and is_standalone(course),
            "current_stage": subj.get("current_stage"), "current_phase": subj.get("current_phase"),
            "stages_passed": sum(1 for s in ladder if status.get(s) == "pass"), "stages_total": len(ladder),
            "complete": complete, "theory_only": bool(course) and complete and bool(withheld_stages(course, subj)),
            "confidence": subj.get("confidence"), "due_reviews": due,
            "unresolved_errors": sum(1 for e in subj.get("error_patterns", []) if isinstance(e, dict) and not e.get("resolved")),
            "coverage_status": course.get("coverage_status"), "grounding_status": course.get("grounding_status"),
            "_live": live, "_left": len(ladder) - sum(1 for s in ladder if status.get(s) in ("pass", "withheld")),
        })
    roster = roster_check.compute(learner_dir, courses_dir)
    live_courses = sorted((c for c in courses if c["_live"] and not c["complete"]), key=lambda c: (-c["_left"], c["course_id"]))
    if not courses:
        nxt = {"command": "/add-course", "reason": "no courses yet"}
    elif due_total:
        nxt = {"command": "/review", "reason": f"{due_total} review card(s) due"}
    elif live_courses:
        nxt = {"command": f"/continue {live_courses[0]['course_id']}", "reason": "most stages remaining among your live courses"}
    elif any(c["roster_state"] == "dormant" for c in courses):
        nxt = {"command": "/list-courses", "reason": "remaining courses are level-locked; finish the lower level first"}
    elif all(c["complete"] or c["roster_state"] == "dropped" for c in courses):
        nxt = {"command": "/add-course", "reason": "everything enrolled is finished or dropped"}
    else:
        nxt = {"command": "/list-courses", "reason": "nothing is currently teachable; check suspended or dropped courses"}
    for c in courses:
        c.pop("_live"), c.pop("_left")
    return {
        "learner": profile.get("learner_id") or os.path.basename(learner_dir), "session_slot": slot,
        "consent": consent.status_for(os.path.join(learner_dir, "student_profile.json")),
        "roster": {"occupancy": roster.get("roster_occupancy"), "max": roster.get("max_incomplete_courses"), "can_add": roster.get("can_add_course")},
        "courses": courses, "due_reviews_total": due_total, "next_action": nxt,
    }


def main(argv):
    if len(argv) != 2:
        print(json.dumps({"error": "usage: status.py <learner_dir> <courses_dir>"}))
        return 2
    return cli.emit(build(argv[0], argv[1]))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
