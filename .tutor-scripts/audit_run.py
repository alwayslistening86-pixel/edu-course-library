#!/usr/bin/env python3
"""
audit_run.py -- the whole deterministic audit of a course library as one JSON report, with a diff against the previous report (K-14). Read-only.

    python3 audit_run.py <courses_dir> [--today YYYY-MM-DD] [--out <report.json>] [--compare <previous report.json>]

Runs, per course folder, everything the course-auditor's mechanical tiers check: `postcompile_gate` (structure, coverage, injection scan,
test-integrity, rubric and change.md notes), `validate_schema --course-dir`, `rubric_lint`, `change_log` and `audit_status`'s reasons. Nothing is fixed or
written in the library. `--out` saves the report (put it OUTSIDE the courses folder, e.g. `<edu root>/audit/last_report.json`); `--compare`
adds `changes` listing, per course, problems that are new and problems that are gone since the earlier report.

Report: {report_version, engine_version, today, courses_checked, totals{can_ship, blocked, schema_invalid, audit_recommended, blocking_findings, advisory_findings},
courses{<id>: {can_ship, blocking[], advisory_count, schema_invalid[], rubric{findings, label_only_stages}, change_log{entries, problems[]}, audit_reasons[]}}, changes?}.
Judgement items (is the source still live? is the itemisation faithful?) stay with the auditor; this is only the part code can decide.
"""
import json
import os
import sys

import audit_status
import change_log
import postcompile_gate
import rubric_lint
import validate_schema
from tutorlib import cli, version

REPORT_VERSION = 1


def audit_course(course_dir, engine):
    gate = postcompile_gate._gate(course_dir)
    schema_res = validate_schema.check_course_dir(course_dir)
    rub = rubric_lint.lint(course_dir)
    chg = change_log.read(course_dir)
    course = {}
    try:
        with open(os.path.join(course_dir, "course.json"), encoding="utf-8") as f:
            course = json.load(f)
    except (OSError, ValueError):
        pass
    return {
        "can_ship": bool(gate.get("can_ship")),
        "blocking": [str(b)[:200] for b in gate.get("blocking_reasons", [])],
        "advisory_count": len(gate.get("advisory_notes", [])),
        "schema_invalid": [f"{i['file']}: {i['errors'][0]}" for i in schema_res.get("invalid", [])] if "error" not in schema_res else [schema_res["error"]],
        "rubric": {"findings": rub.get("finding_count", 0), "label_only_stages": rub.get("by_rule", {}).get("label_only_stage", 0)},
        "change_log": {"entries": chg.get("entry_count", 0), "problems": [p["rule"] for p in chg.get("problems", [])]},
        "audit_reasons": audit_status.course_reasons(course, engine) if course else ["unreadable"],
    }


def problems_of(entry):
    out = {f"blocking: {b}" for b in entry["blocking"]} | {f"schema: {s}" for s in entry["schema_invalid"]}
    out |= {f"change.md: {p}" for p in entry["change_log"]["problems"]} | {f"audit: {r}" for r in entry["audit_reasons"]}
    if entry["rubric"]["label_only_stages"]:
        out.add(f"rubric: {entry['rubric']['label_only_stages']} label-only stage(s)")
    return out


def run(courses_dir, today=None, previous=None):
    if not os.path.isdir(courses_dir):
        return {"error": f"FileNotFoundError: courses_dir does not exist: {courses_dir}"}
    engine = version.engine_version()
    courses = {}
    for cid in sorted(os.listdir(courses_dir)):
        cdir = os.path.join(courses_dir, cid)
        if os.path.isfile(os.path.join(cdir, "course.json")):
            courses[cid] = audit_course(cdir, engine)
    totals = {
        "can_ship": sum(1 for c in courses.values() if c["can_ship"]), "blocked": sum(1 for c in courses.values() if not c["can_ship"]),
        "schema_invalid": sum(1 for c in courses.values() if c["schema_invalid"]), "audit_recommended": sum(1 for c in courses.values() if c["audit_reasons"]),
        "blocking_findings": sum(len(c["blocking"]) for c in courses.values()), "advisory_findings": sum(c["advisory_count"] for c in courses.values()),
    }
    report = {"report_version": REPORT_VERSION, "engine_version": ".".join(map(str, engine)) if engine else None, "today": today,
              "courses_checked": len(courses), "totals": totals, "courses": courses}
    if previous is not None:
        changes = {}
        for cid in sorted(set(courses) | set(previous.get("courses", {}))):
            now = problems_of(courses[cid]) if cid in courses else set()
            before = problems_of(previous["courses"][cid]) if cid in previous.get("courses", {}) else set()
            if now != before or (cid in courses) != (cid in previous.get("courses", {})):
                changes[cid] = {"new": sorted(now - before), "resolved": sorted(before - now)}
                if cid not in courses:
                    changes[cid]["course_removed"] = True
                if cid not in previous.get("courses", {}):
                    changes[cid]["course_added"] = True
        report["changes"] = changes
    return report


def main(argv):
    args = list(argv)
    opts = {}
    for flag in ("--today", "--out", "--compare"):
        if flag in args:
            i = args.index(flag)
            if i + 1 >= len(args):
                print(json.dumps({"error": f"{flag} needs a value"}))
                return 2
            opts[flag] = args[i + 1]
            del args[i:i + 2]
    if len(args) != 1:
        print(json.dumps({"error": "usage: audit_run.py <courses_dir> [--today YYYY-MM-DD] [--out <report.json>] [--compare <previous.json>]"}))
        return 2
    previous = None
    if "--compare" in opts:
        try:
            with open(opts["--compare"], encoding="utf-8") as f:
                previous = json.load(f)
        except (OSError, ValueError) as e:
            print(json.dumps({"error": f"FileNotFoundError: cannot read the previous report: {e}"}))
            return 1
    report = run(args[0], opts.get("--today"), previous)
    if "error" not in report and "--out" in opts:
        out = os.path.abspath(opts["--out"])
        if os.path.commonpath([out, os.path.abspath(args[0])]) == os.path.abspath(args[0]):
            print(json.dumps({"error": "write the report outside the courses folder (course content stays free of audit output)"}))
            return 1
        os.makedirs(os.path.dirname(out), exist_ok=True)
        from tutorlib import atomic_io
        atomic_io.write_json(out, report)
        report["saved_to"] = out
    return cli.emit(report)


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
