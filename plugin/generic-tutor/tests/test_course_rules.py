"""
Tests for the 1.3.0 rules: standalone courses, list prerequisites, practical units by declaration,
learner notices, level_basis, and the course.json 3->4 / subjects 2->3 migration. Stdlib only.

    python3 -m unittest discover tests -v
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

import apply_capabilities  # noqa: E402
import cohort_status  # noqa: E402
import gate_check  # noqa: E402
import migrate_schema  # noqa: E402
import prereq_check  # noqa: E402
import roster_check  # noqa: E402
import validate_structure  # noqa: E402

TODAY = "2026-09-26"


def _w(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


def _r(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


class Lib:
    """A throwaway learner + course library."""

    def __init__(self, tmp, cap=4, cleared=0, caps=None):
        self.profile = os.path.join(tmp, "profile")
        self.subjects = os.path.join(self.profile, "subjects")
        self.courses = os.path.join(tmp, "courses")
        os.makedirs(self.subjects)
        os.makedirs(self.courses)
        self.pfile = os.path.join(self.profile, "student_profile.json")
        prof = {"roster": {"max_incomplete_courses": cap}, "highest_level_cleared": cleared}
        if caps is not None:
            prof["capabilities"] = caps
        _w(self.pfile, prof)

    def course(self, cid, stages=3, level=2, standalone=False, requires=None, practical=None,
               notices=None, exam=False, cmap=None):
        d = {
            "schema_version": 4, "stage_ladder": [f"S{i}" for i in range(stages)],
            "academic_level": None if standalone else level, "standalone": standalone,
            "level_basis": "standalone" if standalone else "framework", "level_source": "x",
            "grounding_status": "verified", "exam": {"enabled": exam},
            "folder_access": {"status": "isolated_confirmed"}, "currency": "live",
            "last_live_recheck": TODAY, "requires_complete": requires if requires is not None else [],
            "practical_stages": practical or {}, "learner_notices": notices or [],
        }
        _w(self.cpath(cid), d)
        if cmap is not None:
            _w(os.path.join(self.courses, cid, "curriculum_map.json"), cmap)
        return d

    def enrol(self, cid, state="active", passed=0, stages=3, cohort=2, status=None, current="S0", acked=None):
        ss = {f"S{i}": ("pass" if i < passed else "unsat") for i in range(stages)}
        if status:
            ss.update(status)
        _w(self.spath(cid), {
            "course_id": cid, "roster_state": state, "cohort_id": cohort, "current_stage": current,
            "syllabus_status": ss, "exam_status": "locked", "notices_acknowledged": acked or []})

    def spath(self, cid):
        return os.path.join(self.subjects, f"{cid}.json")

    def cpath(self, cid):
        return os.path.join(self.courses, cid, "course.json")

    def gate(self, cid):
        sp = self.spath(cid) if os.path.exists(self.spath(cid)) else "NONE"
        return gate_check.evaluate(self.cpath(cid), sp, self.subjects, self.courses, TODAY)


class Case(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.tmp = self._td.name
        self.addCleanup(self._td.cleanup)
        self.L = Lib(self.tmp)


# ---------------------------------------------------------------- standalone

class StandaloneTests(Case):
    def test_standalone_candidate_joins_freely_even_below_the_floor(self):
        L = self.L
        L.course("gcse"); L.enrol("gcse", cohort=2)
        L.course("alevel", level=3); L.enrol("alevel", cohort=3)
        r = roster_check.compute(L.profile, L.courses, "standalone")
        self.assertEqual((r["lock_consequence"], r["candidate_state"], r["courses_that_would_lock"]),
                         ("joins_freely", "active", []))

    def test_standalone_still_needs_a_roster_slot(self):
        L = Lib(os.path.join(self.tmp, "x"), cap=1)
        L.course("py", standalone=True); L.enrol("py", cohort=None)
        r = roster_check.compute(L.profile, L.courses, "standalone")
        self.assertEqual(r["roster_occupancy"], 1)
        self.assertFalse(r["can_add_course"])

    def test_enrolled_standalone_never_sets_the_floor(self):
        L = self.L
        L.course("sqe1", standalone=True); L.enrol("sqe1", cohort=6)  # stale numeric cohort on file
        L.course("gcse"); L.enrol("gcse", cohort=2)
        r = roster_check.compute(L.profile, L.courses)
        self.assertEqual(r["level_lock_floor"], 2)
        r3 = roster_check.compute(L.profile, L.courses, 3)
        self.assertEqual(r3["candidate_state"], "dormant")  # locked behind the GCSE, not behind sqe1

    def test_standalone_with_a_level_on_file_is_still_ignored_by_the_lock(self):
        L = self.L
        d = L.course("aat", standalone=True)
        d["academic_level"] = 3  # a data error the validator reports; the lock must still ignore it
        _w(L.cpath("aat"), d)
        L.enrol("aat")
        L.course("gcse", level=4); L.enrol("gcse", cohort=4)
        self.assertEqual(roster_check.compute(L.profile, L.courses)["level_lock_floor"], 4)

    def test_dormant_standalone_always_wakes(self):
        L = self.L
        L.course("py", standalone=True); L.enrol("py", state="dormant")
        L.course("gcse"); L.enrol("gcse", cohort=2)
        self.assertIn("py", roster_check.compute(L.profile, L.courses)["wake_now"])

    def test_standalone_is_its_own_cohort_and_never_clears_a_level(self):
        L = self.L
        L.course("py", standalone=True); L.enrol("py", passed=3, cohort=2)
        cohorts, _ = cohort_status.compute_cohorts(L.subjects, L.courses)
        self.assertIn("standalone:py", cohorts)
        self.assertNotIn("2", cohorts)
        walk = cohort_status.level_walk(cohorts, 0)
        self.assertEqual(walk["to"], 0)

    def test_standalone_tests_without_waiting_for_a_gcse(self):
        L = self.L
        L.course("py", standalone=True); L.enrol("py", state="test_pending_convergence", cohort=2)
        L.course("gcse"); L.enrol("gcse", cohort=2)
        g = L.gate("py")
        self.assertTrue(g["gates"]["5_phase_convergence"]["converged"])
        self.assertTrue(g["standalone"])


# ---------------------------------------------------------------- prerequisites

class PrerequisiteTests(Case):
    def test_normalise(self):
        n = cohort_status.normalise_prerequisites
        self.assertEqual(n(None), [])
        self.assertEqual(n("llb"), ["llb"])
        self.assertEqual(n(["a", ["b", "c"]]), ["a", ["b", "c"]])
        self.assertEqual(n(["a", [], 3]), ["a"])  # malformed entries dropped (validator reports them)

    def test_all_of_and_any_of(self):
        L = self.L
        for c in ("maths", "physics", "chem"):
            L.course(c, level=3)
        L.course("beng", level=6, requires=["maths", ["physics", "chem"]])
        L.enrol("maths", passed=3, cohort=3)
        r = prereq_check.check(L.cpath("beng"), L.subjects, L.courses)
        self.assertFalse(r["met"])
        self.assertEqual(r["unmet"], [["physics", "chem"]])
        L.enrol("chem", passed=3, cohort=3)
        self.assertTrue(prereq_check.check(L.cpath("beng"), L.subjects, L.courses)["met"])

    def test_unfinished_or_dropped_prerequisite_is_unmet(self):
        L = self.L
        L.course("llb", level=6); L.enrol("llb", passed=2, cohort=6)
        L.course("sqe1", standalone=True, requires=["llb"])
        self.assertEqual(prereq_check.check(L.cpath("sqe1"), L.subjects, L.courses)["unmet"], ["llb"])

    def test_missing_prerequisite_course_is_reported(self):
        L = self.L
        L.course("ppe", level=6, requires=["alevel_economics"])
        r = prereq_check.check(L.cpath("ppe"), L.subjects, L.courses)
        self.assertEqual(r["missing_courses"], ["alevel_economics"])
        self.assertFalse(r["met"])

    def test_pre_130_single_string_still_works(self):
        L = self.L
        L.course("llb", level=6); L.enrol("llb", passed=3, cohort=6)
        d = L.course("llm", level=7); d["requires_complete"] = "llb"; _w(L.cpath("llm"), d)
        self.assertTrue(prereq_check.check(L.cpath("llm"), L.subjects, L.courses)["met"])

    def test_gate_blocks_teaching_until_prerequisites_complete(self):
        L = self.L
        L.course("llb", level=6); L.enrol("llb", passed=2, cohort=6)
        L.course("sqe1", standalone=True, requires=["llb"]); L.enrol("sqe1")
        g = L.gate("sqe1")
        self.assertFalse(g["can_proceed"])
        self.assertEqual(g["first_blocking_gate"], "3_level_lock")
        L.enrol("llb", passed=3, cohort=6)
        self.assertTrue(L.gate("sqe1")["can_proceed"])

    def test_theory_only_completion_satisfies_a_prerequisite(self):
        L = self.L
        L.course("eng", practical={"S2": ["share_images"]})
        L.enrol("eng", passed=2, status={"S2": "withheld"})
        L.course("next", level=3, requires=["eng"])
        self.assertTrue(prereq_check.check(L.cpath("next"), L.subjects, L.courses)["met"])


# ---------------------------------------------------------------- practical by declaration

class PracticalTests(Case):
    def setUp(self):
        super().setUp()
        self.course = self.L.course("eng", stages=4, practical={"S2": ["share_images"], "S3": ["share_images"]},
                                    cmap={"_meta": {}, "S0": {"covers_items": ["1.1"]}, "S1": {"covers_items": ["1.2", "2.1"]},
                                          "S2": {"covers_items": ["2.1", "2.2"]}, "S3": {"covers_items": ["3.1"]}})

    def _apply(self, caps, status):
        subj = {"syllabus_status": status}
        return apply_capabilities.apply({"capabilities": caps}, self.course, subj)

    def test_without_the_capability_practical_stages_are_withheld(self):
        new, rep = self._apply({}, {"S0": "unsat", "S1": "unsat", "S2": "unsat", "S3": "fail"})
        self.assertEqual(new["syllabus_status"]["S2"], "withheld")
        self.assertEqual(new["syllabus_status"]["S3"], "withheld")
        self.assertEqual(new["syllabus_status"]["S0"], "unsat")  # theory stage untouched
        self.assertTrue(rep["theory_only"])

    def test_declaring_unlocks_and_reports_a_reopened_course(self):
        new, rep = self._apply({"share_images": {"declared": True, "on": TODAY}},
                               {"S0": "pass", "S1": "pass", "S2": "withheld", "S3": "withheld"})
        self.assertEqual(new["syllabus_status"]["S2"], "unsat")
        self.assertTrue(rep["reopens_completed_course"])
        self.assertFalse(rep["theory_only"])

    def test_withdrawing_never_erases_a_real_pass(self):
        new, rep = self._apply({"share_images": {"declared": False}},
                               {"S0": "pass", "S1": "pass", "S2": "pass", "S3": "unsat"})
        self.assertEqual(new["syllabus_status"]["S2"], "pass")
        self.assertEqual(new["syllabus_status"]["S3"], "withheld")

    def test_is_idempotent(self):
        new, _ = self._apply({}, {"S0": "unsat", "S1": "unsat", "S2": "unsat", "S3": "unsat"})
        again, rep = apply_capabilities.apply({}, self.course, new)
        self.assertEqual(rep["changed"], {})

    def test_withheld_counts_only_on_a_practical_stage(self):
        ok = {"syllabus_status": {"S0": "pass", "S1": "pass", "S2": "withheld", "S3": "withheld"}, "exam_status": "locked"}
        self.assertTrue(cohort_status.is_complete(self.course, ok))
        bad = {"syllabus_status": {"S0": "withheld", "S1": "pass", "S2": "pass", "S3": "pass"}, "exam_status": "locked"}
        self.assertFalse(cohort_status.is_complete(self.course, bad))

    def test_gate_reports_items_withheld_for_this_learner_only(self):
        L = self.L
        L.enrol("eng", stages=4, status={"S2": "withheld", "S3": "withheld"}, current="S1")
        p = L.gate("eng")["practical"]
        self.assertTrue(p["theory_only"])
        # 2.1 is also taught in S1, so it is NOT withheld; 2.2 and 3.1 are
        self.assertEqual(sorted(p["items_withheld_for_learner"]), ["2.2", "3.1"])

    def test_cli_dry_run_does_not_write(self):
        L = self.L
        L.enrol("eng", stages=4)
        before = _r(L.spath("eng"))
        out = subprocess.run([sys.executable, os.path.join(SCRIPTS, "apply_capabilities.py"), L.pfile,
                              L.cpath("eng"), L.spath("eng"), "--dry-run"], capture_output=True, text=True)
        rep = json.loads(out.stdout)
        self.assertTrue(rep["changed"])
        self.assertFalse(rep["wrote"])
        self.assertEqual(_r(L.spath("eng")), before)


# ---------------------------------------------------------------- notices

class NoticeTests(Case):
    def setUp(self):
        super().setUp()
        self.L.course("latin", stages=4, notices=[
            {"id": "settext-2028", "text": "Set texts change for 2028.", "stages": ["S2", "S3"], "since": TODAY},
            {"id": "all", "text": "Course-wide.", "stages": None, "since": TODAY},
            "a pre-1.3.0 plain string"])

    def test_stage_notice_only_on_its_stages(self):
        self.L.enrol("latin", stages=4, current="S0")
        self.assertEqual([n["id"] for n in self.L.gate("latin")["notices"]["due"]], ["all"])
        self.L.enrol("latin", stages=4, current="S2")
        self.assertEqual([n["id"] for n in self.L.gate("latin")["notices"]["due"]], ["settext-2028", "all"])

    def test_acknowledged_notice_is_not_repeated(self):
        self.L.enrol("latin", stages=4, current="S2", acked=[{"id": "settext-2028", "on": TODAY}])
        self.assertEqual([n["id"] for n in self.L.gate("latin")["notices"]["due"]], ["all"])


# ---------------------------------------------------------------- migration

class MigrationV4Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.path = os.path.join(self.tmp, "c", "course.json")

    def _v3(self, **kw):
        d = {"schema_version": 3, "academic_level": 2, "level_source": "RQF Level 2, Ofqual", "grounding_status": "verified",
             "last_live_recheck": None, "coverage_status": "full", "requires_complete": None, "stage_ladder": ["S1"]}
        d.update(kw)
        _w(self.path, d)

    def test_adds_fields_and_infers_framework(self):
        self._v3()
        r = migrate_schema.migrate_course(self.path)
        d = _r(self.path)
        self.assertEqual(d["schema_version"], 4)
        self.assertEqual((d["standalone"], d["requires_complete"], d["practical_stages"], d["learner_notices"], d["level_basis"]),
                         (False, [], {}, [], "framework"))
        self.assertTrue(r["wrote"])

    def test_single_prerequisite_becomes_a_list(self):
        self._v3(requires_complete="llb")
        migrate_schema.migrate_course(self.path)
        self.assertEqual(_r(self.path)["requires_complete"], ["llb"])

    def test_declared_level_is_labelled_declared(self):
        self._v3(academic_level=6, level_source="declared, no external framework")
        migrate_schema.migrate_course(self.path)
        self.assertEqual(_r(self.path)["level_basis"], "declared")

    def test_unclear_level_basis_is_left_null_and_reported(self):
        self._v3(academic_level=None, level_source=None)
        r = migrate_schema.migrate_course(self.path)
        self.assertIsNone(_r(self.path)["level_basis"])
        self.assertTrue(any(x.startswith("level_basis") for x in r["needs_sourcing"]))

    def test_plain_string_notices_are_converted_and_flagged(self):
        self._v3(learner_notices=["Set texts change for 2028."])
        r = migrate_schema.migrate_course(self.path)
        n = _r(self.path)["learner_notices"]
        self.assertEqual(n, [{"id": "n1", "text": "Set texts change for 2028.", "stages": None, "since": None}])
        self.assertTrue(any(x.startswith("learner_notices") for x in r["needs_sourcing"]))

    def test_never_makes_a_course_standalone(self):
        self._v3(academic_level=None, level_source=None)
        migrate_schema.migrate_course(self.path)
        self.assertFalse(_r(self.path)["standalone"])

    def test_standalone_course_is_not_flagged_for_a_level(self):
        self._v3(academic_level=None, level_source=None, standalone=True)
        r = migrate_schema.migrate_course(self.path)
        self.assertEqual(_r(self.path)["level_basis"], "standalone")
        self.assertNotIn("academic_level", r["needs_sourcing"])
        self.assertNotIn("level_source", r["needs_sourcing"])

    def test_second_run_is_a_no_op(self):
        self._v3(requires_complete="llb", learner_notices=["x"])
        migrate_schema.migrate_course(self.path)
        again = migrate_schema.migrate_course(self.path)
        self.assertFalse(again["wrote"])
        self.assertEqual(again["changed_fields"], [])

    def test_subject_gets_acknowledgements_and_standalone_cohort(self):
        self._v3(academic_level=None, standalone=True)
        spath = os.path.join(self.tmp, "subjects", "c.json")
        _w(spath, {"schema_version": 2, "course_id": "c", "cohort_id": 6, "syllabus_status": {"S1": "unsat"}})
        migrate_schema.migrate_subject(spath, self.path)
        s = _r(spath)
        self.assertEqual(
            (s["schema_version"], s["cohort_id"], s["notices_acknowledged"]),
            (migrate_schema.SUBJECT_SCHEMA_VERSION, "standalone:c", []),
        )  # pinned to the constant, not a literal, since 1.4.0 (test_adaptive_layer.py owns the current-version behavior)
        self.assertFalse(migrate_schema.migrate_subject(spath, self.path)["wrote"])


# ---------------------------------------------------------------- validator

class ValidatorV13Tests(Case):
    def _stage_files(self, cid, n):
        for i in range(n):
            for k in ("lesson.md", "practice.md", "test.md"):
                p = os.path.join(self.L.courses, cid, "stages", f"S{i}", k)
                os.makedirs(os.path.dirname(p), exist_ok=True)
                open(p, "w").close()
        _w(os.path.join(self.L.courses, cid, "rubric.json"), {"stages": {f"S{i}": {"source": "x"} for i in range(n)}})

    def test_clean_course_passes(self):
        self.L.course("a", practical={"S1": ["share_images"]}, notices=[{"id": "x", "text": "y", "stages": ["S0"]}])
        self._stage_files("a", 3)
        r = validate_structure.validate(os.path.join(self.L.courses, "a"))
        self.assertEqual(r["v13_problems"], {})
        self.assertTrue(r["clean"])

    def test_problems_are_reported(self):
        d = self.L.course("a", standalone=True, practical={"S9": ["share_images"]},
                          notices=[{"id": "x", "text": "y", "stages": ["S7"]}, {"id": "x", "text": "z"}, "plain"],
                          requires=["nope", ["also_nope"]])
        d["academic_level"] = 3; d["level_basis"] = "declared"; _w(self.L.cpath("a"), d)
        self._stage_files("a", 3)
        r = validate_structure.validate(os.path.join(self.L.courses, "a"))
        p = r["v13_problems"]
        for key in ("practical_stages_not_in_ladder", "learner_notices_malformed", "learner_notices_duplicate_ids",
                    "learner_notices_bad_stages", "standalone_has_academic_level", "standalone_level_basis_mismatch",
                    "missing_prerequisite_courses"):
            self.assertIn(key, p, key)
        self.assertFalse(r["clean"])


if __name__ == "__main__":
    unittest.main()
