#!/usr/bin/env python3
"""
CI driver: run validate_structure.py and coverage_check.py against every
course under courses/*/, and fail if any course reports a problem.

Why this exists (v1.11.0 follow-up). plugin-tests.yml only ever ran
`python3 -m unittest discover tests` scoped to plugin/generic-tutor/**. That
suite builds its own tempdirs and never touches the real courses/ tree, so a
courses/-only change -- including the 1253-file test.md migration that
shipped in this same wave of fixes -- could ship with zero CI signal on
whether it actually left every course structurally valid. This script closes
that gap: it's the same two validators course-auditor and manual checks
already use, just run unattended over the whole tree and turned into a
nonzero exit code.

This intentionally does NOT run course-auditor's Tier 2/3 checks (those need
live web verification and are not CI-appropriate). It only catches what
validate_structure.py and coverage_check.py already catch structurally:
missing stage files, orphaned stage dirs, missing/empty rubric entries,
uncovered spec items without a declared reason, coverage-status mismatches.

NOTE (30 Sep 2026): courses/ no longer lives in this repo, so nothing here
calls this script. It is kept here and checked out cross-repo by
edu-courses-private's CI, which passes its own checkout as <repo_root>. The
"1253-file migration" above refers to that content's earlier history.

Usage:
    python3 validate_courses.py <repo_root>

Exit code 0 if every course is clean, 1 otherwise. Always prints a full
per-course summary to stdout so a CI failure is diagnosable from the log
alone, without needing to reproduce locally.
"""
import glob
import json
import os
import sys

def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: validate_courses.py <repo_root>"}))
        sys.exit(2)
    repo_root = sys.argv[1]
    scripts_dir = os.path.join(repo_root, "plugin", "generic-tutor", "scripts")
    sys.path.insert(0, scripts_dir)
    import validate_structure  # noqa: E402
    import coverage_check  # noqa: E402

    course_dirs = sorted(
        d for d in glob.glob(os.path.join(repo_root, "courses", "*"))
        if os.path.isdir(d) and os.path.isfile(os.path.join(d, "course.json"))
    )

    if not course_dirs:
        print(json.dumps({"error": f"no course directories with course.json found under {repo_root}/courses"}))
        sys.exit(2)

    failures = []
    for course_dir in course_dirs:
        course_id = os.path.basename(course_dir)
        v = validate_structure.validate(course_dir)
        c = coverage_check.check(course_dir)

        v_ok = "error" not in v and v.get("clean", False)
        c_ok = "error" not in c and c.get("clean", False)

        status = "OK" if (v_ok and c_ok) else "FAIL"
        print(f"[{status}] {course_id}")

        if not v_ok:
            reason = v.get("error") or {
                k: val for k, val in v.items()
                if k not in ("course_dir", "clean", "stage_ladder_length") and val
            }
            print(f"    validate_structure: {json.dumps(reason, ensure_ascii=False)}")
        if not c_ok:
            reason = c.get("error") or {
                k: val for k, val in c.items()
                if k not in ("course_dir", "clean") and val not in (None, False, [], {})
            }
            print(f"    coverage_check: {json.dumps(reason, ensure_ascii=False)}")

        if status == "FAIL":
            failures.append(course_id)

    print()
    print(f"checked {len(course_dirs)} courses, {len(failures)} failing")
    if failures:
        print("failing courses:", ", ".join(failures))
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
