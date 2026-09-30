#!/usr/bin/env python3
"""
toolkit/progress.py — one read-only snapshot of where a learner stands:
per-course roster state, current stage, confidence, item-mastery summary,
and (folded in per the design discussion, rather than a separate tool)
which courses are currently gated and why they aren't running.

Reads only. Never computes a new confidence, mastery, or gate decision of
its own — course-runner's gate_check.py already computes gates; this module
surfaces what course.json/subjects.json already record about the outcome
of that logic (roster_state, current_stage), not a live re-evaluation.

Usage:
    python3 -m toolkit progress <learner_id> [--course COURSE_ID]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402


def _mastery_summary(subj):
    mastery = subj.get("item_mastery")
    if not isinstance(mastery, dict) or not mastery:
        return {"observed_items": 0}
    values = [e.get("p_mastery") for e in mastery.values() if isinstance(e, dict) and "p_mastery" in e]
    if not values:
        return {"observed_items": len(mastery)}
    low = sorted(
        ((iid, e.get("p_mastery")) for iid, e in mastery.items() if isinstance(e, dict)),
        key=lambda pair: pair[1] if pair[1] is not None else 1.0,
    )[:5]
    return {
        "observed_items": len(mastery),
        "mean_p_mastery": round(sum(values) / len(values), 4),
        "lowest": [{"item_id": iid, "p_mastery": p} for iid, p in low],
    }


def _course_progress(learner_id, course_id, root):
    subj = core.load_subject(learner_id, course_id, root)
    if not core.is_ok(subj):
        return {"course_id": course_id, "error": subj.get("__error__")}
    return {
        "course_id": course_id,
        "roster_state": subj.get("roster_state"),
        "current_stage": subj.get("current_stage"),
        "confidence": subj.get("confidence"),
        "syllabus_status_counts": _tally(subj.get("syllabus_status")),
        "open_error_count": sum(
            1 for e in (subj.get("error_patterns") or [])
            if isinstance(e, dict) and not e.get("resolved")
        ),
        "mastery": _mastery_summary(subj),
    }


def _tally(syllabus_status):
    if not isinstance(syllabus_status, dict):
        return {}
    counts = {}
    for v in syllabus_status.values():
        counts[v] = counts.get(v, 0) + 1
    return counts


def snapshot(learner_id, root=None, course_id=None):
    root = root or core.edu_root()
    prof = core.load_student_profile(learner_id, root)
    if not core.is_ok(prof):
        return {"error": prof.get("__error__")}

    course_ids = [course_id] if course_id else core.list_enrolled_courses(learner_id, root)
    return {
        "learner_id": learner_id,
        "session_slot": prof.get("session_slot"),
        "highest_level_cleared": prof.get("highest_level_cleared"),
        "roster": prof.get("roster"),
        "courses": [_course_progress(learner_id, cid, root) for cid in course_ids],
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "usage: progress.py <learner_id> [--course COURSE_ID]"}))
        sys.exit(2)
    learner_id = sys.argv[1]
    course_id = None
    if "--course" in sys.argv:
        i = sys.argv.index("--course")
        if i + 1 < len(sys.argv):
            course_id = sys.argv[i + 1]
    print(json.dumps(snapshot(learner_id, course_id=course_id), indent=2))


if __name__ == "__main__":
    main()
