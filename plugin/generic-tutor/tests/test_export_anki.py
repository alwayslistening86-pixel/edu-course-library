"""
Tests for toolkit/export_anki.py — the one toolkit module with a real
third-party dependency (genanki). Skips the genanki-dependent tests (not
fails, not errors) when genanki isn't installed in this environment,
mirroring how gui.pyw's tkinter-dependent behaviour is smoke-tested
manually rather than asserted here; the "genanki missing" behaviour itself
is tested directly, since that's core.py rule 7's whole point — a missing
dependency should degrade this one feature cleanly, not break anything.

    python3 -m unittest discover tests -v
"""
import os
import sys
import unittest
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
TOOLKIT = os.path.join(SCRIPTS, "toolkit")
TESTS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPTS)
sys.path.insert(0, TOOLKIT)
sys.path.insert(0, TESTS)

import export_anki  # noqa: E402

from test_toolkit import FakeEduCase  # noqa: E402


CARD_1 = {
    "id": "c1", "stage_id": "S1", "item_id": "RM6", "criterion": "M2",
    "front": "What is 2+2?", "back": "4",
    "interval_sessions": 4, "due_at_slot": 18, "ease": 2.3, "lapses": 0,
}
CARD_2 = {
    "id": "c2", "stage_id": "S2", "item_id": None, "criterion": None,
    "front": "Capital of France?", "back": "Paris",
    "interval_sessions": 1, "due_at_slot": 5, "ease": 2.3, "lapses": 0,
}
CARD_NO_BACK = {"id": "c3", "stage_id": "S1", "front": "Orphan card", "back": ""}


class TestNotInstalled(FakeEduCase):
    """These pass regardless of whether genanki is actually installed —
    they only check that a missing-dependency state (real or simulated) is
    reported as a plain error dict, never an exception."""

    def test_reports_clean_error_when_unavailable(self):
        self.make_learner("alex")
        self.make_review_deck("alex", "gcse_maths", [CARD_1])
        original = export_anki.GENANKI_AVAILABLE
        export_anki.GENANKI_AVAILABLE = False
        try:
            result = export_anki.export_decks("alex", root=self.root)
        finally:
            export_anki.GENANKI_AVAILABLE = original
        self.assertIn("error", result)
        self.assertIn("pip install genanki", result["error"])

    def test_stable_id_deterministic(self):
        self.assertEqual(
            export_anki._stable_id("a", "b", "c"),
            export_anki._stable_id("a", "b", "c"),
        )
        self.assertNotEqual(
            export_anki._stable_id("a", "b", "c"),
            export_anki._stable_id("a", "b", "d"),
        )


@unittest.skipUnless(export_anki.GENANKI_AVAILABLE, "genanki not installed in this environment")
class TestExportDecks(FakeEduCase):
    def test_no_such_learner(self):
        result = export_anki.export_decks("nobody", root=self.root)
        self.assertIn("error", result)

    def test_no_cards_anywhere(self):
        self.make_learner("alex")
        result = export_anki.export_decks("alex", root=self.root)
        self.assertIn("error", result)
        self.assertIn("no exportable cards", result["error"])

    def test_exports_real_apkg_file(self):
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths")
        self.make_review_deck("alex", "gcse_maths", [CARD_1, CARD_2, CARD_NO_BACK])

        result = export_anki.export_decks("alex", root=self.root)
        self.assertNotIn("error", result)
        self.assertEqual(result["deck_count"], 1)
        self.assertEqual(result["card_count"], 2)  # CARD_NO_BACK excluded, empty back
        self.assertEqual(result["courses_exported"], ["gcse_maths"])
        self.assertTrue(os.path.isfile(result["apkg_path"]))
        self.assertTrue(result["apkg_path"].endswith(".apkg"))

        # a real .apkg is a real zip containing a real sqlite collection —
        # confirm it round-trips as an actual file, not just a path string.
        with zipfile.ZipFile(result["apkg_path"]) as zf:
            names = zf.namelist()
            self.assertTrue(any(n.startswith("collection.anki2") for n in names))

    def test_multiple_courses_become_multiple_decks(self):
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths")
        self.make_subject("alex", "gcse_french")
        self.make_review_deck("alex", "gcse_maths", [CARD_1])
        self.make_review_deck("alex", "gcse_french", [CARD_2])

        result = export_anki.export_decks("alex", root=self.root)
        self.assertEqual(result["deck_count"], 2)
        self.assertEqual(result["card_count"], 2)
        self.assertEqual(sorted(result["courses_exported"]), ["gcse_french", "gcse_maths"])

    def test_course_filter_respected(self):
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths")
        self.make_subject("alex", "gcse_french")
        self.make_review_deck("alex", "gcse_maths", [CARD_1])
        self.make_review_deck("alex", "gcse_french", [CARD_2])

        result = export_anki.export_decks("alex", root=self.root, course_ids=["gcse_maths"])
        self.assertEqual(result["courses_exported"], ["gcse_maths"])

    def test_missing_review_deck_is_skipped_not_fatal(self):
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths")
        self.make_subject("alex", "no_deck_course")
        self.make_review_deck("alex", "gcse_maths", [CARD_1])
        # no_deck_course has no _review_deck.json at all

        result = export_anki.export_decks("alex", root=self.root)
        self.assertEqual(result["courses_exported"], ["gcse_maths"])
        self.assertIn("no_deck_course", result["skipped_courses"])

    def test_never_writes_outside_exports_dir(self):
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths")
        self.make_review_deck("alex", "gcse_maths", [CARD_1])
        result = export_anki.export_decks("alex", root=self.root)
        expected_dir = os.path.join(self.root, "profile", "alex", "exports")
        self.assertEqual(os.path.dirname(result["apkg_path"]), expected_dir)

    def test_logs_one_line_to_toolkit_log(self):
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths")
        self.make_review_deck("alex", "gcse_maths", [CARD_1])
        export_anki.export_decks("alex", root=self.root)
        log_path = os.path.join(self.root, "profile", "alex", "toolkit_log", "anki_exports.jsonl")
        self.assertTrue(os.path.isfile(log_path))
        with open(log_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 1)

    def test_tags_carry_item_and_criterion(self):
        # Not directly observable from export_decks' return value, but the
        # note-building path must not raise on a card missing item_id/criterion
        # (CARD_2 has both as None) and must not raise on one that has them
        # (CARD_1) — covered implicitly by test_exports_real_apkg_file
        # succeeding on a deck containing both shapes.
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths")
        self.make_review_deck("alex", "gcse_maths", [CARD_1, CARD_2])
        result = export_anki.export_decks("alex", root=self.root)
        self.assertEqual(result["card_count"], 2)


if __name__ == "__main__":
    unittest.main()
