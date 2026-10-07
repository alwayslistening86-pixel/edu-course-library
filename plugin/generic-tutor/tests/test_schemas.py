"""S-05/S-06/S-07: JSON Schemas, the stdlib validator, and conformance of everything the scripts write."""
import copy
import glob
import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
from tutorlib import schema  # noqa: E402


class Validator(unittest.TestCase):
    def check(self, sch, value):
        errs = []
        schema._check(value, sch, sch, "", errs)
        return errs

    def test_types_and_bool_is_not_integer(self):
        self.assertEqual(self.check({"type": "integer"}, 3), [])
        self.assertTrue(self.check({"type": "integer"}, True))
        self.assertTrue(self.check({"type": "number"}, "1"))
        self.assertEqual(self.check({"type": ["string", "null"]}, None), [])

    def test_required_enum_bounds_pattern(self):
        s = {"type": "object", "required": ["a"], "properties": {
            "a": {"enum": ["x", "y"]}, "n": {"type": "number", "minimum": 0, "maximum": 1}, "p": {"pattern": "^a"}}}
        self.assertEqual(self.check(s, {"a": "x", "n": 0.5, "p": "abc"}), [])
        self.assertEqual(len(self.check(s, {"n": 2, "p": "b"})), 3)
        self.assertTrue(self.check(s, {"a": "z"}))

    def test_additional_and_pattern_properties_and_items(self):
        s = {"type": "object", "properties": {"k": {"type": "string"}}, "additionalProperties": False}
        self.assertTrue(self.check(s, {"k": "v", "z": 1}))
        s = {"type": "object", "patternProperties": {"^S": {"type": "integer"}}}
        self.assertTrue(self.check(s, {"S1": "no"}))
        self.assertEqual(self.check(s, {"_meta": "ok"}), [])
        s = {"type": "array", "minItems": 1, "items": {"type": "integer"}}
        self.assertTrue(self.check(s, []))
        self.assertTrue(self.check(s, [1, "a"]))

    def test_ref_oneof_anyof(self):
        s = {"definitions": {"i": {"type": "integer"}}, "anyOf": [{"$ref": "#/definitions/i"}, {"type": "string"}]}
        self.assertEqual(self.check(s, 1), [])
        self.assertEqual(self.check(s, "a"), [])
        self.assertTrue(self.check(s, None))
        self.assertTrue(self.check({"oneOf": [{"type": "number"}, {"type": "integer"}]}, 1))  # matches both


