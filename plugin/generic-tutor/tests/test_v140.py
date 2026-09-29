"""
Tests for the 1.4.0 adaptive-teaching layer: error_log.py, diagnostic_gate.py,
remediation_state.py, confidence_update.py, and the subjects.json 3->4 migration
and validate_structure.py's misconceptions_status. Stdlib only.

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

import confidence_update  # noqa: E402
import diagnostic_gate  # noqa: E402
import error_log  # noqa: E402
import migrate_schema  # noqa: E402
import remediation_state  # noqa: E402
import validate_structure  # noqa: E402


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
        base = {"schema_version": 4, "course_id": "x", "error_patterns": []}
        base.update(extra)
        _w(p, base)
        return p


class TestErrorLog(TmpDirCase):
    def test_append_basic_shape(self):
        p = self.subj()
        result = error_log.append(p, "S09", "RM6", "practice", "misconception", "MC-RM6-2", "sign confusion", 214)
        self.assertEqual(result["entry"]["cause"], "misconception")
        self.assertFalse(result["recurring"])
        self.assertEqual(_r(p)["error_patterns"][0]["resolved"], False)

    def test_bad_cause_rejected(self):
        p = self.subj()
        result = error_log.append(p, "S09", "RM6", "practice", "not_a_real_cause", "NONE", "x", 1)
        self.assertIn("error", result)
        self.assertEqual(_r(p)["error_patterns"], [])  # never partially written

    def test_bad_source_phase_rejected(self):
        p = self.subj()
        result = error_log.append(p, "S09", "RM6", "homework", "slip", "NONE", "x", 1)
        self.assertIn("error", result)

    def test_recurring_after_second_same_pair(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "misconception", "NONE", "a", 1)
        r2 = error_log.append(p, "S09", "RM6", "practice", "misconception", "NONE", "b", 2)
        self.assertTrue(r2["recurring"])

    def test_not_recurring_across_different_causes(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "a", 1)
        r2 = error_log.append(p, "S09", "RM6", "practice", "comprehension", "NONE", "b", 2)
        self.assertFalse(r2["recurring"])  # different cause, same item — not the same pair

    def test_resolve_flips_flag_and_records_slot(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "misconception", "NONE", "a", 1)
        error_log.resolve(p, "RM6", 50)
        entry = _r(p)["error_patterns"][0]
        self.assertTrue(entry["resolved"])
        self.assertEqual(entry["resolved_at_slot"], 50)

    def test_resolve_leaves_already_resolved_alone(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "misconception", "NONE", "a", 1)
        error_log.resolve(p, "RM6", 50)
        r2 = error_log.resolve(p, "RM6", 60)
        self.assertEqual(r2["count"], 0)  # nothing left unresolved to flip

    def test_resolve_respects_cause_filter(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "a", 1)
        error_log.append(p, "S09", "RM6", "practice", "comprehension", "NONE", "b", 2)
        error_log.resolve(p, "RM6", 10, "slip")
        entries = _r(p)["error_patterns"]
        resolved = {e["cause"]: e["resolved"] for e in entries}
        self.assertTrue(resolved["slip"])
        self.assertFalse(resolved["comprehension"])

    def test_query_recurring_pairs_and_by_cause(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "misconception", "NONE", "a", 1)
        error_log.append(p, "S09", "RM6", "practice", "misconception", "NONE", "b", 2)
        error_log.append(p, "S09", "RM7", "practice", "slip", "NONE", "c", 3)
        q = error_log.query(p, "S09")
        self.assertEqual(q["unresolved_count"], 3)
        self.assertEqual(q["unresolved_by_cause"]["misconception"], 2)
        self.assertEqual(len(q["recurring_pairs"]), 1)

    def test_query_stage_filter_excludes_other_stages(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "a", 1)
        error_log.append(p, "S10", "RM9", "practice", "slip", "NONE", "b", 2)
        q = error_log.query(p, "S09")
        self.assertEqual(q["total_entries"], 1)


class TestDiagnosticGate(TmpDirCase):
    def test_no_fire_when_nothing_triggers(self):
        p = self.subj()
        r = diagnostic_gate.evaluate(p, "S09", "RM6", False, False)
        self.assertFalse(r["fire"])
        self.assertEqual(r["reasons"], [])

    def test_fires_on_explicit_confusion(self):
        p = self.subj()
        r = diagnostic_gate.evaluate(p, "S09", "RM6", True, False)
        self.assertTrue(r["fire"])
        self.assertIn("explicitly said", r["reasons"][0])

    def test_fires_on_reasoning_mismatch(self):
        p = self.subj()
        r = diagnostic_gate.evaluate(p, "S09", "RM6", False, True)
        self.assertTrue(r["fire"])

    def test_fires_on_repeated_item(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "a", 1)
        error_log.append(p, "S09", "RM6", "practice", "misapplied_procedure", "NONE", "b", 2)
        r = diagnostic_gate.evaluate(p, "S09", "RM6", False, False)
        self.assertTrue(r["fire"])
        self.assertTrue(r["trigger_a_repeated_item"])

    def test_does_not_fire_on_single_miss(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "a", 1)
        r = diagnostic_gate.evaluate(p, "S09", "RM6", False, False)
        self.assertFalse(r["fire"])

    def test_fires_on_recurring_cause_in_stage_across_items(self):
        p = self.subj()
        error_log.append(p, "S09", "RM1", "practice", "misconception", "NONE", "a", 1)
        error_log.append(p, "S09", "RM2", "practice", "misconception", "NONE", "b", 2)
        error_log.append(p, "S09", "RM3", "practice", "misconception", "NONE", "c", 3)
        r = diagnostic_gate.evaluate(p, "S09", "RM4", False, False)
        self.assertTrue(r["fire"])
        self.assertEqual(r["trigger_b_recurring_cause"]["cause"], "misconception")

    def test_resolved_entries_do_not_count_toward_triggers(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "a", 1)
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "b", 2)
        error_log.resolve(p, "RM6", 5)
        r = diagnostic_gate.evaluate(p, "S09", "RM6", False, False)
        self.assertFalse(r["fire"])  # both resolved — no live signal left

    def test_taxonomy_has_all_five_causes(self):
        p = self.subj()
        r = diagnostic_gate.evaluate(p, "S09", "RM6", True, False)
        self.assertEqual(set(r["taxonomy"]), {"slip", "missing_prerequisite", "misconception", "misapplied_procedure", "comprehension"})


class TestRemediationState(TmpDirCase):
    def rem(self, **extra):
        p = os.path.join(self.d, "subjects.json")
        base = {"schema_version": 4, "course_id": "x"}
        base.update(extra)
        _w(p, base)
        return p

    def test_attempt_1_is_reexplain(self):
        p = self.rem()
        r = remediation_state.record(p, "S09", "misconception", 100)
        self.assertEqual(r["action"], "same_framework_reexplain")
        self.assertEqual(r["attempts"], 1)

    def test_attempt_2_is_different_approach(self):
        p = self.rem()
        remediation_state.record(p, "S09", "misconception", 100)
        r = remediation_state.record(p, "S09", "misconception", 110)
        self.assertEqual(r["action"], "different_approach_and_check_earlier_stage")

    def test_attempt_3_escalates(self):
        p = self.rem()
        remediation_state.record(p, "S09", "misconception", 100)
        remediation_state.record(p, "S09", "misconception", 110)
        r = remediation_state.record(p, "S09", "misconception", 120)
        self.assertEqual(r["action"], "escalate")
        self.assertTrue(r["escalated"])

    def test_never_a_fourth_system_driven_loop(self):
        p = self.rem()
        for slot in (100, 110, 120, 130, 140):
            r = remediation_state.record(p, "S09", "misconception", slot)
        self.assertEqual(r["action"], "already_escalated")
        self.assertEqual(_r(p)["remediation"]["S09"]["attempts"], 3)  # frozen at 3, never counts past escalation

    def test_reset_clears_counter_for_a_future_struggle(self):
        p = self.rem()
        remediation_state.record(p, "S09", "misconception", 100)
        remediation_state.record(p, "S09", "misconception", 110)
        remediation_state.reset(p, "S09")
        r = remediation_state.record(p, "S09", "slip", 200)
        self.assertEqual(r["action"], "same_framework_reexplain")  # back to attempt 1, unrelated later struggle

    def test_stages_are_independent(self):
        p = self.rem()
        remediation_state.record(p, "S09", "misconception", 100)
        remediation_state.record(p, "S09", "misconception", 110)
        remediation_state.record(p, "S09", "misconception", 120)  # S09 now escalated
        r = remediation_state.record(p, "S10", "slip", 130)
        self.assertEqual(r["action"], "same_framework_reexplain")  # S10 untouched by S09's cap

    def test_status_on_untouched_stage(self):
        p = self.rem()
        r = remediation_state.status(p, "S09")
        self.assertEqual(r["attempts"], 0)
        self.assertFalse(r["escalated"])


class TestConfidenceUpdate(unittest.TestCase):
    def test_pass_clean_increases(self):
        r = confidence_update.compute(0.5, "pass_clean")
        self.assertGreater(r["new_confidence"], 0.5)

    def test_fail_decreases(self):
        r = confidence_update.compute(0.5, "fail")
        self.assertLess(r["new_confidence"], 0.5)

    def test_pass_clean_beats_pass_remediated(self):
        clean = confidence_update.compute(0.5, "pass_clean")["new_confidence"]
        remediated = confidence_update.compute(0.5, "pass_remediated")["new_confidence"]
        self.assertGreater(clean, remediated)

    def test_never_exceeds_one(self):
        r = confidence_update.compute(0.999, "pass_clean")
        self.assertLessEqual(r["new_confidence"], 1.0)

    def test_never_goes_below_zero(self):
        r = confidence_update.compute(0.001, "fail", misconception=True)
        self.assertGreaterEqual(r["new_confidence"], 0.0)

    def test_misconception_flag_costs_more_than_plain_fail(self):
        plain = confidence_update.compute(0.5, "fail")["new_confidence"]
        with_misc = confidence_update.compute(0.5, "fail", misconception=True)["new_confidence"]
        self.assertLess(with_misc, plain)

    def test_delta_shrinks_near_ceiling(self):
        low = confidence_update.compute(0.2, "pass_clean")
        high = confidence_update.compute(0.9, "pass_clean")
        low_gain = low["new_confidence"] - 0.2
        high_gain = high["new_confidence"] - 0.9
        self.assertGreater(low_gain, high_gain)

    def test_unknown_event_rejected(self):
        with self.assertRaises(ValueError):
            confidence_update.compute(0.5, "pass_with_flying_colours")

    def test_out_of_range_input_is_clamped_not_rejected(self):
        r = confidence_update.compute(1.5, "fail")
        self.assertLessEqual(r["old_confidence"], 1.0)


class TestSubjectMigrationV140(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def test_adds_three_fields_and_bumps_version(self):
        subj = os.path.join(self.d, "subjects.json")
        course = os.path.join(self.d, "course.json")
        _w(subj, {"schema_version": 3, "syllabus_status": {}, "cohort_id": 2, "notices_acknowledged": []})
        _w(course, {"schema_version": 4, "academic_level": 2, "standalone": False})
        result = migrate_schema.migrate_subject(subj, course)
        self.assertTrue(result["wrote"])
        d = _r(subj)
        self.assertEqual(d["error_patterns"], [])
        self.assertEqual(d["confidence"], 0.5)
        self.assertEqual(d["remediation"], {})
        self.assertEqual(d["schema_version"], 4)

    def test_idempotent_second_run_writes_nothing(self):
        subj = os.path.join(self.d, "subjects.json")
        course = os.path.join(self.d, "course.json")
        _w(subj, {"schema_version": 3, "syllabus_status": {}, "cohort_id": 2, "notices_acknowledged": []})
        _w(course, {"schema_version": 4, "academic_level": 2, "standalone": False})
        migrate_schema.migrate_subject(subj, course)
        result2 = migrate_schema.migrate_subject(subj, course)
        self.assertFalse(result2["wrote"])
        self.assertEqual(result2["changed_fields"], [])

    def test_does_not_overwrite_existing_confidence(self):
        subj = os.path.join(self.d, "subjects.json")
        course = os.path.join(self.d, "course.json")
        _w(subj, {"schema_version": 3, "confidence": 0.83, "syllabus_status": {}, "cohort_id": 2, "notices_acknowledged": []})
        _w(course, {"schema_version": 4, "academic_level": 2, "standalone": False})
        migrate_schema.migrate_subject(subj, course)
        self.assertEqual(_r(subj)["confidence"], 0.83)


class TestValidateStructureMisconceptions(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        _w(os.path.join(self.d, "course.json"), {"stage_ladder": ["S1"]})
        os.makedirs(os.path.join(self.d, "stages", "S1"))
        for kind in ("lesson.md", "practice.md", "test.md"):
            open(os.path.join(self.d, "stages", "S1", kind), "w").close()
        _w(os.path.join(self.d, "rubric.json"), {"stage_rubrics": {"S1": {"source": "x"}}})

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def test_absent_is_reported_but_non_blocking(self):
        r = validate_structure.validate(self.d)
        self.assertTrue(r["clean"])  # absence of misconceptions.json never fails validation
        self.assertFalse(r["misconceptions_status"]["per_stage"]["S1"]["present"])

    def test_well_formed_file_reported(self):
        _w(os.path.join(self.d, "stages", "S1", "misconceptions.json"),
           [{"pattern": "p", "correction": "c", "source": "plausible, not board-documented"}])
        r = validate_structure.validate(self.d)
        self.assertTrue(r["misconceptions_status"]["per_stage"]["S1"]["well_formed"])
        self.assertEqual(r["misconceptions_status"]["per_stage"]["S1"]["entry_count"], 1)

    def test_malformed_entry_flagged_but_still_non_blocking(self):
        _w(os.path.join(self.d, "stages", "S1", "misconceptions.json"), [{"pattern": "p"}])  # missing correction/source
        r = validate_structure.validate(self.d)
        self.assertTrue(r["clean"])
        self.assertFalse(r["misconceptions_status"]["per_stage"]["S1"]["well_formed"])
        self.assertEqual(r["misconceptions_status"]["per_stage"]["S1"]["malformed_entry_indices"], [0])


if __name__ == "__main__":
    unittest.main()
