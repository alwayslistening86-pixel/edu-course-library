#!/usr/bin/env python3
"""
Content CI driver (N-03): validate every course in a content library against the engine's own checks.

    python3 validate_courses.py --courses <dir> [--engine <dir>]
    python3 validate_courses.py <repo_root>                     # legacy form: <repo_root>/courses + <repo_root>/plugin/generic-tutor

--engine is the checkout of THIS repository (default: the repository containing this script). The content repository
(`edu-courses-private` or any library) is checked out separately; nothing here assumes the two share a tree.

For each course folder under --courses (a folder with a course.json) it runs, in order:
  1. validate_structure.py      stage files, rubric sources, 1.3.0 field consistency, orphaned stage folders
  2. coverage_check.py          itemised specification vs stages, status mismatch
  3. JSON Schemas               course.json, curriculum_map.json, rubric.json, question_bank.json (if present), every stages/*/misconceptions.json
  4. scan_untrusted.py          instruction-like text in web-derived files (BLOCKING hits fail the course)
  5. min_engine_version         the course's declared minimum must not exceed the engine under test
A course fails if any step reports a problem. Advisory findings are printed but do not fail. Not run here (needs live web
access and judgement): grounding re-verification, coverage re-derivation - that is /audit.

Exit 0 if every course is clean, 1 if any fails, 2 on usage errors or no courses found. The full per-course report is
printed so a CI failure is diagnosable from the log alone.
"""
import glob
import json
import os
import sys


def _arg(args, flag):
    if flag in args:
        i = args.index(flag)
        if i + 1 >= len(args):
            print(json.dumps({"error": f"{flag} needs a value"}))
            sys.exit(2)
        val = args[i + 1]
        del args[i:i + 2]
        return val
    return None


def main(argv):
    args = list(argv)
    courses_dir, engine = _arg(args, "--courses"), _arg(args, "--engine")
    if courses_dir is None:
        if len(args) != 1:
            print(json.dumps({"error": "usage: validate_courses.py --courses <dir> [--engine <dir>]  |  validate_courses.py <repo_root>"}))
            return 2
        courses_dir, engine = os.path.join(args[0], "courses"), engine or args[0]
    elif args:
        print(json.dumps({"error": f"unexpected arguments: {args}"}))
        return 2
    engine = engine or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    scripts_dir = os.path.join(engine, "plugin", "generic-tutor", "scripts")
    if not os.path.isdir(scripts_dir):
        print(json.dumps({"error": f"engine scripts not found at {scripts_dir}"}))
        return 2
    sys.path.insert(0, scripts_dir)
    import coverage_check  # noqa: E402
    import validate_structure  # noqa: E402
    from tutorlib import schema, untrusted, version  # noqa: E402

    course_dirs = sorted(d for d in glob.glob(os.path.join(courses_dir, "*")) if os.path.isfile(os.path.join(d, "course.json")))
    if not course_dirs:
        print(json.dumps({"error": f"no course directories with course.json found under {courses_dir}"}))
        return 2

    failures = []
    for cdir in course_dirs:
        cid = os.path.basename(cdir)
        problems, notes = [], []

        v = validate_structure.validate(cdir)
        if "error" in v:
            problems.append(f"validate_structure: {v['error']}")
        elif not v.get("clean", False):
            reason = {k: val for k, val in v.items() if k not in ("course_dir", "clean", "stage_ladder_length", "misconceptions_status") and val}
            problems.append(f"validate_structure: {json.dumps(reason, ensure_ascii=False)}")

        c = coverage_check.check(cdir)
        if "error" in c:
            problems.append(f"coverage_check: {c['error']}")
        elif not c.get("clean", False):
            reason = {k: val for k, val in c.items() if k not in ("course_dir", "clean") and val not in (None, False, [], {})}
            problems.append(f"coverage_check: {json.dumps(reason, ensure_ascii=False)}")

        for kind in ("course", "curriculum_map", "rubric"):
            for e in schema.validate_file(os.path.join(cdir, f"{kind}.json"), kind):
                problems.append(f"schema {kind}.json: {e}")
        qb = os.path.join(cdir, "question_bank.json")
        if os.path.isfile(qb):
            for e in schema.validate_file(qb, "question_bank"):
                problems.append(f"schema question_bank.json: {e}")
        for mis in sorted(glob.glob(os.path.join(cdir, "stages", "*", "misconceptions.json"))):
            for e in schema.validate_file(mis, "misconceptions"):
                problems.append(f"schema {os.path.relpath(mis, cdir)}: {e}")

        for rel, found in untrusted.scan_path(cdir).items():
            for f in found:
                line = f"{rel}:{f['line']} [{f['rule']}] {f['excerpt']}"
                (problems if f["severity"] == untrusted.BLOCKING else notes).append(f"untrusted content: {line}" if f["severity"] == untrusted.BLOCKING else line)

        try:
            with open(os.path.join(cdir, "course.json"), encoding="utf-8") as fh:
                need = json.load(fh).get("min_engine_version")
        except (OSError, ValueError):
            need = None
        ok, have = version.check_min(need, scripts_dir)
        if not ok:
            problems.append(f"min_engine_version {need} is newer than the engine under test ({have})")

        print(f"[{'FAIL' if problems else 'OK'}] {cid}")
        for p in problems:
            print(f"    {p}")
        for n in notes:
            print(f"    (advisory) {n}")
        if problems:
            failures.append(cid)

    print(f"\nchecked {len(course_dirs)} courses, {len(failures)} failing")
    if failures:
        print("failing courses:", ", ".join(failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
