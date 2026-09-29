-- schema_design.sql — DESIGN REFERENCE ONLY, not wired into any script yet.
--
-- Proposed SQLite schema for the tutor-core adaptive-teaching additions
-- scoped in the "Tutor core: current state and the adaptive-teaching gap"
-- document (29 Sep 2026). Nothing here is live: error_log.py,
-- diagnostic_gate.py, remediation_state.py and confidence_update.py still
-- need to be built and wired into course-runner/tutor-core before any of
-- this is read or written for real. This file exists so that work starts
-- from an agreed shape instead of inventing the schema mid-build.
--
-- One file per learner, alongside their existing profile:
--   /EDU/profile/<learner_id>/tutor.sqlite3
-- (review decks and error logs are per-learner, not shared across the
-- profile-kernel's multiple learners, same isolation rule as the rest of
-- /EDU/profile/.)

PRAGMA foreign_keys = ON;

-- One row per classified wrong answer / diagnosed struggle.
-- Backs error_log.py from the tutor-core scoping document.
CREATE TABLE error_events (
  id              INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id       TEXT NOT NULL,
  stage_id        TEXT NOT NULL,
  item_id         TEXT,                      -- null if the course isn't itemised
  source_phase    TEXT NOT NULL CHECK (source_phase IN ('practice','test')),
  cause           TEXT NOT NULL CHECK (cause IN
                    ('slip','missing_prerequisite','misconception',
                     'misapplied_procedure','comprehension')),
  misconception_id TEXT,                     -- references misconceptions.json's own id scheme, not a DB table (that file stays per-course JSON, sourced at compile time)
  note            TEXT,                      -- what the learner actually said/did, free text
  slot            INTEGER NOT NULL,          -- session_slot at the time, not a date
  resolved        INTEGER NOT NULL DEFAULT 0 CHECK (resolved IN (0,1)),
  resolved_at_slot INTEGER,
  created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX idx_error_events_lookup ON error_events (course_id, stage_id, item_id, cause);
CREATE INDEX idx_error_events_unresolved ON error_events (course_id, resolved) WHERE resolved = 0;

-- Review cards — replaces the per-course subjects/<id>_review_deck.json
-- array-in-a-file pattern with rows, once decks are large enough across
-- enough courses/years that "which cards are due" stops being a cheap
-- full-file scan. Columns mirror the existing JSON card shape exactly
-- (review-scheduler's SM-2-lite fields), so review_math.py's math is
-- unchanged — only where the row lives changes.
CREATE TABLE review_cards (
  id              TEXT PRIMARY KEY,          -- existing card id scheme
  course_id       TEXT NOT NULL,
  stage_id        TEXT NOT NULL,
  front           TEXT NOT NULL,
  back            TEXT NOT NULL,
  interval_sessions INTEGER NOT NULL,
  due_at_slot     INTEGER NOT NULL,
  ease            REAL NOT NULL,
  lapses          INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX idx_review_cards_due ON review_cards (course_id, due_at_slot);

-- Confidence history — one row per graded event that moves the needle,
-- not just the current value, so a trend ("has this been declining")
-- is a query instead of something nobody can currently ask at all.
-- tutor-core's pacing rules would read the latest row per course_id.
CREATE TABLE confidence_events (
  id              INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id       TEXT NOT NULL,
  slot            INTEGER NOT NULL,
  event_type      TEXT NOT NULL CHECK (event_type IN
                    ('pass_clean','pass_after_remediation','fail','misconception_logged')),
  delta           REAL NOT NULL,
  confidence_after REAL NOT NULL CHECK (confidence_after BETWEEN 0 AND 1),
  created_at      TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX idx_confidence_events_course ON confidence_events (course_id, slot);

-- Example of the query this is actually for — not runnable until the
-- tables have real rows, kept here so the intent is legible up front:
--
--   SELECT item_id, cause, COUNT(*) AS n
--   FROM error_events
--   WHERE course_id = 'alevel_psychology' AND resolved = 0
--   GROUP BY item_id, cause
--   ORDER BY n DESC;
--
-- ...is a query. The equivalent over review_deck.json-shaped files is a
-- bespoke script every time the question changes.
