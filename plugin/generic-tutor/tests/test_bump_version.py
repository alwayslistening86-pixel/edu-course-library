"""tools/bump_version.py edits every version carrier together and refuses to go backwards."""
import json
import os
import shutil
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(REPO, "tools"))
import bump_version  # noqa: E402


class Bump(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.d, True)
        self.saved = (bump_version.ROOT, bump_version.PLUGIN_JSON, bump_version.MARKETPLACE, bump_version.PYPROJECT, bump_version.CHANGELOG)
        self.addCleanup(self.restore)
        bump_version.ROOT = self.d
        bump_version.PLUGIN_JSON = os.path.join(self.d, "plugin", "generic-tutor", ".claude-plugin", "plugin.json")
        bump_version.MARKETPLACE = os.path.join(self.d, ".claude-plugin", "marketplace.json")
        bump_version.PYPROJECT = os.path.join(self.d, "pyproject.toml")
        bump_version.CHANGELOG = os.path.join(self.d, "CHANGELOG.md")
        for p, text in ((bump_version.PLUGIN_JSON, json.dumps({"name": "x", "version": "1.2.3"}, indent=2)),
                        (bump_version.MARKETPLACE, json.dumps({"plugins": [{"name": "x", "version": "1.2.3"}]}, indent=2)),
                        (bump_version.PYPROJECT, '[project]\nname = "x"\nversion = "1.2.3"\nrequires-python = ">=3.10"\n'),
                        (bump_version.CHANGELOG, "# Changelog\n\n## [Unreleased]\n\n## [1.2.3] — 2026-01-01\n- old\n")):
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w") as f:
                f.write(text)

    def restore(self):
        (bump_version.ROOT, bump_version.PLUGIN_JSON, bump_version.MARKETPLACE, bump_version.PYPROJECT, bump_version.CHANGELOG) = self.saved

    def read(self, p):
        with open(p) as f:
            return f.read()

    def test_all_three_files_change_and_the_changelog_gets_its_heading(self):
        r = bump_version.bump("1.3.0", "did a thing", root_scripts=False)
        self.assertEqual((r["from"], r["to"]), ("1.2.3", "1.3.0"))
        self.assertEqual(json.loads(self.read(bump_version.PLUGIN_JSON))["version"], "1.3.0")
        self.assertEqual(json.loads(self.read(bump_version.MARKETPLACE))["plugins"][0]["version"], "1.3.0")
        self.assertIn('version = "1.3.0"', self.read(bump_version.PYPROJECT))
        self.assertIn('requires-python = ">=3.10"', self.read(bump_version.PYPROJECT))
        log = self.read(bump_version.CHANGELOG)
        self.assertLess(log.index("## [1.3.0]"), log.index("## [1.2.3]"))
        self.assertIn("- did a thing", log)

    def test_refuses_equal_lower_and_malformed_and_changes_nothing(self):
        before = [self.read(p) for p in (bump_version.PLUGIN_JSON, bump_version.MARKETPLACE, bump_version.PYPROJECT)]
        for v in ("1.2.3", "1.2.2", "1.10", "banana", ""):
            self.assertIn("error", bump_version.bump(v, root_scripts=False), v)
        self.assertEqual(before, [self.read(p) for p in (bump_version.PLUGIN_JSON, bump_version.MARKETPLACE, bump_version.PYPROJECT)])

    def test_dry_run_writes_nothing_and_a_minor_ordering_is_numeric(self):
        before = self.read(bump_version.PLUGIN_JSON)
        self.assertEqual(bump_version.bump("1.10.0", dry_run=True, root_scripts=False)["to"], "1.10.0")
        self.assertEqual(self.read(bump_version.PLUGIN_JSON), before)

    def test_a_carrier_without_exactly_one_version_is_an_error(self):
        with open(bump_version.PYPROJECT, "w") as f:
            f.write("[project]\nname = 'x'\n")
        self.assertIn("exactly one version", bump_version.bump("1.3.0", root_scripts=False)["error"])


if __name__ == "__main__":
    unittest.main()
