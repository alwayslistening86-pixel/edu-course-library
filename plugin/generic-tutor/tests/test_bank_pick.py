"""B-02.4: bank_pick.py offers only keyed questions, never prints the key, remembers what was met, refuses invented ids."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
from tutorlib import schema  # noqa: E402


class BankPick(unittest.TestCase):
    def setUp(self):
        self.d = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)
        self.fx = gs.build_fixture(self.d)
        self.bank = os.path.join(self.fx["C"], "mathA", "question_bank.json")
        self.subj = os.path.join(self.fx["S"], "mathA.json")
        with open(self.bank, encoding="utf-8") as f:
            data = json.load(f)
        qs = {q["id"]: q for q in data["questions"]}
        qs["S1-Q2"]["key"] = {"kind": "mcq", "options": ["red", "blue"], "correct": "B"}
        qs["S1-Q4"]["key"] = {"kind": "short", "accepted": ["x"]}
        qs["S1-Q4"]["item_ids"] = ["S1.9"]
        with open(self.bank, "w", encoding="utf-8") as f:
            json.dump(data, f)           # keyed in S1: Q1 (numeric), Q2 (mcq), Q3 (short), Q4 (short); S2 has none

    def run_it(self, *args):
        return gs.run_step("bank_pick.py", list(args), self.fx, self.d)

    def state(self):
        with open(self.subj, encoding="utf-8") as f:
            return json.load(f)

    def test_next_offers_a_keyed_question_and_never_the_key(self):
        r = self.run_it("next", self.subj, self.bank, "S1")
        self.assertEqual(r["exit"], 0, r)
        out = r["stdout"]
        self.assertEqual((out["keyed_total"], out["remaining"], out["recommendation"]), (4, 4, "ask:S1-Q1"))
        text = json.dumps(out)
        for leak in ('"key"', '"correct"', "accepted", "tolerance"):
            self.assertNotIn(leak, text)

    def test_mcq_options_are_shown(self):
        self.run_it("used", self.subj, self.bank, "S1", "S1-Q1")
        out = self.run_it("next", self.subj, self.bank, "S1")["stdout"]
        self.assertEqual(out["question"]["id"], "S1-Q2")
        self.assertEqual(out["question"]["options"], ["red", "blue"])
        self.assertNotIn("correct", json.dumps(out))

    def test_used_questions_are_skipped_and_exhaustion_is_said(self):
        for qid in ("S1-Q1", "S1-Q2", "S1-Q3", "S1-Q4"):
            self.assertEqual(self.run_it("used", self.subj, self.bank, "S1", qid)["exit"], 0)
        out = self.run_it("next", self.subj, self.bank, "S1")["stdout"]
        self.assertEqual((out["recommendation"], out["question"], out["remaining"]), ("none_left", None, 0))

    def test_a_stage_with_no_keyed_questions_goes_to_the_examiner(self):
        out = self.run_it("next", self.subj, self.bank, "S2")["stdout"]
        self.assertEqual((out["recommendation"], out["keyed_total"]), ("no_keyed_questions", 0))

    def test_prefer_puts_weak_items_first_but_keeps_bank_order_otherwise(self):
        out = self.run_it("next", self.subj, self.bank, "S1", "--prefer", "S1.9")["stdout"]
        self.assertEqual(out["question"]["id"], "S1-Q4")
        self.run_it("used", self.subj, self.bank, "S1", "S1-Q4")
        self.assertEqual(self.run_it("next", self.subj, self.bank, "S1", "--prefer", "S1.9")["stdout"]["question"]["id"], "S1-Q1")

    def test_used_refuses_invented_unkeyed_or_other_stage_ids_and_writes_nothing(self):
        before = self.state()
        for stage, qid in (("S1", "nope"), ("S1", "S1-Q5"), ("S2", "S1-Q1")):
            r = self.run_it("used", self.subj, self.bank, stage, qid)
            self.assertEqual(r["exit"], 1, (stage, qid))
        self.assertEqual(self.state(), before)

    def test_used_records_once_and_the_file_stays_valid(self):
        r = self.run_it("used", self.subj, self.bank, "S1", "S1-Q2")
        self.assertEqual((r["exit"], r["stdout"]["written"], r["stdout"]["already_recorded"]), (0, True, False))
        again = self.run_it("used", self.subj, self.bank, "S1", "S1-Q2")["stdout"]
        self.assertTrue(again["already_recorded"])
        rec = self.state()["practice_used"]["S1"]
        self.assertEqual((rec["bank"], rec["bank_last"]), (["S1-Q2"], "S1-Q2"))
        self.assertEqual(schema.validate(self.state(), "subjects"), [])

    def test_usage(self):
        self.assertEqual(self.run_it("next", self.subj)["exit"], 2)
        self.assertEqual(self.run_it("next", self.subj, self.bank, "S1", "--prefer")["exit"], 2)
        self.assertEqual(self.run_it("used", self.subj, self.bank, "S1", "S1-Q1", "--prefer", "x")["exit"], 2)


if __name__ == "__main__":
    unittest.main()
