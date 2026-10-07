"""
Tests for the 1.10.0 SQLite history layer (sqlite_store.py) and the
apply-subcommand write-back fix on confidence_update.py / review_math.py.

Two things are under test here, matching what shipped in this version:

1. sqlite_store.py itself: db creation, the four logging/upsert functions,
   backfill(), and — importantly — that a write failure never raises past
   the _safe wrapper (error_log.py/item_mastery.py call these functions
   inline and must never be blocked by a sqlite problem).

2. The write-back gap fix: confidence_update.py's and review_math.py's new
   `apply` subcommands, which — unlike the old pure `compute()` — actually
   perform the read-modify-write against the JSON file themselves. This is
   the direct, concrete answer to "does the LM actually write back, or
   just say it did": these two scripts now own their write the same way
   error_log.py/item_mastery.py always have, closing the one place in the
   plugin where persistence was 100% prose-trust.

    python3 -m unittest discover tests -v
"""
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

import confidence_update  # noqa: E402
import error_log  # noqa: E402
import item_mastery  # noqa: E402
import review_math  # noqa: E402
import sqlite_store  # noqa: E402


def _w(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


def _r(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


class LearnerDirCase(unittest.TestCase):
    """Mirrors the real deployed layout: <learner_dir>/subjects/<course>.json
    and <learner_dir>/subjects/<course>_review_deck.json, so sqlite_store's
    learner_db_path() (one level above subjects/) resolves inside the
    tempdir rather than leaking a tutor.sqlite3 into a shared /tmp."""

    def setUp(self):
        self.learner_dir = tempfile.mkdtemp()
        self.subjects_dir = os.path.join(self.learner_dir, "subjects")
        os.makedirs(self.subjects_dir, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.learner_dir, ignore_errors=True)

    def subj_path(self, course_id="x", **extra):
        p = os.path.join(self.subjects_dir, f"{course_id}.json")
        base = {"schema_version": 5, "course_id": course_id, "error_patterns": [], "item_mastery": {}}
        base.update(extra)
        _w(p, base)
        return p

    def deck_path(self, course_id="x", cards=None):
        p = os.path.join(self.subjects_dir, f"{course_id}_review_deck.json")
        _w(p, {"schema_version": 1, "course_id": course_id, "cards": cards or []})
        return p

    def db_path(self):
        return os.path.join(self.learner_dir, "tutor.sqlite3")

    def query(self, sql, params=()):
        con = sqlite3.connect(self.db_path())
        try:
            con.row_factory = sqlite3.Row
            return [dict(row) for row in con.execute(sql, params).fetchall()]
        finally:
            con.close()


class TestSqliteStoreErrorEvents(LearnerDirCase):
    def test_log_error_event_creates_db_and_row(self):
        p = self.subj_path()
        entry = {
            "id": "err_2026-09-30_S09_001", "stage_id": "S09", "item_id": "RM6",
            "source_phase": "practice", "cause": "slip", "misconception_id": None,
            "rubric_criterion": None, "note": "arithmetic slip", "slot": 5,
            "resolved": False, "resolved_at_slot": None,
        }
        result = sqlite_store.log_error_event(p, entry)
        self.assertTrue(result["ok"])
        self.assertTrue(os.path.exists(self.db_path()))
        rows = self.query("SELECT * FROM error_events WHERE id = ?", (entry["id"],))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["cause"], "slip")
        self.assertEqual(rows[0]["resolved"], 0)

    def test_resolve_error_events_updates_flag(self):
        p = self.subj_path()
        entry = {
            "id": "err_2026-09-30_S09_001", "stage_id": "S09", "item_id": "RM6",
            "source_phase": "practice", "cause": "slip", "misconception_id": None,
            "rubric_criterion": None, "note": "n", "slot": 5,
            "resolved": False, "resolved_at_slot": None,
        }
        sqlite_store.log_error_event(p, entry)
        result = sqlite_store.resolve_error_events(p, [entry["id"]], 20)
        self.assertTrue(result["ok"])
        self.assertEqual(result["updated"], 1)
        rows = self.query("SELECT resolved, resolved_at_slot FROM error_events WHERE id = ?", (entry["id"],))
        self.assertEqual(rows[0]["resolved"], 1)
        self.assertEqual(rows[0]["resolved_at_slot"], 20)

    def test_resolve_with_no_ids_is_a_noop_ok(self):
        p = self.subj_path()
        result = sqlite_store.resolve_error_events(p, [], 20)
        self.assertEqual(result, {"ok": True, "updated": 0})


class TestSqliteStoreItemMastery(LearnerDirCase):
    def test_log_observation_upserts_current_state_and_appends_log(self):
        p = self.subj_path()
        sqlite_store.log_item_mastery_observation(p, "RM6", False, 0.3, 0.1765, 0.1932, 100)
        sqlite_store.log_item_mastery_observation(p, "RM6", True, 0.1932, 0.5909, 0.5909, 110)
        current = self.query("SELECT * FROM item_mastery WHERE item_id = 'RM6'")
        self.assertEqual(len(current), 1)  # upsert, not insert
        self.assertAlmostEqual(current[0]["p_mastery"], 0.5909, places=4)
        self.assertEqual(current[0]["observations"], 2)
        log_rows = self.query("SELECT * FROM item_mastery_log WHERE item_id = 'RM6' ORDER BY slot")
        self.assertEqual(len(log_rows), 2)  # full history preserved


class TestSqliteStoreReviewAndConfidence(LearnerDirCase):
    def test_upsert_review_card_then_log_pass(self):
        p = self.deck_path()
        card = {
            "id": "c1", "stage_id": "S09", "item_id": "RM6", "criterion": None,
            "front": "Q", "back": "A", "interval_sessions": 1, "due_at_slot": 6,
            "ease": 2.3, "lapses": 0,
        }
        sqlite_store.upsert_review_card(p, card)
        sqlite_store.log_review_pass(p, "c1", True, 1, 3, 2.3, 2.35, 5)
        rows = self.query("SELECT * FROM review_cards WHERE id = 'c1'")
        self.assertEqual(len(rows), 1)
        log_rows = self.query("SELECT * FROM review_log WHERE card_id = 'c1'")
        self.assertEqual(len(log_rows), 1)
        self.assertEqual(log_rows[0]["new_interval"], 3)

    def test_log_confidence_event(self):
        p = self.subj_path()
        result = sqlite_store.log_confidence_event(p, "pass_clean", False, 0.075, 0.575, 12)
        self.assertTrue(result["ok"])
        rows = self.query("SELECT * FROM confidence_events")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["event_type"], "pass_clean")


