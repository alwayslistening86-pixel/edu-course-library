"""L-03/L-04/L-05/L-07/L-10: review_select, next_items, readiness."""
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
import next_items  # noqa: E402
import readiness  # noqa: E402
import review_select  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.L, self.C, self.S = self.fx["L"], self.fx["C"], self.fx["S"]

    def edit(self, path, fn):
        d = gs.read_json(path)
        fn(d)
        with open(path, "w") as f:
            json.dump(d, f)

    def cards(self, course, specs):
        deck = {"schema_version": 1, "course_id": course, "cards": [
            {"id": cid, "stage_id": st, "item_id": it, "front": f"f-{cid}", "back": f"b-{cid}", "interval_sessions": 1,
             "ease": ease, "lapses": lap, "due_at_slot": due} for cid, st, it, ease, lap, due in specs]}
        with open(f"{self.S}/{course}_review_deck.json", "w") as f:
            json.dump(deck, f)


class ReviewSelect(Base):
    def test_due_filter_priority_and_stable_order(self):
        # slot is 5. a: overdue by 3, b: overdue 0 low ease, c: overdue 0 high ease, d: not due
        self.cards("mathA", [("a", "S1", "S1.1", 2.5, 0, 2), ("b", "S1", "S1.1", 1.5, 0, 5), ("c", "S1", "S1.1", 2.9, 0, 5), ("d", "S1", "S1.1", 2.0, 0, 9)])
        r = review_select.select(self.L, self.C)
        self.assertEqual([c["card_id"] for c in r["selected"]], ["a", "b", "c"])
        self.assertEqual((r["due_total"], r["remaining_due"], r["selected"][0]["overdue_by"]), (3, 0, 3))
        self.assertIn("front", r["selected"][0])

    def test_weak_items_come_before_strong_at_equal_overdue(self):
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(item_mastery={"S1.1": {"p_mastery": 0.9, "observations": 5}, "S2.1": {"p_mastery": 0.2, "observations": 5}}))
        self.cards("mathA", [("strong", "S1", "S1.1", 2.3, 0, 5), ("weak", "S2", "S2.1", 2.3, 0, 5)])
        self.assertEqual([c["card_id"] for c in review_select.select(self.L, self.C)["selected"]], ["weak", "strong"])

    def test_round_robin_across_courses_and_limit(self):
        self.cards("mathA", [(f"a{i}", "S1", "S1.1", 2.3, 0, 5 - i) for i in range(4)])
        self.edit(f"{self.S}/solo.json", lambda d: None)
        deck = {"cards": [{"id": f"s{i}", "stage_id": "S1", "item_id": "S1.1", "front": "f", "back": "b", "interval_sessions": 1, "ease": 2.3,
                           "lapses": 0, "due_at_slot": 5 - i} for i in range(4)]}
        with open(f"{self.S}/solo_review_deck.json", "w") as f:
            json.dump(deck, f)
        r = review_select.select(self.L, self.C, limit=4)
        self.assertEqual([c["course_id"] for c in r["selected"]], ["mathA", "solo", "mathA", "solo"])
        self.assertEqual((r["selected_count"], r["remaining_due"]), (4, 4))

    def test_scope_filters_and_non_live_courses_skipped(self):
        self.cards("mathA", [("a", "S1", "S1.1", 2.3, 0, 5), ("b", "S2", "S2.1", 2.3, 0, 5)])
        self.assertEqual([c["card_id"] for c in review_select.select(self.L, self.C, stage="S2")["selected"]], ["b"])
        self.assertEqual([c["card_id"] for c in review_select.select(self.L, self.C, item="S1.1")["selected"]], ["a"])
        self.assertEqual(review_select.select(self.L, self.C, course="nope")["selected_count"], 0)
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(roster_state="dropped"))
        r = review_select.select(self.L, self.C)
        self.assertEqual(r["selected_count"], 0)
        self.assertIn("mathA", r["scope"]["courses_skipped_not_live"])

    def test_cli_and_errors(self):
        self.assertEqual(gs.run_step("review_select.py", ["{L}", "{C}", "--limit", "0"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("review_select.py", ["{L}", "{C}", "--slot", "x"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("review_select.py", ["{L}", "{C}"], self.fx, self.tmp)["exit"], 0)
        self.assertEqual(gs.run_step("review_select.py", ["{L}/nope", "{C}"], self.fx, self.tmp)["exit"], 1)


class NextItems(Base):
    def test_weakest_current_items_and_interleaved_prior(self):
        # mathA: ladder S1 S2 S3, current S2; S1 passed. Items: S1.1, S2.1, S3.1 (one per stage) - add more per stage
        cmap = gs.read_json(f"{self.C}/mathA/curriculum_map.json")
        cmap["_syllabus_items"] += [{"id": f"{s}.{n}", "title": "x", "topic_area": "T"} for s in ("S1", "S2") for n in (2, 3, 4)]
        for s in ("S1", "S2"):
            cmap[s]["covers_items"] += [f"{s}.{n}" for n in (2, 3, 4)]
        with open(f"{self.C}/mathA/curriculum_map.json", "w") as f:
            json.dump(cmap, f)
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(item_mastery={
            "S2.1": {"p_mastery": 0.9, "observations": 6}, "S2.2": {"p_mastery": 0.2, "observations": 6}, "S1.2": {"p_mastery": 0.1, "observations": 6},
            "S1.1": {"p_mastery": 0.95, "observations": 6}}, error_patterns=[
            {"id": "e", "stage_id": "S2", "item_id": "S2.3", "source_phase": "practice", "cause": "slip", "slot": 1, "resolved": False}]))
        r = next_items.choose(self.L, self.C, "mathA", 5)
        pools = [i["pool"] for i in r["items"]]
        self.assertEqual((pools.count("current"), pools.count("prior")), (4, 1))   # ceil(0.7*5)=4 current, the rest prior
        ids = [i["item_id"] for i in r["items"]]
        self.assertIn("S1.2", ids)                    # weakest prior item
        self.assertNotIn("S2.1", ids[:3])             # strong current item is not chosen first
        self.assertNotEqual(pools[:2], ["current", "current"])   # presented interleaved
        self.assertEqual(r["items"][0]["pool"], "current")

    def test_unobserved_items_get_a_bonus_and_errors_raise_weakness(self):
        r = next_items.choose(self.L, self.C, "mathA", 3)
        for i in r["items"]:
            self.assertGreater(i["weakness"], 0.7 - 1e-9)
            self.assertIn("not yet observed", i["reason"])

    def test_not_itemised_and_bad_input(self):
        cmap = gs.read_json(f"{self.C}/mathA/curriculum_map.json")
        cmap["_syllabus_items"] = []
        with open(f"{self.C}/mathA/curriculum_map.json", "w") as f:
            json.dump(cmap, f)
        self.assertFalse(next_items.choose(self.L, self.C, "mathA")["itemised"])
        self.assertIn("error", next_items.choose(self.L, self.C, "ghost"))
        self.assertEqual(gs.run_step("next_items.py", ["{L}", "{C}"], self.fx, self.tmp)["exit"], 2)

    def test_deterministic(self):
        self.assertEqual(next_items.choose(self.L, self.C, "mathA", 4), next_items.choose(self.L, self.C, "mathA", 4))


class Readiness(Base):
    def mastery(self, p, obs=6, items=("S1.1", "S2.1", "S3.1")):
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(item_mastery={i: {"p_mastery": p, "observations": obs} for i in items}))

    def test_bands(self):
        self.assertEqual(readiness.assess(self.L, self.C, "mathA")["band"], "not_enough_evidence")
        self.mastery(0.4)
        self.assertEqual(readiness.assess(self.L, self.C, "mathA")["band"], "early")
        self.mastery(0.7)
        self.assertEqual(readiness.assess(self.L, self.C, "mathA")["band"], "building")
        self.mastery(0.9)
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(syllabus_status={"S1": "pass", "S2": "pass", "S3": "pass"}))
        r = readiness.assess(self.L, self.C, "mathA")
        self.assertEqual((r["band"], r["strength"]), ("solid", "medium"))
        self.assertNotIn("grade", json.dumps(r["evidence"]).lower())

    def test_partial_coverage_caps_the_band_and_is_disclosed(self):
        self.mastery(0.9)
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(syllabus_status={"S1": "pass", "S2": "pass", "S3": "pass"}))
        cmap = gs.read_json(f"{self.C}/mathA/curriculum_map.json")
        cmap["_syllabus_items"].append({"id": "S9.9", "title": "untaught", "topic_area": "T"})
        with open(f"{self.C}/mathA/curriculum_map.json", "w") as f:
            json.dump(cmap, f)
        r = readiness.assess(self.L, self.C, "mathA")
        self.assertEqual(r["band"], "building")
        self.assertTrue(any("Coverage is" in c for c in r["caveats"]))

    def test_strength_scales_with_evidence_and_caveats_always_present(self):
        self.mastery(0.7, obs=1)
        self.assertEqual(readiness.assess(self.L, self.C, "mathA")["strength"], "low")
        self.mastery(0.7, obs=20)
        self.assertEqual(readiness.assess(self.L, self.C, "mathA")["strength"], "high")
        self.assertGreaterEqual(len(readiness.assess(self.L, self.C, "mathA")["caveats"]), 2)

    def test_weakest_items_and_unresolved_errors_reported(self):
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(
            item_mastery={"S1.1": {"p_mastery": 0.2, "observations": 3}, "S2.1": {"p_mastery": 0.9, "observations": 3}, "S3.1": {"p_mastery": 0.4, "observations": 3}},
            error_patterns=[{"id": "e", "stage_id": "S1", "source_phase": "test", "cause": "slip", "slot": 1, "resolved": False}]))
        r = readiness.assess(self.L, self.C, "mathA")
        self.assertEqual([w["item_id"] for w in r["weakest_items"]], ["S1.1", "S3.1"])
        self.assertEqual(r["evidence"]["unresolved_errors"], 1)

    def test_recent_mocks_are_listed_but_do_not_move_the_band(self):
        self.mastery(0.4)
        before = readiness.assess(self.L, self.C, "mathA")
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(mock_results=[
            {"date": "2026-10-01", "total_marks": 40, "awarded": 38, "percent": 95.0, "minutes": 40},
            {"date": "2026-10-02", "total_marks": 40, "awarded": 39, "percent": 97.5, "minutes": 40}]))
        after = readiness.assess(self.L, self.C, "mathA")
        self.assertEqual(after["band"], before["band"])
        self.assertEqual([m["percent"] for m in after["evidence"]["recent_mocks"]], [95.0, 97.5])
        self.assertTrue(any("Mock papers" in c for c in after["caveats"]))

    def test_not_itemised_is_not_enough_evidence_and_errors(self):
        cmap = gs.read_json(f"{self.C}/mathA/curriculum_map.json")
        cmap["_syllabus_items"] = []
        with open(f"{self.C}/mathA/curriculum_map.json", "w") as f:
            json.dump(cmap, f)
        self.assertEqual(readiness.assess(self.L, self.C, "mathA")["band"], "not_enough_evidence")
        self.assertIn("error", readiness.assess(self.L, self.C, "ghost"))
        self.assertEqual(gs.run_step("readiness.py", ["{L}", "{C}"], self.fx, self.tmp)["exit"], 2)


if __name__ == "__main__":
    unittest.main()
