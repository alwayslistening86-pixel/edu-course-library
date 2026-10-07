"""S-11: change.md read as data."""
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import change_log  # noqa: E402
import golden_support as gs  # noqa: E402
import postcompile_gate  # noqa: E402

GOOD = """# Change log - demo

## 2026-09-27 - built

Built against Spec v1.

## 2026-09-29 — mark-scheme remediation

**Found by:** the checker.

**Fixed:** two items.

**Revalidated:** clean.

## 2026-10-01 – live recheck
Nothing changed.
"""


class Parse(unittest.TestCase):
    def test_entries_labels_and_dates(self):
        entries, problems = change_log.parse(GOOD)
        self.assertEqual(problems, [])
        self.assertEqual([(e["date"], e["title"]) for e in entries],
                         [("2026-09-27", "built"), ("2026-09-29", "mark-scheme remediation"), ("2026-10-01", "live recheck")])
        self.assertEqual(entries[1]["labels"], ["Found by", "Fixed", "Revalidated"])

    def test_problems(self):
        rules = lambda t: sorted(p["rule"] for p in change_log.parse(t)[1])  # noqa: E731
        self.assertIn("malformed_heading", rules("# Change log - x\n## built sometime\n"))
        self.assertIn("out_of_order", rules("# c\n## 2026-10-01 - built\n## 2026-09-01 - later\n"))
        self.assertIn("no_built_entry", rules("# c\n## 2026-10-01 - tweak\n"))
        self.assertIn("no_title_heading", rules("## 2026-10-01 - built\n"))
        self.assertEqual(rules(GOOD), [])


class Course(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.course = f"{self.fx['C']}/mathA"

    def test_missing_file_is_empty_not_an_error_and_missing_course_is(self):
        r = change_log.read(self.course)
        self.assertEqual((r["entry_count"], r["problems"], r["built_on"]), (0, [], None))
        self.assertIn("error", change_log.read(self.tmp + "/nope"))

    def test_read_summary_and_gate_note(self):
        with open(f"{self.course}/change.md", "w", encoding="utf-8") as f:
            f.write("# Change log - mathA\n\n## 2026-10-01 - tweak\n")
        r = change_log.read(self.course)
        self.assertEqual((r["entry_count"], r["first_date"], r["last_date"], r["built_on"]), (1, "2026-10-01", "2026-10-01", None))
        gate = postcompile_gate._gate(self.course)
        self.assertTrue(gate["can_ship"])
        self.assertTrue(any("change.md" in n and "no_built_entry" in n for n in gate["advisory_notes"]))


if __name__ == "__main__":
    unittest.main()
