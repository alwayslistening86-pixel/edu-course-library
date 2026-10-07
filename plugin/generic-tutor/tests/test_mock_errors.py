"""ADR 0012, build task B-04.5g: an error diagnosed during a mock paper is recorded but moves no mastery estimate and no diagnostic trigger."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

from golden_support import build_fixture  # noqa: E402
from tutorlib import schema  # noqa: E402

SCRIPTS = os.path.join(HERE, "..", "scripts")


def run(script, *args):
    p = subprocess.run([sys.executable, os.path.join(SCRIPTS, script), *args], capture_output=True, text=True)
    return p.returncode, (json.loads(p.stdout) if p.stdout.strip() else {})


class MockErrors(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = build_fixture(self.tmp)
        self.subj = os.path.join(self.fx["S"], "mathA.json")

    def data(self):
        with open(self.subj, encoding="utf-8") as f:
            return json.load(f)

    def append(self, *extra, item="S1.1", cause="slip"):
        return run("error_log.py", "append", self.subj, "S1", item, "test", cause, "NONE", "dropped a sign", "9", "NONE", *extra)

    def test_a_mock_error_is_recorded_but_mastery_does_not_move(self):
        before = self.data().get("item_mastery", {})
        code, out = self.append("--mock")
        self.assertEqual(code, 0, out)
        self.assertEqual(out["action"], "appended")
        self.assertTrue(out["entry"]["mock"])
        self.assertFalse(out["item_mastery"]["updated"])
        after = self.data()
        self.assertEqual(after.get("item_mastery", {}), before)
        self.assertEqual(len(after["error_patterns"]), 1)
        self.assertEqual(schema.validate(after, "subjects"), [])

    def test_the_same_error_outside_a_mock_still_moves_mastery(self):
        code, out = self.append()
        self.assertEqual(code, 0, out)
        self.assertNotIn("mock", out["entry"])
        self.assertIn("S1.1", self.data()["item_mastery"])

    def test_mock_errors_do_not_count_towards_recurrence_or_the_gate(self):
        for _ in range(3):
            code, out = self.append("--mock")
            self.assertEqual(code, 0, out)
        self.assertFalse(out["recurring"])
        self.assertEqual(out["unresolved_same_item_and_cause"], 0)
        code, gate = run("diagnostic_gate.py", self.subj, "S1", "S1.1", "false", "false")
        self.assertEqual(code, 0, gate)
        self.assertIs(gate["fire"], False, gate)

    def test_the_same_three_errors_outside_a_mock_do_fire_the_gate(self):
        for _ in range(3):
            self.append()
        code, gate = run("diagnostic_gate.py", self.subj, "S1", "S1.1", "false", "false")
        self.assertEqual(code, 0, gate)
        self.assertIs(gate["fire"], True, gate)

    def test_a_mock_error_still_shows_as_unresolved_so_the_item_gets_practised(self):
        self.append("--mock")
        code, out = run("error_log.py", "query", self.subj, "S1")
        self.assertEqual(code, 0, out)
        self.assertEqual(json.dumps(out).count("dropped a sign"), 1)

    def test_flag_position_and_usage(self):
        code, out = run("error_log.py", "append", self.subj, "S1", "S1.1", "test", "slip", "NONE", "n", "9", "--mock")
        self.assertEqual(code, 0, out)
        self.assertEqual(run("error_log.py", "append", self.subj, "S1", "S1.1", "test", "slip", "--mock")[0], 2)


if __name__ == "__main__":
    unittest.main()
