"""L-22: goals mapped to syllabus items, and progress against them."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import goal_map  # noqa: E402
import golden_support as gs  # noqa: E402
from tutorlib import schema  # noqa: E402

TODAY = "2026-10-07"


class GoalMap(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        fx = gs.build_fixture(self.tmp)
        self.L, self.C, self.S = fx["L"], fx["C"], fx["S"]
        self.subj = f"{self.S}/mathA.json"
        self.cdir = f"{self.C}/mathA"
        self.edit(f"{self.L}/student_profile.json", lambda d: d.update(goals=["pass the course", "be quick at the second topic"]))

    def edit(self, path, fn):
        d = gs.read_json(path)
        fn(d)
        with open(path, "w") as f:
            json.dump(d, f)

    def raw(self):
        with open(self.subj, encoding="utf-8") as f:
            return f.read()

    def set(self, goal, ids):
        return goal_map.set_goal(self.subj, self.cdir, goal, ids, TODAY)

    def test_set_stores_a_valid_mapping_and_replaces_the_same_goal(self):
        r = self.set("pass the course", ["S1.1", "S2.1", "S1.1"])
        self.assertEqual((r["written"], r["item_count"]), (True, 2), "duplicates are dropped")
        self.assertEqual(schema.validate(gs.read_json(self.subj), "subjects"), [])
        self.set("pass the course", ["S3.1"])
        self.assertEqual(gs.read_json(self.subj)["goal_map"], [{"goal": "pass the course", "items": ["S3.1"], "set_on": TODAY}])

    def test_set_refuses_bad_input_and_writes_nothing(self):
        before = self.raw()
        for goal, ids in (("", ["S1.1"]), ("x" * 121, ["S1.1"]), ("g", []), ("g", ["nope"]), ("g", "S1.1"), ("g", [f"S{i}" for i in range(61)])):
            self.assertIn("error", self.set(goal, ids), (goal[:10], ids))
        self.assertEqual(self.raw(), before)

    def test_report_separates_taught_from_remaining_in_teaching_order(self):
        self.set("pass the course", ["S3.1", "S1.1", "S2.1"])
        g = goal_map.report(self.L, self.C, "mathA")["goals"][0]
        self.assertEqual((g["items_mapped"], g["taught"], g["remaining"], g["next_stage"]), (3, 1, 2, "S2"))
        self.assertEqual([x["item"] for x in g["remaining_in_teaching_order"]], ["S2.1", "S3.1"])

    def test_mastery_is_only_reported_for_observed_taught_items(self):
        self.set("pass the course", ["S1.1", "S2.1"])
        self.edit(self.subj, lambda d: d.update(item_mastery={"S1.1": {"p_mastery": 0.4}, "S2.1": {"p_mastery": 0.9}}))
        g = goal_map.report(self.L, self.C, "mathA")["goals"][0]
        self.assertEqual((g["observed"], g["mean_observed_mastery"]), (1, 0.4), "S2 is not passed, so S2.1 is not counted")
        self.assertEqual([w["item"] for w in g["weakest_taught"]], ["S1.1"])
        self.set("none seen", ["S3.1"])
        none = [x for x in goal_map.report(self.L, self.C, "mathA")["goals"] if x["goal"] == "none seen"][0]
        self.assertEqual((none["observed"], none["mean_observed_mastery"]), (0, None))

    def test_an_item_no_stage_teaches_is_a_gap_not_a_claim(self):
        self.edit(f"{self.cdir}/curriculum_map.json", lambda d: d["_syllabus_items"].append({"id": "X.1", "title": "Orphan", "topic_area": "T"}))
        self.set("orphan", ["X.1", "S1.1"])
        r = goal_map.report(self.L, self.C, "mathA")
        g = r["goals"][0]
        self.assertEqual((g["not_taught_by_this_course"], g["taught"]), (["X.1"], 1))
        self.assertTrue(any("not taught by any stage" in c for c in r["caveats"]))

    def test_unmapped_goals_are_listed_and_the_report_is_honest(self):
        self.set("pass the course", ["S1.1"])
        r = goal_map.report(self.L, self.C, "mathA")
        self.assertEqual(r["unmapped_goals"], ["be quick at the second topic"])
        self.assertTrue(any("not that the item is learned" in c for c in r["caveats"]))

    def test_clear_one_or_all(self):
        self.set("a", ["S1.1"])
        self.set("b", ["S2.1"])
        self.assertEqual(goal_map.clear_goal(self.subj, "a")["removed"], 1)
        self.assertEqual([m["goal"] for m in gs.read_json(self.subj)["goal_map"]], ["b"])
        self.assertEqual(goal_map.clear_goal(self.subj)["removed"], 1)
        self.assertNotIn("goal_map", gs.read_json(self.subj))
        self.assertEqual(goal_map.clear_goal(self.subj, "zzz")["removed"], 0)

    def test_consent_limited_still_writes_progress_bookkeeping_but_revoked_does_not(self):
        self.edit(f"{self.L}/student_profile.json", lambda d: d.setdefault("consent", {}).update(status="limited"))
        self.assertTrue(self.set("pass the course", ["S1.1"])["written"])
        self.edit(f"{self.L}/student_profile.json", lambda d: d.setdefault("consent", {}).update(status="revoked"))
        r = self.set("another goal", ["S2.1"])
        self.assertFalse(r.get("written"))
        self.assertEqual([m["goal"] for m in gs.read_json(self.subj)["goal_map"]], ["pass the course"])

    def test_items_lists_topic_areas_goals_and_items(self):
        r = goal_map.list_items(self.L, self.C, "mathA")
        self.assertEqual((r["item_count"], r["topic_areas"], r["goals"][0]), (3, {"T": 3}, "pass the course"))
        self.assertEqual({i["id"]: i["stage"] for i in r["items"]}, {"S1.1": "S1", "S2.1": "S2", "S3.1": "S3"})
        self.assertEqual(goal_map.list_items(self.L, self.C, "mathA", area="nothing")["items"], [])

    def test_a_big_course_lists_areas_first(self):
        def grow(d):
            d["_syllabus_items"] += [{"id": f"B{i}", "title": f"b{i}", "topic_area": "Big"} for i in range(goal_map.LIST_ALL_UP_TO)]
        self.edit(f"{self.cdir}/curriculum_map.json", grow)
        r = goal_map.list_items(self.L, self.C, "mathA")
        self.assertNotIn("items", r)
        self.assertIn("--area", r["note"])
        self.assertEqual(len(goal_map.list_items(self.L, self.C, "mathA", area="Big")["items"]), goal_map.LIST_ALL_UP_TO)

    def test_missing_course_and_usage(self):
        self.assertIn("error", goal_map.list_items(self.L, self.C, "ghost"))
        self.assertIn("error", goal_map.report(self.L, self.C, "ghost"))
        self.assertEqual(goal_map.main([]), 2)
        self.assertEqual(goal_map.main(["set", self.subj, self.cdir, "g", "not json", TODAY]), 1)


if __name__ == "__main__":
    unittest.main()
