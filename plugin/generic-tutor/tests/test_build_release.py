"""R-11/R-12/P-02: deterministic plugin build, release notes, marketplace consistency."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(ROOT))
sys.path.insert(0, os.path.join(REPO, "tools"))

import build_plugin  # noqa: E402
import release_notes  # noqa: E402


class Build(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.d, True)

    def test_two_builds_are_byte_identical(self):
        a = build_plugin.build(REPO, os.path.join(self.d, "a.plugin"))
        b = build_plugin.build(REPO, os.path.join(self.d, "b.plugin"))
        self.assertEqual(a["sha256"], b["sha256"])

    def test_contents(self):
        out = build_plugin.build(REPO, os.path.join(self.d, "a.plugin"))["output"]
        with zipfile.ZipFile(out) as z:
            names = z.namelist()
            self.assertEqual(names, sorted(names))
            self.assertIn(".claude-plugin/plugin.json", names)
            self.assertIn("skills/health-status/SKILL.md", names)
            self.assertIn("scripts/tutorlib/schemas/subjects.json", names)
            self.assertIn("docs/UNTRUSTED_CONTENT.md", names)
            for bad in ("tests/", "__pycache__", ".pyc", ".DS_Store"):
                self.assertFalse([n for n in names if bad in n], bad)
            self.assertTrue(all(i.date_time == build_plugin.FIXED_TIME for i in z.infolist()))

    def test_every_script_referenced_by_skills_ships(self):
        out = build_plugin.build(REPO, os.path.join(self.d, "a.plugin"))["output"]
        with zipfile.ZipFile(out) as z:
            shipped = set(z.namelist())
        for f in os.listdir(os.path.join(ROOT, "scripts")):
            if f.endswith(".py"):
                self.assertIn("scripts/" + f, shipped)

    def test_built_zip_validates_with_claude_cli_when_available(self):
        if not shutil.which("claude"):
            self.skipTest("claude CLI not installed")
        out = build_plugin.build(REPO, os.path.join(self.d, "a.plugin"))["output"]
        dest = os.path.join(self.d, "x")
        with zipfile.ZipFile(out) as z:
            z.extractall(dest)
        p = subprocess.run(["claude", "plugin", "validate", dest, "--strict"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)


class Release(unittest.TestCase):
    def test_section_extraction(self):
        text = "# Changelog\n\n## [2.0.0] — d\n- a\n\n## [1.0.0]\n- b\n"
        self.assertEqual(release_notes.section(text, "v2.0.0"), "## [2.0.0] — d\n- a\n")
        self.assertEqual(release_notes.section(text, "1.0.0"), "## [1.0.0]\n- b\n")
        self.assertIsNone(release_notes.section(text, "3.0.0"))

    def test_current_version_has_notes(self):
        with open(os.path.join(ROOT, ".claude-plugin", "plugin.json")) as f:
            v = json.load(f)["version"]
        with open(os.path.join(REPO, "CHANGELOG.md"), encoding="utf-8") as f:
            self.assertIsNotNone(release_notes.section(f.read(), v))


class Marketplace(unittest.TestCase):
    def test_entry_points_at_the_plugin_and_versions_agree(self):
        with open(os.path.join(REPO, ".claude-plugin", "marketplace.json")) as f:
            m = json.load(f)
        with open(os.path.join(ROOT, ".claude-plugin", "plugin.json")) as f:
            p = json.load(f)
        (entry,) = m["plugins"]
        self.assertEqual(entry["name"], p["name"])
        self.assertEqual(entry["version"], p["version"])
        self.assertTrue(os.path.isfile(os.path.join(REPO, entry["source"], ".claude-plugin", "plugin.json")))


if __name__ == "__main__":
    unittest.main()
