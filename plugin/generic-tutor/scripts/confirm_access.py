#!/usr/bin/env python3
"""
confirm_access.py -- record the learner's one-time answer to "connect this folder isolated, or proceed under the shared connection?"

    python3 confirm_access.py <folder> <isolated|shared> <today YYYY-MM-DD>

Writes `<folder>/access.json` = {"status": "isolated_confirmed"|"shared_confirmed", "confirmed_on": <today>} atomically.
`<folder>` is the courses folder (`/EDU/courses`) or the profile folder (`/EDU/profile`). One answer covers every course in the
library: `gate_check.py` accepts a confirmed `courses/access.json` in place of a per-course `folder_access` (the 54 of 62 real courses that
ship as `pending_confirmation` would otherwise each ask the same question again). A course's own confirmed status still counts.
Only run this after the learner has actually answered; it does not decide anything.
"""
import datetime
import json
import os
import sys

from tutorlib import cli, state

STATUS = {"isolated": "isolated_confirmed", "shared": "shared_confirmed"}


def confirm(folder, choice, today_iso):
    if choice not in STATUS:
        return {"error": f"choice must be one of {tuple(STATUS)}, got {choice!r}"}
    try:
        datetime.date.fromisoformat(today_iso)
    except (TypeError, ValueError):
        return {"error": "today must be a valid ISO date (YYYY-MM-DD)"}
    if not os.path.isdir(folder):
        return {"error": f"FileNotFoundError: folder does not exist: {folder}"}
    path = os.path.join(folder, "access.json")
    previous = None
    if os.path.isfile(path):
        try:
            with open(path, encoding="utf-8") as f:
                previous = json.load(f).get("status")
        except (OSError, ValueError, AttributeError):
            previous = None
    state.save(path, {"status": STATUS[choice], "confirmed_on": today_iso}, "access")
    return {"folder": folder, "status": STATUS[choice], "previous_status": previous, "written": True}


def library_status(courses_dir):
    """The confirmed status recorded for a courses folder, or None."""
    try:
        with open(os.path.join(courses_dir, "access.json"), encoding="utf-8") as f:
            status = json.load(f).get("status")
    except (OSError, ValueError, AttributeError, TypeError):
        return None
    return status if status in STATUS.values() else None


def main(argv):
    if len(argv) != 3:
        print(json.dumps({"error": "usage: confirm_access.py <folder> <isolated|shared> <today YYYY-MM-DD>"}))
        return 2
    return cli.emit(confirm(*argv))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
