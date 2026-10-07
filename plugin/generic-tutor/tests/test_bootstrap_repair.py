"""E-22: bootstrap repairs drifted/missing deployed files at the same version and removes retired files."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import bootstrap_scripts  # noqa: E402


def _w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


class Repair(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.d, True)
        self.src = os.path.join(self.d, "src")
        self.target = os.path.join(self.d, "target")
        self.pj = os.path.join(self.d, "plugin.json")
        _w(self.pj, json.dumps({"version": "1.0.0"}))
        _w(os.path.join(self.src, "a.py"), "A=1\n")
        _w(os.path.join(self.src, "b.py"), "B=1\n")
        _w(os.path.join(self.src, "pkg", "__init__.py"), "")
        _w(os.path.join(self.src, "pkg", "m.py"), "M=1\n")

    def run_boot(self):
        return bootstrap_scripts.bootstrap(self.src, self.pj, self.target)

    def test_clean_same_version_is_up_to_date(self):
        self.assertEqual(self.run_boot()["action"], "deployed_fresh")
        self.assertEqual(self.run_boot()["action"], "up_to_date")

    def test_modified_file_is_repaired(self):
        self.run_boot()
        _w(os.path.join(self.target, "a.py"), "A=tampered\n")
        r = self.run_boot()
        self.assertEqual(r["action"], "repaired")
        self.assertEqual(r["drift"]["modified"], ["a.py"])
        with open(os.path.join(self.target, "a.py")) as f:
            self.assertEqual(f.read(), "A=1\n")

    def test_missing_file_and_missing_package_file_are_repaired(self):
        self.run_boot()
        os.unlink(os.path.join(self.target, "b.py"))
        os.unlink(os.path.join(self.target, "pkg", "m.py"))
        r = self.run_boot()
        self.assertEqual(r["action"], "repaired")
        self.assertEqual(sorted(r["drift"]["missing"]), ["b.py", "pkg/m.py"])
        self.assertTrue(os.path.isfile(os.path.join(self.target, "pkg", "m.py")))

    def test_extra_file_in_package_is_left_alone(self):
        self.run_boot()
        _w(os.path.join(self.target, "pkg", "note.txt"), "x")
        self.assertEqual(self.run_boot()["action"], "up_to_date")
        self.assertTrue(os.path.isfile(os.path.join(self.target, "pkg", "note.txt")))

    def test_upgrade_removes_retired_files_and_packages_but_not_unknown_files(self):
        _w(os.path.join(self.src, "old.py"), "O=1\n")
        _w(os.path.join(self.src, "oldpkg", "__init__.py"), "")
        self.run_boot()
        _w(os.path.join(self.target, "user_notes.py"), "# not ours\n")
        os.unlink(os.path.join(self.src, "old.py"))
        shutil.rmtree(os.path.join(self.src, "oldpkg"))
        _w(self.pj, json.dumps({"version": "1.1.0"}))
        r = self.run_boot()
        self.assertEqual(r["action"], "updated")
        self.assertEqual(sorted(r["orphans_removed"]), ["old.py", "oldpkg/"])
        self.assertFalse(os.path.exists(os.path.join(self.target, "old.py")))
        self.assertFalse(os.path.exists(os.path.join(self.target, "oldpkg")))
        self.assertTrue(os.path.isfile(os.path.join(self.target, "user_notes.py")))


if __name__ == "__main__":
    unittest.main()
