"""B-02.3: script marking of keyed items. The tables ARE the edge-case table the design promised; a row that changes is a decision."""
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
from tutorlib import marking, schema  # noqa: E402

T, F, N = True, False, None


class Numeric(unittest.TestCase):
    def check(self, key, rows):
        for answer, want, reason in rows:
            got = marking.mark(key, answer)
            self.assertEqual((got["correct"], got["reason"]), (want, reason), f"{answer!r} against {key}")

    def test_exact_and_decimal_forms(self):
        self.check({"kind": "numeric", "value": "9.81"}, [
            ("9.81", T, "within_tolerance"), (" 9.81 ", T, "within_tolerance"), ("9,81", T, "within_tolerance"),
            ("9.810", T, "within_tolerance"), ("9.8", F, "outside_tolerance"), ("+9.81", T, "within_tolerance"),
            ("-9.81", F, "outside_tolerance"), ("−9.81", F, "outside_tolerance"), ("981e-2", T, "within_tolerance")])

    def test_negative_value_with_unicode_minus(self):
        self.check({"kind": "numeric", "value": "-4.5"}, [("−4.5", T, "within_tolerance"), ("-4,5", T, "within_tolerance"), ("4.5", F, "outside_tolerance")])

    def test_tolerance_is_inclusive_and_decimal_exact(self):
        self.check({"kind": "numeric", "value": "0.3", "tolerance": {"abs": "0.1"}}, [("0.4", T, "within_tolerance"), ("0.2", T, "within_tolerance"), ("0.41", F, "outside_tolerance")])
        self.check({"kind": "numeric", "value": "200", "tolerance": {"rel": "0.05"}}, [("190", T, "within_tolerance"), ("210", T, "within_tolerance"), ("211", F, "outside_tolerance")])

    def test_separators(self):
        self.check({"kind": "numeric", "value": "1000"}, [
            ("1,000", N, "ambiguous_separator"), ("1.000", F, "outside_tolerance"), ("1000", T, "within_tolerance"), ("1 000", N, "ambiguous_separator")])
        self.check({"kind": "numeric", "value": "1000000"}, [("1,000,000", T, "within_tolerance"), ("1.000.000", T, "within_tolerance"), ("1,00,000", N, "ambiguous_separator")])
        self.check({"kind": "numeric", "value": "1234.5"}, [("1,234.5", T, "within_tolerance"), ("1.234,5", T, "within_tolerance"), ("1,2345.5", N, "ambiguous_separator")])

    def test_units(self):
        key = {"kind": "numeric", "value": "9.81", "tolerance": {"abs": "0.05"}, "units": ["m/s^2", "m s^-2"]}
        self.check(key, [("9.81 m/s^2", T, "within_tolerance"), ("9.81m/s^2", T, "within_tolerance"), ("9.8 m s^-2", T, "within_tolerance"),
                         ("9.81", F, "missing_unit"), ("9.81 m/s", F, "wrong_unit"), ("9.81 M/S^2", F, "wrong_unit"), ("9.81 km/s^2", F, "wrong_unit")])
        self.check({"kind": "numeric", "value": "5", "units": ["mA"]}, [("5 mA", T, "within_tolerance"), ("5 MA", F, "wrong_unit")])

    def test_text_the_key_did_not_expect_is_not_ignored(self):
        self.check({"kind": "numeric", "value": "5"}, [("5 metres", N, "unexpected_text"), ("five", N, "unparseable"), ("", N, "empty_answer"), ("   ", N, "empty_answer"), ("nan", N, "unparseable")])

    def test_wrong_value_with_correct_unit_is_wrong(self):
        self.check({"kind": "numeric", "value": "5", "units": ["N"]}, [("6 N", F, "outside_tolerance")])