class TestSqliteStoreNeverRaises(LearnerDirCase):
    def test_failure_returns_ok_false_instead_of_raising(self):
        # A path whose learner_dir can't hold a sqlite file (points inside a
        # file, not a directory) forces sqlite3.connect to fail — the _safe
        # wrapper must turn that into {"ok": False, ...}, never an exception.
        bad_file = os.path.join(self.learner_dir, "not_a_dir")
        with open(bad_file, "w") as f:
            f.write("x")
        bad_subjects_path = os.path.join(bad_file, "subjects", "x.json")
        result = sqlite_store.log_confidence_event(bad_subjects_path, "pass_clean", False, 0.1, 0.6, 1)
        self.assertFalse(result["ok"])
        self.assertIn("error", result)


class TestSqliteStoreBackfill(LearnerDirCase):
    def test_backfill_populates_current_state_only(self):
        self.subj_path(
            course_id="x",
            error_patterns=[
                {"id": "err_1", "stage_id": "S01", "item_id": "A1", "source_phase": "practice",
                 "cause": "slip", "misconception_id": None, "rubric_criterion": None, "note": "n",
                 "slot": 1, "resolved": False, "resolved_at_slot": None},
            ],
            item_mastery={"A1": {"p_mastery": 0.7, "observations": 3, "last_slot": 10, "last_correct": True}},
        )
        self.deck_path(course_id="x", cards=[
            {"id": "c1", "stage_id": "S01", "item_id": "A1", "criterion": None,
             "front": "Q", "back": "A", "interval_sessions": 2, "due_at_slot": 12, "ease": 2.3, "lapses": 0},
        ])
        report = sqlite_store.backfill(self.learner_dir)
        self.assertEqual(len(report["errors"]), 0)
        # current-state tables populated
        self.assertEqual(len(self.query("SELECT * FROM item_mastery")), 1)
        self.assertEqual(len(self.query("SELECT * FROM review_cards")), 1)
        self.assertEqual(len(self.query("SELECT * FROM error_events")), 1)
        # history tables NOT fabricated — backfill never invents observation/pass history
        self.assertEqual(len(self.query("SELECT * FROM item_mastery_log")), 0)
        self.assertEqual(len(self.query("SELECT * FROM review_log")), 0)
        self.assertEqual(len(self.query("SELECT * FROM confidence_events")), 0)


class TestErrorLogSqliteSideEffects(LearnerDirCase):
    def test_append_surfaces_sqlite_result_and_persists_row(self):
        p = self.subj_path()
        result = error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "n", 5)
        self.assertIn("sqlite", result)
        self.assertTrue(result["sqlite"]["ok"])
        rows = self.query("SELECT * FROM error_events WHERE item_id = 'RM6'")
        self.assertEqual(len(rows), 1)

    def test_resolve_surfaces_sqlite_result(self):
        p = self.subj_path()
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "n", 5)
        result = error_log.resolve(p, "RM6", 20)
        self.assertIn("sqlite", result)
        self.assertTrue(result["sqlite"]["ok"])
        rows = self.query("SELECT resolved FROM error_events WHERE item_id = 'RM6'")
        self.assertEqual(rows[0]["resolved"], 1)


