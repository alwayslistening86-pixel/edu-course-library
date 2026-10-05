"""K-14: the deterministic audit as one report, diffable against the last one."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import audit_run  # noqa: E402
import golden_support as gs  # noqa: E402


class Report(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.C = self.fx["C"]

    def tree(self):
        out = {}
        for dp, _dn, fns in os.walk(self.C):
            for f in fns:
                with open(os.path.join(dp, f), "rb") as fh:
                    out[os.path.join(dp, f)] = fh.read()
        return out

    def test_shape_totals_and_read_only(self):
        before = self.tree()
        r = audit_run.run(self.C, "2026-10-05")
        self.assertEqual(self.tree(), before)
        self.assertEqual(r["report_version"], 1)
        self.assertEqual(r["courses_checked"], len(r["courses"]))
        self.assertEqual(r["totals"]["can_ship"] + r["totals"]["blocked"], r["courses_checked"])
        broken = r["courses"]["broken"]                                  # fixture course with a missing stage file
        self.assertFalse(broken["can_ship"])
        self.assertTrue(broken["blocking"])
        self.assertTrue(r["courses"]["mathA"]["can_ship"])
        self.assertIn("old_schema", r["courses"]["old"]["audit_reasons"])

    def test_diff_reports_new_and_resolved_problems(self):
        first = audit_run.run(self.C, "2026-10-05")
        os.remove(f"{self.C}/mathA/stages/S2/lesson.md")                       # a new fault
        with open(f"{self.C}/broken/stages/S2/test.md", "w", encoding="utf-8") as f:   # an old fault repaired
            f.write("# S2 test\n")
        second = audit_run.run(self.C, "2026-10-06", previous=first)
        ch = second["changes"]
        self.assertTrue(any("missing stage files" in n for n in ch["mathA"]["new"]), ch.get("mathA"))
        self.assertTrue(any("missing stage files" in n for n in ch["broken"]["resolved"]), ch.get("broken"))
        self.assertNotIn("solo", ch)                                            # untouched courses do not appear

    def test_cli_saves_outside_the_library_and_refuses_inside(self):
        import subprocess
        script = os.path.join(gs.SCRIPTS, "audit_run.py")
        out = os.path.join(self.tmp, "audit", "last.json")
        p = subprocess.run([sys.executable, script, self.C, "--out", out], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        with open(out, encoding="utf-8") as f:
            saved = json.load(f)
        self.assertEqual(saved["courses_checked"], json.loads(p.stdout)["courses_checked"])
        p = subprocess.run([sys.executable, script, self.C, "--out", os.path.join(self.C, "report.json")], capture_output=True, text=True)
        self.assertEqual(p.returncode, 1)
        self.assertFalse(os.path.exists(os.path.join(self.C, "report.json")))
        p = subprocess.run([sys.executable, script, self.C, "--compare", out], capture_output=True, text=True)
        self.assertEqual(json.loads(p.stdout)["changes"], {})
        self.assertEqual(subprocess.run([sys.executable, script, self.tmp + "/nope"], capture_output=True, text=True).returncode, 1)


if __name__ == "__main__":
    unittest.main()
