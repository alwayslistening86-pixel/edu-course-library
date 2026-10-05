"""confirm_access.py: one library-level answer satisfies gate 1 for every course (a per-course answer still works)."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import confirm_access  # noqa: E402
import gate_check  # noqa: E402
import golden_support as gs  # noqa: E402


class Access(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.course = f"{self.fx['C']}/mathA/course.json"
        d = gs.read_json(self.course)
        d["folder_access"] = {"status": "pending_confirmation"}
        with open(self.course, "w") as f:
            json.dump(d, f)

    def gate(self):
        r = gate_check._evaluate_gates(self.course, "NONE", self.fx["S"], self.fx["C"], "2026-10-05")
        return r, r["gates"]["1_folder_access"]

    def test_pending_course_is_blocked_until_the_library_is_confirmed(self):
        r, g = self.gate()
        self.assertEqual((r["can_proceed"], r["first_blocking_gate"], g["status"]), (False, "1_folder_access", "blocked"))
        self.assertIn("confirm_access.py", g["detail"])
        out = confirm_access.confirm(self.fx["C"], "isolated", "2026-10-05")
        self.assertEqual((out["status"], out["written"]), ("isolated_confirmed", True))
        r, g = self.gate()
        self.assertEqual(g["status"], "pass")
        self.assertIn("whole library", g["detail"])
        self.assertNotEqual(r.get("first_blocking_gate"), "1_folder_access")

    def test_other_courses_in_the_same_library_pass_too(self):
        confirm_access.confirm(self.fx["C"], "shared", "2026-10-05")
        other = f"{self.fx['C']}/mathB/course.json"
        d = gs.read_json(other)
        d["folder_access"] = {"status": "pending_confirmation"}
        with open(other, "w") as f:
            json.dump(d, f)
        r = gate_check._evaluate_gates(other, "NONE", self.fx["S"], self.fx["C"], "2026-10-05")
        self.assertEqual(r["gates"]["1_folder_access"]["value"], "shared_confirmed")

    def test_garbage_or_unknown_status_does_not_unlock(self):
        for text in ("{", json.dumps({"status": "pending_confirmation"}), json.dumps({"status": "yes please"}), "[]"):
            with open(f"{self.fx['C']}/access.json", "w") as f:
                f.write(text)
            self.assertEqual(self.gate()[1]["status"], "blocked", text)

    def test_bad_arguments(self):
        for args in ((self.fx["C"], "maybe", "2026-10-05"), (self.fx["C"], "isolated", "yesterday"), (self.tmp + "/nope", "isolated", "2026-10-05")):
            self.assertIn("error", confirm_access.confirm(*args))
        self.assertFalse(os.path.exists(f"{self.fx['C']}/access.json"))

    def test_re_answering_reports_the_previous_status(self):
        confirm_access.confirm(self.fx["C"], "shared", "2026-10-05")
        self.assertEqual(confirm_access.confirm(self.fx["C"], "isolated", "2026-10-06")["previous_status"], "shared_confirmed")

    def test_access_file_does_not_disturb_scripts_that_walk_the_courses_folder(self):
        confirm_access.confirm(self.fx["C"], "isolated", "2026-10-05")
        runs = [("roster_check.py", ["{P}", "{C}"]), ("status.py", ["{L}", "{C}"]), ("invariants.py", ["{L}", "{C}"]), ("cohort_status.py", ["{S}", "{C}"]),
                ("plan_estimate.py", ["{L}", "{C}", "--today", "2026-10-05"]), ("review_select.py", ["{L}", "{C}"]), ("audit_status.py", ["{C}"]),
                ("next_items.py", ["{L}", "{C}", "mathA"])]
        for script, args in runs:
            r = gs.run_step(script, args, self.fx, self.tmp)
            self.assertEqual(r["exit"], 0, f"{script}: {r['stdout']}")


if __name__ == "__main__":
    unittest.main()
