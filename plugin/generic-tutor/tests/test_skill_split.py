"""Reference files split out of the big skills: every moved section is still reachable, and nothing was lost."""
import os
import re
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SK = os.path.join(ROOT, "skills")


def read(*p):
    with open(os.path.join(SK, *p), encoding="utf-8") as f:
        return f.read()


class Split(unittest.TestCase):
    def test_pointers_name_their_files(self):
        pairs = {
            ("course-runner", "SKILL.md"): "list-courses.md",
            ("journey-planner", "SKILL.md"): "drop.md",
            ("course-auditor", "SKILL.md"): "suspension.md",
            ("profile-kernel", "SKILL.md"): "intake.md",
        }
        for (s, f), target in pairs.items():
            self.assertIn(target, read(s, f))
            self.assertTrue(os.path.isfile(os.path.join(SK, s, target)), target)
        self.assertIn("profile-schema.md", read("profile-kernel", "SKILL.md"))

    def test_moved_key_content_lives_in_the_reference_files(self):
        self.assertIn("coverage_status", read("course-runner", "list-courses.md"))
        self.assertIn("wake what the drop unblocked", read("journey-planner", "drop.md"))
        self.assertIn("may discard it at any time", read("course-auditor", "suspension.md"))
        self.assertIn("roster capacity", read("profile-kernel", "intake.md").lower())
        self.assertIn("highest_level_cleared", read("profile-kernel", "profile-schema.md"))

    def test_core_skills_no_longer_carry_the_moved_text(self):
        self.assertNotIn("wake what the drop unblocked", read("journey-planner", "SKILL.md"))
        self.assertNotIn("may discard it at any time", read("course-auditor", "SKILL.md"))
        self.assertNotIn("Study availability", read("profile-kernel", "SKILL.md"))

    def test_command_includes_cover_what_each_command_needs(self):
        def includes(cmd):
            with open(os.path.join(ROOT, "commands", cmd + ".md"), encoding="utf-8") as f:
                return set(re.findall(r"skills/([\w-]+/[\w.-]+\.md)", f.read()))
        self.assertEqual(includes("drop"), {"journey-planner/drop.md", "course-auditor/suspension.md"})
        self.assertEqual(includes("list-courses"), {"course-runner/list-courses.md"})
        self.assertEqual(includes("add-profile"), {"profile-kernel/SKILL.md", "profile-kernel/intake.md", "profile-kernel/profile-schema.md"})
        self.assertEqual(includes("profile"), {"profile-kernel/SKILL.md", "profile-kernel/profile-schema.md"})
        self.assertEqual(includes("audit"), {"course-auditor/SKILL.md", "course-auditor/suspension.md"})


class GeneratedDocs(unittest.TestCase):
    def test_commands_reference_is_up_to_date(self):
        import sys
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(ROOT)), "tools"))
        import gen_commands_doc
        self.assertEqual(gen_commands_doc.main(["--check"]), 0, "run: python3 tools/gen_commands_doc.py")


if __name__ == "__main__":
    unittest.main()
