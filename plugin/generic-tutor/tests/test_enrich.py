"""Audit enrichment helpers: enrich_plan (what is missing) and exam_to_bank (starter bank from exam/exam.md)."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")
sys.path.insert(0, SCRIPTS)

import enrich_plan as ep  # noqa: E402
import exam_to_bank as eb  # noqa: E402
from tutorlib import schema  # noqa: E402

EXAM = """# X - Cumulative Exam

## Format
Two papers.

## 6 ready-made items (write the rest fresh, never reusing stage-test items)
1. [Paper 1] State two differences between A and B. [4 marks]
2. [Paper 1] Which statement is correct? Choose every correct option.
   A. one
   B. two
3. Discuss the extent to which X holds. [15 marks]
4. What does this print?
```python
print(1)
```
5. Set a problem question on Y and mark it fresh.
6. Explain Z. [3 marks]

## Answer key for the ready-made items (tutor only)
1. [4] M2 first difference; M2 second difference
2. Correct: B (exactly these options, no others)
3. [15] Mark by levels: Level 3 (7-9) developed analysis; Level 4 (10-12) sustained.
4. Actual result:
```
1
```
6. [3] vague prose with no points

## Grading
x
"""


def make(tmp, exam=EXAM, rubric=True):
    cd = os.path.join(tmp, "c1")
    os.makedirs(os.path.join(cd, "exam"))
    os.makedirs(os.path.join(cd, "stages", "S01"))
    os.makedirs(os.path.join(cd, "stages", "S02"))
    with open(os.path.join(cd, "course.json"), "w") as f:
        json.dump({"stage_ladder": ["S01", "S02"]}, f)
    if rubric:
        with open(os.path.join(cd, "rubric.json"), "w") as f:
            json.dump({"source_urls": ["https://example.org/spec.pdf"]}, f)
    if exam is not None:
        with open(os.path.join(cd, "exam", "exam.md"), "w") as f:
            f.write(exam)
    return cd


class Plan(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.cd = make(self.tmp)

    def test_reports_gaps_and_counts_ready_made_items(self):
        r = ep.run(self.tmp)["courses"]["c1"]
        self.assertEqual(r["todo"], ["question_bank", "misconceptions", "exam_technique"])
        self.assertEqual((r["stages"], r["ready_made_items"], r["misconceptions"]["stages_without"]), (2, 6, 2))
        self.assertEqual(r["source_urls"], ["https://example.org/spec.pdf"])

    def test_counts_documented_and_plausible_entries(self):
        with open(os.path.join(self.cd, "stages", "S01", "misconceptions.json"), "w") as f:
            json.dump([{"pattern": "p" * 12, "correction": "c" * 12, "source": "AQA report 2023"},
                       {"pattern": "p" * 12, "correction": "c" * 12, "source": ep.PLAUSIBLE}], f)
        m = ep.run(self.tmp)["courses"]["c1"]["misconceptions"]
        self.assertEqual((m["stages_with_file"], m["stages_without"], m["documented_entries"], m["plausible_entries"]), (1, 1, 1, 1))

    def test_a_learner_observed_entry_is_not_counted_as_board_documented(self):
        note = ep.PLAUSIBLE + " \u2014 recurring in this library's own data"
        with open(os.path.join(self.cd, "stages", "S01", "misconceptions.json"), "w") as f:
            json.dump([{"pattern": "p" * 12, "correction": "c" * 12, "source": note},
                       {"pattern": "p" * 12, "correction": "c" * 12, "source": ep.PLAUSIBLE.upper()},
                       {"pattern": "p" * 12, "correction": "c" * 12, "source": "OCR report 2022 Q4"}], f)
        m = ep.run(self.tmp)["courses"]["c1"]["misconceptions"]
        self.assertEqual((m["documented_entries"], m["plausible_entries"], m["learner_observed_entries"]), (1, 2, 1))

    def test_unknown_course_and_totals(self):
        self.assertIn("error", ep.run(self.tmp, "nope"))
        self.assertEqual(ep.run(self.tmp)["totals"]["without_question_bank"], 1)


class Bank(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.cd = make(self.tmp)

    def test_converts_only_what_converts_cleanly_and_says_why(self):
        r = eb.propose(self.cd)
        self.assertEqual([q["id"] for q in r["bank"]["questions"]], ["exam-1", "exam-2", "exam-3"])
        reasons = {s["item"]: s["reason"] for s in r["skipped"]}
        self.assertIn("code block", reasons[4])
        self.assertIn("instruction", reasons[5])
        self.assertIn("mark scheme", reasons[6])
        self.assertEqual(r["schema_errors"], [])
        self.assertEqual(schema.validate(r["bank"], "question_bank"), [])
        q1, q2, q3 = r["bank"]["questions"]
        self.assertEqual((q1["marks"], [p["marks"] for p in q1["mark_scheme"]], q1["prompt"].startswith("State two")), (4, [2, 2], True))
        self.assertEqual((q2["marks"], q2["mark_scheme"][0]["descriptor"]), (1, "selects exactly option(s) B and no others"))
        self.assertEqual((q3["marks"], q3["mark_scheme"][0]["type"]), (15, "other"))

    def test_write_refuses_to_overwrite_and_missing_exam_is_an_error(self):
        script = os.path.join(SCRIPTS, "exam_to_bank.py")
        out = json.loads(subprocess.run([sys.executable, script, self.cd, "--write"], capture_output=True, text=True).stdout)
        self.assertTrue(out["written"])
        again = json.loads(subprocess.run([sys.executable, script, self.cd, "--write"], capture_output=True, text=True).stdout)
        self.assertIn("not overwritten", again["error"])
        self.assertIn("error", eb.propose(os.path.join(self.tmp, "absent")))

    def test_the_bank_feeds_the_paper_assembler(self):
        import assemble_paper
        eb_out = eb.propose(self.cd)
        with open(os.path.join(self.cd, "question_bank.json"), "w") as f:
            json.dump(eb_out["bank"], f)
        r = assemble_paper.assemble(self.tmp, "c1", marks=20)
        self.assertNotIn("error", r)
        self.assertTrue(17 <= r["total_marks"] <= 23)


if __name__ == "__main__":
    unittest.main()
