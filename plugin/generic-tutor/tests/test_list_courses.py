"""C-14: /list-courses is a script with filters."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import list_courses as lc  # noqa: E402


class Listing(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.L, self.C = self.fx["L"], self.fx["C"]

    def ids(self, **kw):
        return [r["course_id"] for r in lc.build(self.L, self.C, **kw)["courses"]]

    def test_rows_states_and_order(self):
        r = lc.build(self.L, self.C)
        by = {x["course_id"]: x for x in r["courses"]}
        self.assertEqual((by["mathA"]["state"], by["mathB"]["state"], by["design"]["state"], by["broken"]["state"]),
                         ("active", "dormant", "dropped", "not_enrolled"))
        self.assertEqual((by["mathA"]["stages_passed"], by["mathA"]["stages_total"]), (1, 3))
        self.assertEqual(sum(r["by_state"].values()), r["count"])
        levels = [x["level"] for x in r["courses"]]
        self.assertEqual(levels, sorted(levels, key=lambda v: (v is None, v or 0)))              # standalone (None) last
        self.assertTrue(by["solo"]["standalone"])
        self.assertEqual(by["design"]["practical_stages"], ["S2"])

    def test_filters(self):
        self.assertEqual(self.ids(status="dormant"), ["mathB"])
        self.assertEqual(set(self.ids(level=2)), {"mathA", "design", "broken", "old"})
        self.assertEqual(self.ids(standalone_only=True), ["solo"])
        self.assertEqual(self.ids(status="active", level=2), ["mathA"])
        self.assertIn("error", lc.build(self.L, self.C, status="nonsense"))

    def test_compact_rows_are_small_and_complete_is_derived(self):
        row = lc.build(self.L, self.C, compact=True)["courses"][0]
        self.assertEqual(set(row), {"course_id", "level", "state", "stages_passed", "stages_total"})
        d = gs.read_json(f"{self.fx['S']}/mathA.json")
        d["syllabus_status"] = {"S1": "pass", "S2": "pass", "S3": "pass"}
        d["exam_status"] = "passed"
        import json
        with open(f"{self.fx['S']}/mathA.json", "w") as f:
            json.dump(d, f)
        self.assertEqual(self.ids(status="complete"), ["mathA"])

    def test_cli_flags_and_errors(self):
        script = os.path.join(gs.SCRIPTS, "list_courses.py")
        p = subprocess.run([sys.executable, script, self.L, self.C, "--status", "dormant", "--compact"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout)
        self.assertIn("mathB", p.stdout)
        self.assertEqual(subprocess.run([sys.executable, script, self.L, self.C, "--level", "x"], capture_output=True, text=True).returncode, 2)
        self.assertEqual(subprocess.run([sys.executable, script, self.L, self.C, "--status", "nope"], capture_output=True, text=True).returncode, 1)


if __name__ == "__main__":
    unittest.main()
