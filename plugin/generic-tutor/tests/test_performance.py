"""E-25: the per-turn scripts stay fast on a large library (100 courses, 5 learners, 20 enrolments each).

The ceiling is deliberately generous (CI runners are slow and noisy): it catches an accidental quadratic or
a per-course subprocess, not a 20% slowdown. Interpreter start-up is included in every timing.
"""
import os
import shutil
import sys
import tempfile
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import golden_support as gs  # noqa: E402

CEILING_SECONDS = 2.0
COURSES = 100
LEARNERS = 5
PER_LEARNER = 20


def build_large(tmp):
    fx = gs.build_fixture(tmp)
    courses = fx["C"]
    ids = []
    for i in range(COURSES):
        cid = f"c{i:03d}"
        gs.build_course(courses, cid, level=1 + i % 4, stages=("S1", "S2", "S3", "S4"))
        ids.append(cid)
    for n in range(LEARNERS):
        learner = os.path.join(tmp, "profile", f"l{n}")
        gs._w(os.path.join(learner, "student_profile.json"), {
            "schema_version": 2, "learner_id": f"l{n}", "consent": {"status": "granted"}, "roster": {"max_incomplete_courses": 99},
            "highest_level_cleared": 0, "session_slot": 40, "capabilities": {}})
        for k in range(PER_LEARNER):
            cid = ids[(n * 7 + k) % COURSES]
            gs._w(os.path.join(learner, "subjects", f"{cid}.json"), {
                "schema_version": 5, "course_id": cid, "roster_state": "active", "cohort_id": 1 + int(cid[1:]) % 4,
                "syllabus_status": {"S1": "pass", "S2": "unsat", "S3": "unsat", "S4": "unsat"}, "notices_acknowledged": [],
                "current_stage": "S2", "current_phase": "practice", "exam_status": "locked", "confidence": 0.5,
                "error_patterns": [], "item_mastery": {}, "remediation": {}, "last_session_summary": "", "last_updated": "2026-10-01"})
    fx["L"] = os.path.join(tmp, "profile", "l0")
    fx["S"] = os.path.join(fx["L"], "subjects")
    return fx


class Speed(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = os.path.realpath(tempfile.mkdtemp())
        cls.fx = build_large(cls.tmp)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, True)

    def timed(self, script, args):
        start = time.perf_counter()
        r = gs.run_step(script, args, self.fx, self.tmp)
        elapsed = time.perf_counter() - start
        self.assertEqual(r["exit"], 0, f"{script}: {r['stdout']}")
        self.assertLess(elapsed, CEILING_SECONDS, f"{script} took {elapsed:.2f}s")

    def test_per_turn_scripts(self):
        c0 = sorted(f[:-5] for f in os.listdir(self.fx["S"]) if f.endswith(".json"))[0]
        self.timed("cohort_status.py", ["{S}", "{C}"])
        self.timed("roster_check.py", ["{L}", "{C}"])
        self.timed("status.py", ["{L}", "{C}"])
        self.timed("invariants.py", ["{L}", "{C}"])
        self.timed("review_select.py", ["{L}", "{C}"])
        self.timed("plan_estimate.py", ["{L}", "{C}", "--today", "2026-10-04"])
        self.timed("next_items.py", ["{L}", "{C}", c0])
        self.timed("gate_check.py", [f"{{C}}/{c0}/course.json", f"{{S}}/{c0}.json", "{S}", "{C}", "2026-10-04"])


if __name__ == "__main__":
    unittest.main()
