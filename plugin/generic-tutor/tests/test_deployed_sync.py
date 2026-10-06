"""The deployed copy (.tutor-scripts/) must equal scripts/: the same check CI's deployed-sync job runs, so drift fails locally first."""
import filecmp
import json
import os
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
SRC = os.path.join(ROOT, "plugin", "generic-tutor", "scripts")
DEP = os.path.join(ROOT, ".tutor-scripts")


def _diff(a, b, rel=""):
    out = []
    cmp = filecmp.dircmp(a, b, ignore=[".manifest.json", "__pycache__"])
    out += [f"only in scripts: {os.path.join(rel, n)}" for n in cmp.left_only]
    out += [f"only in deployed: {os.path.join(rel, n)}" for n in cmp.right_only]
    for n in cmp.common_files:
        with open(os.path.join(a, n), "rb") as f1, open(os.path.join(b, n), "rb") as f2:
            if f1.read() != f2.read():
                out.append(f"differs: {os.path.join(rel, n)}")
    for d in cmp.common_dirs:
        out += _diff(os.path.join(a, d), os.path.join(b, d), os.path.join(rel, d))
    return out


@unittest.skipUnless(os.path.isdir(DEP), "not run from a repo checkout")
class DeployedSync(unittest.TestCase):
    def test_copy_matches_source(self):
        self.assertEqual(_diff(SRC, DEP), [], "run tools/bump_version.py or bootstrap_scripts.py (see CLAUDE.md)")

    def test_manifest_version_matches_plugin_json(self):
        with open(os.path.join(DEP, ".manifest.json"), encoding="utf-8") as f:
            m = json.load(f)["plugin_version"]
        with open(os.path.join(ROOT, "plugin", "generic-tutor", ".claude-plugin", "plugin.json"), encoding="utf-8") as f:
            self.assertEqual(m, json.load(f)["version"])


if __name__ == "__main__":
    unittest.main()
