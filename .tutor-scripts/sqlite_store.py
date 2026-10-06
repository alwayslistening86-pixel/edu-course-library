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

from tutorlib import cli, consent

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS error_events (
  id                TEXT NOT NULL,
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
  created_at        TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (course_id, id)
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
  id                TEXT NOT NULL,
  course_id         TEXT NOT NULL,
  stage_id          TEXT NOT NULL,
  item_id           TEXT,
  criterion         TEXT,
  front             TEXT NOT NULL,
  back              TEXT NOT NULL,
  interval_sessions INTEGER NOT NULL,
  due_at_slot       INTEGER NOT NULL,
  ease              REAL NOT NULL,
  lapses            INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (course_id, id)
);
CREATE INDEX IF NOT EXISTS idx_review_cards_due ON review_cards (course_id, due_at_slot);

CREATE TABLE IF NOT EXISTS review_log (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id         TEXT,
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
CREATE INDEX IF NOT EXISTS idx_review_log_course ON review_log (course_id, card_id, slot);

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

CREATE TABLE IF NOT EXISTS grading_results (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id         TEXT NOT NULL,
  stage_id          TEXT NOT NULL,
  attempt           INTEGER NOT NULL,
  criterion_index   INTEGER NOT NULL,
  met               INTEGER NOT NULL CHECK (met IN (0,1)),
  marks_awarded     INTEGER NOT NULL,
  marks_available   INTEGER NOT NULL,
  rubric_hash       TEXT NOT NULL,
  slot              INTEGER NOT NULL,
  created_at        TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_grading_results_stage ON grading_results (course_id, stage_id, attempt);
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


# PRAGMA user_version of the history DB (E-15). 0 = created before versioning (same tables; stamped on first use).
DB_SCHEMA_VERSION = 3   # v3 adds grading_results (additive: nothing existing changes)


class NewerDatabase(RuntimeError):
    pass


def _has_column(con, table, column):
    return any(r[1] == column for r in con.execute(f"PRAGMA table_info({table})"))


def _migrate_v1_to_v2(con):
    """v1 keyed error_events and review_cards by id alone, so two courses producing the same id (err_<date>_<stage>_001, a card "S1-c1")
    overwrote each other's rows. v2 keys them by (course_id, id) and records course_id on review_log. Existing rows are kept as they are
    (a row already overwritten under v1 cannot be recovered)."""
    con.execute("BEGIN IMMEDIATE")
    try:
        for table, indexes in (("error_events", ("idx_error_events_lookup", "idx_error_events_unresolved")), ("review_cards", ("idx_review_cards_due",))):
            cols = [r[1] for r in con.execute(f"PRAGMA table_info({table})")]
            con.execute(f"ALTER TABLE {table} RENAME TO {table}_v1")
            for ix in indexes:
                con.execute(f"DROP INDEX IF EXISTS {ix}")
            ddl = _table_ddl(table)
            con.execute(ddl)
            con.execute(f"INSERT INTO {table} ({', '.join(cols)}) SELECT {', '.join(cols)} FROM {table}_v1")
            con.execute(f"DROP TABLE {table}_v1")
        if not _has_column(con, "review_log", "course_id"):
            con.execute("ALTER TABLE review_log ADD COLUMN course_id TEXT")
        con.execute("UPDATE review_log SET course_id = (SELECT course_id FROM review_cards c WHERE c.id = review_log.card_id) WHERE course_id IS NULL")
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        raise


def _table_ddl(table):
    start = SCHEMA.index(f"CREATE TABLE IF NOT EXISTS {table} (")
    return SCHEMA[start:SCHEMA.index(");", start) + 1].replace("IF NOT EXISTS ", "")


def _connect(any_profile_path):
    db_path = learner_db_path(any_profile_path)
    con = sqlite3.connect(db_path, timeout=5, isolation_level=None)
    version = con.execute("PRAGMA user_version").fetchone()[0]
    if version > DB_SCHEMA_VERSION:
        con.close()
        raise NewerDatabase(
            f"{db_path} is history schema v{version}, newer than this plugin understands (v{DB_SCHEMA_VERSION}); "
            "update the generic-tutor plugin")
    existing = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    if "review_log" in existing and not _has_column(con, "review_log", "course_id"):
        _migrate_v1_to_v2(con)
    con.executescript(SCHEMA)
    if version < DB_SCHEMA_VERSION:
        con.execute(f"PRAGMA user_version = {DB_SCHEMA_VERSION}")
    return con


def check(learner_dir):
    """Read-only health report for a learner's history DB: version, integrity, row counts."""
    db_path = os.path.join(learner_dir, "tutor.sqlite3")
    if not os.path.isfile(db_path):
        return {"exists": False}
    con = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        version = con.execute("PRAGMA user_version").fetchone()[0]
        integrity = [r[0] for r in con.execute("PRAGMA integrity_check")]
        tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
        counts = {t: con.execute(f'SELECT COUNT(*) FROM "{t}"').fetchone()[0] for t in tables}
    finally:
        con.close()
    ok = integrity == ["ok"] and version <= DB_SCHEMA_VERSION
    return {"exists": True, "user_version": version, "supported_version": DB_SCHEMA_VERSION,
            "integrity": integrity, "row_counts": counts, "healthy": ok}


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
    course_id = _course_id_from_path(subjects_path)
    con = _connect(subjects_path)
    try:
        con.executemany(
            "UPDATE error_events SET resolved = 1, resolved_at_slot = ? WHERE course_id = ? AND id = ?",
            [(int(resolved_at_slot), course_id, eid) for eid in entry_ids],
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
               ON CONFLICT(course_id, id) DO UPDATE SET
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
    course_id = _course_id_from_path(subjects_path)
    con = _connect(subjects_path)
    try:
        con.execute(
            """INSERT INTO review_log
               (course_id, card_id, correct, old_interval, new_interval, old_ease, new_ease, slot)
               VALUES (?,?,?,?,?,?,?,?)""",
            (course_id, card_id, int(bool(correct)), int(old_interval), int(new_interval), old_ease, new_ease, int(slot)),
        )
        con.commit()
    finally:
        con.close()
    return {"ok": True}


@_safe()
def log_grading(subjects_path, stage_id, rows, slot):
    """One test attempt's per-criterion outcomes. `rows` = [(criterion_index, met, marks_awarded, marks_available, rubric_hash)].
    Only indexes, booleans and numbers are stored, never the learner's answer text or the rubric's wording (V-09)."""
    course_id = _course_id_from_path(subjects_path)
    con = _connect(subjects_path)
    try:
        attempt = con.execute("SELECT COALESCE(MAX(attempt), 0) + 1 FROM grading_results WHERE course_id = ? AND stage_id = ?",
                              (course_id, stage_id)).fetchone()[0]
        con.executemany(
            """INSERT INTO grading_results (course_id, stage_id, attempt, criterion_index, met, marks_awarded, marks_available, rubric_hash, slot)
               VALUES (?,?,?,?,?,?,?,?,?)""",
            [(course_id, stage_id, attempt, i, int(bool(m)), a, o, h, int(slot)) for i, m, a, o, h in rows])
        con.commit()
    finally:
        con.close()
    return {"ok": True, "attempt": attempt}


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
    cli.handle_help(__doc__)
    if len(sys.argv) == 3 and sys.argv[1] == "backfill":
        print(json.dumps(backfill(sys.argv[2]), indent=2))
    elif len(sys.argv) == 3 and sys.argv[1] == "check":
        _r = check(sys.argv[2])
        print(json.dumps(_r, indent=2))
        sys.exit(0 if _r.get("healthy", True) else 1)
    else:
        print(json.dumps({"error": "usage: sqlite_store.py backfill|check <learner_dir>  (this module is otherwise imported, not run directly)"}))
        sys.exit(2)