class Mcq(unittest.TestCase):
    KEY = {"kind": "mcq", "options": ["a cat", "a dog", "a bird"], "correct": "B"}

    def test_forms(self):
        for answer, want in (("B", T), ("b", T), ("(b)", T), ("B.", T), ("b)", T), (" b ", T), ("a dog", T), ("A DOG.", T),
                             ("A", F), ("C", F), ("a cat", F), ("D", F), ("AB", F), ("b c", F), ("dog", F)):
            self.assertIs(marking.mark(self.KEY, answer)["correct"], want, answer)

    def test_empty_cannot_be_marked(self):
        self.assertIsNone(marking.mark(self.KEY, "")["correct"])


class Short(unittest.TestCase):
    KEY = {"kind": "short", "accepted": ["photosynthesis", "Photo-synthesis"]}

    def test_normalisation(self):
        for answer, want in (("photosynthesis", T), ("  PHOTOSYNTHESIS. ", T), ("“photosynthesis”", T), ("photo-synthesis", T),
                             ("photosynthesys", F), ("respiration", F), ("photosynthesis and respiration", F)):
            self.assertIs(marking.mark(self.KEY, answer)["correct"], want, answer)

    def test_case_sensitive_when_asked(self):
        key = {"kind": "short", "accepted": ["Fe"], "case_sensitive": True}
        self.assertIs(marking.mark(key, "Fe")["correct"], True)
        self.assertIs(marking.mark(key, "fe")["correct"], False)

    def test_whitespace_collapses(self):
        self.assertIs(marking.mark({"kind": "short", "accepted": ["forty two"]}, "forty   two\n")["correct"], True)

    def test_only_punctuation_cannot_be_marked(self):
        self.assertIsNone(marking.mark(self.KEY, "...")["correct"])


class Keys(unittest.TestCase):
    def test_malformed_keys_are_named(self):
        bad = [
            ({"kind": "essay"}, "kind"), ("x", "object"),
            ({"kind": "mcq", "options": ["only one"], "correct": "A"}, "options"),
            ({"kind": "mcq", "options": ["a", "b"], "correct": "C"}, "correct"),
            ({"kind": "mcq", "options": ["a", "A "], "correct": "A"}, "same"),
            ({"kind": "numeric", "value": "nine"}, "value"), ({"kind": "numeric", "value": "1", "tolerance": {"abs": "-1"}}, "zero or more"),
            ({"kind": "numeric", "value": "1", "tolerance": {"abs": "1", "rel": "1"}}, "tolerance"),
            ({"kind": "numeric", "value": "1", "units": [" m"]}, "units"), ({"kind": "short", "accepted": []}, "accepted"),
            ({"kind": "short", "accepted": ["x"], "case_sensitive": "no"}, "case_sensitive")]
        for key, word in bad:
            problems = marking.check_key(key)
            self.assertTrue(problems and word in " ".join(problems), (key, problems))
            with self.assertRaises(ValueError):
                marking.mark(key, "x")

    def test_good_keys_have_no_problems(self):
        for key in (Mcq.KEY, Short.KEY, {"kind": "numeric", "value": "1.5", "tolerance": {"rel": "0.1"}, "units": ["m"]}):
            self.assertEqual(marking.check_key(key), [])

    def test_the_schema_check_rejects_a_bad_key_in_a_bank(self):
        bank = {"schema_version": 1, "questions": [{"id": "q", "stage_id": "S1", "marks": 1, "prompt": "Pick one.", "source": "tests",
                                                    "mark_scheme": [{"id": "B1", "marks": 1, "descriptor": "right"}], "key": {"kind": "mcq", "options": ["a", "b"], "correct": "Z"}}]}
        errors = schema.validate(bank, "question_bank")
        self.assertTrue(any("'q'" in e and "correct" in e for e in errors), errors)
        bank["questions"][0]["key"]["correct"] = "A"
        self.assertEqual(schema.validate(bank, "question_bank"), [])


