"""E-13: what happens when each state writer is called twice with the same arguments. The table is in docs/DATA_MODEL.md."""
import glob
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402


class Repeat(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.s = f"{self.fx['S']}/mathA.json"
        self.c = f"{self.fx['C']}/mathA/course.json"
        self.deck = glob.glob(self.fx["S"] + "/*deck*")[0]
        self.p = f"{self.fx['P']}/student_profile.json"

    def twice(self, script, args):
        return [gs.run_step(script, args, self.fx, self.tmp)["stdout"] for _ in range(2)]

    def get(self, path=None):
        return gs.read_json(path or self.s)

    # --- idempotent: the second call changes nothing -------------------------------------------------
    def test_notice_is_acknowledged_once(self):
        a, b = self.twice("session_state.py", ["notice", self.s, "n1", "2026-10-04"])
        self.assertTrue(a["written"])
        self.assertFalse(b["written"])
        self.assertEqual(len(self.get()["notices_acknowledged"]), 1)

    def test_slot_advances_once_per_sitting(self):
        a, b = self.twice("slot_advance.py", [self.p])
        self.assertEqual(b["current_slot"], a["current_slot"])
        self.assertIn("skipped", b)

    def test_resolve_second_call_resolves_nothing(self):
        gs.run_step("error_log.py", ["append", self.s, "S2", "S2.1", "practice", "slip", "NONE", "x", "6"], self.fx, self.tmp)
        a, b = self.twice("error_log.py", ["resolve", self.s, "S2.1", "8"])
        self.assertEqual((a["count"], b["count"]), (1, 0))

    def test_pass_replay_never_moves_the_learner_backwards(self):
        import json
        course = gs.read_json(self.c)
        course["stage_ladder"] = course["stage_ladder"] + ["S4"]
        with open(self.c, "w") as f:
            json.dump(course, f)
        for stage in ("S2", "S3"):
            gs.run_step("record_stage_result.py", ["apply", self.s, self.c, stage, "pass"], self.fx, self.tmp)
        self.assertEqual(self.get()["current_stage"], "S4")
        before = self.get()["current_stage"]
        a, b = self.twice("record_stage_result.py", ["apply", self.s, self.c, "S2", "pass"])
        self.assertEqual(self.get()["current_stage"], before)
        self.assertIsNone(b["advanced_to"])

    def test_pass_twice_in_a_row_is_stable(self):
        a, b = self.twice("record_stage_result.py", ["apply", self.s, self.c, "S2", "pass"])
        self.assertEqual(a["advanced_to"], "S3")
        self.assertEqual(self.get()["current_stage"], "S3")
        self.assertEqual(self.get()["syllabus_status"]["S2"], "pass")

    def test_phase_and_target_set_to_same_value_are_stable(self):
        self.twice("session_state.py", ["phase", self.s, "test"])
        self.assertEqual(self.get()["current_phase"], "test")
        self.twice("plan_target.py", ["set", self.s, "2026-12-01", "2026-10-04"])
        self.assertEqual(self.get()["target"], {"date": "2026-12-01", "set_on": "2026-10-04"})

    # --- by design NOT idempotent: each call is a real event --------------------------------------------
    def test_events_count_again(self):
        a, b = self.twice("error_log.py", ["append", self.s, "S2", "S2.1", "practice", "slip", "NONE", "x", "6"])
        self.assertNotEqual(a["entry"]["id"], b["entry"]["id"])
        a, b = self.twice("confidence_update.py", ["apply", self.s, "pass_clean", "7"])
        self.assertGreater(b["new_confidence"], a["new_confidence"])
        a, b = self.twice("item_mastery.py", ["observe", self.s, "S1.1", "true", "5"])
        self.assertEqual((a["observations"], b["observations"]), (1, 2))
        a, b = self.twice("remediation_state.py", ["record", self.s, "S2", "slip", "6"])
        self.assertEqual((a["attempts"], b["attempts"]), (1, 2))
        a, b = self.twice("review_math.py", ["apply", self.deck, "k1", "6", "true"])
        self.assertGreater(b["interval_sessions"], a["interval_sessions"])
        a, b = self.twice("record_mock.py", [self.s, "40", "30", "50", "2026-10-04"])
        self.assertEqual((a["mocks_on_file"], b["mocks_on_file"]), (1, 2))


if __name__ == "__main__":
    unittest.main()
