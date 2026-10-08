"""ADR 0012, build task B-04.5b: a wrong answer is counted by a script from the answer alone, so the diagnostic gate no longer waits for a cause."""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SCRIPTS = os.path.join(HERE, "..", "scripts")

from golden_support import build_fixture  # noqa: E402


def run(script, *args):
    p = subprocess.run([sys.executable, os.path.join(SCRIPTS, script), *args], capture_output=True, text=True)
    return json.loads(p.stdout) if p.stdout.strip() else {}


class MissCounter(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = build_fixture(self.tmp)
        self.subj = os.path.join(self.fx["S"], "mathA.json")

    def observe(self, correct, item="S2.1"):
        return run("item_mastery.py", "observe", self.subj, item, correct, "5")

    def gate(self, item="S2.1"):
        return run("diagnostic_gate.py", self.subj, "S2", item, "false", "false")

    def entry(self, item="S2.1"):
        with open(self.subj, encoding="utf-8") as f:
            return json.load(f)["item_mastery"][item]

    def test_the_second_miss_fires_the_gate_with_no_error_ever_logged(self):
        self.observe("false")
        self.assertFalse(self.gate()["fire"])
        self.observe("false")
        g = self.gate()
        self.assertTrue(g["fire"], g)
        self.assertIn("two-or-more misses", json.dumps(g))

    def test_without_the_counter_the_same_replay_never_fires(self):
        """The old behaviour: with no observation and no logged error, two wrong answers leave the gate silent."""
        self.assertFalse(self.gate()["fire"])

    def test_a_right_answer_resets_the_run(self):
        self.observe("false")
        self.observe("true")
        self.observe("false")
        self.assertEqual(self.entry()["consecutive_misses"], 1)
        self.assertFalse(self.gate()["fire"])

    def test_misses_are_counted_per_item(self):
        self.observe("false", "S2.1")
        self.observe("false", "S3.1")
        self.assertFalse(self.gate("S2.1")["fire"])

    def test_no_observe_logs_the_error_without_counting_the_miss_twice(self):
        self.observe("false")
        r = run("error_log.py", "append", self.subj, "S2", "S2.1", "practice", "slip", "NONE", "dropped a sign", "5", "--no-observe")
        self.assertNotIn("error", r, r)
        e = self.entry()
        self.assertEqual((e["consecutive_misses"], e["observations"]), (1, 1))

    def test_append_without_the_flag_still_observes(self):
        run("error_log.py", "append", self.subj, "S2", "S2.1", "practice", "slip", "NONE", "dropped a sign", "5")
        self.assertEqual(self.entry()["consecutive_misses"], 1)


class SkillText(unittest.TestCase):
    def test_both_course_runner_places_say_to_observe_every_wrong_answer(self):
        with open(os.path.join(HERE, "..", "skills", "course-runner", "SKILL.md"), encoding="utf-8") as f:
            text = f.read()
        self.assertGreaterEqual(len(re.findall(r"item_mastery\.py observe <subjects\.json> <item_id> false <slot>", text)), 2)
        self.assertIn("--no-observe", text)


if __name__ == "__main__":
    unittest.main()
