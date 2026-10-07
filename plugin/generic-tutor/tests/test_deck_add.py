"""deck_add.py: card quality, dedupe, caps, defaults, consent."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import deck_add  # noqa: E402
import golden_support as gs  # noqa: E402
from tutorlib import schema  # noqa: E402


class Add(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.deck = f"{self.fx['S']}/solo_review_deck.json"              # does not exist yet
        self.mathdeck = f"{self.fx['S']}/mathA_review_deck.json"

    def card(self, n, **kw):
        return {"front": f"What is fact number {n}?", "back": f"Fact {n}.", **kw}

    def test_creates_deck_with_defaults_and_valid_shape(self):
        r = deck_add.add(self.deck, "solo", "S1", [self.card(1, item_id="S1.1", criterion="M1"), self.card(2)])
        self.assertEqual((r["added"], r["written"]), (["S1-c1", "S1-c2"], True))
        d = gs.read_json(self.deck)
        self.assertEqual(schema.validate(d, "review_deck"), [])
        c = d["cards"][0]
        self.assertEqual((c["interval_sessions"], c["ease"], c["lapses"], c["due_at_slot"]), (1, 2.3, 0, 6))   # slot 5 + 1
        self.assertIsNone(d["cards"][1]["item_id"])

    def test_ids_continue_and_never_collide(self):
        deck_add.add(self.mathdeck, "mathA", "S1", [self.card(1)])
        self.assertEqual(deck_add.add(self.mathdeck, "mathA", "S1", [self.card(2)])["added"], ["S1-c2"])

    def test_quality_rules(self):
        bad = [
            {"front": "", "back": "x"}, {"front": "q?", "back": ""}, {"front": "x" * 201, "back": "y"},
            {"front": "What is a? And what is b?", "back": "x"}, {"front": "a) one b) two", "back": "x"}, "nope",
            {"front": "q", "back": "y" * 401}, {"front": "q", "back": "a", "item_id": 3},
        ]
        r = deck_add.add(self.deck, "solo", "S1", bad + [self.card(9)])
        self.assertEqual(r["added"], ["S1-c1"])
        self.assertEqual(len(r["rejected"]), len(bad))

    def test_duplicates_are_skipped_even_when_formatted_differently(self):
        deck_add.add(self.deck, "solo", "S1", [{"front": "What is 2 + 2?", "back": "4"}])
        r = deck_add.add(self.deck, "solo", "S2", [{"front": "  what is 2+2 ", "back": "4"}, {"front": "what is 2 + 2?", "back": "4"}])
        self.assertEqual(r["added"], [])
        self.assertTrue(all("duplicate" in x["reason"] for x in r["rejected"]))
        self.assertFalse(r["written"])

    def test_per_call_cap(self):
        r = deck_add.add(self.deck, "solo", "S1", [self.card(i) for i in range(20)], max_per_stage=5)
        self.assertEqual((len(r["added"]), len(r["rejected"])), (5, 15))

    def test_consent(self):
        pf = f"{self.fx['L']}/student_profile.json"
        for status, wrote in (("limited", True), ("revoked", False)):
            p = gs.read_json(pf)
            p["consent"]["status"] = status
            with open(pf, "w") as f:
                json.dump(p, f)
            r = deck_add.add(self.deck, "solo", "S1", [self.card(len(status))])
            self.assertEqual(r.get("written", False), wrote, status)
        self.assertEqual(r["action"], "not_persisted")

    def test_cli_reads_stdin(self):
        p = subprocess.run([sys.executable, os.path.join(gs.SCRIPTS, "deck_add.py"), self.deck, "solo", "S1"],
                           input=json.dumps([self.card(1)]), capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout)
        self.assertEqual(json.loads(p.stdout)["added"], ["S1-c1"])
        p = subprocess.run([sys.executable, os.path.join(gs.SCRIPTS, "deck_add.py"), self.deck, "solo", "S1"], input="{", capture_output=True, text=True)
        self.assertEqual(p.returncode, 1)


class Lifecycle(Add):
    """K-22: retire and mature."""
    def fill(self):
        deck_add.add(self.deck, "solo", "S1", [self.card(i) for i in range(1, 5)])
        d = gs.read_json(self.deck)
        d["cards"][0].update(interval_sessions=25, lapses=0)
        d["cards"][1].update(interval_sessions=30, lapses=2)          # old but lapsed: not mature
        d["cards"][2].update(interval_sessions=21, lapses=0)
        with open(self.deck, "w") as f:
            json.dump(d, f)

    def test_mature_lists_only_long_known_cards_without_lapses(self):
        self.fill()
        r = deck_add.mature(self.deck)
        self.assertEqual([c["id"] for c in r["mature"]], ["S1-c1", "S1-c3"])
        self.assertIn("error", deck_add.mature(self.deck + ".none"))

    def test_retire_removes_only_the_named_cards_and_reports_unknowns(self):
        self.fill()
        r = deck_add.retire(self.deck, ["S1-c1", "S1-c3", "S1-c99"])
        self.assertEqual((r["retired"], r["unknown"], r["deck_size"], r["written"]), (["S1-c1", "S1-c3"], ["S1-c99"], 2, True))
        d = gs.read_json(self.deck)
        self.assertEqual([c["id"] for c in d["cards"]], ["S1-c2", "S1-c4"])
        self.assertEqual(schema.validate(d, "review_deck"), [])
        self.assertFalse(deck_add.retire(self.deck, ["S1-c99"])["written"])
        self.assertIn("error", deck_add.retire(self.deck + ".none", ["x"]))

    def test_retiring_makes_room_in_a_full_deck(self):
        self.fill()
        d = gs.read_json(self.deck)
        d["cards"] += [{"id": f"X-c{i}", "stage_id": "X", "item_id": None, "criterion": None, "front": f"filler {i}", "back": "b",
                        "interval_sessions": 1, "ease": 2.3, "lapses": 0, "due_at_slot": 9} for i in range(deck_add.MAX_DECK - 4)]
        with open(self.deck, "w") as f:
            json.dump(d, f)
        self.assertIn("deck is full", deck_add.add(self.deck, "solo", "S2", [self.card(77)])["rejected"][0]["reason"])
        deck_add.retire(self.deck, ["S1-c1"])
        self.assertEqual(deck_add.add(self.deck, "solo", "S2", [self.card(77)])["added"], ["S2-c1"])

    def test_retire_consent_and_cli(self):
        self.fill()
        pf = f"{self.fx['L']}/student_profile.json"
        p = gs.read_json(pf)
        p["consent"]["status"] = "revoked"
        with open(pf, "w") as f:
            json.dump(p, f)
        self.assertEqual(deck_add.retire(self.deck, ["S1-c1"])["action"], "not_persisted")
        self.assertEqual(len(gs.read_json(self.deck)["cards"]), 4)
        out = subprocess.run([sys.executable, os.path.join(gs.SCRIPTS, "deck_add.py"), "mature", self.deck], capture_output=True, text=True)
        self.assertEqual(json.loads(out.stdout)["deck_size"], 4)


if __name__ == "__main__":
    unittest.main()
