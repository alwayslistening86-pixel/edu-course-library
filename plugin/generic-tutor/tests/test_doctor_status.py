"""P-13 /doctor and C-06 /status."""
import json
import os
import shutil
import sys
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import doctor  # noqa: E402
import golden_support as gs  # noqa: E402
import status  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        os.makedirs(os.path.join(self.tmp, ".tutor-scripts"), exist_ok=True)
        with open(os.path.join(self.tmp, ".tutor-scripts", ".manifest.json"), "w") as f:
            json.dump({"plugin_version": "9.9.9", "files": [], "packages": []}, f)

    def edit(self, path, fn):
        d = gs.read_json(path)
        fn(d)
        with open(path, "w") as f:
            json.dump(d, f)


class Doctor(Base):
    def by_name(self, res):
        return {c["name"]: c for c in res["checks"]}

    def test_healthy_install(self):
        res = doctor.run(self.tmp)
        names = self.by_name(res)
        self.assertTrue(res["ok"], res["checks"])
        self.assertEqual(names["data-root"]["status"], "ok")
        self.assertEqual(names["learner-schema:amy"]["status"], "ok")
        self.assertEqual(names["consent:amy"]["status"], "ok")

    def test_missing_deployed_file_fails(self):
        self.edit(os.path.join(self.tmp, ".tutor-scripts", ".manifest.json"), lambda d: d.update(files=["ghost.py"]))
        res = doctor.run(self.tmp)
        self.assertFalse(res["ok"])
        self.assertEqual(self.by_name(res)["deployed-scripts"]["status"], "fail")

    def test_no_courses_dir_is_hard_failure_but_no_profile_is_only_a_warning(self):
        shutil.rmtree(self.fx["C"])
        self.assertEqual(self.by_name(doctor.run(self.tmp))["data-root"]["status"], "fail")
        self.setUp()
        shutil.rmtree(os.path.join(self.tmp, "profile"))
        res = doctor.run(self.tmp)
        self.assertEqual(self.by_name(res)["data-root"]["status"], "warn")
        self.assertTrue(res["ok"])

    def test_learner_problems_surface(self):
        self.edit(self.fx["S"] + "/mathA.json", lambda d: d.update(confidence="medium"))
        self.assertEqual(self.by_name(doctor.run(self.tmp))["learner-schema:amy"]["status"], "warn")

    def test_stale_lock_revoked_consent_and_newer_db(self):
        lock = self.fx["S"] + "/mathA.json.lock"
        open(lock, "w").close()
        old = time.time() - 3600
        os.utime(lock, (old, old))
        self.edit(self.fx["L"] + "/student_profile.json", lambda d: d["consent"].update(status="revoked"))
        import sqlite3
        con = sqlite3.connect(self.fx["L"] + "/tutor.sqlite3")
        con.execute("PRAGMA user_version = 99")
        con.commit()
        con.close()
        res = doctor.run(self.tmp)
        names = self.by_name(res)
        self.assertEqual(names["stale-locks:amy"]["status"], "warn")
        self.assertEqual(names["consent:amy"]["status"], "warn")
        self.assertEqual(names["history-db:amy"]["status"], "fail")
        self.assertFalse(res["ok"])

    def test_missing_writes_from_last_session_are_reported(self):
        gs.run_step("slot_advance.py", ["{P}/student_profile.json", "--min-gap-minutes", "0"], self.fx, self.tmp)
        gs.grade(self.fx, self.tmp, "mathA", "S2")
        gs.run_step("record_stage_result.py", ["apply", "{S}/mathA.json", "{C}/mathA/course.json", "S2", "pass"], self.fx, self.tmp)
        gs.run_step("slot_advance.py", ["{P}/student_profile.json", "--min-gap-minutes", "0"], self.fx, self.tmp)
        self.assertEqual(self.by_name(doctor.run(self.tmp))["last-session:amy"]["status"], "warn")

    def test_learner_filter_and_cli(self):
        res = doctor.run(self.tmp, learner="nobody")
        self.assertFalse(any(":" in c["name"] for c in res["checks"]))
        r = gs.run_step("doctor.py", ["--root", "{T}"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 0, r)
        self.assertEqual(gs.run_step("doctor.py", ["--bogus"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("doctor.py", ["--root", "{T}/nope"], self.fx, self.tmp)["exit"], 1)


class Status(Base):
    def test_summary_fields_and_next_action(self):
        s = status.build(self.fx["L"], self.fx["C"])
        self.assertEqual(s["learner"], "amy")
        self.assertEqual(s["session_slot"], 5)
        by = {c["course_id"]: c for c in s["courses"]}
        self.assertEqual((by["mathA"]["stages_passed"], by["mathA"]["stages_total"]), (1, 3))
        self.assertEqual(by["mathA"]["due_reviews"], 1)
        self.assertEqual(s["due_reviews_total"], 1)
        self.assertEqual(s["next_action"]["command"], "/review")
        self.assertTrue(by["solo"]["standalone"])
        self.assertIsNone(by["solo"]["level"])

    def test_next_action_without_due_cards(self):
        self.edit(self.fx["S"] + "/mathA_review_deck.json", lambda d: d["cards"][0].update(due_at_slot=99))
        s = status.build(self.fx["L"], self.fx["C"])
        self.assertTrue(s["next_action"]["command"].startswith("/continue "))

    def test_empty_and_dormant_only(self):
        for f in os.listdir(self.fx["S"]):
            os.unlink(os.path.join(self.fx["S"], f))
        self.assertEqual(status.build(self.fx["L"], self.fx["C"])["next_action"]["command"], "/add-course")

    def test_missing_profile_is_an_error_and_cli(self):
        self.assertIn("error", status.build(self.fx["L"] + "/nope", self.fx["C"]))
        r = gs.run_step("status.py", ["{L}", "{C}"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 0)
        self.assertEqual(gs.run_step("status.py", ["{L}"], self.fx, self.tmp)["exit"], 2)


if __name__ == "__main__":
    unittest.main()
