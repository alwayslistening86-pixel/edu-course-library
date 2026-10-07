"""E-16: canned reports over the history database."""
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import history_report as hr  # noqa: E402


class Reports(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.s = f"{self.fx['S']}/mathA.json"
        self.deck = f"{self.fx['S']}/mathA_review_deck.json"
        self.L = self.fx["L"]

    def step(self, script, *args):
        return gs.run_step(script, list(args), self.fx, self.tmp)

    def test_missing_database_is_an_error_not_a_creation(self):
        self.assertIn("error", hr.run("mastery", self.tmp))
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "tutor.sqlite3")))

    def test_bad_report_name(self):
        self.assertIn("error", hr.run("nope", self.L))

    def test_mastery_trend(self):
        for slot, ok in enumerate(("true", "true", "true", "false"), start=5):
            self.step("item_mastery.py", "observe", self.s, "S1.1", ok, str(slot))
        self.step("item_mastery.py", "observe", self.s, "S1.2", "false", "5")
        r = hr.run("mastery", self.L)
        by = {e["item_id"]: e for e in r["items"]}
        self.assertEqual(by["S1.1"]["observations"], 4)
        self.assertEqual(by["S1.1"]["correct"], 3)
        self.assertFalse(by["S1.1"]["last_correct"])
        self.assertEqual(by["S1.2"]["trend"], "down")
        self.assertEqual(hr.run("mastery", self.L, "no-such-course")["items"], [])

    def test_ease_drift(self):
        for slot, ok in ((6, "true"), (8, "false"), (9, "true")):
            self.step("review_math.py", "apply", self.deck, "k1", str(slot), ok)
        card = hr.run("ease", self.L)["cards"][0]
        self.assertEqual((card["card_id"], card["reviews"], card["wrong"]), ("k1", 3, 1))
        self.assertEqual(card["ease_change"], round(card["latest_ease"] - card["first_ease"], 3))

    def test_error_recurrence_orders_by_count(self):
        for slot in (6, 7, 8):
            self.step("error_log.py", "append", self.s, "S2", "S2.1", "practice", "misconception", "MC-1", "x", str(slot))
        self.step("error_log.py", "append", self.s, "S2", "S2.2", "practice", "slip", "NONE", "y", "9")
        self.step("error_log.py", "resolve", self.s, "S2.2", "10")
        r = hr.run("errors", self.L)
        self.assertEqual((r["groups"][0]["count"], r["groups"][0]["misconception_id"], r["groups"][0]["open"]), (3, "MC-1", 3))
        self.assertEqual(r["recurring_groups"], 1)
        self.assertEqual(r["groups"][1]["open"], 0)
        self.assertIsNone(r["groups"][1]["misconception_id"])

    def test_database_is_opened_read_only(self):
        self.step("item_mastery.py", "observe", self.s, "S1.1", "true", "5")
        con = hr._connect(self.L)
        self.addCleanup(con.close)
        import sqlite3
        with self.assertRaises(sqlite3.OperationalError):
            con.execute("DELETE FROM item_mastery_log")


if __name__ == "__main__":
    unittest.main()
