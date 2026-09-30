#!/usr/bin/env python3
"""
toolkit/health.py — an honest, read-only status report: schema versions,
unreadable files, suspended/ungrounded courses, and which version of the
plugin's scripts is actually deployed on this machine. Never runs a
migration (that stays the plugin's own /audit, run from a live session) —
this only says what it finds.

Usage:
    python3 -m toolkit health [--learner LEARNER_ID]
    (omit --learner to check every learner under profile/)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402


def _deployed_scripts_version(root):
    manifest = core.load_json(os.path.join(root, ".tutor-scripts", ".manifest.json"))
    if not core.is_ok(manifest):
        return {"status": "manifest_unreadable", "detail": manifest.get("__error__")}
    return {"status": "ok", "plugin_version": manifest.get("plugin_version"),
            "packages": manifest.get("packages", [])}


def _learner_health(learner_id, root):
    prof = core.load_student_profile(learner_id, root)
    entry = {"learner_id": learner_id}
    if not core.is_ok(prof):
        entry["profile_error"] = prof.get("__error__")
        return entry

    entry["consent_status"] = (prof.get("consent") or {}).get("status")
    entry["session_slot"] = prof.get("session_slot")
    entry["highest_level_cleared"] = prof.get("highest_level_cleared")

    subjects = []
    for course_id in core.list_enrolled_courses(learner_id, root):
        subj = core.load_subject(learner_id, course_id, root)
        s_entry = {"course_id": course_id}
        if not core.is_ok(subj):
            s_entry["error"] = subj.get("__error__")
            subjects.append(s_entry)
            continue
        s_entry["schema"] = core.schema_status(subj, "subject")
        s_entry["roster_state"] = subj.get("roster_state")
        s_entry["current_stage"] = subj.get("current_stage")
        subjects.append(s_entry)
    entry["subjects"] = subjects
    entry["off_current_schema"] = [
        s["course_id"] for s in subjects if s.get("schema", {}).get("status") not in ("current",) and "error" not in s
    ]
    return entry


def _course_health(course_id, root):
    course = core.load_course(course_id, root)
    entry = {"course_id": course_id}
    if not core.is_ok(course):
        entry["error"] = course.get("__error__")
        return entry
    entry["schema"] = core.schema_status(course, "course")
    entry["grounding_status"] = course.get("grounding_status")
    entry["coverage_status"] = course.get("coverage_status")
    entry["last_live_recheck"] = course.get("last_live_recheck")
    entry["needs_attention"] = course.get("grounding_status") in (None, "suspended")
    return entry


def check_health(root=None, learner_id=None):
    root = root or core.edu_root()
    result = {"edu_root": root, "deployed_scripts": _deployed_scripts_version(root)}

    learners = [learner_id] if learner_id else core.list_learners(root)
    if not learners:
        result["learners"] = []
        result["note"] = "no learner profile found under profile/ — nothing to check yet"
        return result

    result["learners"] = [_learner_health(lid, root) for lid in learners]

    course_ids = sorted(
        d for d in os.listdir(core.courses_dir(root))
        if os.path.isdir(os.path.join(core.courses_dir(root), d))
    ) if os.path.isdir(core.courses_dir(root)) else []
    result["courses"] = [_course_health(cid, root) for cid in course_ids]
    result["courses_needing_attention"] = [
        c["course_id"] for c in result["courses"] if c.get("needs_attention")
    ]
    return result


def main():
    learner_id = None
    args = sys.argv[1:]
    if "--learner" in args:
        i = args.index("--learner")
        if i + 1 < len(args):
            learner_id = args[i + 1]
    print(json.dumps(check_health(learner_id=learner_id), indent=2))


if __name__ == "__main__":
    main()
