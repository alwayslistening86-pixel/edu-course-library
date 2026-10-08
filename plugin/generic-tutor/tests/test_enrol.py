"""enrol.py: one way to create a progress file, valid by construction."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import enrol  # noqa: E402
import golden_support as gs  # noqa: E402
from tutorlib import ids, schema  # noqa: E402


class Enrol(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.P, self.C, self.S = self.fx["P"], self.fx["C"], self.fx["S"]
        os.remove(f"{self.S}/solo.json")                         # free up solo, and a roster slot
        gs.build_course(self.C, "fresh", level=4, stages=("A1", "A2"))

    def edit_profile(self, fn):
        p = f"{self.P}/student_profile.json"
        d = gs.read_json(p)
        fn(d)
        with open(p, "w") as f:
            json.dump(d, f)

    def test_creates_a_valid_file_with_the_documented_defaults(self):
        r = enrol.enrol(self.P, self.C, "fresh", "active", "2026-10-05")
        self.assertEqual((r["written"], r["cohort_id"], r["current_stage"], r["theory_only"]), (True, 4, "A1", False))
        d = gs.read_json(f"{self.S}/fresh.json")
        self.assertEqual(schema.validate(d, "subjects"), [])
        self.assertEqual((d["syllabus_status"], d["confidence"], d["current_phase"], d["exam_status"]), ({"A1": "unsat", "A2": "unsat"}, 0.5, "lesson", "locked"))

    def set_lifecycle(self, value):
        path = f"{self.C}/fresh/course.json"
        d = gs.read_json(path)
        d["lifecycle"] = value
        with open(path, "w") as f:
            json.dump(d, f)

    def test_a_retiring_course_takes_no_new_enrolments(self):
        self.set_lifecycle("retiring")
        r = enrol.enrol(self.P, self.C, "fresh", "active", "2026-10-05")
        self.assertIn("retiring", r["error"])
        self.assertFalse(os.path.exists(f"{self.S}/fresh.json"))

    def test_a_live_course_still_enrols_and_a_bad_lifecycle_is_a_schema_error(self):
        self.set_lifecycle("live")
        self.assertTrue(enrol.enrol(self.P, self.C, "fresh", "active", "2026-10-05")["written"])
        self.set_lifecycle("archived")
        self.assertTrue(schema.validate(gs.read_json(f"{self.C}/fresh/course.json"), "course"))

    def test_list_courses_shows_the_lifecycle(self):
        import list_courses
        self.set_lifecycle("retiring")
        rows = {r["course_id"]: r for r in list_courses.build(self.P, self.C)["courses"]}
        self.assertEqual((rows["fresh"]["lifecycle"], rows["solo"]["lifecycle"]), ("retiring", "live"))

    def test_standalone_gets_its_own_cohort_and_dormant_is_honoured(self):
        r = enrol.enrol(self.P, self.C, "solo", "dormant", "2026-10-05")
        self.assertEqual((r["cohort_id"], r["roster_state"]), ("standalone:solo", "dormant"))

    def test_practical_stage_is_withheld_until_the_capability_is_declared(self):
        shutil.rmtree(f"{self.C}/design")
        gs.build_course(self.C, "design", level=2, stages=("S1", "S2"), practical={"S2": ["share_images"]})
        os.remove(f"{self.S}/design.json")
        r = enrol.enrol(self.P, self.C, "design", "active", "2026-10-05")
        self.assertEqual((r["theory_only"], r["withheld_stages"]), (True, ["S2"]))
        self.assertEqual(gs.read_json(f"{self.S}/design.json")["syllabus_status"]["S2"], "withheld")

    def test_refusals_change_nothing(self):
        self.assertIn("already enrolled", enrol.enrol(self.P, self.C, "mathA", "active", "2026-10-05")["error"])
        self.assertIn("error", enrol.enrol(self.P, self.C, "ghost", "active", "2026-10-05"))
        self.assertIn("error", enrol.enrol(self.P, self.C, "fresh", "dropped", "2026-10-05"))
        with self.assertRaises(ids.InvalidId):
            enrol.enrol(self.P, self.C, "../x", "active", "2026-10-05")
        self.edit_profile(lambda d: d["roster"].update(max_incomplete_courses=1))
        r = enrol.enrol(self.P, self.C, "fresh", "active", "2026-10-05")
        self.assertIn("roster is full", r["error"])
        self.assertFalse(os.path.exists(f"{self.S}/fresh.json"))

    def test_revoked_consent_persists_nothing(self):
        self.edit_profile(lambda d: d["consent"].update(status="revoked"))
        r = enrol.enrol(self.P, self.C, "fresh", "active", "2026-10-05")
        self.assertEqual(r["action"], "not_persisted")
        self.assertFalse(os.path.exists(f"{self.S}/fresh.json"))


if __name__ == "__main__":
    unittest.main()
