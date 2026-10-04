#!/usr/bin/env python3
"""
sqlite_store.py — wires schema_design.sql into real, additive, per-learner
history tables, and closes a specific structural gap the library owner
flagged directly: confidence and review-card updates were, until this
version, the one place in the plugin where "the model computes a value and
is trusted to write it back" was the *entire* mechanism — no script ever
performed or verified the write, unlike every other piece of learner state
(`error_log.py`, `item_mastery.py`, `gate_check.py`'s callers, etc. all
have a script that owns the actual file write).

Two things ship together here, deliberately:

1. **SQLite history tables**, per `schema_design.sql` (schema unchanged
   from that design, this file just creates and writes it for real): one
   file per learner, `<learner_dir>/tutor.sqlite3`, holding `error_events`,
   `item_mastery` + `item_mastery_log`, `review_cards` + `review_log`, and
   `confidence_events`. JSON under `subjects/<course_id>.json` and the
   `*_review_deck.json` files remain the live source of truth for
   *current* state — nothing here is ever read back into a teaching
   decision. This is purely an additive, queryable history a human or
   `course-auditor` can ask real questions against later
   ("is this item actually trending up", "how has this card's ease moved
   over a term") that a snapshot-only JSON file can't answer.

2. **`review_math.py apply` and `confidence_update.py apply`** (added in
   the same version, in their own files) now perform the read-modify-write
   against the JSON file themselves, the same way `error_log.py` and
   `item_mastery.py` always have — closing the write-back gap above. The
   old pure-calculator subcommands (`review_math.py` positional-args form,
   `confidence_update.py compute`) still exist unchanged, for testing and
   for any caller that genuinely only wants the arithmetic; but
   `course-runner.md` and `review-scheduler.md` are updated in this same
   version to call `apply` instead of hand-writing the result back
   themselves.

Every write function here is best-effort and NEVER raises past its own
try/except: a SQLite failure (disk full, a locked file, a corrupt db) must
never block or roll back the JSON write, which stays authoritative. Callers
get `{"ok": true}` or `{"ok": false, "error": "..."}` back and can surface
it, but nothing here throws.

Functions (all take `subjects_path` — the path to `subjects/<course_id>.json`,
or for review functions, the path to `<course_id>_review_deck.json` — and
derive both the learner's db path and the course_id from it):
    learner_db_path(any_profile_path) -> str
    log_error_event(subjects_path, entry: dict) -> dict
    resolve_error_events(subjects_path, entry_ids: list[str], resolved_at_slot: int) -> dict
    log_item_mastery_observation(subjects_path, item_id, correct, prior, posterior, new_p_mastery, slot) -> dict
    upsert_review_card(subjects_path, card: dict) -> dict
    log_review_pass(subjects_path, card_id, correct, old_interval, new_interval, old_ease, new_ease, slot) -> dict
    log_confidence_event(subjects_path, event_type, misconception, delta, confidence_after, slot) -> dict
    backfill(learner_dir) -> dict   # one-time: current-state snapshot only, see its own docstring

Not a subcommand-driven script like its siblings — this is a library
imported by error_log.py, item_mastery.py, review_math.py and
confidence_update.py. It has no `main()` and is not meant to be invoked
directly, though `python3 sqlite_store.py backfill <learner_dir>` is
provided for the one-time manual migration of an existing learner folder.
"""
import json
import os
import sqlite3
import sys

