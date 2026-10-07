"""
Tests for the 1.5.0 mastery layer: item_mastery.py, error_log.py's
rubric_criterion tagging + automatic item_mastery feed, migrate_schema.py's
4->5 subjects.json migration, and postcompile_gate.py. Stdlib only.

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

import diagnostic_gate  # noqa: E402
import error_log  # noqa: E402
import item_mastery  # noqa: E402
import migrate_schema  # noqa: E402
import postcompile_gate  # noqa: E402


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
        base = {"schema_version": 5, "course_id": "x", "error_patterns": [], "item_mastery": {}}
        base.update(extra)
        _w(p, base)
        return p


class TestItemMastery(TmpDirCase):
    def test_first_observation_uses_prior(self):
        p = self.subj()
        r = item_mastery.observe(p, "RM6", False, 100)
        self.assertEqual(r["prior"], item_mastery.P_INIT)
        self.assertEqual(r["observations"], 1)
        self.assertEqual(_r(p)["item_mastery"]["RM6"]["p_mastery"], r["new_p_mastery"])

    def test_incorrect_then_correct_sequence_matches_manual_verification(self):
        # Same sequence manually verified during development: false, true, true
        # -> priors 0.3 -> 0.1932 -> 0.5909 -> 0.8867 (rounded to 4dp).
        p = self.subj()
        r1 = item_mastery.observe(p, "RM6", False, 100)
        self.assertAlmostEqual(r1["new_p_mastery"], 0.1932, places=4)
        r2 = item_mastery.observe(p, "RM6", True, 110)
        self.assertAlmostEqual(r2["new_p_mastery"], 0.5909, places=4)
        r3 = item_mastery.observe(p, "RM6", True, 120)
        self.assertAlmostEqual(r3["new_p_mastery"], 0.8867, places=4)
        self.assertEqual(r3["observations"], 3)

    def test_mastery_climbs_monotonically_on_repeated_correct(self):
        # Bounded at 1.0, so only asserted while still below the ceiling —
        # it does saturate after enough correct observations (by design).
        p = self.subj()
        prev = item_mastery.P_INIT
        for slot in range(100, 108):
            r = item_mastery.observe(p, "RM6", True, slot)
            if prev < 1.0:
                self.assertGreaterEqual(r["new_p_mastery"], prev)
            prev = r["new_p_mastery"]

    def test_status_unobserved_item_returns_prior_only(self):
        p = self.subj()
        r = item_mastery.status(p, "RM9")
        self.assertEqual(r["mastery"]["p_mastery"], item_mastery.P_INIT)
        self.assertEqual(r["mastery"]["observations"], 0)

    def test_status_all_returns_every_observed_item(self):
        p = self.subj()
        item_mastery.observe(p, "RM6", True, 1)
        item_mastery.observe(p, "RM7", False, 2)
        r = item_mastery.status(p)
        self.assertEqual(r["count"], 2)
        self.assertIn("RM6", r["items"])
        self.assertIn("RM7", r["items"])

    def test_bounds_stay_within_zero_one(self):
        p = self.subj()
        r = None
        for slot in range(50):
            r = item_mastery.observe(p, "RM6", True, slot)
        self.assertLessEqual(r["new_p_mastery"], 1.0)
        self.assertGreaterEqual(r["new_p_mastery"], 0.0)


class TestErrorLogMasteryFeed(TmpDirCase):
    def test_append_feeds_item_mastery_as_incorrect(self):
        p = self.subj()
        result = error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "forgot to carry", 200, "M2")
        self.assertIn("item_mastery", result)
        self.assertEqual(result["item_mastery"]["item_id"], "RM6")
        self.assertLess(result["item_mastery"]["new_p_mastery"], item_mastery.P_INIT)
        self.assertEqual(_r(p)["item_mastery"]["RM6"]["last_correct"], False)

    def test_append_without_rubric_criterion_defaults_to_none(self):
        p = self.subj()
        result = error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "no criterion given", 200)
        self.assertIsNone(result["entry"]["rubric_criterion"])

    def test_append_rubric_criterion_stored_when_given(self):
        p = self.subj()
        result = error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "x", 200, "M2")
        self.assertEqual(result["entry"]["rubric_criterion"], "M2")

    def test_append_rubric_criterion_none_literal_normalizes_to_null(self):
        p = self.subj()
        result = error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "x", 200, "NONE")
        self.assertIsNone(result["entry"]["rubric_criterion"])

    def test_resolve_feeds_item_mastery_as_correct(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "x", 100)
        prior_mastery = _r(p)["item_mastery"]["RM6"]["p_mastery"]
        result = error_log.resolve(p, "RM6", 110)
        self.assertIsNotNone(result["item_mastery"])
        self.assertGreater(result["item_mastery"]["new_p_mastery"], prior_mastery)
        self.assertEqual(_r(p)["item_mastery"]["RM6"]["last_correct"], True)

    def test_resolve_with_nothing_to_resolve_has_no_mastery_call(self):
        p = self.subj()
        result = error_log.resolve(p, "RM_never_logged", 110)
        self.assertEqual(result["count"], 0)
        self.assertIsNone(result["item_mastery"])


class TestDiagnosticGateMasterySurfacing(TmpDirCase):
    def test_unobserved_item_reports_null_mastery(self):
        p = self.subj()
        r = diagnostic_gate.evaluate(p, "S09", "RM9", False, False)
        self.assertIsNone(r["item_mastery"])

    def test_observed_item_surfaces_mastery_without_forcing_a_fire(self):
        p = self.subj()
        item_mastery.observe(p, "RM6", False, 1)
        r = diagnostic_gate.evaluate(p, "S09", "RM6", False, False)
        self.assertIsNotNone(r["item_mastery"])
        self.assertEqual(r["item_mastery"]["observations"], 1)
        self.assertFalse(r["fire"])  # a single low-mastery observation is not itself a trigger

    def test_mastery_surfacing_never_overrides_a_real_trigger(self):
        p = self.subj()
        error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "a", 1)
        r = error_log.append(p, "S09", "RM6", "practice", "slip", "NONE", "b", 2)
        self.assertTrue(r["recurring"])
        gate = diagnostic_gate.evaluate(p, "S09", "RM6", False, False)
        self.assertTrue(gate["fire"])
        self.assertIsNotNone(gate["item_mastery"])


class TestMigrateSchemaItemMastery(TmpDirCase):
    def _course(self):
        p = os.path.join(self.d, "course.json")
        _w(p, {"schema_version": 4, "standalone": True})
        return p

    def test_item_mastery_added_when_absent(self):
        subj = os.path.join(self.d, "subjects.json")
        _w(subj, {"schema_version": 4, "course_id": "x"})
        course = self._course()
        result = migrate_schema.migrate_subject(subj, course)
        d = _r(subj)
        self.assertEqual(d["item_mastery"], {})
        self.assertEqual(d["schema_version"], migrate_schema.SUBJECT_SCHEMA_VERSION)
        self.assertIn("item_mastery: added as {}", result["changed_fields"])

    def test_item_mastery_not_overwritten_if_present(self):
        subj = os.path.join(self.d, "subjects.json")
        existing = {"RM6": {"p_mastery": 0.7, "observations": 2, "last_slot": 5, "last_correct": True}}
        _w(subj, {"schema_version": 4, "course_id": "x", "item_mastery": existing})
        course = self._course()
        migrate_schema.migrate_subject(subj, course)
        self.assertEqual(_r(subj)["item_mastery"], existing)

    def test_idempotent_second_run_writes_nothing(self):
        subj = os.path.join(self.d, "subjects.json")
        _w(subj, {"schema_version": 4, "course_id": "x"})
        course = self._course()
        migrate_schema.migrate_subject(subj, course)
        result2 = migrate_schema.migrate_subject(subj, course)
        self.assertFalse(result2["wrote"])


class TestPostcompileGate(TmpDirCase):
    def _course_dir(self):
        cd = os.path.join(self.d, "course")
        os.makedirs(os.path.join(cd, "stages", "S1"))
        _w(os.path.join(cd, "course.json"), {"stage_ladder": ["S1"]})
        for kind in ("lesson.md", "practice.md", "test.md"):
            with open(os.path.join(cd, "stages", "S1", kind), "w") as f:
                f.write("content mentioning nothing in particular")
        _w(os.path.join(cd, "rubric.json"), {"stage_rubrics": {"S1": {"source": "AQA specimen paper 2024"}}})
        return cd

    def test_clean_course_can_ship(self):
        cd = self._course_dir()
        result = postcompile_gate.check(cd)
        self.assertTrue(result["can_ship"])
        self.assertEqual(result["blocking_reasons"], [])

    def test_missing_stage_file_blocks(self):
        cd = self._course_dir()
        os.remove(os.path.join(cd, "stages", "S1", "test.md"))
        result = postcompile_gate.check(cd)
        self.assertFalse(result["can_ship"])
        self.assertTrue(any("missing stage files" in r for r in result["blocking_reasons"]))

    def test_missing_rubric_entry_blocks(self):
        cd = self._course_dir()
        _w(os.path.join(cd, "rubric.json"), {"stage_rubrics": {}})
        result = postcompile_gate.check(cd)
        self.assertFalse(result["can_ship"])
        self.assertTrue(any("no rubric.json entry" in r for r in result["blocking_reasons"]))

    def test_empty_source_blocks(self):
        cd = self._course_dir()
        _w(os.path.join(cd, "rubric.json"), {"stage_rubrics": {"S1": {"source": ""}}})
        result = postcompile_gate.check(cd)
        self.assertFalse(result["can_ship"])
        self.assertTrue(any("empty source citation" in r for r in result["blocking_reasons"]))

    def test_coverage_not_full_is_advisory_not_blocking(self):
        cd = self._course_dir()
        # no curriculum_map.json at all -> coverage computed_status "unverified"
        result = postcompile_gate.check(cd)
        self.assertTrue(result["can_ship"])
        self.assertTrue(any("coverage is" in n for n in result["advisory_notes"]))

    def test_orphaned_stage_dir_is_advisory_not_blocking(self):
        cd = self._course_dir()
        os.makedirs(os.path.join(cd, "stages", "S2_orphan"))
        result = postcompile_gate.check(cd)
        self.assertTrue(result["can_ship"])
        self.assertTrue(any("orphaned stage dirs" in n for n in result["advisory_notes"]))

    def test_override_forces_can_ship_true_and_records_reason(self):
        cd = self._course_dir()
        os.remove(os.path.join(cd, "stages", "S1", "test.md"))
        blocked = postcompile_gate.check(cd)
        self.assertFalse(blocked["can_ship"])
        overridden = postcompile_gate.override(cd, "source still being tracked down, learner informed")
        self.assertTrue(overridden["can_ship"])
        self.assertTrue(overridden["overridden"])
        self.assertEqual(overridden["override_reason"], "source still being tracked down, learner informed")
        # the underlying problem is still visible, not erased by the override
        self.assertTrue(any("missing stage files" in r for r in overridden["blocking_reasons"]))


if __name__ == "__main__":
    unittest.main()
