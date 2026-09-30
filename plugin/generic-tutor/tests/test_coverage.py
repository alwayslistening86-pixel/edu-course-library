"""
Tests for the 1.2.0 syllabus-coverage layer: coverage_check.py, gate_check's non-blocking coverage block,
and migrate_schema's course schema 3. Stdlib only; fixtures are built in temp dirs.

Run from the plugin root:  python3 -m unittest discover tests -v
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

import coverage_check  # noqa: E402
import gate_check  # noqa: E402
import migrate_schema  # noqa: E402


def _w(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        if isinstance(obj, str):
            f.write(obj)
        else:
            json.dump(obj, f)


def _r(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


ITEMS = [
    {"id": "1.01a", "title": "add and subtract integers", "topic_area": "Number"},
    {"id": "1.01b", "title": "multiply integers", "topic_area": "Number"},
    {"id": "2.01", "title": "solve linear equations", "topic_area": "Algebra"},
]
SRC = {"document": "Test Spec J000", "url": "https://example.org/spec.pdf", "version": "1.0", "itemised_on": "2026-09-19"}


class CourseCase(unittest.TestCase):
    """A two-stage course: S1 teaches 1.01a + 1.01b, S2 teaches 2.01. Override pieces per test."""

    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.cdir = os.path.join(self.tmp, "courses", "maths")
        self.cpath = os.path.join(self.cdir, "course.json")
        self.build()

    def build(self, cmap=None, lessons=None, course_extra=None):
        course = {"schema_version": 3, "stage_ladder": ["S1", "S2"], "folder_access": {"status": "isolated_confirmed"},
                  "currency": "historical", "grounding_status": "verified", "coverage_status": "full"}
        course.update(course_extra or {})
        _w(self.cpath, course)
        base = {
            "_meta": {"purpose": "x"}, "_items_source": SRC, "_syllabus_items": ITEMS,
            "S1": {"covers_syllabus_refs": ["Number"], "syllabus_topic": "Number", "covers_items": ["1.01a", "1.01b"]},
            "S2": {"covers_syllabus_refs": ["Algebra"], "syllabus_topic": "Algebra", "covers_items": ["2.01"]},
        }
        if cmap is not None:
            base = cmap
        _w(os.path.join(self.cdir, "curriculum_map.json"), base)
        ls = {"S1": "# S1\n## Syllabus items taught here\n- 1.01a add\n- 1.01b multiply\n",
              "S2": "# S2\n## Syllabus items taught here\n- 2.01 equations\n"}
        ls.update(lessons or {})
        for st, txt in ls.items():
            _w(os.path.join(self.cdir, "stages", st, "lesson.md"), txt)

    def cmap(self):
        return _r(os.path.join(self.cdir, "curriculum_map.json"))

    def check(self):
        return coverage_check.check(self.cdir)


class CoverageCheckTests(CourseCase):
    def test_fully_mapped_and_named_is_full(self):
        r = self.check()
        self.assertEqual(r["computed_status"], "full")
        self.assertTrue(r["clean"])
        self.assertEqual((r["items_total"], r["items_taught"], r["uncovered_items"]), (3, 3, []))
        self.assertFalse(r["status_mismatch"])

    def test_unitemised_course_is_unverified_not_full(self):
        cm = self.cmap()
        for k in ("_syllabus_items", "_items_source"):
            cm.pop(k)
        self.build(cmap=cm)
        r = self.check()
        self.assertEqual(r["computed_status"], "unverified")
        self.assertFalse(r["items_declared"])
        self.assertTrue(r["status_mismatch"])  # stored "full" is not supportable

    def test_old_style_map_with_only_refs_is_unverified(self):
        self.build(cmap={"S1": {"covers_syllabus_refs": ["Number"], "syllabus_topic": "Number"},
                         "S2": {"covers_syllabus_refs": ["Algebra"], "syllabus_topic": "Algebra"}})
        self.assertEqual(self.check()["computed_status"], "unverified")

    def test_an_item_no_stage_teaches_is_partial_and_listed(self):
        cm = self.cmap()
        cm["S1"]["covers_items"] = ["1.01a"]
        self.build(cmap=cm)
        r = self.check()
        self.assertEqual(r["computed_status"], "partial")
        self.assertEqual(r["uncovered_items"], ["1.01b"])
        self.assertEqual(r["items_taught"], 2)

    def test_declared_exclusion_with_reason_counts_as_handled(self):
        cm = self.cmap()
        cm["S1"]["covers_items"] = ["1.01a"]
        cm["_declared_exclusions"] = [{"id": "1.01b", "reason": "higher tier only; course is foundation"}]
        self.build(cmap=cm)
        r = self.check()
        self.assertEqual(r["computed_status"], "full")
        self.assertEqual(r["items_excluded"], 1)

    def test_exclusion_without_a_reason_does_not_count(self):
        cm = self.cmap()
        cm["S1"]["covers_items"] = ["1.01a"]
        cm["_declared_exclusions"] = [{"id": "1.01b", "reason": "  "}]
        self.build(cmap=cm)
        r = self.check()
        self.assertEqual(r["computed_status"], "partial")
        self.assertIn("1.01b", r["problems"]["exclusions_without_reason"])
        self.assertEqual(r["uncovered_items"], ["1.01b"])

    def test_exclusion_of_an_unknown_item_is_a_problem(self):
        cm = self.cmap()
        cm["_declared_exclusions"] = [{"id": "9.99", "reason": "whatever"}]
        self.build(cmap=cm)
        self.assertIn("9.99", self.check()["problems"]["exclusions_of_unknown_item"])

    def test_stage_claiming_an_unknown_item_id_is_flagged(self):
        cm = self.cmap()
        cm["S2"]["covers_items"] = ["2.01", "2.99"]
        self.build(cmap=cm)
        r = self.check()
        self.assertEqual(r["problems"]["unknown_item_refs"], {"S2": ["2.99"]})
        self.assertEqual(r["computed_status"], "partial")

    def test_a_map_cannot_claim_what_the_lesson_never_names(self):
        self.build(lessons={"S2": "# S2\nAlgebra, but the item id is never written down.\n"})
        r = self.check()
        self.assertEqual(r["problems"]["claimed_but_not_in_lesson"], {"S2": ["2.01"]})
        self.assertEqual(r["uncovered_items"], ["2.01"])  # not counted as taught
        self.assertEqual(r["computed_status"], "partial")

    def test_missing_lesson_file_counts_as_not_named(self):
        os.remove(os.path.join(self.cdir, "stages", "S2", "lesson.md"))
        self.assertEqual(self.check()["computed_status"], "partial")

    def test_id_match_is_whole_token(self):
        # '1.01' must not be satisfied by '1.01a', nor '1.01a' by '1.01ab'/'1.01a.2'
        self.assertTrue(coverage_check._id_in_text("1.01a", "see 1.01a."))
        self.assertTrue(coverage_check._id_in_text("1.01a", "- 1.01A add"))
        self.assertFalse(coverage_check._id_in_text("1.01", "covers 1.01a and 1.01b"))
        self.assertFalse(coverage_check._id_in_text("1.01a", "covers 1.01ab"))
        self.assertFalse(coverage_check._id_in_text("1.01", "covers 1.01.2"))
        self.assertTrue(coverage_check._id_in_text("1.01", "covers 1.01, and more"))

    def test_item_taught_by_two_stages_is_reported_not_penalised(self):
        cm = self.cmap()
        cm["S2"]["covers_items"] = ["2.01", "1.01a"]
        self.build(cmap=cm, lessons={"S2": "# S2\n2.01 and revisit 1.01a\n"})
        r = self.check()
        self.assertEqual(r["computed_status"], "full")
        self.assertEqual(r["items_in_multiple_stages"], {"1.01a": ["S1", "S2"]})

    def test_stage_with_no_covers_items_blocks_full(self):
        cm = self.cmap()
        del cm["S2"]["covers_items"]
        self.build(cmap=cm)
        r = self.check()
        self.assertEqual(r["problems"]["stages_without_covers_items"], ["S2"])
        self.assertEqual(r["computed_status"], "partial")

    def test_duplicate_or_incomplete_items_are_flagged(self):
        cm = self.cmap()
        cm["_syllabus_items"] = ITEMS + [{"id": "2.01", "title": "dup"}, {"id": "3.01"}]
        self.build(cmap=cm)
        r = self.check()
        self.assertEqual(r["problems"]["duplicate_item_ids"], ["2.01"])
        self.assertEqual(r["problems"]["items_missing_id_or_title"], 1)
        self.assertEqual(r["computed_status"], "partial")

    def test_missing_provenance_blocks_full(self):
        cm = self.cmap()
        del cm["_items_source"]
        self.build(cmap=cm)
        r = self.check()
        self.assertIn("items_source_missing", r["problems"])
        self.assertEqual(r["computed_status"], "partial")

    def test_underscore_keys_are_never_treated_as_stages(self):
        r = self.check()
        self.assertEqual(r["stage_ladder_length"], 2)
        self.assertNotIn("_meta", r["lesson_words_per_stage"])

    def test_unreadable_map_is_unverified_not_a_crash(self):
        _w(os.path.join(self.cdir, "curriculum_map.json"), "{not json")
        self.assertEqual(self.check()["computed_status"], "unverified")

    def test_unreadable_course_reports_an_error(self):
        _w(self.cpath, "{nope")
        self.assertIn("error", self.check())

    def test_lesson_word_counts_are_reported_but_never_judged(self):
        r = self.check()
        self.assertGreater(r["lesson_words_per_stage"]["S1"], 0)
        self.assertEqual(r["computed_status"], "full")  # a short lesson is not, by itself, a problem

    def test_status_mismatch_flags_a_stale_full(self):
        cm = self.cmap()
        cm["_syllabus_items"] = ITEMS + [{"id": "3.01", "title": "new item added by a spec revision"}]
        self.build(cmap=cm)  # stored coverage_status is still "full"
        r = self.check()
        self.assertEqual(r["computed_status"], "partial")
        self.assertTrue(r["status_mismatch"])

    def test_cli_prints_json(self):
        import subprocess
        out = subprocess.run([sys.executable, os.path.join(SCRIPTS, "coverage_check.py"), self.cdir],
                             capture_output=True, text=True, check=True).stdout
        self.assertEqual(json.loads(out)["computed_status"], "full")


class GateCheckCoverageBlockTests(CourseCase):
    def gate(self):
        subj_dir = os.path.join(self.tmp, "profile", "u", "subjects")
        os.makedirs(subj_dir, exist_ok=True)
        return gate_check.evaluate(self.cpath, "NONE", subj_dir, os.path.join(self.tmp, "courses"), "2026-09-19")

    def test_full_and_full_means_no_disclosure(self):
        g = self.gate()
        self.assertTrue(g["can_proceed"])
        self.assertEqual(g["coverage"]["effective_status"], "full")
        self.assertEqual(g["coverage"]["items_excluded"], 0)
        self.assertFalse(g["coverage"]["disclose_to_learner"])

    def test_full_with_declared_exclusions_still_discloses(self):
        # v1.11.0 fix: 'full' only because some items were declared out of scope (e.g. an
        # unselected exam-board option) must still tell the learner something was left out --
        # this was the exact gap a real course (174/298 items taught, 124 excluded, computed
        # 'full') fell into before this fix, with disclose_to_learner silently False.
        cm = self.cmap()
        cm["S1"]["covers_items"] = ["1.01a"]
        cm["_declared_exclusions"] = [{"id": "1.01b", "reason": "higher tier only; course is foundation"}]
        self.build(cmap=cm)
        c = self.gate()["coverage"]
        self.assertEqual(c["effective_status"], "full")
        self.assertEqual(c["items_excluded"], 1)
        self.assertTrue(c["disclose_to_learner"])
        self.assertIn("out of scope", c["detail"])
        self.assertEqual(c["excluded_items"], {"1.01b": "higher tier only; course is foundation"})

    def test_unitemised_v2_course_must_be_disclosed_but_stays_teachable(self):
        _w(self.cpath, {"schema_version": 2, "stage_ladder": ["S1", "S2"], "folder_access": {"status": "isolated_confirmed"},
                        "currency": "historical", "grounding_status": "verified"})
        _w(os.path.join(self.cdir, "curriculum_map.json"), {"S1": {"covers_syllabus_refs": ["x"]}})
        g = self.gate()
        self.assertTrue(g["can_proceed"], "coverage is disclosure, not a gate")
        self.assertEqual(g["coverage"]["effective_status"], "unverified")
        self.assertTrue(g["coverage"]["disclose_to_learner"])
        self.assertIsNone(g["coverage"]["declared_status"])

    def test_a_stale_stored_full_does_not_silence_the_disclosure(self):
        cm = self.cmap()
        cm["S1"]["covers_items"] = ["1.01a"]
        self.build(cmap=cm)  # stored "full", computed partial
        c = self.gate()["coverage"]
        self.assertEqual(c["effective_status"], "partial")
        self.assertTrue(c["disclose_to_learner"])
        self.assertEqual(c["uncovered_items"], ["1.01b"])
        self.assertEqual((c["items_total"], c["items_taught"]), (3, 2))

    def test_stored_partial_is_never_upgraded_by_the_computation(self):
        self.build(course_extra={"coverage_status": "partial"})  # files say full, audit last said partial
        c = self.gate()["coverage"]
        self.assertEqual(c["effective_status"], "partial")
        self.assertTrue(c["disclose_to_learner"])

    def test_blocked_gates_still_report_coverage_without_changing_the_block(self):
        self.build(course_extra={"grounding_status": "suspended_ungrounded"})
        g = self.gate()
        self.assertFalse(g["can_proceed"])
        self.assertEqual(g["first_blocking_gate"], "2_grounding")
        self.assertIn("coverage", g)

    def test_unreadable_course_json_has_no_coverage_block(self):
        _w(self.cpath, "{nope")
        g = gate_check.evaluate(self.cpath, "NONE", self.tmp, self.tmp, "2026-09-19")
        self.assertEqual(g["first_blocking_gate"], "read_error")
        self.assertNotIn("coverage", g)


class MigrateCourseV3Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.path = os.path.join(self.tmp, "course.json")

    def test_v2_course_moves_to_current_with_unverified_and_is_flagged(self):
        _w(self.path, {"schema_version": 2, "academic_level": 2, "level_source": "RQF", "grounding_status": "verified",
                       "last_live_recheck": None, "stage_ladder": ["S1"]})
        r = migrate_schema.migrate_course(self.path)
        d = _r(self.path)
        self.assertEqual((d["schema_version"], d["coverage_status"]), (migrate_schema.COURSE_SCHEMA_VERSION, "unverified"))
        self.assertTrue(r["wrote"])
        self.assertTrue(any(x.startswith("coverage_status") for x in r["needs_sourcing"]))
        self.assertEqual(d["academic_level"], 2)  # nothing else disturbed

    def test_v1_course_migrates_straight_to_current_in_one_hop(self):
        _w(self.path, {"schema_version": 1, "stage_ladder": ["S1"]})
        migrate_schema.migrate_course(self.path)
        d = _r(self.path)
        self.assertEqual(d["schema_version"], migrate_schema.COURSE_SCHEMA_VERSION)
        self.assertEqual(d["coverage_status"], "unverified")
        self.assertIsNone(d["academic_level"])

    def test_existing_coverage_status_is_never_overwritten_and_not_flagged(self):
        _w(self.path, {"schema_version": 2, "academic_level": 2, "level_source": "x", "grounding_status": "verified",
                       "last_live_recheck": None, "coverage_status": "full"})
        r = migrate_schema.migrate_course(self.path)
        self.assertEqual(_r(self.path)["coverage_status"], "full")
        self.assertFalse(any(x.startswith("coverage_status") for x in r["needs_sourcing"]))

    def test_partial_is_a_known_state_and_not_flagged_as_unsourced(self):
        _w(self.path, {"schema_version": 4, "academic_level": 2, "level_source": "x", "grounding_status": "verified",
                       "last_live_recheck": None, "coverage_status": "partial", "standalone": False,
                       "requires_complete": [], "practical_stages": {}, "learner_notices": [], "level_basis": "framework"})
        r = migrate_schema.migrate_course(self.path)
        self.assertFalse(r["wrote"])
        self.assertFalse(any(x.startswith("coverage_status") for x in r["needs_sourcing"]))

    def test_second_run_is_a_no_op(self):
        _w(self.path, {"schema_version": 2, "academic_level": 2, "level_source": "x", "grounding_status": "verified",
                       "last_live_recheck": None})
        migrate_schema.migrate_course(self.path)
        again = migrate_schema.migrate_course(self.path)
        self.assertFalse(again["wrote"])
        self.assertEqual(again["changed_fields"], [])

    def test_migration_never_sets_full(self):
        _w(self.path, {"schema_version": 2, "academic_level": 2, "level_source": "x", "grounding_status": "verified",
                       "last_live_recheck": None})
        migrate_schema.migrate_course(self.path)
        self.assertNotEqual(_r(self.path)["coverage_status"], "full")

    def test_subject_migrates_to_current(self):
        cpath = os.path.join(self.tmp, "c", "course.json")
        _w(cpath, {"schema_version": 3, "academic_level": 2})
        spath = os.path.join(self.tmp, "s.json")
        _w(spath, {"schema_version": 1, "stage_progress": {"S1": "unsat"}})
        migrate_schema.migrate_subject(spath, cpath)
        d = _r(spath)
        self.assertEqual(d["schema_version"], migrate_schema.SUBJECT_SCHEMA_VERSION)
        self.assertIn("syllabus_status", d)


class ShippedTemplateTests(unittest.TestCase):
    def test_templates_parse_and_are_current_schema(self):
        tpl = os.path.join(ROOT, "_template")
        # course.json template carries {{placeholders}} inside strings only, so it is valid JSON
        course = _r(os.path.join(tpl, "course.json"))
        self.assertEqual(course["schema_version"], migrate_schema.COURSE_SCHEMA_VERSION)
        self.assertEqual(course["coverage_status"], "unverified")
        cmap = _r(os.path.join(tpl, "curriculum_map.json"))
        for k in ("_meta", "_items_source", "_syllabus_items", "_declared_exclusions"):
            self.assertIn(k, cmap)
        self.assertIn("covers_items", cmap["S1"])

    def test_lesson_template_has_the_items_section(self):
        with open(os.path.join(ROOT, "_template", "stages", "S1", "lesson.md"), encoding="utf-8") as f:
            self.assertIn("## Syllabus items taught here", f.read())

    def test_bootstrap_ships_the_new_script(self):
        self.assertTrue(os.path.isfile(os.path.join(SCRIPTS, "coverage_check.py")))


if __name__ == "__main__":
    unittest.main()
