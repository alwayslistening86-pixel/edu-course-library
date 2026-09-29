#!/usr/bin/env python3
"""
prereq_check.py - v1.3.0 course prerequisites, for course-compiler's /add-course (before any
enrolment is created) and as the same rule gate_check.py's Gate 3 applies before teaching.

A course's `requires_complete` is a list. Each entry is either a course_id (that course must be
complete) or a list of course_ids (any one of them complete). A pre-1.3.0 single string is read as
a one-item list. "Complete" is cohort_status.is_complete() - every stage passed (or withheld, for a
theory-only completion of a practical course) and the exam passed if enabled. A theory-only
completion satisfies a prerequisite (decided 26 Sep 2026).

Prerequisites are about content, not sequencing: they are checked in addition to the level-lock
(roster_check.py), never instead of it. A standalone course checks only its prerequisites.

Usage:
    python3 prereq_check.py <course.json> <the learner's profile subjects/ dir> <courses dir>

Output: JSON {"met": bool, "required": [...], "unmet": [...], "missing_courses": [...]} where
missing_courses lists prerequisite ids with no course folder at all (the course is unreachable
until they are built - course-auditor reports these).
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cohort_status import prerequisites_status  # noqa: E402


def check(course_json_path, subjects_dir, courses_dir):
    try:
        with open(course_json_path, "r", encoding="utf-8") as f:
            course = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        return {"error": f"course.json unreadable: {type(e).__name__}: {e}"}
    result = prerequisites_status(course, subjects_dir, courses_dir)
    ids = set()
    for entry in result["required"]:
        ids.update(entry if isinstance(entry, list) else [entry])
    result["missing_courses"] = sorted(
        cid for cid in ids if not os.path.isfile(os.path.join(courses_dir, cid, "course.json"))
    )
    return result


def main():
    if len(sys.argv) != 4:
        print(json.dumps({"error": "usage: prereq_check.py <course.json> <profile subjects dir> <courses dir>"}))
        sys.exit(2)
    print(json.dumps(check(*sys.argv[1:4]), indent=2))


if __name__ == "__main__":
    main()
