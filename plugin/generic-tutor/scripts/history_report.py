#!/usr/bin/env python3
"""
history_report.py -- read-only canned reports over a learner's append-only history database (E-16).

    python3 history_report.py <mastery|ease|errors> <learner_dir> [--course <course_id>]

  mastery  per item: observations, first -> latest p_mastery, change, latest correct/incorrect (trend over the slots seen)
  ease     per review card: reviews, first -> latest ease, current interval, lapses, wrong answers (ease drift)
  errors   per course/stage/item/cause: how often it happened, how many are still open, last slot; recurring misconceptions first

Nothing here is read back into a teaching decision (the JSON files stay authoritative); it answers questions for
course-auditor and for a human. The database is opened read-only; a missing database is reported, not created.
Output is sorted so it is stable. `<learner_dir>` is the learner's profile folder (the one holding `tutor.sqlite3`).
"""
import json
import os
import sqlite3
import sys

from tutorlib import cli

REPORTS = ("mastery", "ease", "errors")


def _connect(learner_dir):
    path = os.path.join(learner_dir, "tutor.sqlite3")
    if not os.path.isfile(path):
        return None
    con = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def _where(course, column="course_id"):
    return (f" WHERE {column} = ?", (course,)) if course else ("", ())


def mastery(con, course=None):
    w, args = _where(course)
    rows = con.execute(f"SELECT course_id, item_id, correct, new_p_mastery, prior, slot, id FROM item_mastery_log{w} ORDER BY course_id, item_id, slot, id", args).fetchall()
    out, cur = [], {}
    for r in rows:
        key = (r["course_id"], r["item_id"])
        e = cur.setdefault(key, {"course_id": key[0], "item_id": key[1], "observations": 0, "first_p": round(r["prior"], 4), "correct": 0})
        e["observations"] += 1
        e["correct"] += r["correct"]
        e["latest_p"] = round(r["new_p_mastery"], 4)
        e["last_slot"] = r["slot"]
        e["last_correct"] = bool(r["correct"])
    for e in cur.values():
        e["change"] = round(e["latest_p"] - e["first_p"], 4)
        e["trend"] = "up" if e["change"] > 0.05 else "down" if e["change"] < -0.05 else "flat"
        out.append(e)
    return {"report": "mastery", "items": sorted(out, key=lambda e: (e["course_id"], e["item_id"]))}


def ease(con, course=None):
    w, args = _where(course, "c.course_id")
    cards = con.execute(f"SELECT c.id, c.course_id, c.stage_id, c.interval_sessions, c.ease, c.lapses FROM review_cards c{w} ORDER BY c.course_id, c.id", args).fetchall()
    out = []
    for c in cards:
        log = con.execute("SELECT correct, old_ease, new_ease FROM review_log WHERE card_id = ? AND (course_id = ? OR course_id IS NULL) ORDER BY slot, id",
                          (c["id"], c["course_id"])).fetchall()
        if not log:
            continue
        out.append({
            "course_id": c["course_id"], "card_id": c["id"], "stage_id": c["stage_id"], "reviews": len(log),
            "wrong": sum(1 for r in log if not r["correct"]), "first_ease": round(log[0]["old_ease"], 3),
            "latest_ease": round(log[-1]["new_ease"], 3), "ease_change": round(log[-1]["new_ease"] - log[0]["old_ease"], 3),
            "interval_sessions": c["interval_sessions"], "lapses": c["lapses"],
        })
    return {"report": "ease", "cards": out}


def errors(con, course=None):
    w, args = _where(course)
    rows = con.execute(
        f"SELECT course_id, stage_id, COALESCE(item_id, '') AS item_id, cause, COALESCE(misconception_id, '') AS misconception_id, "
        f"COUNT(*) AS n, SUM(1 - resolved) AS open_n, MAX(slot) AS last_slot FROM error_events{w} "
        "GROUP BY course_id, stage_id, item_id, cause, misconception_id", args).fetchall()
    out = [{"course_id": r["course_id"], "stage_id": r["stage_id"], "item_id": r["item_id"] or None, "cause": r["cause"],
            "misconception_id": r["misconception_id"] if r["misconception_id"] not in ("", "NONE") else None,
            "count": r["n"], "open": r["open_n"], "last_slot": r["last_slot"], "recurring": r["n"] >= 2} for r in rows]
    out.sort(key=lambda e: (-e["count"], e["course_id"], e["stage_id"], e["item_id"] or "", e["cause"]))
    return {"report": "errors", "groups": out, "recurring_groups": sum(1 for e in out if e["recurring"])}


def run(report, learner_dir, course=None):
    if report not in REPORTS:
        return {"error": f"report must be one of {REPORTS}, got {report!r}"}
    con = _connect(learner_dir)
    if con is None:
        return {"error": f"no history database in {learner_dir} (it is created when scripts first log an event)"}
    try:
        return globals()[report](con, course)
    finally:
        con.close()


def main():
    args = sys.argv[1:]
    course = None
    if "--course" in args:
        i = args.index("--course")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--course needs a value"}))
            sys.exit(2)
        course = args[i + 1]
        del args[i:i + 2]
    if len(args) != 2:
        print(json.dumps({"error": "usage: history_report.py <mastery|ease|errors> <learner_dir> [--course <course_id>]"}))
        sys.exit(2)
    try:
        out = run(args[0], args[1], course)
    except sqlite3.Error as e:
        print(json.dumps({"error": f"history database unreadable: {e}"}))
        sys.exit(1)
    sys.exit(cli.emit(out))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
