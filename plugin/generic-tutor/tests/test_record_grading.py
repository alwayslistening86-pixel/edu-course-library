"""V-09: per-criterion grading provenance, with no answer text."""
import json
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import purge_history  # noqa: E402
import record_grading as rg  # noqa: E402


class Grading(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.subj = os.path.join(self.fx["S"], "mathA.json")
        self.course = os.path.join(self.fx["C"], "mathA", "course.json")      # rubric S1: criteria M1, A1

    def rows(self):
        con = sqlite3.connect(os.path.join(self.fx["L"], "tutor.sqlite3"))
        try:
            return con.execute("SELECT stage_id, attempt, criterion_index, met, marks_awarded, marks_available, rubric_hash, slot FROM grading_results ORDER BY id").fetchall()
        finally:
            con.close()

    def rec(self, results, stage="S1", slot=5):
        return rg.record(self.subj, self.course, stage, slot, results)

    def test_records_each_criterion_and_numbers_the_attempts(self):
        r = self.rec([{"criterion": 1, "met": True, "marks": 2, "of": 2}, {"criterion": 2, "met": False, "marks": 0, "of": 3}])
        self.assertEqual((r["attempt"], r["criteria"], r["marks_awarded"], r["marks_available"], r["written"]), (1, 2, 2, 5, True))
        self.assertEqual(self.rec([{"criterion": 1, "met": True, "marks": 2, "of": 2}])["attempt"], 2)
        rows = self.rows()
        self.assertEqual([x[:6] for x in rows[:2]], [("S1", 1, 1, 1, 2, 2), ("S1", 1, 2, 0, 0, 3)])
        self.assertEqual(len({x[6] for x in rows}), 1)                           # one rubric hash for one rubric entry
        self.assertEqual(self.rec([{"criterion": 1, "met": True, "marks": 1, "of": 1}], stage="S2")["attempt"], 1)          # per stage

    def test_a_changed_rubric_gives_a_different_hash(self):
        a = self.rec([{"criterion": 1, "met": True, "marks": 1, "of": 1}])["rubric_hash"]
        rp = os.path.join(self.fx["C"], "mathA", "rubric.json")
        with open(rp) as f:
            rub = json.load(f)
        rub["stage_rubrics"]["S1"]["criteria"][0] = "A different first criterion, reworded after a source change."
        with open(rp, "w") as f:
            json.dump(rub, f)
        self.assertNotEqual(a, self.rec([{"criterion": 1, "met": True, "marks": 1, "of": 1}])["rubric_hash"])

    def test_bad_input_writes_nothing(self):
        bad = [[], "x", [{"criterion": 3, "met": True, "marks": 1, "of": 1}], [{"criterion": 0, "met": True, "marks": 1, "of": 1}],
               [{"criterion": 1, "met": "yes", "marks": 1, "of": 1}], [{"criterion": 1, "met": True, "marks": 5, "of": 2}],
               [{"criterion": 1, "met": True, "marks": 1, "of": 0}], [{"criterion": 1, "met": True, "marks": 1.5, "of": 2}],
               [{"criterion": 1, "met": True, "marks": 1, "of": 1}, {"criterion": 1, "met": False, "marks": 0, "of": 1}], [None]]
        for b in bad:
            self.assertIn("error", self.rec(b), b)
        self.assertIn("no rubric entry", self.rec([{"criterion": 1, "met": True, "marks": 1, "of": 1}], stage="S9")["error"])
        self.assertFalse(os.path.exists(os.path.join(self.fx["L"], "tutor.sqlite3")) and self.rows())

    def test_no_answer_text_or_rubric_wording_is_stored(self):
        self.rec([{"criterion": 1, "met": True, "marks": 1, "of": 1, "answer": "SECRET LEARNER ANSWER", "note": "quote"}])
        con = sqlite3.connect(os.path.join(self.fx["L"], "tutor.sqlite3"))
        try:
            cols = [r[1] for r in con.execute("PRAGMA table_info(grading_results)")]
            dump = json.dumps(con.execute("SELECT * FROM grading_results").fetchall())
        finally:
            con.close()
        self.assertNotIn("SECRET", dump)
        self.assertEqual(cols, ["id", "course_id", "stage_id", "attempt", "criterion_index", "met", "marks_awarded", "marks_available", "rubric_hash", "slot", "created_at"])

    def test_consent_limited_writes_nothing(self):
        pf = os.path.join(self.fx["L"], "student_profile.json")
        p = gs.read_json(pf)
        p["consent"]["status"] = "limited"
        with open(pf, "w") as f:
            json.dump(p, f)
        r = self.rec([{"criterion": 1, "met": True, "marks": 1, "of": 1}])
        self.assertEqual(r["written"], False)
        self.assertFalse(os.path.exists(os.path.join(self.fx["L"], "tutor.sqlite3")) and self.rows())

    def test_purge_by_course_removes_the_rows(self):
        self.rec([{"criterion": 1, "met": True, "marks": 1, "of": 1}])
        self.assertEqual(len(self.rows()), 1)
        r = purge_history.purge(self.fx["R"], "amy", "course", "mathA", confirm="PURGE amy mathA")
        self.assertTrue(r.get("purged"), r)
        self.assertEqual(self.rows(), [])

    def test_cli_reads_stdin(self):
        p = subprocess.run([sys.executable, os.path.join(gs.SCRIPTS, "record_grading.py"), self.subj, self.course, "S1", "5"],
                           input=json.dumps([{"criterion": 2, "met": True, "marks": 1, "of": 1}]), capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertEqual(json.loads(p.stdout)["attempt"], 1)
        self.assertEqual(subprocess.run([sys.executable, os.path.join(gs.SCRIPTS, "record_grading.py"), self.subj, self.course, "S1", "5"],
                                        input="{", capture_output=True, text=True).returncode, 1)


if __name__ == "__main__":
    unittest.main()
