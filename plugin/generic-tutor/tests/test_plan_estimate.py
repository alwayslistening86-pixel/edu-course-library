"""L-12 / K-20: plan_estimate.py and plan_target.py."""
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
import plan_estimate  # noqa: E402
import plan_target  # noqa: E402
from tutorlib import ledger, schema  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.L, self.C, self.S = self.fx["L"], self.fx["C"], self.fx["S"]
        self.edit(f"{self.L}/student_profile.json", lambda d: d.update(availability={"sessions_per_week": 2, "session_minutes": 60}))

    def edit(self, path, fn):
        d = gs.read_json(path)
        fn(d)
        with open(path, "w") as f:
            json.dump(d, f)

    def row(self, cid="mathA", today=None):
        r = plan_estimate.estimate(self.L, self.C, today)
        return next(c for c in r["courses"] if c["course_id"] == cid)


class Estimate(Base):
    def test_default_estimate_with_review_overhead(self):
        r = self.row()
        # mathA: S1 pass; S2, S3 remaining -> 2 stages * 3 = 6, + ceil(10%) = 1 -> 7
        self.assertEqual((r["stages_remaining"], r["slots_remaining_estimate"], r["weeks_remaining_estimate"]), (2, 7, 3.5))

    def test_course_overrides(self):
        self.edit(f"{self.C}/mathA/course.json", lambda d: d.update(slots_per_stage=5))
        self.assertEqual(self.row()["slots_remaining_estimate"], 11)       # 10 + 1
        self.edit(f"{self.C}/mathA/course.json", lambda d: d.update(slot_estimates={"S2": 4, "S3": 8}))
        self.assertEqual(self.row()["slots_remaining_estimate"], 14)       # 12 + 2

    def test_only_courses_that_can_draw_slots_are_counted(self):
        ids = {c["course_id"] for c in plan_estimate.estimate(self.L, self.C)["courses"]}
        self.assertEqual(ids, {"mathA", "solo"})                           # mathB dormant, design dropped

    def test_no_rate_gives_no_week_projection(self):
        self.edit(f"{self.L}/student_profile.json", lambda d: d.pop("availability"))
        r = plan_estimate.estimate(self.L, self.C)
        self.assertIsNone(r["sessions_per_week"])
        self.assertIsNone(r["courses"][0]["weeks_remaining_estimate"])

    def test_estimate_is_read_only_and_states_its_assumptions(self):
        def raw():
            with open(f"{self.S}/mathA.json", "rb") as f:
                return f.read()
        before = raw()
        r = plan_estimate.estimate(self.L, self.C, "2026-10-04")
        self.assertEqual(raw(), before)
        self.assertIn("rough estimates", r["assumptions"]["note"])


class Deadline(Base):
    def target(self, date):
        self.edit(f"{self.S}/mathA.json", lambda d: d.update(target={"date": date, "set_on": "2026-10-04"}))

    def test_feasibility_bands(self):
        # need 7 slots at 2/week: 4 weeks -> 8 available (tight: 8 >= 7 but < 8.75); 6 weeks -> 12 (on track); 2 weeks -> 4 (short)
        self.target("2026-11-01")
        self.assertEqual(self.row(today="2026-10-04")["target"]["feasibility"], "tight")
        self.target("2026-11-15")
        self.assertEqual(self.row(today="2026-10-04")["target"]["feasibility"], "on_track")
        self.target("2026-10-18")
        t = self.row(today="2026-10-04")["target"]
        self.assertEqual((t["feasibility"], t["shortfall_slots"]), ("short", 3))
        self.assertEqual(len(t["options"]), 3)
        self.assertIn("raise sessions per week to about 4", t["options"][0])

    def test_expired_target_is_reported_not_planned_around(self):
        self.target("2026-09-01")
        self.assertEqual(self.row(today="2026-10-04")["target"]["feasibility"], "expired")

    def test_no_today_means_no_deadline_maths(self):
        self.target("2026-11-01")
        self.assertNotIn("target", self.row())

    def test_unknown_without_a_rate(self):
        self.edit(f"{self.L}/student_profile.json", lambda d: d.pop("availability"))
        self.target("2026-11-01")
        self.assertEqual(self.row(today="2026-10-04")["target"]["feasibility"], "unknown")

    def test_bad_today(self):
        self.assertIn("error", plan_estimate.estimate(self.L, self.C, "yesterday"))


class Target(Base):
    def test_set_and_clear_round_trip_and_schema(self):
        p = f"{self.S}/mathA.json"
        r = plan_target.set_target(p, "2026-12-01", "2026-10-04")
        self.assertTrue(r["written"])
        d = gs.read_json(p)
        self.assertEqual(d["target"], {"date": "2026-12-01", "set_on": "2026-10-04"})
        self.assertEqual(schema.validate(d, "subjects"), [])
        self.assertTrue(plan_target.clear_target(p)["written"])
        self.assertNotIn("target", gs.read_json(p))
        self.assertFalse(plan_target.clear_target(p)["had_target"])

    def test_refusals(self):
        p = f"{self.S}/mathA.json"
        self.assertIn("past", plan_target.set_target(p, "2026-09-01", "2026-10-04")["error"])
        self.assertIn("ISO", plan_target.set_target(p, "next friday", "2026-10-04")["error"])
        self.assertIn("ISO", plan_target.set_target(p, "2026-13-45", "2026-10-04")["error"])
        self.assertNotIn("target", gs.read_json(p))

    def test_consent_and_ledger(self):
        p = f"{self.S}/mathA.json"
        self.edit(f"{self.L}/student_profile.json", lambda d: d["consent"].update(status="limited"))
        self.assertTrue(plan_target.set_target(p, "2026-12-01", "2026-10-04")["written"])      # progress class survives 'limited'
        self.edit(f"{self.L}/student_profile.json", lambda d: d["consent"].update(status="revoked"))
        r = plan_target.clear_target(p)
        self.assertFalse(r["written"])
        self.assertIn("target", gs.read_json(p))
        scripts = [e["script"] for e in ledger.read(self.L)]
        self.assertIn("plan_target.py", scripts)

    def test_cli(self):
        r = gs.run_step("plan_target.py", ["set", "{S}/mathA.json", "2026-12-01", "2026-10-04"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 0, r)
        self.assertEqual(gs.run_step("plan_target.py", ["set", "{S}/mathA.json", "2020-01-01", "2026-10-04"], self.fx, self.tmp)["exit"], 1)
        self.assertEqual(gs.run_step("plan_target.py", ["set"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("plan_estimate.py", ["{L}", "{C}", "--today", "2026-10-04"], self.fx, self.tmp)["exit"], 0)
        self.assertEqual(gs.run_step("plan_estimate.py", ["{L}"], self.fx, self.tmp)["exit"], 2)


if __name__ == "__main__":
    unittest.main()