from tutorlib import consent

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS error_events (
  id                TEXT PRIMARY KEY,
  course_id         TEXT NOT NULL,
  stage_id          TEXT NOT NULL,
  item_id           TEXT,
  source_phase      TEXT NOT NULL CHECK (source_phase IN ('practice','test')),
  cause             TEXT NOT NULL CHECK (cause IN
                      ('slip','missing_prerequisite','misconception',
                       'misapplied_procedure','comprehension')),
  misconception_id  TEXT,
  rubric_criterion  TEXT,
  note              TEXT,
  slot              INTEGER NOT NULL,
  resolved          INTEGER NOT NULL DEFAULT 0 CHECK (resolved IN (0,1)),
  resolved_at_slot  INTEGER,
  created_at        TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_error_events_lookup ON error_events (course_id, stage_id, item_id, cause);
CREATE INDEX IF NOT EXISTS idx_error_events_unresolved ON error_events (course_id, resolved) WHERE resolved = 0;

CREATE TABLE IF NOT EXISTS item_mastery (
  course_id     TEXT NOT NULL,
  item_id       TEXT NOT NULL,
  p_mastery     REAL NOT NULL CHECK (p_mastery BETWEEN 0 AND 1),
  observations  INTEGER NOT NULL DEFAULT 0,
  last_slot     INTEGER,
  last_correct  INTEGER CHECK (last_correct IN (0,1)),
  PRIMARY KEY (course_id, item_id)
);

CREATE TABLE IF NOT EXISTS item_mastery_log (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id     TEXT NOT NULL,
  item_id       TEXT NOT NULL,
  correct       INTEGER NOT NULL CHECK (correct IN (0,1)),
  prior         REAL NOT NULL,
  posterior     REAL NOT NULL,
  new_p_mastery REAL NOT NULL,
  slot          INTEGER NOT NULL,
  created_at    TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_item_mastery_log_item ON item_mastery_log (course_id, item_id, slot);

CREATE TABLE IF NOT EXISTS review_cards (
  id                TEXT PRIMARY KEY,
  course_id         TEXT NOT NULL,
  stage_id          TEXT NOT NULL,
  item_id           TEXT,
  criterion         TEXT,
  front             TEXT NOT NULL,
  back              TEXT NOT NULL,
  interval_sessions INTEGER NOT NULL,
  due_at_slot       INTEGER NOT NULL,
  ease              REAL NOT NULL,
  lapses            INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS idx_review_cards_due ON review_cards (course_id, due_at_slot);

CREATE TABLE IF NOT EXISTS review_log (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  card_id           TEXT NOT NULL,
  correct           INTEGER NOT NULL CHECK (correct IN (0,1)),
  old_interval      INTEGER NOT NULL,
  new_interval      INTEGER NOT NULL,
  old_ease          REAL NOT NULL,
  new_ease          REAL NOT NULL,
  slot              INTEGER NOT NULL,
  created_at        TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_review_log_card ON review_log (card_id, slot);

CREATE TABLE IF NOT EXISTS confidence_events (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id         TEXT NOT NULL,
  slot              INTEGER NOT NULL,
  event_type        TEXT NOT NULL CHECK (event_type IN
                      ('pass_clean','pass_remediated','fail')),
  misconception     INTEGER NOT NULL DEFAULT 0 CHECK (misconception IN (0,1)),
  delta             REAL NOT NULL,
  confidence_after  REAL NOT NULL CHECK (confidence_after BETWEEN 0 AND 1),
  created_at        TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_confidence_events_course ON confidence_events (course_id, slot);
"""


def learner_db_path(any_profile_path):
    """Given any file path under a learner's /EDU/profile/<learner_id>/... tree
    (subjects/<course_id>.json or subjects/<course_id>_review_deck.json), return
    the path to that learner's tutor.sqlite3, sitting one level above 'subjects/'.
    """
    subjects_dir = os.path.dirname(os.path.abspath(any_profile_path))
    learner_dir = os.path.dirname(subjects_dir)
    return os.path.join(learner_dir, "tutor.sqlite3")


def _course_id_from_path(subjects_or_deck_path):
    base = os.path.basename(subjects_or_deck_path)
    name = base[:-5] if base.endswith(".json") else base
    if name.endswith("_review_deck"):
        name = name[: -len("_review_deck")]
    return name


def _connect(any_profile_path):
    db_path = learner_db_path(any_profile_path)
    con = sqlite3.connect(db_path, timeout=5)
    con.executescript(SCHEMA)
    return con


def _safe(kind=consent.SIGNAL):
    """Never raises; also enforces learner consent (first argument is a path under the learner folder)."""
    def deco(fn):
        def wrapped(*args, **kwargs):
            try:
                allowed, cstatus = consent.check(args[0], kind)
                if not allowed:
                    return {"ok": True, "written": False, "skipped": f"consent {cstatus}: {kind} writes are not persisted"}
                return fn(*args, **kwargs)
            except Exception as e:  # noqa: BLE001 - deliberately broad: this must never propagate
                return {"ok": False, "error": f"{type(e).__name__}: {e}"}
        wrapped.__name__ = fn.__name__
        wrapped.__doc__ = fn.__doc__
        return wrapped
    return deco


@_safe()
def log_error_event(subjects_path, entry):
    course_id = _course_id_from_path(subjects_path)
    con = _connect(subjects_path)
    try:
        con.execute(
            """INSERT OR REPLACE INTO error_events
               (id, course_id, stage_id, item_id, source_phase, cause,
                misconception_id, rubric_criterion, note, slot, resolved, resolved_at_slot)
               VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                entry["id"], course_id, entry["stage_id"], entry.get("item_id"),
                entry["source_phase"], entry["cause"], entry.get("misconception_id"),
                entry.get("rubric_criterion"), entry.get("note"), entry["slot"],
                int(bool(entry.get("resolved", False))), entry.get("resolved_at_slot"),
            ),
        )
        con.commit()
    finally:
        con.close()
    return {"ok": True}


@_safe()
def resolve_error_events(subjects_path, entry_ids, resolved_at_slot):
    if not entry_ids:
        return {"ok": True, "updated": 0}
    con = _connect(subjects_path)
    try:
        con.executemany(
            "UPDATE error_events SET resolved = 1, resolved_at_slot = ? WHERE id = ?",
            [(int(resolved_at_slot), eid) for eid in entry_ids],
        )
        con.commit()
    finally:
        con.close()
    return {"ok": True, "updated": len(entry_ids)}


@_safe()
def log_item_mastery_observation(subjects_path, item_id, correct, prior, posterior, new_p_mastery, slot):
    course_id = _course_id_from_path(subjects_path)
    con = _connect(subjects_path)
    try:
        con.execute(
            """INSERT INTO item_mastery (course_id, item_id, p_mastery, observations, last_slot, last_correct)
               VALUES (?,?,?,1,?,?)
               ON CONFLICT(course_id, item_id) DO UPDATE SET
                 p_mastery = excluded.p_mastery,
                 observations = item_mastery.observations + 1,
                 last_slot = excluded.last_slot,
                 last_correct = excluded.last_correct""",
            (course_id, item_id, new_p_mastery, int(slot), int(bool(correct))),
        )
        con.execute(
            """INSERT INTO item_mastery_log
               (course_id, item_id, correct, prior, posterior, new_p_mastery, slot)
               VALUES (?,?,?,?,?,?,?)""",
            (course_id, item_id, int(bool(correct)), prior, posterior, new_p_mastery, int(slot)),
        )
        con.commit()
    finally:
        con.close()
    return {"ok": True}


@_safe(consent.SCHEDULING)
def upsert_review_card(subjects_path, card):
    course_id = _course_id_from_path(subjects_path)
    con = _connect(subjects_path)
    try:
        con.execute(
            """INSERT INTO review_cards
               (id, course_id, stage_id, item_id, criterion, front, back,
                interval_sessions, due_at_slot, ease, lapses)
               VALUES (?,?,?,?,?,?,?,?,?,?,?)
               ON CONFLICT(id) DO UPDATE SET
                 interval_sessions = excluded.interval_sessions,
                 due_at_slot = excluded.due_at_slot,
                 ease = excluded.ease,
                 lapses = excluded.lapses""",
            (
                card["id"], course_id, card["stage_id"], card.get("item_id"),
                card.get("criterion"), card["front"], card["back"],
                card["interval_sessions"], card["due_at_slot"], card["ease"], card.get("lapses", 0),
            ),
        )
        con.commit()
    finally:
        con.close()
    return {"ok": True}


@_safe()
def log_review_pass(subjects_path, card_id, correct, old_interval, new_interval, old_ease, new_ease, slot):
    con = _connect(subjects_path)
    try:
        con.execute(
            """INSERT INTO review_log
               (card_id, correct, old_interval, new_interval, old_ease, new_ease, slot)
               VALUES (?,?,?,?,?,?,?)""",
            (card_id, int(bool(correct)), int(old_interval), int(new_interval), old_ease, new_ease, int(slot)),
        )
        con.commit()
    finally:
        con.close()
    return {"ok": True}


@_safe()
def log_confidence_event(subjects_path, event_type, misconception, delta, confidence_after, slot):
    course_id = _course_id_from_path(subjects_path)
    con = _connect(subjects_path)
    try:
        con.execute(
            """INSERT INTO confidence_events
               (course_id, slot, event_type, misconception, delta, confidence_after)
               VALUES (?,?,?,?,?,?)""",
            (course_id, int(slot), event_type, int(bool(misconception)), delta, confidence_after),
        )
        con.commit()
    finally:
        con.close()
    return {"ok": True}


@_safe()
def _upsert_item_mastery_current_only(subjects_path, item_id, p_mastery, observations, last_slot, last_correct):
    """Current-state-only upsert, no log row — used by backfill() so a
    synthetic 'first observation' never gets fabricated into
    item_mastery_log for history that was never actually recorded."""
    course_id = _course_id_from_path(subjects_path)
    con = _connect(subjects_path)
    try:
        con.execute(
            """INSERT INTO item_mastery (course_id, item_id, p_mastery, observations, last_slot, last_correct)
               VALUES (?,?,?,?,?,?)
               ON CONFLICT(course_id, item_id) DO UPDATE SET
                 p_mastery = excluded.p_mastery,
                 observations = excluded.observations,
                 last_slot = excluded.last_slot,
                 last_correct = excluded.last_correct""",
            (course_id, item_id, p_mastery, int(observations), last_slot, int(bool(last_correct))),
        )
        con.commit()
    finally:
        con.close()
    return {"ok": True}


def backfill(learner_dir):
    """One-time, best-effort snapshot migration for a learner folder that
    already has subjects/*.json and *_review_deck.json files from before
    this version existed. This can only ever populate *current-state*
    tables (item_mastery, review_cards) from what the JSON already holds —
    there is no way to reconstruct the individual observation/pass history
    that was never logged, and this function does not pretend to: it
    writes zero rows to item_mastery_log, review_log, error_events'
    genuinely historical shape, or confidence_events, since none of that
    data exists anywhere to recover. error_events themselves (the entries
    array, not just current state) ARE backfillable in full, since
    error_patterns already is a durable list, not a snapshot.
    Returns a per-file report; never raises.
    """
    subjects_dir = os.path.join(learner_dir, "subjects")
    report = {"learner_dir": learner_dir, "files": [], "errors": []}
    if not os.path.isdir(subjects_dir):
        report["errors"].append(f"no subjects/ dir under {learner_dir}")
        return report

    for name in sorted(os.listdir(subjects_dir)):
        path = os.path.join(subjects_dir, name)
        if not name.endswith(".json"):
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            report["errors"].append(f"{name}: {type(e).__name__}: {e}")
            continue

        if name.endswith("_review_deck.json"):
            cards = data.get("cards", [])
            n = 0
            for card in cards:
                if isinstance(card, dict) and "id" in card:
                    result = upsert_review_card(path, card)
                    if result.get("ok"):
                        n += 1
            report["files"].append({"file": name, "kind": "review_deck", "cards_backfilled": n})
            continue

        # a course subjects file
        n_errors = 0
        for entry in data.get("error_patterns", []) if isinstance(data.get("error_patterns"), list) else []:
            if isinstance(entry, dict) and "id" in entry:
                result = log_error_event(path, entry)
                if result.get("ok"):
                    n_errors += 1

        n_mastery = 0
        mastery = data.get("item_mastery", {})
        if isinstance(mastery, dict):
            for item_id, m in mastery.items():
                if not isinstance(m, dict):
                    continue
                # snapshot only: log a single "backfill" observation row equal to
                # current state, so item_mastery (current-state table) is populated;
                # item_mastery_log necessarily starts from this one synthetic point,
                # not the real history, which was never recorded before now.
                result = _upsert_item_mastery_current_only(
                    path, item_id,
                    p_mastery=m.get("p_mastery", 0.3),
                    observations=m.get("observations", 0),
                    last_slot=m.get("last_slot"),
                    last_correct=m.get("last_correct", True),
                )
                if result.get("ok"):
                    n_mastery += 1

        report["files"].append({"file": name, "kind": "subjects", "error_events_backfilled": n_errors, "item_mastery_backfilled": n_mastery})

    return report


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "backfill":
        print(json.dumps(backfill(sys.argv[2]), indent=2))
    else:
        print(json.dumps({"error": "usage: sqlite_store.py backfill <learner_dir>  (this module is otherwise imported, not run directly)"}))
        sys.exit(2)
