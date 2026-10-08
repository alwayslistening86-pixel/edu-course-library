"""ADR 0012, build task B-04.5a: a mistyped true/false flag is an error, never a quiet 'false'. Stdlib only."""
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
from tutorlib import cli  # noqa: E402

SCRIPTS = os.path.join(HERE, "..", "scripts")
BAD = ("yes", "1", "ture", "", "T", "no", "0", "truee")


def run(script, *args):
    p = subprocess.run([sys.executable, os.path.join(SCRIPTS, script), *args], capture_output=True, text=True)
    return p.returncode, (json.loads(p.stdout) if p.stdout.strip() else {})


class ParseBool(unittest.TestCase):
    def test_accepts_only_true_and_false(self):
        for raw, want in (("true", True), ("false", False), ("True", True), (" FALSE ", False)):
            self.assertIs(cli.parse_bool(raw), want, raw)
        for raw in BAD:
            with self.assertRaises(ValueError, msg=raw):
                cli.parse_bool(raw, "correct")

    def test_message_names_the_field_and_the_value(self):
        with self.assertRaisesRegex(ValueError, r"correct must be true or false, got 'yes'"):
            cli.parse_bool("yes", "correct")


class ScriptsRefuseMistypedFlags(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = build_fixture(self.tmp)
        self.subj = os.path.join(self.fx["S"], "mathA.json")
        self.deck = os.path.join(self.fx["S"], "mathA_review_deck.json")

    def snapshot(self):
        out = {}
        for p in (self.subj, self.deck):
            with open(p, "rb") as f:
                out[p] = f.read()
        return out

    def test_item_mastery_observe(self):
        before = self.snapshot()
        for bad in BAD:
            code, out = run("item_mastery.py", "observe", self.subj, "S1.1", bad, "3")
            self.assertEqual(code, 1, bad)
            self.assertIn("correct must be true or false", out["error"])
        self.assertEqual(self.snapshot(), before, "a refused call must write nothing")
        code, out = run("item_mastery.py", "observe", self.subj, "S1.1", "True", "3")
        self.assertEqual(code, 0, out)

    def test_review_math_apply(self):
        before = self.snapshot()
        for bad in BAD:
            code, out = run("review_math.py", "apply", self.deck, "k1", "9", bad)
            self.assertEqual(code, 1, bad)
            self.assertIn("correct must be true or false", out["error"])
        self.assertEqual(self.snapshot(), before)
        code, out = run("review_math.py", "apply", self.deck, "k1", "9", "false")
        self.assertEqual(code, 0, out)

    def test_review_math_positional_form(self):
        code, out = run("review_math.py", "5", "2.3", "0", "9", "yes")
        self.assertEqual(code, 1)
        self.assertIn("correct must be true or false", out["error"])
        self.assertEqual(run("review_math.py", "5", "2.3", "0", "9", "true")[0], 0)

    def test_diagnostic_gate(self):
        for pos in (4, 5):
            for bad in ("yes", "1"):
                args = ["diagnostic_gate.py", self.subj, "S1", "S1.1", "false", "false"]
                args[pos] = bad
                code, out = run(*args)
                self.assertEqual(code, 1, (pos, bad))
                self.assertIn("must be true or false", out["error"])
        self.assertEqual(run("diagnostic_gate.py", self.subj, "S1", "S1.1", "true", "false")[0], 0)


if __name__ == "__main__":
    unittest.main()
