-- schema_design.sql — DESIGN REFERENCE ONLY, still not wired into any
-- script. JSON under subjects/<course_id>.json remains the live source of
-- truth; nothing here is read or written for real yet.
--
-- Revision 2 (30 Sep 2026). Revision 1 (29 Sep 2026) predated error_log.py,
-- item_mastery.py, confidence_update.py and the review-deck item_id/
-- criterion fields — all of which shipped in v1.5.0 before this file was
-- ever updated to match them. This revision brings the design in line with
-- what those scripts actually read and write today, and borrows two
-- specific, genuinely useful ideas from reviewing another open-source
-- tutoring project (LearnOS, github.com/Abelo9996/LearnOS) against our own
-- design — noted inline where taken. Everything else in that project's
-- schema (users/auth, XP/streaks, badges, a social course registry) is
-- either handled elsewhere in this system (profile-kernel's per-folder
-- learner isolation) or deliberately out of scope (see profile-kernel.md's
-- "What this deliberately avoids") and is not reflected here.
--
-- One file per learner, alongside their existing profile:
--   /EDU/profile/<learner_id>/tutor.sqlite3
-- (per-learner, not shared — same isolation rule as the rest of
-- /EDU/profile/. course_id scopes rows within one learner's own file;
-- there is no cross-learner table anywhere in this design.)

PRAGMA foreign_keys = ON;

