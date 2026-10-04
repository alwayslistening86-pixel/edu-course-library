"""S-05/S-06/S-07: JSON Schemas, the stdlib validator, and conformance of everything the scripts write."""
import copy
import glob
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
        return out

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

    def test_legacy_test_fixture_shape_is_flagged(self):
        # tests/test_scripts.py's Learner fixture uses confidence "medium" and error_patterns ["x"]; the schema must not bless that.
        legacy = {"schema_version": 5, "course_id": "A", "roster_state": "active", "syllabus_status": {}, "current_stage": "S0",
                  "confidence": "medium", "error_patterns": ["x"]}
        self.assertEqual(len(schema.validate(legacy, "subjects")), 2)


if __name__ == "__main__":
    unittest.main()
