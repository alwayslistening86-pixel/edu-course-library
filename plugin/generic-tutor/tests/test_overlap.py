"""A-07 / K-26: test items must not appear in practice, lesson or a take-home worksheet."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import postcompile_gate  # noqa: E402
import worksheet_check  # noqa: E402
from tutorlib import overlap  # noqa: E402

TEST_MD = """# S1 - Test

## How to run this
Give all items at once.

## Test items
1. A laptop costs 640. In a sale it is reduced by 15%. Work out the sale price.
2. A car depreciates by 12% each year. It was bought for 14000. Work out its value after 3 years.

## Grading
1. this numbered line is outside the section and not an item
"""
ONE = "# S1 - Test\n\n## Test scenario\nFoundation: 'A laptop costs 640 and is reduced by 15% in a sale; find the sale price.'\n\n## Grading\n"


class Items(unittest.TestCase):
    def test_extraction(self):
        self.assertEqual(len(overlap.test_items(TEST_MD)), 2)
        self.assertEqual(len(overlap.test_items(ONE)), 1)
        self.assertEqual(overlap.test_items("# nothing\n## Grading\nx"), [])

    def test_verbatim_ignores_case_and_punctuation_but_not_changed_numbers(self):
        items = overlap.test_items(TEST_MD)
        same = "Practice:\n- a laptop costs 640 -- in a SALE it is reduced by 15%, work out the sale price"
        self.assertEqual(len(overlap.verbatim_items(items, same)), 1)
        changed = "A laptop costs 520. In a sale it is reduced by 20%. Work out the sale price."
        self.assertEqual(overlap.verbatim_items(items, changed), [])

    def test_long_runs(self):
        a = " ".join(f"w{i}" for i in range(30))
        self.assertEqual(overlap.long_runs(a, a, 20), 11)
        self.assertEqual(overlap.long_runs(a, "short text", 20), 0)


class Worksheet(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.test_md = os.path.join(self.tmp, "test.md")
        with open(self.test_md, "w") as f:
            f.write(TEST_MD)

    def test_copied_item_is_reported_and_new_values_pass(self):
        bad = worksheet_check.check(self.test_md, "Q1. A laptop costs 640. In a sale it is reduced by 15%. Work out the sale price.\nAnswer: 544")
        self.assertEqual((bad["ok"], bad["copied_items"]), (False, [1]))
        good = worksheet_check.check(self.test_md, "Q1. A phone costs 480. In a sale it is reduced by 25%. Work out the sale price.\nAnswer: 360")
        self.assertEqual((good["ok"], good["copied_items"]), (True, []))

    def test_cli_exit_codes_and_stdin(self):
        script = os.path.join(gs.SCRIPTS, "worksheet_check.py")
        p = subprocess.run([sys.executable, script, self.test_md], input="nothing alike", capture_output=True, text=True)
        self.assertEqual(p.returncode, 0)
        p = subprocess.run([sys.executable, script, self.test_md], input=TEST_MD, capture_output=True, text=True)
        self.assertEqual(p.returncode, 1)
        p = subprocess.run([sys.executable, script, self.tmp + "/nope.md"], input="x", capture_output=True, text=True)
        self.assertEqual(p.returncode, 1)


class Gate(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.stage = f"{self.fx['C']}/mathA/stages/S1"

    def write(self, name, text):
        with open(f"{self.stage}/{name}", "w") as f:
            f.write(text)

    def test_leaked_test_item_blocks_shipping_and_clean_content_does_not(self):
        self.write("test.md", TEST_MD)
        self.write("practice.md", "# P\n\n## Practice items\n1. Try another one.\n")
        self.assertTrue(postcompile_gate._gate(f"{self.fx['C']}/mathA")["can_ship"])
        self.write("practice.md", "# P\n\n## Practice items\n1. A laptop costs 640. In a sale it is reduced by 15%. Work out the sale price.\n")
        r = postcompile_gate._gate(f"{self.fx['C']}/mathA")
        self.assertFalse(r["can_ship"])
        self.assertTrue(any("word for word in practice.md" in b for b in r["blocking_reasons"]))


if __name__ == "__main__":
    unittest.main()