class RealSchemas(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.addCleanup(self._td.cleanup)
        self.tmp = os.path.realpath(self._td.name)
        self.fx = gs.build_fixture(self.tmp)

    def fixture_files(self):
        out = [("student_profile", self.fx["L"] + "/student_profile.json")]
        for f in sorted(glob.glob(self.fx["S"] + "/*.json")):
            out.append(("review_deck" if f.endswith("_review_deck.json") else "subjects", f))
        for c in sorted(os.listdir(self.fx["C"])):
            if c == "old":
                continue  # deliberately pre-migration shape
            for kind in ("course", "curriculum_map", "rubric"):
                out.append((kind, f"{self.fx['C']}/{c}/{kind}.json"))
            qb = f"{self.fx['C']}/{c}/question_bank.json"
            if os.path.isfile(qb):
                out.append(("question_bank", qb))
            mis = f"{self.fx['C']}/{c}/stages/S1/misconceptions.json"
            if os.path.isfile(mis):
                out.append(("misconceptions", mis))
        # files written by their own scripts into scratch folders
        import bootstrap_scripts
        import confirm_access
        acc = os.path.join(self.tmp, "accessdir")
        os.makedirs(acc)
        confirm_access.confirm(acc, "shared", "2026-10-06")
        out.append(("access", os.path.join(acc, "access.json")))
        dep = os.path.join(self.tmp, "deployed")
        bootstrap_scripts.bootstrap(os.path.join(os.path.dirname(HERE), "scripts"), os.path.join(os.path.dirname(HERE), ".claude-plugin", "plugin.json"), dep)
        out.append(("manifest", os.path.join(dep, ".manifest.json")))
        import verify_sources
        snap_course = os.path.join(self.tmp, "snapcourse")
        os.makedirs(snap_course)
        with open(os.path.join(snap_course, "course.json"), "w") as f:
            json.dump({"stage_ladder": []}, f)
        with open(os.path.join(snap_course, "rubric.json"), "w") as f:
            json.dump({"source_urls": ["https://example.org/a", "https://example.org/b"]}, f)
        verify_sources.verify(snap_course, "2026-10-07", write=True, fetcher=lambda u: {"status": "ok", "http": 200, "sha256": "a" * 64, "bytes": 5} if u.endswith("a") else {"status": "dead", "http": 404})
        out.append(("source_snapshots", os.path.join(snap_course, "source_snapshots.json")))
        return out

    def test_plan_estimate_output_matches_its_schema(self):
        r = gs.run_step("plan_estimate.py", ["{L}", "{C}"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 0)
        self.assertEqual(schema.validate_output(r["stdout"], "plan_estimate"), [])
        bad = dict(r["stdout"])
        bad.pop("courses")
        self.assertTrue(schema.validate_output(bad, "plan_estimate"))

    def test_all_kinds_have_a_fixture(self):
        self.assertEqual(sorted({k for k, _ in self.fixture_files()}), schema.kinds())

    def test_fixture_files_conform(self):
        for kind, path in self.fixture_files():
            self.assertEqual(schema.validate_file(path, kind), [], path)

    def test_files_written_by_scripts_conform(self):
        flows = [
            ("error_log.py", ["append", "{S}/mathA.json", "S2", "S2.1", "practice", "misconception", "MC-1", "n", "6"]),
            ("error_log.py", ["resolve", "{S}/mathA.json", "S2.1", "8"]),
            ("item_mastery.py", ["observe", "{S}/mathA.json", "S1.1", "true", "5"]),
            ("confidence_update.py", ["apply", "{S}/mathA.json", "pass_clean", "7"]),
            ("remediation_state.py", ["record", "{S}/mathA.json", "S2", "slip", "6"]),
            ("record_stage_result.py", ["apply", "{S}/mathA.json", "{C}/mathA/course.json", "S2", "pass"]),
            ("review_math.py", ["apply", "{S}/mathA_review_deck.json", "k1", "6", "false"]),
            ("slot_advance.py", ["{L}/student_profile.json", "--min-gap-minutes", "0"]),
            ("resume_enrollment.py", ["{S}/design.json", "{C}/design/course.json", "active", "2026-10-04"]),
        ]
        for script, args in flows:
            r = gs.run_step(script, args, self.fx, self.tmp)
            self.assertEqual(r["exit"], 0, (script, r))
        for kind, path in self.fixture_files():
            self.assertEqual(schema.validate_file(path, kind), [], path)

    def test_known_bad_shapes_are_rejected(self):
        subj = gs.read_json(self.fx["S"] + "/mathA.json")
        for mutate, why in (
            (lambda d: d.update(confidence="medium"), "legacy string confidence"),
            (lambda d: d.update(confidence=1.5), "confidence out of range"),
            (lambda d: d.update(roster_state="paused"), "unknown roster_state"),
            (lambda d: d["syllabus_status"].update(S1="passed"), "passed vs pass (the v1.11 bug)"),
            (lambda d: d["error_patterns"].append({"id": "e"}), "incomplete error entry"),
            (lambda d: d.pop("course_id"), "missing course_id"),
        ):
            bad = copy.deepcopy(subj)
            mutate(bad)
            self.assertTrue(schema.validate(bad, "subjects"), why)

    def test_misconceptions_schema_rejects_empty_and_incomplete_entries(self):
        self.assertEqual(schema.validate([], "misconceptions")[0].split(":")[1].strip()[:4], "fewe")
        self.assertTrue(schema.validate([{"pattern": "a wrong idea about fractions", "correction": "the right idea"}], "misconceptions"))
        self.assertTrue(schema.validate({"pattern": "x"}, "misconceptions"))

    def test_legacy_test_fixture_shape_is_flagged(self):
        # tests/test_regressions.py's Learner fixture uses confidence "medium" and error_patterns ["x"]; the schema must not bless that.
        legacy = {"schema_version": 5, "course_id": "A", "roster_state": "active", "syllabus_status": {}, "current_stage": "S0",
                  "confidence": "medium", "error_patterns": ["x"]}
        self.assertEqual(len(schema.validate(legacy, "subjects")), 2)


if __name__ == "__main__":
    unittest.main()


class CourseDirCheck(unittest.TestCase):
    def setUp(self):
        import shutil
        import tempfile
        import golden_support as gs
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.d = f"{self.fx['C']}/mathA"

    def test_fixture_course_is_valid_and_counts_files(self):
        import validate_schema
        r = validate_schema.check_course_dir(self.d)
        self.assertEqual((r["valid"], r["invalid"]), (True, []))
        self.assertGreaterEqual(r["files_checked"], 4)                  # course, map, rubric, S1 misconceptions (+ question bank)

    def test_broken_and_missing_files_are_listed(self):
        import json
        import validate_schema
        with open(f"{self.d}/rubric.json", "w") as f:
            json.dump({"stage_rubrics": "nope"}, f)
        os.remove(f"{self.d}/curriculum_map.json")
        r = validate_schema.check_course_dir(self.d)
        by = {i["file"]: i for i in r["invalid"]}
        self.assertFalse(r["valid"])
        self.assertEqual(by["curriculum_map.json"]["errors"], ["file is missing"])
        self.assertIn("rubric.json", by)
        self.assertIn("error", validate_schema.check_course_dir(self.tmp + "/nope"))