-- One row per classified wrong answer / diagnosed struggle.
-- Mirrors error_log.py's error_patterns entry exactly, field for field.
CREATE TABLE error_events (
  id                TEXT PRIMARY KEY,          -- error_log.py's own id scheme: err_<date>_<stage>_<seq>
  course_id         TEXT NOT NULL,
  stage_id          TEXT NOT NULL,
  item_id           TEXT,                      -- null if the course isn't itemised
  source_phase      TEXT NOT NULL CHECK (source_phase IN ('practice','test')),
  cause             TEXT NOT NULL CHECK (cause IN
                      ('slip','missing_prerequisite','misconception',
                       'misapplied_procedure','comprehension')),
  misconception_id  TEXT,                      -- references misconceptions.json's own id scheme, not a DB table (that file stays per-course JSON, sourced at compile time)
  rubric_criterion  TEXT,                      -- added v1.5.0: the rubric.json entry this was graded against, or null
  note              TEXT,                      -- what the learner actually said/did, free text
  slot              INTEGER NOT NULL,          -- session_slot at the time, not a date
  resolved          INTEGER NOT NULL DEFAULT 0 CHECK (resolved IN (0,1)),
  resolved_at_slot  INTEGER,
  created_at        TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX idx_error_events_lookup ON error_events (course_id, stage_id, item_id, cause);
CREATE INDEX idx_error_events_unresolved ON error_events (course_id, resolved) WHERE resolved = 0;

-- Per-item BKT mastery state (v1.5.0, item_mastery.py). One row per
-- (course_id, item_id) pair, always the *current* belief — history of how
-- it got there lives in item_mastery_log below, not here.
CREATE TABLE item_mastery (
  course_id     TEXT NOT NULL,
  item_id       TEXT NOT NULL,
  p_mastery     REAL NOT NULL CHECK (p_mastery BETWEEN 0 AND 1),
  observations  INTEGER NOT NULL DEFAULT 0,
  last_slot     INTEGER,
  last_correct  INTEGER CHECK (last_correct IN (0,1)),
  PRIMARY KEY (course_id, item_id)
);

-- Idea taken from LearnOS's flashcard_reviews table: keep the observation
-- history, not just the current belief, so "is this item actually
-- trending up" is a query instead of something nobody can currently ask —
-- item_mastery.py's JSON form only ever holds the latest state. This table
-- is a genuine capability gain from migrating, not a straight port of an
-- existing JSON shape.
CREATE TABLE item_mastery_log (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  course_id     TEXT NOT NULL,
  item_id       TEXT NOT NULL,
  correct       INTEGER NOT NULL CHECK (correct IN (0,1)),
  prior         REAL NOT NULL,
  posterior     REAL NOT NULL,
  new_p_mastery REAL NOT NULL,
  slot          INTEGER NOT NULL,
  created_at    TEXT NOT NULL DEFAULT (datetime('now')),
  FOREIGN KEY (course_id, item_id) REFERENCES item_mastery(course_id, item_id)
);
CREATE INDEX idx_item_mastery_log_item ON item_mastery_log (course_id, item_id, slot);

-- Review cards — replaces the per-course subjects/<id>.json review-deck
-- array-in-a-file pattern with rows, once decks are large enough across
-- enough courses/years that "which cards are due" stops being a cheap
-- full-file scan. Columns mirror the existing JSON card shape exactly
-- (review-scheduler's SM-2-lite fields, including the v1.5.0 item_id/
-- criterion tags), so review_math.py's math is unchanged — only where the
-- row lives changes.
CREATE TABLE review_cards (
  id                TEXT PRIMARY KEY,          -- existing card id scheme
  course_id         TEXT NOT NULL,
  stage_id          TEXT NOT NULL,
  item_id           TEXT,                      -- v1.5.0: the syllabus item this card exercises, or null
  criterion         TEXT,                      -- v1.5.0: the rubric criterion this card exercises, or null
  front             TEXT NOT NULL,
  back              TEXT NOT NULL,
  interval_sessions INTEGER NOT NULL,
  due_at_slot       INTEGER NOT NULL,
  ease              REAL NOT NULL,
  lapses            INTEGER NOT NULL DEFAULT 0
);
CREATE INDEX idx_review_cards_due ON review_cards (course_id, due_at_slot);

-- Second idea taken from LearnOS: their flashcards/flashcard_reviews split
-- (current state vs. append-only history) is the same pattern applied
-- above to item_mastery — applying it here too for the same reason: a
-- review pass currently overwrites a card's four scheduling fields in
-- place, so "how has this card's ease actually moved over a term" isn't
-- answerable from the JSON today. This table is what review_math.py's
-- caller would additionally insert on every pass, straight from its
-- output — the function itself needs no change.
CREATE TABLE review_log (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  card_id           TEXT NOT NULL REFERENCES review_cards(id) ON DELETE CASCADE,
  correct           INTEGER NOT NULL CHECK (correct IN (0,1)),
  old_interval      INTEGER NOT NULL,
  new_interval      INTEGER NOT NULL,
  old_ease          REAL NOT NULL,
  new_ease          REAL NOT NULL,
  slot              INTEGER NOT NULL,
  created_at        TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX idx_review_log_card ON review_log (card_id, slot);

-- Confidence history — one row per graded event that moves the needle, not
-- just the current value. Note: this is a genuine new capability, not a
-- migration of anything that exists today — confidence_update.py is a
-- pure calculator (see its own docstring) that never persists history;
-- course-runner currently only ever writes the single resulting scalar to
-- subjects/<course_id>.json. This table is what course-runner would
-- additionally insert alongside that write.
CREATE TABLE confidence_events (
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
CREATE INDEX idx_confidence_events_course ON confidence_events (course_id, slot);

-- Deliberately not included, and why:
--   - No users/auth table — profile-kernel's one-learner-per-folder
--     isolation already is the access boundary; a DB table would be a
--     second, redundant one to keep in sync.
--   - No XP/streak/badge/certificate tables — gamification is explicitly
--     out of scope (profile-kernel.md, "What this deliberately avoids");
--     LearnOS has these, we don't want them.
--   - No course-registry/sharing tables — this system's courses live under
--     the shared /EDU/courses/ folder, not per-learner state, and aren't
--     in scope for this per-learner schema at all.
--
-- Example of the query this is actually for — not runnable until the
-- tables have real rows, kept here so the intent is legible up front:
--
--   SELECT item_id, cause, COUNT(*) AS n
--   FROM error_events
--   WHERE course_id = 'alevel_psychology' AND resolved = 0
--   GROUP BY item_id, cause
--   ORDER BY n DESC;
--
-- ...is a query. The equivalent over subjects/<course_id>.json-shaped
-- files is a bespoke script every time the question changes.
