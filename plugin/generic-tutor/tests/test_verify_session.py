"""V-01/V-03/V-05/V-06: session ledger, verifier rules, and a fault-injection detection-rate check."""
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
import verify_session  # noqa: E402
from tutorlib import ledger  # noqa: E402

S = "{S}/mathA.json"
COURSE = "{C}/mathA/course.json"
DECK = "{S}/mathA_review_deck.json"


class Session(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)

    def call(self, script, args, expect_exit=0):
        r = gs.run_step(script, args, self.fx, self.tmp)
        self.assertEqual(r["exit"], expect_exit, (script, r))
        return r

    def start(self):
        self.call("slot_advance.py", ["{P}/student_profile.json", "--min-gap-minutes", "0"])

    def seed_cards(self, stage):
        deck = gs.read_json(self.fx["S"] + "/mathA_review_deck.json")
        deck["cards"].append({"id": f"c_{stage}", "stage_id": stage, "front": "f", "back": "b", "interval_sessions": 1,
                              "ease": 2.3, "lapses": 0, "due_at_slot": 99})
        with open(self.fx["S"] + "/mathA_review_deck.json", "w") as f:
            json.dump(deck, f)

    def verify(self, slot=None):
        entries = ledger.read(self.fx["L"])
        slot = slot if slot is not None else gs.read_json(self.fx["L"] + "/student_profile.json")["session_slot"]
        return verify_session.verify(entries, self.fx["L"], slot)

    # --- complete sessions: no findings -------------------------------------------------------------
    def test_complete_pass_session_is_clean(self):
        self.start()
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        self.call("record_stage_result.py", ["apply", S, COURSE, "S2", "pass"])
        self.call("confidence_update.py", ["apply", S, "pass_clean", "6"])
        self.seed_cards("S2")
        self.assertEqual(self.verify(), [])

    def test_complete_fail_session_is_clean(self):
        self.start()
        self.call("record_stage_result.py", ["apply", S, COURSE, "S2", "fail"])
        self.call("confidence_update.py", ["apply", S, "fail", "6"])
        self.call("remediation_state.py", ["record", S, "S2", "slip", "6"])
        self.assertEqual(self.verify(), [])

    def test_remediated_pass_variant_is_clean(self):
        self.start()
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        self.call("record_stage_result.py", ["apply", S, COURSE, "S2", "pass"])
        self.call("confidence_update.py", ["apply", S, "pass_remediated", "6"])
        self.call("remediation_state.py", ["reset", S, "S2"])
        self.seed_cards("S2")
        self.assertEqual(self.verify(), [])

    def test_practice_only_session_is_clean(self):
        self.start()
        self.call("error_log.py", ["append", S, "S2", "S2.1", "practice", "slip", "NONE", "n", "6"])
        self.call("review_math.py", ["apply", DECK, "k1", "6", "true"])
        self.assertEqual(self.verify(), [])

    # --- fault injection (V-05) ---------------------------------------------------------------------
    def faults(self):
        """(name, expected rule, steps run after /run) -- each omits or repeats exactly one required write."""
        P = ("record_stage_result.py", ["apply", S, COURSE, "S2", "pass"])
        F = ("record_stage_result.py", ["apply", S, COURSE, "S2", "fail"])
        CP = ("confidence_update.py", ["apply", S, "pass_clean", "6"])
        CF = ("confidence_update.py", ["apply", S, "fail", "6"])
        R = ("remediation_state.py", ["record", S, "S2", "slip", "6"])
        return [
            ("pass without confidence", "stage-pass-confidence", [P], True),
            ("pass without cards", "stage-pass-cards", [P, CP], False),
            ("fail without confidence", "stage-fail-confidence", [F, R], False),
            ("fail without remediation", "stage-fail-remediation", [F, CF], False),
            ("confidence applied twice", "confidence-duplicated", [P, CP, CP], True),
            ("result recorded twice", "stage-result-duplicated", [P, P, CP], True),
            ("wrong confidence event for pass", "stage-pass-confidence", [P, CF], True),
            ("wrong confidence event for fail", "stage-fail-confidence", [F, CP, R], False),
        ]

    def test_every_injected_fault_is_detected_and_nothing_extra_is_missing(self):
        detected = 0
        faults = self.faults()
        for name, rule, steps, seed in faults:
            with self.subTest(name):
                self.tearDown_fixture()
                self.start()
                gs.grade(self.fx, self.tmp, "mathA", "S2")
                for script, args in steps:
                    self.call(script, args)
                if seed:
                    self.seed_cards("S2")
                rules = [f["rule"] for f in self.verify()]
                self.assertIn(rule, rules, name)
                detected += rule in rules
        self.assertGreaterEqual(detected / len(faults), 0.95)  # PLAN section 9 target

    def tearDown_fixture(self):
        shutil.rmtree(self.tmp, True)
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)

    def test_no_slot_advance_is_flagged(self):
        self.call("error_log.py", ["append", S, "S2", "S2.1", "practice", "slip", "NONE", "n", "5"])
        self.assertIn("no-slot-advance", [f["rule"] for f in self.verify()])

    # --- ledger behaviour ---------------------------------------------------------------------------
    def test_ledger_lines_carry_slot_and_detail(self):
        self.start()
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        self.call("record_stage_result.py", ["apply", S, COURSE, "S2", "pass"])
        lines = ledger.read(self.fx["L"])
        self.assertEqual([e["script"] for e in lines], ["slot_advance.py", "record_grading.py", "record_stage_result.py"])
        self.assertEqual(lines[2]["slot"], 6)
        self.assertEqual(lines[2]["detail"]["stage_id"], "S2")
        self.assertEqual(lines[2]["detail"]["result"], "pass")
        self.assertEqual(lines[2]["course_id"], "mathA")

    def test_revoked_consent_writes_no_ledger_and_limited_still_does(self):
        prof = self.fx["L"] + "/student_profile.json"
        d = gs.read_json(prof)
        d["consent"]["status"] = "revoked"
        with open(prof, "w") as f:
            json.dump(d, f)
        self.call("error_log.py", ["append", S, "S2", "S2.1", "practice", "slip", "NONE", "n", "5"])
        self.assertFalse(os.path.exists(self.fx["L"] + "/.session_ledger.jsonl"))
        d["consent"]["status"] = "limited"
        with open(prof, "w") as f:
            json.dump(d, f)
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        self.call("record_stage_result.py", ["apply", S, COURSE, "S2", "pass"])
        self.assertEqual(len(ledger.read(self.fx["L"])), 1)

    def test_skipped_writes_are_not_counted_as_writes(self):
        prof = self.fx["L"] + "/student_profile.json"
        d = gs.read_json(prof)
        d["consent"]["status"] = "limited"
        with open(prof, "w") as f:
            json.dump(d, f)
        self.start()
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        self.call("record_stage_result.py", ["apply", S, COURSE, "S2", "pass"])
        self.call("confidence_update.py", ["apply", S, "pass_clean", "6"])  # skipped under limited
        entries = ledger.read(self.fx["L"])
        self.assertFalse(entries[-1]["written"])
        self.assertIn("stage-pass-confidence", [f["rule"] for f in self.verify()])

    def test_cli_previous_flag_and_exit(self):
        self.start()
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        self.call("record_stage_result.py", ["apply", S, COURSE, "S2", "pass"])
        self.start()  # next session: slot 7
        r = self.call("verify_session.py", ["{L}", "--previous"])
        self.assertEqual(r["stdout"]["slot"], 6)
        self.assertFalse(r["stdout"]["ok"])
        self.assertEqual({f["rule"] for f in r["stdout"]["findings"]}, {"stage-pass-confidence", "stage-pass-cards"})
        self.call("verify_session.py", ["{L}", "--slot"], expect_exit=2)
        self.call("verify_session.py", [], expect_exit=2)

    def test_corrupt_ledger_line_does_not_crash(self):
        self.start()
        with open(self.fx["L"] + "/.session_ledger.jsonl", "a") as f:
            f.write("{not json\n")
        self.assertIsInstance(self.verify(), list)


if __name__ == "__main__":
    unittest.main()
