"""N-06: quotation policy / verbatim-run check (advisory)."""
import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import paraphrase_check as pc  # noqa: E402

SRC = "The candidate must show that a fraction is a number of equal parts of a whole and relate it to division of integers."


def course(tmp, lesson, rubric=None):
    d = os.path.join(tmp, "c")
    os.makedirs(os.path.join(d, "stages", "S1"))
    with open(os.path.join(d, "stages", "S1", "lesson.md"), "w", encoding="utf-8") as f:
        f.write(lesson)
    if rubric:
        with open(os.path.join(d, "rubric.json"), "w", encoding="utf-8") as f:
            json.dump({"stage_rubrics": {"S1": {"criteria": rubric}}}, f)
    src = os.path.join(tmp, "src.txt")
    with open(src, "w", encoding="utf-8") as f:
        f.write(SRC)
    return d, src


def rules(r):
    return sorted({f["rule"] for f in r["findings"]})


class Check(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.tmp = self._t.name
        self.addCleanup(self._t.cleanup)

    def test_original_text_is_clean(self):
        d, src = course(self.tmp, "A fraction splits something into equal pieces; the bottom number says how many.")
        self.assertEqual(pc.check(d, [src])["finding_count"], 0)

    def test_verbatim_run_is_found_with_source(self):
        d, src = course(self.tmp, "Remember: a fraction is a number of equal parts of a whole and relate it to division of integers, ok?")
        r = pc.check(d, [src])
        self.assertEqual(rules(r), ["verbatim_run"])
        self.assertGreaterEqual(int(r["findings"][0]["detail"].split()[0]), 8)
        self.assertEqual(pc.check(d)["finding_count"], 0, "no source, no verbatim check")

    def test_short_attributed_quote_is_allowed_long_one_is_not(self):
        d, src = course(self.tmp, 'The board calls it "a number of equal parts of a whole" (spec 2.1).')
        self.assertEqual(pc.check(d, [src])["finding_count"], 0)
        long_q = " ".join(["word"] * 16)
        other = os.path.join(self.tmp, "other")
        os.makedirs(other)
        d2, _ = course(other, f'Quote: "{long_q}"')
        self.assertEqual(rules(pc.check(d2)), ["long_quote"])

    def test_more_than_one_quote_per_stage(self):
        d, _ = course(self.tmp, 'One "a number of equal parts" and two "division of whole integers here".')
        self.assertEqual(rules(pc.check(d)), ["many_quotes"])

    def test_rubric_criteria_are_checked(self):
        d, src = course(self.tmp, "Plain.", ["Shows that a fraction is a number of equal parts of a whole and relate it to division of integers"])
        r = pc.check(d, [src])
        self.assertEqual([f["where"] for f in r["findings"]], ["rubric.json:S1"])

    def test_bad_inputs_report_errors(self):
        self.assertIn("error", pc.check(os.path.join(self.tmp, "none")))
        d, _ = course(self.tmp, "x")
        self.assertIn("error", pc.check(d, [os.path.join(self.tmp, "missing.txt")]))
        self.assertEqual(pc.main([]), 2)


if __name__ == "__main__":
    unittest.main()