class Script(unittest.TestCase):
    def setUp(self):
        self.d = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)
        self.fx = gs.build_fixture(self.d)
        self.bank = os.path.join(self.fx["C"], "mathA", "question_bank.json")

    def run_it(self, qid, answer):
        return gs.run_step("mark_answer.py", [self.bank, qid, answer], self.fx, self.d)

    def test_marks_are_all_or_nothing_and_nothing_is_written(self):
        with open(self.bank, "rb") as f:
            before = f.read()
        r = self.run_it("S1-Q1", "42 m")
        self.assertEqual((r["exit"], r["stdout"]["marks_awarded"], r["stdout"]["marks_available"]), (0, 3, 3))
        r = self.run_it("S1-Q1", "50 m")
        self.assertEqual((r["stdout"]["correct"], r["stdout"]["marks_awarded"]), (False, 0))
        with open(self.bank, "rb") as f:
            self.assertEqual(f.read(), before)

    def test_unmarkable_answer_is_null_not_wrong(self):
        r = self.run_it("S1-Q1", "")
        self.assertEqual((r["exit"], r["stdout"]["correct"], r["stdout"]["marks_awarded"]), (0, None, 0))

    def test_unkeyed_or_unknown_question_is_an_error_sending_the_caller_to_the_examiner(self):
        r = self.run_it("S1-Q2", "42")
        self.assertEqual(r["exit"], 1)
        self.assertIn("examiner", r["stdout"]["error"])
        self.assertEqual(self.run_it("nope", "42")["exit"], 1)

    def test_a_bank_with_a_bad_key_is_refused(self):
        with open(self.bank, encoding="utf-8") as f:
            data = json.load(f)
        data["questions"][0]["key"] = {"kind": "mcq", "options": ["a", "b"], "correct": "Z"}
        with open(self.bank, "w", encoding="utf-8") as f:
            json.dump(data, f)
        r = self.run_it("S1-Q1", "A")
        self.assertEqual(r["exit"], 1)
        self.assertIn("invalid", r["stdout"]["error"])


class PapersNeverShowTheKey(unittest.TestCase):
    def test_assembled_paper_has_no_key_but_mcq_shows_options(self):
        d = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d, True)
        fx = gs.build_fixture(d)
        path = os.path.join(fx["C"], "mathA", "question_bank.json")
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        data["questions"][1]["key"] = {"kind": "mcq", "options": ["red", "blue"], "correct": "B"}
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f)
        r = gs.run_step("assemble_paper.py", [fx["C"], "mathA", "--marks", "200"], fx, d)
        self.assertEqual(r["exit"], 0, r)
        text = json.dumps(r["stdout"])
        self.assertNotIn('"key"', text)
        self.assertNotIn('"correct"', text)
        self.assertNotIn("forty", text)
        shown = {q["id"]: q for q in r["stdout"]["questions"]}
        self.assertEqual(shown["S1-Q2"].get("options"), ["red", "blue"])
        self.assertNotIn("options", shown["S1-Q1"])


class CompilerWritesKeysOnlyWhenSafe(unittest.TestCase):
    EXAM = """## 4 ready-made items
1. Which is a mammal?
   A. trout
   B. whale
   C. eagle
2. Which are even?
   A. 2
   B. 3
   C. 4
3. Pick one.
   A. first
   C. third
4. Pick one more.
   A. first
   B. second

## Answer key for the ready-made items (tutor only)
1. Correct: B
2. Correct: A, C
3. Correct: C
4. Correct: D
"""

    def test_keys_for_clean_single_answer_items_only(self):
        import exam_to_bank
        d = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, d, True)
        os.makedirs(os.path.join(d, "exam"))
        with open(os.path.join(d, "exam", "exam.md"), "w", encoding="utf-8") as f:
            f.write(self.EXAM)
        proposal = exam_to_bank.propose(d)
        self.assertEqual(proposal["schema_errors"], [])
        qs = {q["id"]: q for q in proposal["bank"]["questions"]}
        self.assertEqual(qs["exam-1"]["key"], {"kind": "mcq", "options": ["trout", "whale", "eagle"], "correct": "B"})
        self.assertEqual(marking.mark(qs["exam-1"]["key"], "whale")["correct"], True)
        for n in ("2", "3", "4"):
            self.assertNotIn("key", qs[f"exam-{n}"], n)                       # multi-answer, options out of order, correct letter not offered


if __name__ == "__main__":
    unittest.main()
