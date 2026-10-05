"""
Tests for the 1.11.0 fix: record_stage_result.py now owns the write-back for
syllabus_status and current_stage advancement -- the single most load-bearing
field pair in the system, previously hand-write-back-only (like confidence/
review cards were before v1.10.0), and the exact field whose corresponding
content instruction (stages/<id>/test.md) told the model to write the wrong
literal values ("passed"/"not_passed") for 445 of 1253 stage test files.

    python3 -m unittest discover tests -v
"""
import json
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

import record_stage_result  # noqa: E402


def _w(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


def _r(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


class TmpDirCase(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def subj(self, **extra):
        p = os.path.join(self.d, "subjects.json")
        base = {
            "schema_version": 5, "course_id": "x",
            "syllabus_status": {}, "current_stage": "S01", "current_phase": "test",
        }
        base.update(extra)
        _w(p, base)
        return p

    def course(self, stage_ladder=None):
        p = os.path.join(self.d, "course.json")
        base = {"course_id": "x", "stage_ladder": stage_ladder or ["S01", "S02", "S03"]}
        _w(p, base)
        return p


class TestRecordStageResultApply(TmpDirCase):
    def test_pass_sets_status_and_advances_stage(self):
        subj = self.subj(current_stage="S01", syllabus_status={})
        course = self.course()
        r = record_stage_result.apply(subj, course, "S01", "pass")
        self.assertTrue(r["written"])
        self.assertEqual(r["advanced_to"], "S02")
        d = _r(subj)
        self.assertEqual(d["syllabus_status"]["S01"], "pass")
        self.assertEqual(d["current_stage"], "S02")
        self.assertEqual(d["current_phase"], "lesson")

    def test_fail_sets_status_and_does_not_advance(self):
        subj = self.subj(current_stage="S01", syllabus_status={}, current_phase="test")
        course = self.course()
        r = record_stage_result.apply(subj, course, "S01", "fail")
        self.assertTrue(r["written"])
        self.assertIsNone(r["advanced_to"])
        d = _r(subj)
        self.assertEqual(d["syllabus_status"]["S01"], "fail")
        self.assertEqual(d["current_stage"], "S01")   # unchanged
        self.assertEqual(d["current_phase"], "test")  # unchanged -- remediation stays in this stage

    def test_pass_skips_withheld_stages(self):
        subj = self.subj(current_stage="S01", syllabus_status={"S02": "withheld"})
        course = self.course(stage_ladder=["S01", "S02", "S03"])
        r = record_stage_result.apply(subj, course, "S01", "pass")
        self.assertEqual(r["advanced_to"], "S03")

    def test_pass_on_last_stage_leaves_current_stage_unchanged(self):
        subj = self.subj(current_stage="S03", syllabus_status={"S01": "pass", "S02": "pass"})
        course = self.course()
        r = record_stage_result.apply(subj, course, "S03", "pass")
        self.assertIsNone(r["advanced_to"])
        d = _r(subj)
        self.assertEqual(d["syllabus_status"]["S03"], "pass")
        self.assertEqual(d["current_stage"], "S03")  # completion is derived elsewhere, not decided here

    def test_pass_when_every_remaining_stage_is_withheld_leaves_current_stage_unchanged(self):
        subj = self.subj(current_stage="S01", syllabus_status={"S02": "withheld", "S03": "withheld"})
        course = self.course()
        r = record_stage_result.apply(subj, course, "S01", "pass")
        self.assertIsNone(r["advanced_to"])
        d = _r(subj)
        self.assertEqual(d["current_stage"], "S01")

    def test_unknown_stage_id_is_an_error_not_a_silent_noop(self):
        subj = self.subj()
        course = self.course()
        r = record_stage_result.apply(subj, course, "S99_does_not_exist", "pass")
        self.assertIn("error", r)
        d = _r(subj)
        self.assertEqual(d["syllabus_status"], {})  # nothing written

    def test_invalid_result_value_is_rejected(self):
        subj = self.subj()
        course = self.course()
        r = record_stage_result.apply(subj, course, "S01", "passed")  # the exact old bug value
        self.assertIn("error", r)

    def test_records_previous_status(self):
        subj = self.subj(syllabus_status={"S01": "fail"})
        course = self.course()
        r = record_stage_result.apply(subj, course, "S01", "pass")
        self.assertEqual(r["previous_status"], "fail")
        self.assertEqual(r["result"], "pass")

    def test_re_pass_after_fail_still_advances(self):
        subj = self.subj(current_stage="S01", syllabus_status={"S01": "fail"})
        course = self.course()
        r = record_stage_result.apply(subj, course, "S01", "pass")
        self.assertEqual(r["advanced_to"], "S02")


if __name__ == "__main__":
    unittest.main()
