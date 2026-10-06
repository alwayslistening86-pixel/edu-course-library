#!/usr/bin/env python3
"""
list_courses.py -- every course in the library with the learner's standing in it, filterable (C-14). Read-only.

    python3 list_courses.py <learner_dir> <courses_dir> [--status S] [--level N] [--standalone] [--compact]

--status   one of: active, dormant, test_pending_convergence, dropped, complete, not_enrolled
--level    only courses at this academic level
--standalone  only standalone courses
--compact  rows reduced to id, level, state and stages passed / total

Row fields (full form): course_id, name, level (int|null), standalone, level_basis, state (the learner's roster_state, `complete` when finished,
or `not_enrolled`), current_stage, current_phase, stages_passed, stages_total, theory_only, coverage {status, items_taught, items_total},
prerequisites {required, met, unmet}, practical_stages, grounding_status. Rows sort by level (standalone last) then id. Counts by state
are returned with the rows. The computation reuses cohort_status / coverage_check, so "complete" and "met" mean what the gates mean.
"""
import json
import os
import sys

import coverage_check
from cohort_status import is_complete, is_standalone, prerequisites_status, withheld_stages
from tutorlib import cli

STATES = ("active", "dormant", "test_pending_convergence", "dropped", "complete", "not_enrolled")


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else None
    except (OSError, ValueError):
        return None


def build(learner_dir, courses_dir, status=None, level=None, standalone_only=False, compact=False):
    if not os.path.isdir(courses_dir):
        return {"error": f"FileNotFoundError: courses_dir does not exist: {courses_dir}"}
    if status is not None and status not in STATES:
        return {"error": f"--status must be one of {STATES}"}
    sdir = os.path.join(learner_dir, "subjects")
    rows = []
    for cid in sorted(os.listdir(courses_dir)):
        cpath = os.path.join(courses_dir, cid, "course.json")
        course = _load(cpath)
        if course is None:
            continue
        subj = _load(os.path.join(sdir, f"{cid}.json"))
        standalone = is_standalone(course)
        lvl = None if standalone else course.get("academic_level")
        if standalone_only and not standalone:
            continue
        if level is not None and lvl != level:
            continue
        ladder = course.get("stage_ladder") or []
        if subj is None:
            state, passed = "not_enrolled", 0
        else:
            passed = sum(1 for v in (subj.get("syllabus_status") or {}).values() if v == "pass")
            state = "complete" if is_complete(course, subj) else subj.get("roster_state", "unknown")
        if status is not None and state != status:
            continue
        row = {"course_id": cid, "level": lvl, "state": state, "stages_passed": passed, "stages_total": len(ladder)}
        if not compact:
            cov = coverage_check.check(os.path.join(courses_dir, cid))
            prereq = prerequisites_status(course, sdir, courses_dir)
            row.update({
                "name": course.get("name"), "standalone": standalone, "level_basis": course.get("level_basis"),
                "current_stage": subj.get("current_stage") if subj else None, "current_phase": subj.get("current_phase") if subj else None,
                "theory_only": bool(subj and withheld_stages(course, subj)),
                "coverage": {"status": cov.get("computed_status") or cov.get("declared_status"), "items_taught": cov.get("items_taught"), "items_total": cov.get("items_total")},
                "prerequisites": {"required": prereq.get("required", []), "met": prereq.get("met"), "unmet": prereq.get("unmet", [])},
                "practical_stages": sorted((course.get("practical_stages") or {}).keys()), "grounding_status": course.get("grounding_status"),
            })
        rows.append(row)
    rows.sort(key=lambda r: (r["level"] is None, r["level"] if r["level"] is not None else 0, r["course_id"]))
    counts = {}
    for r in rows:
        counts[r["state"]] = counts.get(r["state"], 0) + 1
    return {"count": len(rows), "by_state": dict(sorted(counts.items())), "courses": rows}


def main(argv):
    args = list(argv)
    opts = {"status": None, "level": None, "standalone_only": False, "compact": False}
    try:
        for flag, key in (("--status", "status"), ("--level", "level")):
            if flag in args:
                i = args.index(flag)
                opts[key] = args[i + 1]
                del args[i:i + 2]
        if opts["level"] is not None:
            opts["level"] = int(opts["level"])
    except (IndexError, ValueError):
        print(json.dumps({"error": "--status and --level need a value (--level an integer)"}))
        return 2
    for flag, key in (("--standalone", "standalone_only"), ("--compact", "compact")):
        if flag in args:
            args.remove(flag)
            opts[key] = True
    if len(args) != 2:
        print(json.dumps({"error": "usage: list_courses.py <learner_dir> <courses_dir> [--status S] [--level N] [--standalone] [--compact]"}))
        return 2
    return cli.emit(build(args[0], args[1], **opts))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
