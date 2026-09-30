#!/usr/bin/env python3
"""
toolkit/errors.py — aggregate the error log across a learner's courses,
using error_log.py's own query() rather than re-parsing error_patterns by
hand (core.py's design rule 3). No re-diagnosis: this only groups and
counts what's already been classified.

Usage:
    python3 -m toolkit errors <learner_id> [--course COURSE_ID] [--open-only]
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402
import error_log  # noqa: E402  (sibling .tutor-scripts module)


def aggregate(learner_id, root=None, course_id=None, open_only=False):
    root = root or core.edu_root()
    course_ids = [course_id] if course_id else core.list_enrolled_courses(learner_id, root)

    by_cause, by_course, entries = {}, {}, []
    for cid in course_ids:
        subj_path = os.path.join(core.subjects_dir(learner_id, root), f"{cid}.json")
        if not os.path.isfile(subj_path):
            continue
        result = error_log.query(subj_path, "ALL")
        if "error" in result:
            continue
        for e in result.get("entries", []):
            if not isinstance(e, dict):
                continue
            if open_only and e.get("resolved"):
                continue
            cause = e.get("cause")
            by_cause[cause] = by_cause.get(cause, 0) + 1
            by_course[cid] = by_course.get(cid, 0) + 1
            entries.append({**e, "course_id": cid})

    most_frequent_open = sorted(
        ((c, n) for c, n in by_cause.items()),
        key=lambda pair: -pair[1],
    )
    return {
        "learner_id": learner_id,
        "total_entries": len(entries),
        "by_cause": by_cause,
        "by_course": by_course,
        "most_frequent_causes": [{"cause": c, "count": n} for c, n in most_frequent_open],
        "entries": entries,
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "usage: errors.py <learner_id> [--course COURSE_ID] [--open-only]"}))
        sys.exit(2)
    learner_id = sys.argv[1]
    course_id = None
    if "--course" in sys.argv:
        i = sys.argv.index("--course")
        if i + 1 < len(sys.argv):
            course_id = sys.argv[i + 1]
    open_only = "--open-only" in sys.argv
    print(json.dumps(aggregate(learner_id, course_id=course_id, open_only=open_only), indent=2))


if __name__ == "__main__":
    main()
