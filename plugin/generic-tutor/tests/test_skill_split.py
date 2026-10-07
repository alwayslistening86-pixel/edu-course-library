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
        self.assertIn("list_courses.py", read("course-runner", "list-courses.md"))
        self.assertIn("roster_apply.py drop", read("journey-planner", "drop.md"))
        self.assertIn("wakes every dormant course that the drop unblocked", read("journey-planner", "drop.md"))
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


class CommandNaming(unittest.TestCase):
    """C-15: file names are lower-case hyphenated; argument hints use snake_case placeholders and --kebab flags; every command that reads
    its arguments declares them."""
    def _commands(self):
        d = os.path.join(ROOT, "commands")
        for fn in sorted(os.listdir(d)):
            with open(os.path.join(d, fn), encoding="utf-8") as f:
                yield fn, f.read()

    def test_names_and_hints(self):
        for fn, text in self._commands():
            self.assertRegex(fn, r"^[a-z]+(-[a-z]+)*\.md$")
            m = re.search(r"^argument-hint:\s*(.*)$", text, re.M)
            if m:
                for tok in re.findall(r"[<\[]([^\]>]+)[\]>]", m.group(1)):
                    for word in tok.split():
                        self.assertRegex(word, r"^(--[a-z]+(-[a-z]+)*|[a-z]+(_[a-z]+)*|[A-Z]|\d|[a-z]+(_[a-z]+)*\.[a-z]+)$", f"{fn}: {word}")

    def test_commands_that_read_arguments_declare_them(self):
        for fn, text in self._commands():
            if re.search(r"\$1|\$ARGUMENTS|passing any arguments", text):
                self.assertRegex(text, r"(?m)^argument-hint:", fn)


class GeneratedDocs(unittest.TestCase):
    def test_commands_reference_is_up_to_date(self):
        import sys
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(ROOT)), "tools"))
        import gen_commands_doc
        self.assertEqual(gen_commands_doc.main(["--check"]), 0, "run: python3 tools/gen_commands_doc.py")


if __name__ == "__main__":
    unittest.main()
