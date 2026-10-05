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
import tasks_status  # noqa: E402


class RealRepo(unittest.TestCase):
    def test_repo_is_clean_strict(self):
        errors, warnings = lint_docs.lint(REPO)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])


class TaskCounts(unittest.TestCase):
    def test_counts_in_tasks_md_are_current(self):
        with open(os.path.join(REPO, "docs", "TASKS.md"), encoding="utf-8") as f:
            keep, current = tasks_status.split(f.read())
        self.assertEqual(current, tasks_status.render(tasks_status.counts(keep), keep), "run: python3 tools/tasks_status.py --write")

    def test_every_unfinished_task_is_in_a_wave(self):
        with open(os.path.join(REPO, "docs", "TASKS.md"), encoding="utf-8") as f:
            keep, _ = tasks_status.split(f.read())
        self.assertEqual(tasks_status.wave_problems(keep), [])

    def test_wave_check_catches_a_dropped_task(self):
        text = "| R-01 🟡 | t | d | - | S | 0 |\n| R-02 🟡 | t | d | - | S | 0 |\n## Progress\n| R-01 | ✅ done | y |\n## Suggested first sprint\n\n## Remaining waves\n\n| Wave | Theme | Tasks | Why |\n|---|---|---|---|\n| 1 | x | R-09 | y |\n\n## Task counts\n"
        problems = tasks_status.wave_problems(text)
        self.assertIn("R-02 is not done but is in no wave", problems)
        self.assertIn("wave names unknown task R-09", problems)

    def test_parser_reads_the_log_last_row_wins(self):
        text = "| R-01 🟡 | t | d |\n| R-02 🟡 | t | d |\n## Progress\n| R-01 | 🟡 partial | x |\n| R-01 | ✅ done | y |\n\n## Suggested first sprint\n"
        t = tasks_status.counts(text + "\n## Task counts\n")
        self.assertEqual((t["R"]["done"], t["R"]["open"]), (1, 1))


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

    def test_release_history_prose_in_a_skill_is_flagged(self):
        self._append("skills/tutor-core/SKILL.md", "\nThis rule was added in a later release (v1.9.9) after a bug.\n")
        _, warnings = lint_docs.lint(self.d)
        self.assertTrue(any("release-history prose" in w for w in warnings))
        self._append("skills/stage-recap/SKILL.md", "\nSee `DESIGN_NOTES.md` for why.\n")
        _, warnings = lint_docs.lint(self.d)
        self.assertEqual(sum("release-history prose" in w for w in warnings), 2)

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
