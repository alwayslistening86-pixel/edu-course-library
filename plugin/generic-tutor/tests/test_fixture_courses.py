"""A-02: the sample courses used by evals and tests are valid, complete, and usable by the real scripts."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import assemble_paper  # noqa: E402
import coverage_check  # noqa: E402
import enrol  # noqa: E402
import exam_to_bank  # noqa: E402
import postcompile_gate  # noqa: E402
import record_stage_result  # noqa: E402
import rubric_lint  # noqa: E402
import validate_schema  # noqa: E402

FX = os.path.join(ROOT, "evals", "fixtures", "courses")
COURSES = ("fx_maths_fractions", "fx_english_persuasion", "fx_law_contract")


class FixtureCourses(unittest.TestCase):
    def test_all_three_exist_and_pass_the_real_gates(self):
        self.assertEqual(sorted(os.listdir(FX)), sorted(COURSES))
        for c in COURSES:
            d = os.path.join(FX, c)
            gate = postcompile_gate._gate(d)
            self.assertTrue(gate["can_ship"], (c, gate["blocking_reasons"]))
            self.assertEqual(validate_schema.check_course_dir(d)["invalid"], [], c)
            self.assertEqual(coverage_check.check(d)["computed_status"], "full", c)
            self.assertEqual(rubric_lint.lint(d)["finding_count"], 0, c)

    def test_question_banks_match_what_the_converter_makes_from_exam_md(self):
        for c in COURSES:
            d = os.path.join(FX, c)
            made = exam_to_bank.propose(d)
            self.assertEqual(made["skipped"], [], c)
            with open(os.path.join(d, "question_bank.json"), encoding="utf-8") as f:
                self.assertEqual(json.load(f), made["bank"], c)

    def test_the_banks_assemble_a_paper(self):
        r = assemble_paper.assemble(FX, "fx_maths_fractions", marks=10)
        self.assertNotIn("error", r)
        self.assertLessEqual(abs(r["total_marks"] - 10), assemble_paper.TOLERANCE)

    def test_a_learner_can_work_through_each_course_to_the_end(self):
        for c in COURSES:
            tmp = os.path.realpath(tempfile.mkdtemp())
            self.addCleanup(shutil.rmtree, tmp, True)
            courses, learner = os.path.join(tmp, "courses"), os.path.join(tmp, "profile", "amy")
            shutil.copytree(os.path.join(FX, c), os.path.join(courses, c))
            os.makedirs(os.path.join(learner, "subjects"))
            with open(os.path.join(learner, "student_profile.json"), "w") as f:
                json.dump({"schema_version": 2, "learner_id": "amy", "consent": {"status": "granted"}, "roster": {"max_incomplete_courses": 3},
                           "highest_level_cleared": 1, "session_slot": 1, "capabilities": {}}, f)
            r = enrol.enrol(learner, courses, c, "active", "2026-10-06")
            self.assertTrue(r.get("written"), (c, r))
            subj, cj = os.path.join(learner, "subjects", f"{c}.json"), os.path.join(courses, c, "course.json")
            with open(cj) as f:
                ladder = json.load(f)["stage_ladder"]
            for sid in ladder:
                out = record_stage_result.apply(subj, cj, sid, "pass")
                self.assertTrue(out.get("written"), (c, sid, out))
            with open(subj) as f:
                self.assertEqual(set(json.load(f)["syllabus_status"].values()), {"pass"})

    def test_the_fixtures_are_not_git_ignored(self):
        """A broad ignore rule once hid evals/fixtures/courses from git, so CI ran without them. Skipped where git is absent."""
        import subprocess
        try:
            r = subprocess.run(["git", "check-ignore", "-q", os.path.join(FX, COURSES[0], "course.json")], capture_output=True, cwd=ROOT)
        except OSError:
            self.skipTest("git not available")
        if r.returncode == 128:
            self.skipTest("not a git checkout")
        self.assertEqual(r.returncode, 1, "evals/fixtures/courses is matched by a .gitignore rule")

    def test_no_exam_board_wording_or_private_data_slipped_in(self):
        banned = ("AQA", "OCR ", "Edexcel", "Pearson", "SQE", "mark scheme for")
        for dp, _, fns in os.walk(FX):
            for fn in fns:
                with open(os.path.join(dp, fn), encoding="utf-8") as f:
                    text = f.read()
                for b in banned:
                    if b in text:
                        self.assertIn("generic-tutor", text, f"{fn} mentions {b!r}")


if __name__ == "__main__":
    unittest.main()
