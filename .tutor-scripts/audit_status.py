#!/usr/bin/env python3
"""
audit_status.py -- the "an audit is recommended" check, decided by code instead of prose (K-15). Read-only.

    python3 audit_status.py <courses_dir>

A course is flagged when:
  unreadable        course.json cannot be read as JSON
  old_schema        its schema_version is older than this engine's course schema (migrate_schema.py would change it)
  never_audited     no `last_audited_plugin_version`
  audited_earlier   `last_audited_plugin_version` is an earlier major.minor than the running engine (patch releases do not count)
  never_rechecked   `last_live_recheck` missing on a course whose currency is not "historical"
The engine version comes from the deployed manifest / plugin.json (tutorlib.version). If it cannot be determined, the
audited_earlier test is skipped. Passive by design: this reports; applying anything is `/audit`.
"""
import json
import os
import sys

from migrate_schema import COURSE_SCHEMA_VERSION
from tutorlib import cli, version


def course_reasons(course, engine):
    reasons = []
    sv = course.get("schema_version")
    if not isinstance(sv, int) or sv < COURSE_SCHEMA_VERSION:
        reasons.append("old_schema")
    audited = course.get("last_audited_plugin_version")
    if not audited:
        reasons.append("never_audited")
    elif engine is not None:
        parsed = version.parse(audited)
        if parsed is None or parsed[:2] < engine[:2]:
            reasons.append("audited_earlier")
    if not course.get("last_live_recheck") and course.get("currency") != "historical":
        reasons.append("never_rechecked")
    return reasons


def audit_status(courses_dir, scripts_dir=None):
    if not os.path.isdir(courses_dir):
        return {"error": f"courses_dir does not exist: {courses_dir}"}
    engine = version.engine_version(scripts_dir)
    rows = []
    for cid in sorted(os.listdir(courses_dir)):
        path = os.path.join(courses_dir, cid, "course.json")
        if not os.path.isfile(path):
            continue
        try:
            with open(path, encoding="utf-8") as f:
                course = json.load(f)
            reasons = course_reasons(course, engine) if isinstance(course, dict) else ["unreadable"]
        except (OSError, ValueError):
            reasons = ["unreadable"]
        if reasons:
            rows.append({"course_id": cid, "reasons": reasons})
    checked = sum(1 for c in os.listdir(courses_dir) if os.path.isfile(os.path.join(courses_dir, c, "course.json")))
    return {"engine_version": ".".join(map(str, engine)) if engine else None, "courses_checked": checked,
            "audit_recommended": bool(rows), "affected_count": len(rows), "affected": rows}


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: audit_status.py <courses_dir>"}))
        sys.exit(2)
    sys.exit(cli.emit(audit_status(sys.argv[1])))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
