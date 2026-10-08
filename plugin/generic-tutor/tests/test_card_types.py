"""L-06: review-card types are validated on the way in and shown properly on the way out. Stdlib only."""
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "toolkit"))

import deck_add  # noqa: E402
import export_anki  # noqa: E402
import review_select  # noqa: E402
from golden_support import build_fixture  # noqa: E402
from tutorlib import cards, schema  # noqa: E402


class CardTypes(unittest.TestCase):
    def test_older_cards_read_as_basic(self):
        self.assertEqual(cards.type_of({"front": "q", "back": "a"}), "basic")
        self.assertEqual(cards.type_of({"card_type": "nonsense"}), "basic")

    def test_check_type_per_type(self):
        ok = [{"card_type": "cloze", "front": "The {{c1::mitochondria}} release energy."},
              {"card_type": "explain_why", "front": "Why does ice float on water?"},
              {"card_type": "worked_step", "front": "Solve 2x+3=9. Step 1: 2x=6. What is the next step?"},
              {"card_type": "basic", "front": "What is 2+2?"}, {"front": "What is 2+2?"}]
        for c in ok:
            self.assertIsNone(cards.check_type(c), c)
        bad = [{"card_type": "cloze", "front": "No deletion here"}, {"card_type": "explain_why", "front": "Define osmosis."},
               {"card_type": "worked_step", "front": "Solve 2x+3=9."}, {"card_type": "flashy", "front": "x"}]
        for c in bad:
            self.assertIsNotNone(cards.check_type(c), c)

    def test_cloze_prompt_and_answers(self):
        c = {"card_type": "cloze", "front": "The {{c1::mitochondria}} make {{c2::ATP}}."}
        self.assertEqual(cards.prompt_for(c), "The [...] make [...].")
        self.assertEqual(cards.answers_for(c), ["mitochondria", "ATP"])
        self.assertEqual(cards.prompt_for({"front": "Plain {{c1::x}} front"}), "Plain {{c1::x}} front")

    def test_schema_accepts_card_type_and_rejects_unknown(self):
        deck = {"cards": [{"id": "a", "front": "f", "back": "b", "interval_sessions": 1, "ease": 2.3, "lapses": 0, "due_at_slot": 1, "card_type": "cloze"}]}
        self.assertEqual(schema.validate(deck, "review_deck"), [])
        deck["cards"][0]["card_type"] = "nope"
        self.assertTrue(schema.validate(deck, "review_deck"))

    def test_anki_tags_the_new_types(self):
        kind, _, tags = export_anki.note_parts({"front": "Why is the sky blue?", "back": "Scattering.", "card_type": "explain_why"}, "sci")
        self.assertEqual(kind, "basic")
        self.assertIn("type_explain_why", tags)


class DeckFlow(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = build_fixture(self.tmp)
        self.deck = os.path.join(self.fx["S"], "mathA_review_deck.json")

    def test_deck_add_stores_type_and_rejects_misfiled(self):
        r = deck_add.add(self.deck, "mathA", "S2", [
            {"front": "Plants make {{c1::glucose}} by photosynthesis.", "back": "Glucose is the sugar plants make.", "card_type": "cloze"},
            {"front": "Why do plants need light?", "back": "Light energy drives photosynthesis.", "card_type": "explain_why"},
            {"front": "Name the organ.", "back": "Heart.", "card_type": "cloze"},
            {"front": "Plain question one?", "back": "Yes."}])
        self.assertEqual(len(r["added"]), 3)
        self.assertEqual(len(r["rejected"]), 1)
        self.assertIn("cloze", r["rejected"][0]["reason"])
        with open(self.deck, encoding="utf-8") as f:
            saved = {c["front"]: c for c in json.load(f)["cards"]}
        self.assertEqual(saved["Plants make {{c1::glucose}} by photosynthesis."]["card_type"], "cloze")
        self.assertNotIn("card_type", saved["Plain question one?"])

    def test_review_select_shows_blanked_prompt(self):
        with open(self.deck, encoding="utf-8") as f:
            d = json.load(f)
        d["cards"].append({"id": "S1-c9", "stage_id": "S1", "item_id": None, "criterion": None, "front": "The {{c1::heart}} pumps blood.",
                           "back": "Heart.", "card_type": "cloze", "interval_sessions": 1, "ease": 2.3, "lapses": 0, "due_at_slot": 0})
        with open(self.deck, "w", encoding="utf-8") as f:
            json.dump(d, f)
        out = review_select.select(self.fx["L"], self.fx["C"])
        card = next(c for c in out["selected"] if c["card_id"] == "S1-c9")
        self.assertEqual((card["card_type"], card["prompt"], card["answers"]), ("cloze", "The [...] pumps blood.", ["heart"]))
        plain = next(c for c in out["selected"] if c["card_id"] == "k1")
        self.assertEqual((plain["card_type"], plain["prompt"]), ("basic", plain["front"]))


if __name__ == "__main__":
    unittest.main()
