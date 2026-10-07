"""L-13: practice items already met are tracked, so a repeat of a stage gets fresh ones."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import practice_pick as pp  # noqa: E402
from tutorlib import schema  # noqa: E402

ITEMS = """# S1 - Practice

## Goal
x

## Practice items
1. First item?
2. Second item, with options.
   A. one
   B. two

## Answers (for the tutor; reveal only after a genuine attempt)
1. [2] M1 A1.
2. Correct: A

## How to run it
1. this numbered line is outside the item section
"""
SCENARIOS = """# S1 - Practice

## Practice scenarios (use or adapt as needed)
1. a
2. b
3. c
4. d

## How to run it
"""


class Pick(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.s = f"{self.fx['S']}/mathA.json"
        self.items = os.path.join(self.tmp, "items.md")
        self.scen = os.path.join(self.tmp, "scen.md")
        for path, text in ((self.items, ITEMS), (self.scen, SCENARIOS)):
            with open(path, "w") as f:
                f.write(text)

    def test_parsing_both_real_formats(self):
        self.assertEqual(pp.fixed_items(ITEMS), [1, 2])               # option lines and the later section are not items
        self.assertEqual(pp.fixed_items(SCENARIOS), [1, 2, 3, 4])
        self.assertEqual(pp.fixed_items("# no section here\n1. x\n"), [])

    def test_walks_through_fixed_items_then_asks_for_new_ones(self):
        r = pp.next_item(self.s, self.items, "S2")
        self.assertEqual((r["recommendation"], r["fixed_total"]), ("use_fixed:1", 2))
        pp.mark_used(self.s, "S2", "fixed", 1)
        self.assertEqual(pp.next_item(self.s, self.items, "S2")["recommendation"], "use_fixed:2")
        pp.mark_used(self.s, "S2", "fixed", 2)
        r = pp.next_item(self.s, self.items, "S2")
        self.assertEqual((r["recommendation"], r["unused_fixed"], r["generated_count"]), ("generate_new", [], 0))
        pp.mark_used(self.s, "S2", "generated")
        pp.mark_used(self.s, "S2", "generated")
        self.assertEqual(pp.next_item(self.s, self.items, "S2")["generated_count"], 2)

    def test_stages_are_independent_and_fixed_marks_are_idempotent(self):
        pp.mark_used(self.s, "S2", "fixed", 1)
        r = pp.mark_used(self.s, "S2", "fixed", 1)
        self.assertEqual((r["already_recorded"], r["written"]), (True, False))
        self.assertEqual(pp.next_item(self.s, self.scen, "S3")["recommendation"], "use_fixed:1")

    def test_written_file_still_validates_and_other_fields_survive(self):
        before = gs.read_json(self.s)
        pp.mark_used(self.s, "S2", "fixed", 2)
        pp.mark_used(self.s, "S2", "generated")
        after = gs.read_json(self.s)
        self.assertEqual(schema.validate(after, "subjects"), [])
        self.assertEqual({k: v for k, v in after.items() if k != "practice_used"}, before)
        self.assertEqual(after["practice_used"], {"S2": {"fixed": [2], "generated": 1}})

    def test_bad_input(self):
        self.assertIn("error", pp.mark_used(self.s, "S2", "fixed", 0))
        self.assertIn("error", pp.mark_used(self.s, "S2", "fixed", None))
        self.assertIn("error", pp.mark_used(self.s, "S2", "bogus"))
        self.assertIn("error", pp.next_item(self.s, self.tmp + "/missing.md", "S2"))

    def test_consent_gate_and_read_only_next(self):
        pf = f"{self.fx['L']}/student_profile.json"
        p = gs.read_json(pf)
        p["consent"]["status"] = "revoked"
        with open(pf, "w") as f:
            json.dump(p, f)
        before = gs.read_json(self.s)
        r = pp.mark_used(self.s, "S2", "fixed", 1)
        self.assertFalse(r["written"])
        self.assertIn("consent", r["skipped"])
        self.assertEqual(gs.read_json(self.s), before)
        pp.next_item(self.s, self.items, "S2")
        self.assertEqual(gs.read_json(self.s), before)


if __name__ == "__main__":
    unittest.main()
