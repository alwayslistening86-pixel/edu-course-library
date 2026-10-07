"""V-08: cross-file invariants."""
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
import invariants  # noqa: E402


class Invariants(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.subj = self.fx["S"] + "/mathA.json"

    def run_check(self):
        return invariants.check(self.fx["L"], self.fx["C"])

    def edit(self, path, fn):
        d = gs.read_json(path)
        fn(d)
        with open(path, "w") as f:
            json.dump(d, f)

    def kinds(self):
        return {p["check"] for p in self.run_check()["problems"]}

    def test_fixture_is_clean(self):
        r = self.run_check()
        self.assertTrue(r["ok"], r["problems"])

    def test_ladder_keys_and_current_stage(self):
        self.edit(self.subj, lambda d: d["syllabus_status"].pop("S3"))
        self.assertIn("ladder-keys", self.kinds())
        self.setUp()
        self.edit(self.subj, lambda d: d.update(current_stage="S9"))
        self.assertIn("current-stage", self.kinds())

    def test_linear_order_violation(self):
        self.edit(self.subj, lambda d: d["syllabus_status"].update(S1="unsat", S3="pass"))
        self.assertIn("linear-order", self.kinds())

    def test_deck_checks(self):
        deck = self.fx["S"] + "/mathA_review_deck.json"
        self.edit(deck, lambda d: d["cards"].append(dict(d["cards"][0])))
        self.assertIn("deck-duplicate-id", self.kinds())
        self.edit(deck, lambda d: d["cards"][0].update(stage_id="S9"))
        self.assertIn("deck-stage", self.kinds())

    def test_error_checks(self):
        e = {"id": "e1", "stage_id": "S1", "source_phase": "practice", "cause": "slip", "slot": 1, "resolved": True, "resolved_at_slot": None}
        self.edit(self.subj, lambda d: d["error_patterns"].extend([e, dict(e)]))
        self.assertTrue({"error-duplicate-id", "error-resolved"} <= self.kinds())

    def test_schema_violation_and_unknown_course(self):
        self.edit(self.subj, lambda d: d.update(confidence="medium"))
        self.assertIn("schema", self.kinds())
        self.edit(self.fx["S"] + "/solo.json", lambda d: d.update(course_id="ghost"))
        self.assertIn("unknown-course", self.kinds())

    def test_slot_regression(self):
        with open(self.fx["L"] + "/.session_ledger.jsonl", "w") as f:
            f.write(json.dumps({"slot": 50, "script": "x", "action": "y", "written": True}) + "\n")
        self.assertIn("slot-regression", self.kinds())

    def test_cli(self):
        r = gs.run_step("invariants.py", ["{L}", "{C}"], self.fx, self.tmp)
        self.assertEqual((r["exit"], r["stdout"]["ok"]), (0, True))
        self.assertEqual(gs.run_step("invariants.py", ["{L}"], self.fx, self.tmp)["exit"], 2)


if __name__ == "__main__":
    unittest.main()