class TestItemMasterySqliteSideEffects(LearnerDirCase):
    def test_observe_surfaces_sqlite_result_and_logs_history(self):
        p = self.subj_path()
        r1 = item_mastery.observe(p, "RM6", False, 100)
        self.assertIn("sqlite", r1)
        self.assertTrue(r1["sqlite"]["ok"])
        item_mastery.observe(p, "RM6", True, 110)
        log_rows = self.query("SELECT * FROM item_mastery_log WHERE item_id = 'RM6'")
        self.assertEqual(len(log_rows), 2)


class TestConfidenceUpdateApply(LearnerDirCase):
    def test_apply_writes_confidence_into_subjects_json(self):
        p = self.subj_path(confidence=0.5)
        result = confidence_update.apply(p, "pass_clean", 12)
        self.assertTrue(result["written"])
        self.assertEqual(_r(p)["confidence"], result["new_confidence"])
        self.assertGreater(result["new_confidence"], 0.5)

    def test_apply_defaults_missing_confidence_to_0_5(self):
        p = self.subj_path()  # no "confidence" key at all
        result = confidence_update.apply(p, "fail", 3)
        self.assertEqual(result["old_confidence"], 0.5)

    def test_apply_logs_to_sqlite(self):
        p = self.subj_path(confidence=0.5)
        result = confidence_update.apply(p, "pass_clean", 12)
        self.assertTrue(result["sqlite"]["ok"])
        rows = self.query("SELECT * FROM confidence_events")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["event_type"], "pass_clean")

    def test_apply_matches_compute_for_same_inputs(self):
        p = self.subj_path(confidence=0.4)
        computed = confidence_update.compute(0.4, "fail", misconception=True)
        applied = confidence_update.apply(p, "fail", 7, misconception=True)
        self.assertEqual(applied["new_confidence"], computed["new_confidence"])

    def test_compute_subcommand_still_pure_no_file_needed(self):
        # the old pure form must keep working unchanged
        r = confidence_update.compute(0.5, "pass_clean")
        self.assertIn("new_confidence", r)


class TestReviewMathApply(LearnerDirCase):
    def test_apply_writes_fields_back_onto_the_card(self):
        p = self.deck_path(cards=[
            {"id": "c1", "stage_id": "S09", "item_id": "RM6", "criterion": None,
             "front": "Q", "back": "A", "interval_sessions": 1, "due_at_slot": 6,
             "ease": 2.3, "lapses": 0},
        ])
        result = review_math.apply(p, "c1", 5, True)
        self.assertTrue(result["written"])
        card = _r(p)["cards"][0]
        self.assertEqual(card["interval_sessions"], result["interval_sessions"])
        self.assertEqual(card["ease"], result["ease"])
        self.assertEqual(card["due_at_slot"], result["due_at_slot"])

    def test_apply_unknown_card_id_returns_error_not_exception(self):
        p = self.deck_path(cards=[])
        result = review_math.apply(p, "nope", 5, True)
        self.assertIn("error", result)

    def test_apply_matches_compute_for_same_inputs(self):
        p = self.deck_path(cards=[
            {"id": "c1", "stage_id": "S09", "item_id": "RM6", "criterion": None,
             "front": "Q", "back": "A", "interval_sessions": 3, "due_at_slot": 6,
             "ease": 2.1, "lapses": 1},
        ])
        computed = review_math.compute(3, 2.1, 1, 10, False)
        applied = review_math.apply(p, "c1", 10, False)
        self.assertEqual(applied["interval_sessions"], computed["interval_sessions"])
        self.assertEqual(applied["ease"], computed["ease"])
        self.assertEqual(applied["lapses"], computed["lapses"])
        self.assertEqual(applied["due_at_slot"], computed["due_at_slot"])

    def test_apply_logs_pass_and_upserts_card_in_sqlite(self):
        p = self.deck_path(cards=[
            {"id": "c1", "stage_id": "S09", "item_id": "RM6", "criterion": None,
             "front": "Q", "back": "A", "interval_sessions": 1, "due_at_slot": 6,
             "ease": 2.3, "lapses": 0},
        ])
        result = review_math.apply(p, "c1", 5, True)
        self.assertTrue(result["sqlite"]["log_review_pass"]["ok"])
        self.assertTrue(result["sqlite"]["upsert_review_card"]["ok"])
        cards = self.query("SELECT * FROM review_cards WHERE id = 'c1'")
        self.assertEqual(cards[0]["interval_sessions"], result["interval_sessions"])

    def test_positional_compute_form_still_works_unchanged(self):
        r = review_math.compute(1, 2.3, 0, 0, True)
        self.assertIn("interval_sessions", r)


if __name__ == "__main__":
    unittest.main()
