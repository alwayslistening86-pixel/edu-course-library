"""X-05: selective purge (history only, or one course) with a typed confirmation."""
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import purge_history as ph  # noqa: E402


class Purge(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.root, self.L, self.S = self.fx["R"], self.fx["L"], self.fx["S"]
        for cid in ("mathA", "solo"):
            s = f"{self.S}/{cid}.json"
            gs.run_step("item_mastery.py", ["observe", s, "S1.1", "true", "5"], self.fx, self.tmp)
            gs.run_step("error_log.py", ["append", s, "S1", "S1.1", "practice", "slip", "NONE", "x", "6"], self.fx, self.tmp)
        gs.run_step("review_math.py", ["apply", f"{self.S}/mathA_review_deck.json", "k1", "6", "true"], self.fx, self.tmp)

    def rows(self, table, cid):
        con = sqlite3.connect(f"{self.L}/tutor.sqlite3")
        try:
            return con.execute(f"SELECT COUNT(*) FROM {table} WHERE course_id = ?", (cid,)).fetchone()[0]
        finally:
            con.close()

    def test_dry_run_deletes_nothing_and_names_the_phrase(self):
        r = ph.purge(self.root, "amy", "history")
        self.assertEqual((r["purged"], r["dry_run"], r["required_confirmation"]), (False, True, "PURGE amy history"))
        self.assertTrue(os.path.exists(f"{self.L}/tutor.sqlite3"))
        r = ph.purge(self.root, "amy", "course", "mathA")
        self.assertEqual(r["required_confirmation"], "PURGE amy mathA")
        self.assertGreater(r["history_rows"]["error_events"], 0)
        self.assertTrue(os.path.exists(f"{self.S}/mathA.json"))

    def test_wrong_phrase_is_refused(self):
        for phrase in ("yes", "PURGE amy", "purge amy history", "PURGE bob history"):
            self.assertIn("error", ph.purge(self.root, "amy", "history", None, phrase), phrase)
        self.assertTrue(os.path.exists(f"{self.L}/tutor.sqlite3"))

    def test_history_purge_keeps_progress_and_teaching_continues(self):
        before = gs.read_json(f"{self.S}/mathA.json")
        r = ph.purge(self.root, "amy", "history", None, "PURGE amy history")
        self.assertTrue(r["purged"])
        self.assertFalse(os.path.exists(f"{self.L}/tutor.sqlite3"))
        self.assertFalse(os.path.exists(f"{self.L}/.session_ledger.jsonl"))
        self.assertEqual(gs.read_json(f"{self.S}/mathA.json"), before)
        out = gs.run_step("error_log.py", ["append", f"{self.S}/mathA.json", "S1", "S1.1", "practice", "slip", "NONE", "y", "7"], self.fx, self.tmp)
        self.assertEqual(out["exit"], 0)

    def test_course_purge_removes_only_that_course(self):
        r = ph.purge(self.root, "amy", "course", "mathA", "PURGE amy mathA")
        self.assertTrue(r["purged"])
        self.assertFalse(os.path.exists(f"{self.S}/mathA.json"))
        self.assertFalse(os.path.exists(f"{self.S}/mathA_review_deck.json"))
        self.assertTrue(os.path.exists(f"{self.S}/solo.json"))
        self.assertTrue(os.path.exists(f"{self.L}/student_profile.json"))
        self.assertEqual((self.rows("error_events", "mathA"), self.rows("item_mastery", "mathA"), self.rows("item_mastery_log", "mathA")), (0, 0, 0))
        self.assertGreater(self.rows("error_events", "solo"), 0)
        con = sqlite3.connect(f"{self.L}/tutor.sqlite3")
        try:
            self.assertEqual(con.execute("SELECT COUNT(*) FROM review_log").fetchone()[0], 0)
        finally:
            con.close()
        with open(f"{self.L}/.session_ledger.jsonl") as f:
            courses = {json.loads(line)["course_id"] for line in f}
        self.assertNotIn("mathA", courses)
        self.assertIn("solo", courses)

    def test_bad_inputs(self):
        self.assertIn("error", ph.purge(self.root, "../x", "history"))
        self.assertIn("error", ph.purge(self.root, "amy", "course", "../etc"))
        self.assertIn("not enrolled", ph.purge(self.root, "amy", "course", "ghost")["error"])
        self.assertIn("error", ph.purge(self.root, "nobody", "history"))
        self.assertIn("error", ph.purge(self.root, "amy", "everything"))


if __name__ == "__main__":
    unittest.main()
