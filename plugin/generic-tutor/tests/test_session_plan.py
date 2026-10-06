"""L-20: session length awareness."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import session_plan as sp  # noqa: E402


class Plan(unittest.TestCase):
    def test_split_and_the_test_minimum(self):
        p = sp.plan(60)
        self.assertEqual(p["phase_minutes"], {"lesson": 21, "practice": 24, "test": 15})
        self.assertEqual(sp.plan(20)["phase_minutes"]["test"], 8)            # never under 8

    def test_advice_ladder(self):
        self.assertEqual(sp.plan(45, 10, "lesson")["advice"], "continue")
        self.assertEqual(sp.plan(45, 41, "lesson")["advice"], "wrap_up")
        self.assertEqual(sp.plan(45, 50, "lesson")["advice"], "over_time")

    def test_practice_done_with_too_little_left_stops_before_the_test(self):
        p = sp.plan(45, 38, "practice")                                      # 7 left, a test needs 11
        self.assertEqual((p["advice"], p["can_start_test"]), ("stop_before_test", False))
        self.assertEqual(sp.plan(45, 20, "practice")["advice"], "continue")

    def test_a_test_in_progress_is_finished_not_abandoned(self):
        self.assertEqual(sp.plan(45, 44, "test")["advice"], "finish_the_test")
        self.assertEqual(sp.plan(45, 60, "test")["advice"], "finish_the_test")


class Profile(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def write(self, data):
        with open(os.path.join(self.tmp, "student_profile.json"), "w") as f:
            json.dump(data, f)

    def test_uses_the_profile_minutes_then_override_then_default(self):
        self.write({"availability": {"session_minutes": 30}})
        self.assertEqual(sp.run(self.tmp)["available_minutes"], 30)
        self.assertEqual(sp.run(self.tmp, available=15)["available_minutes"], 15)
        self.write({})
        r = sp.run(self.tmp)
        self.assertEqual((r["available_minutes"], r["minutes_defaulted"]), (45, True))

    def test_errors(self):
        self.assertIn("error", sp.run(os.path.join(self.tmp, "none")))
        self.assertIn("error", sp.run(self.tmp, phase="exam", available=10))
        self.assertEqual(sp.main([self.tmp, "--elapsed", "x"]), 2)


if __name__ == "__main__":
    unittest.main()
