"""ADR 0012 build task B-04.5e: a stage pass needs a grading record (and, where the rubric publishes one, a pass mark)."""
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
import record_stage_result as rsr  # noqa: E402
from tutorlib import schema  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.s = f"{self.fx['S']}/mathA.json"
        self.c = f"{self.fx['C']}/mathA/course.json"
        self.rubric = f"{self.fx['C']}/mathA/rubric.json"

    def get(self):
        return gs.read_json(self.s)

    def edit(self, path, fn):
        d = gs.read_json(path)
        fn(d)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f)

    def set_pass_percent(self, n, stage="S2"):
        self.edit(self.rubric, lambda d: d["stage_rubrics"][stage].update(pass_percent=n))


class Gate(Base):
    def test_a_pass_with_no_grading_record_is_refused_and_nothing_is_written(self):
        before = self.get()
        r = rsr.apply(self.s, self.c, "S2", "pass")
        self.assertIn("no grading record", r["error"])
        self.assertIn("record_grading.py", r["error"])
        self.assertEqual(self.get(), before)

    def test_a_graded_test_can_be_passed_and_the_evidence_is_reported(self):
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        r = rsr.apply(self.s, self.c, "S2", "pass")
        self.assertTrue(r["written"], r)
        self.assertEqual((r["grading"]["attempt"], r["grading"]["awarded"], r["grading"]["available"], r["grading"]["percent"]), (1, 2, 2, 100.0))
        self.assertEqual(self.get()["grading_used"], {"S2": 1})
        self.assertEqual(schema.validate(self.get(), "subjects"), [])

    def test_one_record_cannot_back_two_results(self):
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        rsr.apply(self.s, self.c, "S2", "fail")                                   # the fail consumes it
        r = rsr.apply(self.s, self.c, "S2", "pass")
        self.assertIn("already used", r["error"])
        self.assertEqual(self.get()["syllabus_status"]["S2"], "fail")
        gs.grade(self.fx, self.tmp, "mathA", "S2", slot=2)                       # the re-test is graded
        self.assertTrue(rsr.apply(self.s, self.c, "S2", "pass")["written"])
        self.assertEqual(self.get()["grading_used"]["S2"], 2)

    def test_repeating_a_recorded_pass_is_not_re_checked(self):
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        rsr.apply(self.s, self.c, "S2", "pass")
        again = rsr.apply(self.s, self.c, "S2", "pass")
        self.assertTrue(again["written"], again)
        self.assertNotIn("grading", again)

    def test_a_fail_is_never_refused(self):
        r = rsr.apply(self.s, self.c, "S2", "fail")
        self.assertTrue(r["written"], r)
        self.assertNotIn("grading_used", self.get())                              # nothing to consume

    def test_grading_one_stage_does_not_cover_another(self):
        gs.grade(self.fx, self.tmp, "mathA", "S3")
        self.assertIn("no grading record", rsr.apply(self.s, self.c, "S2", "pass")["error"])


class PassMark(Base):
    def test_marks_below_the_published_pass_mark_are_refused_naming_the_numbers(self):
        self.set_pass_percent(70)
        gs.grade(self.fx, self.tmp, "mathA", "S2", marks=1, of=2)                # 2 of 4 marks: 50%
        r = rsr.apply(self.s, self.c, "S2", "pass")
        self.assertIn("2 of 4", r["error"])
        self.assertIn("50.0%", r["error"])
        self.assertIn("70%", r["error"])
        self.assertNotEqual(self.get()["syllabus_status"].get("S2"), "pass")

    def test_the_pass_mark_itself_passes_and_a_refusal_does_not_use_up_the_record(self):
        self.set_pass_percent(50)
        gs.grade(self.fx, self.tmp, "mathA", "S2", marks=1, of=2)                # exactly 50%
        self.assertTrue(rsr.apply(self.s, self.c, "S2", "pass")["written"])
        self.set_pass_percent(75, "S3")
        gs.grade(self.fx, self.tmp, "mathA", "S3", marks=1, of=2)
        self.assertIn("below the pass mark", rsr.apply(self.s, self.c, "S3", "pass")["error"])
        self.assertNotIn("S3", self.get().get("grading_used", {}))                # still unused: a better grading may follow
        gs.grade(self.fx, self.tmp, "mathA", "S3", slot=2)
        self.assertTrue(rsr.apply(self.s, self.c, "S3", "pass")["written"])

    def test_the_rubric_schema_checks_pass_percent(self):
        rub = gs.read_json(self.rubric)
        self.assertEqual(schema.validate(rub, "rubric"), [])
        for bad in (0, 101, "70", 70.5):
            rub["stage_rubrics"]["S2"]["pass_percent"] = bad
            self.assertTrue(schema.validate(rub, "rubric"), bad)
        rub["stage_rubrics"]["S2"]["pass_percent"] = 70
        self.assertEqual(schema.validate(rub, "rubric"), [])


class Waivers(Base):
    """Where the check cannot apply it is skipped and says so, never silently and never by refusing."""

    def test_signal_data_not_kept_under_limited_consent(self):
        self.edit(f"{self.fx['L']}/student_profile.json", lambda d: d["consent"].update(status="limited"))
        r = rsr.apply(self.s, self.c, "S2", "pass")
        self.assertTrue(r["written"], r)
        self.assertIn("not kept under this consent", r["grading_check"])

    def test_a_stage_with_no_rubric_entry(self):
        self.edit(self.rubric, lambda d: d["stage_rubrics"].pop("S2"))
        r = rsr.apply(self.s, self.c, "S2", "pass")
        self.assertTrue(r["written"], r)
        self.assertIn("no rubric entry", r["grading_check"])

    def test_an_unreadable_history_database(self):
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        with open(f"{self.fx['L']}/tutor.sqlite3", "wb") as f:
            f.write(b"this is not a database" * 50)
        r = rsr.apply(self.s, self.c, "S2", "pass")
        self.assertTrue(r["written"], r)
        self.assertIn("could not be read", r["grading_check"])


class Cli(Base):
    def test_the_refusal_is_an_error_exit_through_the_command_line(self):
        r = gs.run_step("record_stage_result.py", ["apply", "{S}/mathA.json", "{C}/mathA/course.json", "S2", "pass"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 1)
        self.assertIn("record_grading.py", r["stdout"]["error"])
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        r = gs.run_step("record_stage_result.py", ["apply", "{S}/mathA.json", "{C}/mathA/course.json", "S2", "pass"], self.fx, self.tmp)
        self.assertEqual((r["exit"], r["stdout"]["grading"]["attempt"]), (0, 1))


if __name__ == "__main__":
    unittest.main()
