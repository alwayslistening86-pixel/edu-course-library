#!/usr/bin/env python3
"""
currency_report.py -- which courses need their sources looked at again? (N-10) Read-only, no network.

    python3 currency_report.py <courses_dir> [--today YYYY-MM-DD] [--stale-days N]

Reads each course's `source_snapshots.json` (written by `verify_sources.py --write`) and `course.json.last_live_recheck`, and reports, most urgent first:
  dead         a cited URL answered 404/410 or its host is gone (the rubric may now cite nothing; `/audit` grounding decides)
  changed      a cited page's hash differs from the previous check (look again; it does not prove the specification changed)
  never        the course has no snapshot at all
  stale        the newest check is older than --stale-days (default 120), or the last live recheck is
  blocked      every check failed on access (a network or site that refuses us), so nothing is known
Report only: it changes no course, schedules nothing and fetches nothing. To refresh the evidence run `verify_sources.py <course_dir> --write` per course
from a machine that can reach the sources (for a private content repository, a scheduled CI job or a monthly manual run), then run this.
"""
import datetime
import json
import os
import sys

import verify_sources
from tutorlib import cli

STALE_DAYS = 120
ORDER = ("dead", "changed", "never", "stale", "blocked")


def _days(today, then):
    try:
        return (datetime.date.fromisoformat(today) - datetime.date.fromisoformat(then)).days
    except (TypeError, ValueError):
        return None


def course_status(course_dir, today, stale_days):
    snaps = verify_sources.load_snapshots(course_dir)["snapshots"]
    flags, detail = [], {}
    try:
        with open(os.path.join(course_dir, "course.json"), encoding="utf-8") as f:
            recheck = json.load(f).get("last_live_recheck")
    except (OSError, ValueError):
        recheck = None
    if not snaps:
        flags.append("never")
    else:
        dead = [u for u, s in snaps.items() if s.get("status") == "dead"]
        changed = [u for u, s in snaps.items() if s.get("changed")]
        if dead:
            flags.append("dead")
            detail["dead"] = dead[:3]
        if changed:
            flags.append("changed")
            detail["changed"] = changed[:3]
        if all(s.get("status") in ("blocked", "error") for s in snaps.values()):
            flags.append("blocked")
        newest = max((s.get("checked_on") or "" for s in snaps.values()), default="")
        age = _days(today, newest)
        if age is not None and age > stale_days:
            flags.append("stale")
            detail["days_since_check"] = age
    age_recheck = _days(today, recheck) if recheck else None
    if recheck is None or (age_recheck is not None and age_recheck > stale_days):
        if "stale" not in flags:
            flags.append("stale")
        detail["days_since_live_recheck"] = age_recheck
    flags.sort(key=ORDER.index)
    return {"flags": flags, "urls": len(snaps), **detail}


def run(courses_dir, today=None, stale_days=STALE_DAYS):
    if not os.path.isdir(courses_dir):
        return {"error": f"FileNotFoundError: no courses folder at {courses_dir}"}
    today = today or datetime.date.today().isoformat()
    rows = []
    for cid in sorted(os.listdir(courses_dir)):
        if os.path.isfile(os.path.join(courses_dir, cid, "course.json")):
            st = course_status(os.path.join(courses_dir, cid), today, stale_days)
            if st["flags"]:
                rows.append({"course_id": cid, **st})
    rows.sort(key=lambda r: (ORDER.index(r["flags"][0]), r["course_id"]))
    counts = {k: sum(k in r["flags"] for r in rows) for k in ORDER}
    return {"checked_on": today, "stale_days": stale_days, "courses_needing_attention": len(rows), "counts": counts, "courses": rows}


def main(argv):
    args, today, stale = list(argv), None, STALE_DAYS
    for flag in ("--today", "--stale-days"):
        if flag in args:
            i = args.index(flag)
            if i + 1 >= len(args):
                print(json.dumps({"error": f"{flag} needs a value"}))
                return 2
            if flag == "--today":
                today = args[i + 1]
            else:
                try:
                    stale = int(args[i + 1])
                except ValueError:
                    print(json.dumps({"error": "--stale-days needs a whole number"}))
                    return 2
            del args[i:i + 2]
    if len(args) != 1:
        print(json.dumps({"error": "usage: currency_report.py <courses_dir> [--today YYYY-MM-DD] [--stale-days N]"}))
        return 2
    return cli.emit(run(args[0], today, stale))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
