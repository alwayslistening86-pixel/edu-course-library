#!/usr/bin/env python3
"""
plan_target.py -- record or clear a learner's OPTIONAL target date for a course (L-12).

    python3 plan_target.py set   <subjects.json> <YYYY-MM-DD> <today YYYY-MM-DD>
    python3 plan_target.py clear <subjects.json>

Stores `target: {"date": ..., "set_on": ...}` in the learner's subjects file - the one place a calendar date appears in the
system, and only because the learner asked for deadline-aware planning (everything else stays in session slots). It is not a
schedule: nothing is placed on a calendar, and `plan_estimate.py` only compares remaining slots with the slots the learner's
stated rate would give before that date. A target more than 14 days in the past is treated as expired (reported, ignored for
planning); re-setting replaces it. Refuses dates that are not valid ISO dates or are already in the past.
Consent class: progress (functional bookkeeping the learner chose to give), written atomically under the file lock and ledgered.
"""
import datetime
import json
import sys

from tutorlib import atomic_io, cli, consent, filelock, ledger, state


def _date(s):
    try:
        return datetime.date.fromisoformat(s)
    except (TypeError, ValueError):
        return None


@ledger.logged("plan_target.py", "subjects_path")
@filelock.locked("subjects_path")
def set_target(subjects_path, date_iso, today_iso):
    d, today = _date(date_iso), _date(today_iso)
    if d is None or today is None:
        return {"error": "dates must be valid ISO dates (YYYY-MM-DD)"}
    if d < today:
        return {"error": f"{date_iso} is already in the past (today is {today_iso})"}
    data = state.load(subjects_path, "subjects")
    data["target"] = {"date": date_iso, "set_on": today_iso}
    allowed, status = consent.check(subjects_path, consent.PROGRESS)
    if not allowed:
        return {"action": "set", "target": data["target"], **consent.skipped(status, consent.PROGRESS)}
    atomic_io.write_json(subjects_path, data)
    return {"action": "set", "target": data["target"], "written": True}


@ledger.logged("plan_target.py", "subjects_path")
@filelock.locked("subjects_path")
def clear_target(subjects_path):
    data = state.load(subjects_path, "subjects")
    had = "target" in data
    if had:
        data.pop("target")
        allowed, status = consent.check(subjects_path, consent.PROGRESS)
        if not allowed:
            return {"action": "clear", "had_target": True, **consent.skipped(status, consent.PROGRESS)}
        atomic_io.write_json(subjects_path, data)
    return {"action": "clear", "had_target": had, "written": had}


def main(argv):
    try:
        if len(argv) == 4 and argv[0] == "set":
            return cli.emit(set_target(argv[1], argv[2], argv[3]))
        if len(argv) == 2 and argv[0] == "clear":
            return cli.emit(clear_target(argv[1]))
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1
    print(json.dumps({"error": "usage: plan_target.py set <subjects.json> <YYYY-MM-DD> <today> | clear <subjects.json>"}))
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
