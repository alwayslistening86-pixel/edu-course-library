"""Tests for tools/lint_docs.py: the real repo must be clean, and seeded faults must be caught."""
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(ROOT))
sys.path.insert(0, os.path.join(REPO, "tools"))
import lint_docs  # noqa: E402


class RealRepo(unittest.TestCase):
    def test_repo_is_clean_strict(self):
        errors, warnings = lint_docs.lint(REPO)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])


class SeededFaults(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.d, True)
        shutil.copytree(os.path.join(REPO, "plugin"), os.path.join(self.d, "plugin"),
                        ignore=shutil.ignore_patterns("__pycache__", "tests"))
        shutil.copytree(os.path.join(REPO, ".tutor-scripts"), os.path.join(self.d, ".tutor-scripts"),
                        ignore=shutil.ignore_patterns("__pycache__"))

    def _append(self, rel, text):
        with open(os.path.join(self.d, "plugin", "generic-tutor", rel), "a", encoding="utf-8") as f:
            f.write(text)

    def test_missing_script_reference(self):
        self._append("skills/tutor-core/SKILL.md", "\npython3 /EDU/.tutor-scripts/nope_script.py\n")
        errors, _ = lint_docs.lint(self.d)
        self.assertTrue(any("nope_script.py" in e for e in errors))

    def test_command_includes_missing_skill(self):
        self._append("commands/plan.md", "\n@${CLAUDE_PLUGIN_ROOT}/skills/ghost/SKILL.md\n")
        errors, _ = lint_docs.lint(self.d)
        self.assertTrue(any("ghost" in e for e in errors))

    def test_orphan_skill(self):
        os.makedirs(os.path.join(self.d, "plugin", "generic-tutor", "skills", "orphan"))
        with open(os.path.join(self.d, "plugin", "generic-tutor", "skills", "orphan", "SKILL.md"), "w") as f:
            f.write("---\nname: orphan\ndescription: x\n---\n# Orphan\n")
        errors, _ = lint_docs.lint(self.d)
        self.assertTrue(any("orphan" in e and "not included" in e for e in errors))

    def test_command_missing_from_help(self):
        with open(os.path.join(self.d, "plugin", "generic-tutor", "commands", "newcmd.md"), "w") as f:
            f.write("---\ndescription: x\n---\n@${CLAUDE_PLUGIN_ROOT}/skills/tutor-core/SKILL.md\n")
        errors, _ = lint_docs.lint(self.d)
        self.assertTrue(any("newcmd.md" in e and "help.md" in e for e in errors))

    def test_version_mismatch(self):
        p = os.path.join(self.d, ".tutor-scripts", ".manifest.json")
        with open(p, encoding="utf-8") as f:
            s = f.read()
        with open(p, "w", encoding="utf-8") as f:
            f.write(s.replace('"plugin_version": "', '"plugin_version": "0.0.', 1))
        errors, _ = lint_docs.lint(self.d)
        self.assertTrue(any("version mismatch" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
