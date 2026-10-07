"""L-21: where to go back to when the cause is missing_prerequisite."""
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
import prereq_pointer as pp  # noqa: E402


class Pointer(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.L, self.C, self.S = self.fx["L"], self.fx["C"], self.fx["S"]

    def edit(self, rel, fn):
        p = os.path.join(self.S, rel) if rel.endswith(".json") and "/" not in rel else rel
        with open(p) as f:
            d = json.load(f)
        fn(d)
        with open(p, "w") as f:
            json.dump(d, f)

    def test_weak_earlier_stage_is_pointed_at_with_a_review_command(self):
        def weak(d):
            d["item_mastery"] = {"S1.1": {"p_mastery": 0.2, "observations": 4}}
            d["error_patterns"] = [{"stage_id": "S1", "item_id": "S1.1", "resolved": False}]
        self.edit("mathA.json", weak)
        r = pp.point(self.L, self.C, "mathA", "S3")
        c = r["candidates"][0]
        self.assertEqual((c["kind"], c["stage_id"], c["command"]), ("earlier_stage", "S1", "/review mathA S1"))
        self.assertIn("unresolved", c["why"])

    def test_no_evidence_falls_back_to_the_stage_just_before(self):
        r = pp.point(self.L, self.C, "mathA", "S3")
        self.assertEqual([c["stage_id"] for c in r["candidates"]], ["S2"])
        self.assertEqual(pp.point(self.L, self.C, "mathA", "S1")["candidates"], [])           # nothing earlier

    def test_prerequisite_courses_by_state(self):
        def req(d):
            d["requires_complete"] = ["mathA"]
        cj = os.path.join(self.C, "mathB", "course.json")
        self.edit(cj, req)
        c = pp.point(self.L, self.C, "mathB", "S2")["candidates"]
        self.assertIn(("prerequisite_course", "/continue mathA"), [(x["kind"], x["command"]) for x in c])         # mathA is unfinished
        os.remove(os.path.join(self.S, "mathA.json"))
        c = pp.point(self.L, self.C, "mathB", "S2")["candidates"]
        self.assertIn("/add-course mathA", [x["command"] for x in c])
        self.edit(cj, lambda d: d.update(requires_complete=[["solo", "mathA"]]))
        c = pp.point(self.L, self.C, "mathB", "S2")["candidates"]
        self.assertIn("/continue solo", [x["command"] for x in c])                              # the alternative the learner started

    def test_a_completed_prerequisite_points_at_its_weakest_stage(self):
        def done(d):
            d["syllabus_status"] = {"S1": "pass", "S2": "pass", "S3": "pass"}
            d["item_mastery"] = {"S1.1": {"p_mastery": 0.9}, "S2.1": {"p_mastery": 0.3}}
        self.edit("mathA.json", done)
        self.edit(os.path.join(self.C, "mathB", "course.json"), lambda d: d.update(requires_complete=["mathA"]))
        c = [x for x in pp.point(self.L, self.C, "mathB", "S2")["candidates"] if x["kind"] == "prerequisite_course"][0]
        self.assertEqual(c["command"], "/review mathA S2")

    def test_at_most_three_and_errors(self):
        r = pp.point(self.L, self.C, "mathA", "S3")
        self.assertLessEqual(len(r["candidates"]), 3)
        self.assertIn("error", pp.point(self.L, self.C, "nope", "S1"))
        self.assertIn("error", pp.point(self.L, self.C, "mathA", "S9"))
        self.assertIn("error", pp.point(self.L, self.C, "../x", "S1"))
        self.assertEqual(pp.main(["a"]), 2)


if __name__ == "__main__":
    unittest.main()
