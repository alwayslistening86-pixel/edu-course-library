#!/usr/bin/env python3
"""
purge_history.py -- selective, irreversible deletion short of a full /erase (X-05).

    python3 purge_history.py <profile_root> <user_id> history              [--confirm "PURGE <user_id> history"]
    python3 purge_history.py <profile_root> <user_id> course <course_id>   [--confirm "PURGE <user_id> <course_id>"]

  history   deletes the analytics history (`tutor.sqlite3` and its -wal/-shm files) and the write ledger (`.session_ledger.jsonl`).
            Current progress files, review decks and the profile are untouched: teaching continues exactly where it was; only the
            record of *how* it got there is gone (a new history starts from the next event).
  course    removes ONE course's enrolment: `subjects/<course_id>.json`, its review deck, that course's rows in the history database,
            and that course's lines in the write ledger. The profile, other courses and `highest_level_cleared` are untouched. To pause a
            course without deleting anything use /drop instead.

Without --confirm nothing is deleted: it reports what WOULD go and the phrase required. The phrase must be typed by the learner.
Refuses an invalid user or course id and symlinked targets. Full deletion of everything is erase_profile.py.
"""
import json
import os
import sqlite3
import sys

from tutorlib import atomic_io, cli, filelock, ids, ledger, paths

_COURSE_TABLES = ("error_events", "item_mastery", "item_mastery_log", "review_cards", "confidence_events")


def _targets_history(d):
    names = ["tutor.sqlite3", "tutor.sqlite3-wal", "tutor.sqlite3-shm", ledger.LEDGER_NAME]
    return [n for n in names if os.path.exists(os.path.join(d, n))]


def _count_rows(db, course_id):
    counts = {}
    con = sqlite3.connect(db)
    try:
        for t in _COURSE_TABLES:
            try:
                counts[t] = con.execute(f"SELECT COUNT(*) FROM {t} WHERE course_id = ?", (course_id,)).fetchone()[0]
            except sqlite3.Error:
                counts[t] = 0
    finally:
        con.close()
    return counts


def _ledger_lines(d, course_id):
    return sum(1 for e in ledger.read(d) if e.get("course_id") == course_id)


def purge(profile_root, user_id, what, course_id=None, confirm=None):
    try:
        d = paths.learner_dir(profile_root, user_id)
        if what == "course":
            ids.validate(course_id or "", "course id")
    except (ValueError, ids.InvalidId) as e:
        return {"purged": False, "error": str(e)}
    if what not in ("history", "course"):
        return {"purged": False, "error": "what must be 'history' or 'course'"}
    if not os.path.isdir(d):
        return {"purged": False, "error": f"no profile folder for {user_id!r}"}
    expected = f"PURGE {user_id} {'history' if what == 'history' else course_id}"
    db = os.path.join(d, "tutor.sqlite3")
    if what == "history":
        plan = {"what": "history", "files": _targets_history(d)}
    else:
        subj = [n for n in (f"{course_id}.json", f"{course_id}_review_deck.json") if os.path.exists(os.path.join(d, "subjects", n))]
        if not subj:
            return {"purged": False, "error": f"{course_id!r} is not enrolled for {user_id!r}"}
        plan = {"what": "course", "course_id": course_id, "files": [os.path.join("subjects", n) for n in subj],
                "history_rows": _count_rows(db, course_id) if os.path.exists(db) else {}, "ledger_lines": _ledger_lines(d, course_id)}
    for rel in plan["files"]:
        if os.path.islink(os.path.join(d, rel)):
            return {"purged": False, "error": f"refusing symlinked target {rel}"}
    if confirm is None:
        return {**plan, "purged": False, "dry_run": True, "required_confirmation": expected}
    if confirm != expected:
        return {**plan, "purged": False, "error": f"confirmation must be exactly {expected!r}"}

    if what == "history":
        for rel in plan["files"]:
            os.remove(os.path.join(d, rel))
        return {**plan, "purged": True}
    with filelock.file_lock(os.path.join(d, "student_profile.json")):
        for rel in plan["files"]:
            os.remove(os.path.join(d, rel))
        if os.path.exists(db):
            con = sqlite3.connect(db)
            try:
                con.execute("DELETE FROM review_log WHERE course_id = ? OR (course_id IS NULL AND card_id IN (SELECT id FROM review_cards WHERE course_id = ?))", (course_id, course_id))
                for t in _COURSE_TABLES:
                    con.execute(f"DELETE FROM {t} WHERE course_id = ?", (course_id,))
                con.commit()
            except sqlite3.Error as e:
                return {**plan, "purged": True, "warning": f"files removed but the history database could not be cleaned: {e}"}
            finally:
                con.close()
        lp = os.path.join(d, ledger.LEDGER_NAME)
        if os.path.exists(lp):
            keep = [e for e in ledger.read(d) if e.get("course_id") != course_id and "corrupt" not in e]
            tmp = lp + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                for e in keep:
                    f.write(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n")
            atomic_io.replace(tmp, lp)
    return {**plan, "purged": True}


def main(argv):
    args = list(argv)
    confirm = None
    if "--confirm" in args:
        i = args.index("--confirm")
        if i + 1 >= len(args):
            print(json.dumps({"purged": False, "error": "--confirm needs a value"}))
            return 1
        confirm = args[i + 1]
        del args[i:i + 2]
    try:
        if len(args) == 3 and args[2] == "history":
            return cli.emit(purge(args[0], args[1], "history", None, confirm))
        if len(args) == 4 and args[2] == "course":
            return cli.emit(purge(args[0], args[1], "course", args[3], confirm))
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1
    print(json.dumps({"error": 'usage: purge_history.py <profile_root> <user_id> history | course <course_id> [--confirm "PURGE <user_id> history|<course_id>"]'}))
    return 2


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
