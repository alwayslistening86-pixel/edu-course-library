"""roster_apply.py: drop + wake, ledger advance, lock — decided by roster_check / cohort_status, written by the script."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import roster_apply as ra  # noqa: E402
from tutorlib import schema  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.P, self.C, self.S = self.fx["P"], self.fx["C"], self.fx["S"]

    def sj(self, cid):
        return gs.read_json(f"{self.S}/{cid}.json")

    def put(self, cid, **kw):
        p = f"{self.S}/{cid}.json"
        d = gs.read_json(p)
        d.update(kw)
        with open(p, "w") as f:
            json.dump(d, f)

    def profile(self, **kw):
        p = f"{self.P}/student_profile.json"
        d = gs.read_json(p)
        d.update(kw)
        with open(p, "w") as f:
            json.dump(d, f)


class Drop(Base):
    def test_drop_keeps_the_rest_of_the_file_and_wakes_what_it_unblocked(self):
        # mathA (level 2, active) is the floor; mathB (level 3) is dormant behind it
        before = self.sj("mathA")
        r = ra.drop(self.P, self.C, "mathA")
        self.assertEqual((r["previous_state"], r["written"]), ("active", True))
        after = self.sj("mathA")
        self.assertEqual({k: v for k, v in after.items() if k != "roster_state"}, {k: v for k, v in before.items() if k != "roster_state"})
        self.assertEqual(after["roster_state"], "dropped")
        self.assertIn("mathB", r["woke"])
        self.assertEqual(self.sj("mathB")["roster_state"], "active")
        self.assertEqual(schema.validate(self.sj("mathA"), "subjects"), [])

    def test_preview_reports_the_consequence_and_writes_nothing(self):
        before = (self.sj("mathA"), self.sj("mathB"))
        r = ra.drop_preview(self.P, self.C, "mathA")
        self.assertEqual((r["action"], r["written"], r["previous_state"]), ("drop_preview", False, "active"))
        self.assertIn("mathB", r["would_wake"])
        self.assertEqual((self.sj("mathA"), self.sj("mathB")), before)
        self.assertIn("error", ra.drop_preview(self.P, self.C, "nope"))
        self.assertTrue(ra.drop_preview(self.P, self.C, "design")["already_dropped"])

    def test_refusals(self):
        self.assertIn("error", ra.drop(self.P, self.C, "nope"))
        self.assertIn("error", ra.drop(self.P, self.C, "../x"))
        self.assertTrue(ra.drop(self.P, self.C, "design")["already_dropped"])             # fixture: design is already dropped
        self.put("mathA", syllabus_status={"S1": "pass", "S2": "pass", "S3": "pass"}, exam_status="passed")
        self.assertIn("complete", ra.drop(self.P, self.C, "mathA")["error"])
        solo = f"{self.C}/solo/course.json"
        course = gs.read_json(solo)
        course["grounding_status"] = "suspended_ungrounded"
        with open(solo, "w") as f:
            json.dump(course, f)
        self.assertIn("suspended", ra.drop(self.P, self.C, "solo")["error"])
        self.assertEqual(self.sj("solo")["roster_state"], "active")

    def test_consent_revoked_changes_nothing(self):
        pf = gs.read_json(f"{self.P}/student_profile.json")
        pf["consent"]["status"] = "revoked"
        with open(f"{self.P}/student_profile.json", "w") as f:
            json.dump(pf, f)
        r = ra.drop(self.P, self.C, "mathA")
        self.assertFalse(r["written"])
        self.assertEqual(self.sj("mathA")["roster_state"], "active")


class Advance(Base):
    def finish(self, cid):
        n = len(gs.read_json(f"{self.C}/{cid}/course.json")["stage_ladder"])
        self.put(cid, syllabus_status={f"S{i}": "pass" for i in range(1, n + 1)}, exam_status="passed")

    def test_ledger_rises_and_the_unlocked_level_wakes(self):
        self.finish("mathA")
        r = ra.advance(self.P, self.C)
        self.assertEqual((r["from"], r["to"], r["written"]), (1, 2, True))
        self.assertEqual(gs.read_json(f"{self.P}/student_profile.json")["highest_level_cleared"], 2)
        self.assertEqual(r["woke"], ["mathB"])
        self.assertEqual(self.sj("mathB")["roster_state"], "active")

    def test_nothing_new_cleared_changes_nothing_and_never_lowers(self):
        before = gs.read_json(f"{self.P}/student_profile.json")
        r = ra.advance(self.P, self.C)
        self.assertEqual((r["written"], r["woke"]), (False, []))
        self.assertEqual(gs.read_json(f"{self.P}/student_profile.json"), before)
        self.profile(highest_level_cleared=5)
        self.finish("mathA")
        self.assertEqual(ra.advance(self.P, self.C)["to"], 5)
        self.assertEqual(gs.read_json(f"{self.P}/student_profile.json")["highest_level_cleared"], 5)


class Lock(Base):
    def test_locks_live_courses_and_refuses_the_rest_atomically(self):
        r = ra.lock(self.P, ["mathA", "solo"])
        self.assertEqual(r["locked"], ["mathA", "solo"])
        self.assertEqual((self.sj("mathA")["roster_state"], self.sj("solo")["roster_state"]), ("dormant", "dormant"))
        self.put("mathA", roster_state="active")
        bad = ra.lock(self.P, ["mathA", "design"])                      # design is dropped: nothing may change
        self.assertIn("error", bad)
        self.assertEqual(self.sj("mathA")["roster_state"], "active")
        self.assertIn("error", ra.lock(self.P, []))
        self.assertIn("error", ra.lock(self.P, ["ghost"]))


class Cli(Base):
    def test_usage_and_ledger_entries(self):
        script = os.path.join(gs.SCRIPTS, "roster_apply.py")
        p = subprocess.run([sys.executable, script], capture_output=True, text=True)
        self.assertEqual(p.returncode, 2)
        p = subprocess.run([sys.executable, script, "drop", self.P, self.C, "mathA"], capture_output=True, text=True)
        self.assertEqual(p.returncode, 0, p.stdout)
        with open(f"{self.P}/.session_ledger.jsonl") as f:
            entries = [json.loads(line) for line in f]
        self.assertTrue(any(e["action"] == "set_roster_state" and e["detail"]["new"] == "dropped" for e in entries))


if __name__ == "__main__":
    unittest.main()
