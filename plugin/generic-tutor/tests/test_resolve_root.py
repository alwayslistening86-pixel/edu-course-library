"""E-07: data-root resolution in code."""
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
from tutorlib import paths  # noqa: E402


class Resolve(unittest.TestCase):
    def setUp(self):
        self.d = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)

    def test_precedence_explicit_then_env_then_location(self):
        self.assertEqual(paths.resolve_root("/a/b", env={"EDU_ROOT": "/c"}), os.path.abspath("/a/b"))
        self.assertEqual(paths.resolve_root(None, env={"EDU_ROOT": "/c"}), os.path.abspath("/c"))
        deployed = os.path.join(self.d, "EDU", ".tutor-scripts", "tutorlib", "paths.py")
        self.assertEqual(paths.resolve_root(None, env={}, here=deployed), os.path.join(self.d, "EDU"))
        self.assertIsNone(paths.resolve_root(None, env={}, here=os.path.join(self.d, "src", "scripts", "tutorlib", "paths.py")))

    def test_layout_reports_problems(self):
        root = os.path.join(self.d, "EDU")
        os.makedirs(root)
        r = paths.layout(root)
        self.assertFalse(r["valid"])
        self.assertEqual(len(r["problems"]), 3)
        for sub in ("courses", "profile", ".tutor-scripts"):
            os.makedirs(os.path.join(root, sub))
        self.assertTrue(paths.layout(root)["valid"])
        self.assertFalse(paths.layout(os.path.join(self.d, "nope"))["valid"])
        self.assertFalse(paths.layout(None)["valid"])

    def test_cli(self):
        fx = gs.build_fixture(self.d)
        os.makedirs(os.path.join(self.d, ".tutor-scripts"))
        os.makedirs(os.path.join(self.d, "profile"), exist_ok=True)
        r = gs.run_step("resolve_root.py", ["--root", "{T}"], fx, self.d)
        self.assertEqual(r["exit"], 0, r)
        self.assertTrue(r["stdout"]["valid"])
        r = gs.run_step("resolve_root.py", ["--root", "{T}/nope"], fx, self.d)
        self.assertEqual(r["exit"], 1)
        self.assertEqual(gs.run_step("resolve_root.py", ["--bogus"], fx, self.d)["exit"], 2)


if __name__ == "__main__":
    unittest.main()
