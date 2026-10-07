"""L-08: assemble_paper.py and record_mock.py (exam simulation tooling)."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import assemble_paper  # noqa: E402
import golden_support as gs  # noqa: E402
import record_mock  # noqa: E402
from tutorlib import ledger, schema  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        gs.add_question_bank(self.fx["C"], "mathA")
        self.C = self.fx["C"]


class Assemble(Base):
    def test_bank_validates_and_paper_hits_the_marks_within_tolerance(self):
        self.assertEqual(schema.validate_file(f"{self.C}/mathA/question_bank.json", "question_bank"), [])
        p = assemble_paper.assemble(self.C, "mathA", marks=20)
        self.assertLessEqual(abs(p["total_marks"] - 20), assemble_paper.TOLERANCE)
        self.assertEqual(p["total_marks"], sum(q["marks"] for q in p["questions"]))
        self.assertEqual(p["minutes_suggested"], round(p["total_marks"] * assemble_paper.MINUTES_PER_MARK))

    def test_deterministic_per_seed_and_seed_changes_the_paper(self):
        a = assemble_paper.assemble(self.C, "mathA", marks=20, seed=1)
        self.assertEqual(a, assemble_paper.assemble(self.C, "mathA", marks=20, seed=1))
        others = {tuple(q["id"] for q in assemble_paper.assemble(self.C, "mathA", marks=20, seed=s)["questions"]) for s in range(6)}
        self.assertGreater(len(others), 1)

    def test_spreads_across_stages_and_items_before_repeating(self):
        p = assemble_paper.assemble(self.C, "mathA", marks=20)
        self.assertEqual(p["stages_covered"], ["S1", "S2", "S3"])

    def test_no_mark_scheme_or_answers_leak_into_the_paper(self):
        text = json.dumps(assemble_paper.assemble(self.C, "mathA", marks=20))
        self.assertNotIn("mark_scheme", text)
        self.assertNotIn("model_answer", text)
        self.assertNotIn("valid method", text)

    def test_filters_and_exclusions(self):
        p = assemble_paper.assemble(self.C, "mathA", marks=8, stages=["S2"])
        self.assertTrue(all(q["stage_id"] == "S2" for q in p["questions"]))
        ids = [q["id"] for q in p["questions"]]
        q = assemble_paper.assemble(self.C, "mathA", marks=8, stages=["S2"], exclude=ids)
        self.assertFalse(set(ids) & {x["id"] for x in q["questions"]})
        nocalc = assemble_paper.assemble(self.C, "mathA", marks=20, calculator="no")
        self.assertTrue(all(x["calculator"] in (None, False) for x in nocalc["questions"]))

    def test_honest_notes_and_unreachable_marks(self):
        p = assemble_paper.assemble(self.C, "mathA", marks=20)
        self.assertTrue(any("Grade boundaries" in n for n in p["notes"]))
        big = assemble_paper.assemble(self.C, "mathA", marks=500)
        self.assertTrue(any("could not reach" in n for n in big["notes"]))

    def test_errors(self):
        self.assertIn("no question_bank.json", assemble_paper.assemble(self.C, "solo")["error"])
        self.assertIn("no questions match", assemble_paper.assemble(self.C, "mathA", stages=["S9"])["error"])
        bank = f"{self.C}/mathA/question_bank.json"
        d = gs.read_json(bank)
        d["questions"][0].pop("mark_scheme")
        with open(bank, "w") as f:
            json.dump(d, f)
        self.assertIn("invalid", assemble_paper.assemble(self.C, "mathA")["error"])

    def test_cli(self):
        r = gs.run_step("assemble_paper.py", ["{C}", "mathA", "--marks", "12", "--seed", "3"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 0, r)
        self.assertEqual(gs.run_step("assemble_paper.py", ["{C}", "mathA", "--calculator", "maybe"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("assemble_paper.py", ["{C}", "mathA", "--marks", "x"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("assemble_paper.py", ["{C}", "solo"], self.fx, self.tmp)["exit"], 1)


class Mock(Base):
    def setUp(self):
        super().setUp()
        self.subj = f"{self.fx['S']}/mathA.json"
        self.prof = f"{self.fx['L']}/student_profile.json"

    def set_consent(self, status):
        d = gs.read_json(self.prof)
        d["consent"]["status"] = status
        with open(self.prof, "w") as f:
            json.dump(d, f)

    def test_records_percent_and_validates(self):
        r = record_mock.record(self.subj, 40, 31, 52, "2026-10-04", ["S1-Q1", "S2-Q2"])
        self.assertEqual((r["written"], r["mock"]["percent"]), (True, 77.5))
        d = gs.read_json(self.subj)
        self.assertEqual(schema.validate(d, "subjects"), [])
        self.assertEqual(d["mock_results"][0]["questions"], ["S1-Q1", "S2-Q2"])

    def test_keeps_the_most_recent_twenty_and_never_touches_progress(self):
        before = gs.read_json(self.subj)["syllabus_status"]
        for i in range(25):
            record_mock.record(self.subj, 10, i % 11, 5, "2026-10-04")
        d = gs.read_json(self.subj)
        self.assertEqual(len(d["mock_results"]), record_mock.KEEP)
        self.assertEqual(d["syllabus_status"], before)

    def test_refusals(self):
        for args in ((0, 0, 5), (10, 11, 5), (10, -1, 5), (10, 5, -2)):
            self.assertIn("error", record_mock.record(self.subj, *args, "2026-10-04"), args)
        self.assertIn("error", record_mock.record(self.subj, 10, 5, 5, "soon"))
        self.assertNotIn("mock_results", gs.read_json(self.subj))

    def test_signal_consent_and_ledger(self):
        self.set_consent("limited")
        r = record_mock.record(self.subj, 10, 5, 5, "2026-10-04")
        self.assertFalse(r["written"])
        self.assertNotIn("mock_results", gs.read_json(self.subj))
        self.set_consent("granted")
        record_mock.record(self.subj, 10, 5, 5, "2026-10-04")
        self.assertIn("record_mock.py", [e["script"] for e in ledger.read(self.fx["L"])])

    def test_cli(self):
        r = gs.run_step("record_mock.py", ["{S}/mathA.json", "40", "30", "50", "2026-10-04", "S1-Q1,S2-Q2"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 0, r)
        self.assertEqual(gs.run_step("record_mock.py", ["{S}/mathA.json", "x", "3", "4", "2026-10-04"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("record_mock.py", ["{S}/mathA.json"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("record_mock.py", ["{S}/mathA.json", "10", "11", "4", "2026-10-04"], self.fx, self.tmp)["exit"], 1)


if __name__ == "__main__":
    unittest.main()
