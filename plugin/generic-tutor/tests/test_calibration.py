"""L-15: self-rating calibration (opt-in, signal-class)."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import calibration as cal  # noqa: E402
import golden_support as gs  # noqa: E402
from tutorlib import schema  # noqa: E402


class Calibration(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        fx = gs.build_fixture(self.tmp)
        self.L = fx["L"]
        self.path = os.path.join(fx["S"], "mathA.json")

    def data(self):
        with open(self.path) as f:
            return json.load(f)

    def rec(self, stage, rating, result):
        return cal.record(self.path, stage, rating, result, "2026-10-06")

    def test_nothing_is_recorded_until_the_learner_says_yes(self):
        self.assertIn("not switched on", self.rec("S1", 3, "pass")["error"])
        self.assertNotIn("calibration", self.data())
        self.assertTrue(cal.optin(self.path, "yes")["written"])
        self.assertTrue(self.rec("S1", 3, "pass")["written"])
        cal.optin(self.path, "no")
        self.assertIn("error", self.rec("S2", 3, "pass"))

    def test_validation(self):
        cal.optin(self.path, "yes")
        for bad in (0, 6, "x", None):
            self.assertIn("error", self.rec("S1", bad, "pass"))
        self.assertIn("error", self.rec("S1", 3, "maybe"))
        self.assertIn("error", cal.optin(self.path, "perhaps"))

    def test_a_repeat_replaces_and_the_file_stays_valid(self):
        cal.optin(self.path, "yes")
        self.rec("S1", 2, "fail")
        self.rec("S1", 4, "fail")
        self.assertEqual([e["rating"] for e in self.data()["calibration"]["entries"]], [4])
        self.assertEqual(schema.validate(self.data(), "subjects"), [])

    def test_verdicts(self):
        cal.optin(self.path, "yes")
        for i in range(4):
            self.rec(f"S{i}", 5, "fail")
        self.assertEqual(cal.report(self.path)["verdict"], "too_few")
        self.rec("S4", 5, "fail")
        r = cal.report(self.path)
        self.assertEqual((r["verdict"], r["pass_rate"], r["mean_predicted"]), ("overconfident", 0.0, 0.9))
        for i in range(5):
            self.rec(f"T{i}", 1, "pass")                      # five more, now predicting low and passing
        self.assertEqual(cal.report(self.path)["verdict"], "well_calibrated")      # (0.9*5 + 0.1*5)/10 = 0.5 vs 0.5

    def test_underconfident(self):
        cal.optin(self.path, "yes")
        for i in range(6):
            self.rec(f"S{i}", 1, "pass")
        self.assertEqual(cal.report(self.path)["verdict"], "underconfident")

    def test_consent_limited_writes_nothing(self):
        pp = os.path.join(self.L, "student_profile.json")
        with open(pp) as f:
            p = json.load(f)
        p["consent"] = {"status": "limited"}
        with open(pp, "w") as f:
            json.dump(p, f)
        r = cal.optin(self.path, "yes")
        self.assertFalse(r["written"])
        self.assertNotIn("calibration", self.data())

    def test_cli_usage_and_the_cap(self):
        self.assertEqual(cal.main([]), 2)
        cal.optin(self.path, "yes")
        for i in range(60):
            self.rec(f"S{i}", 3, "pass")
        self.assertEqual(len(self.data()["calibration"]["entries"]), cal.KEEP)


if __name__ == "__main__":
    unittest.main()
