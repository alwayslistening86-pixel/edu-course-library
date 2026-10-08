"""session_state.py: the last hand-written progress fields now have a script owner."""
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
import session_state as ss  # noqa: E402
from tutorlib import ledger, schema  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.s = f"{self.fx['S']}/mathA.json"
        self.c = f"{self.fx['C']}/mathA/course.json"

    def get(self):
        return gs.read_json(self.s)

    def edit(self, fn, path=None):
        path = path or self.s
        d = gs.read_json(path)
        fn(d)
        with open(path, "w") as f:
            json.dump(d, f)

    def pending(self):
        """The legitimate route to a test: the course first waits in test_pending_convergence."""
        self.edit(lambda d: d.update(roster_state="test_pending_convergence"))

    def consent(self, status):
        self.edit(lambda d: d["consent"].update(status=status), f"{self.fx['L']}/student_profile.json")


class Phase(Base):
    def test_phase_changes_only_the_phase(self):
        self.pending()
        before = self.get()
        r = ss.set_phase(self.s, "test")
        self.assertEqual((r["old"], r["new"], r["written"]), ("practice", "test", True))
        after = self.get()
        self.assertEqual({k: v for k, v in after.items() if k != "current_phase"}, {k: v for k, v in before.items() if k != "current_phase"})
        self.assertIn("error", ss.set_phase(self.s, "exam"))


class Roster(Base):
    def test_only_live_states_can_be_switched(self):
        self.assertEqual(ss.set_roster(self.s, "test_pending_convergence")["new"], "test_pending_convergence")
        self.assertEqual(ss.set_roster(self.s, "active")["new"], "active")
        for bad in ("dormant", "dropped", "complete"):
            self.assertIn("error", ss.set_roster(self.s, bad), bad)
        for fn in ("mathB", "design"):                         # dormant / dropped enrolments cannot be moved here
            self.assertIn("error", ss.set_roster(f"{self.fx['S']}/{fn}.json", "active"), fn)
        self.assertEqual(gs.read_json(f"{self.fx['S']}/design.json")["roster_state"], "dropped")


class Exam(Base):
    def course_with_exam(self):
        self.edit(lambda d: d.update(exam={"enabled": True, "requires_all_stage_tests_passed": True}), self.c)
        self.edit(lambda d: d["syllabus_status"].update(S1="pass", S2="pass", S3="pass"))

    def test_exam_needs_an_exam_and_every_stage_done(self):
        self.assertIn("no exam", ss.set_exam(self.s, self.c, "available")["error"])
        self.edit(lambda d: d.update(exam={"enabled": True, "requires_all_stage_tests_passed": True}), self.c)
        self.assertIn("still open", ss.set_exam(self.s, self.c, "available")["error"])

    def test_state_machine(self):
        self.course_with_exam()
        self.assertIn("only from 'available'", ss.set_exam(self.s, self.c, "passed")["error"])
        self.assertTrue(ss.set_exam(self.s, self.c, "available")["written"])
        self.assertTrue(ss.set_exam(self.s, self.c, "passed")["written"])
        self.assertEqual(self.get()["exam_status"], "passed")
        self.assertTrue(ss.set_exam(self.s, self.c, "locked")["written"])
        self.assertIn("error", ss.set_exam(self.s, self.c, "maybe"))

    def test_withheld_practical_stage_does_not_block_the_exam(self):
        self.edit(lambda d: d.update(exam={"enabled": True}, practical_stages={"S3": ["share_images"]}), self.c)
        self.edit(lambda d: d["syllabus_status"].update(S1="pass", S2="pass", S3="withheld"))
        self.assertTrue(ss.set_exam(self.s, self.c, "available")["written"])


class Notices(Base):
    def test_ack_is_idempotent(self):
        r1 = ss.ack_notice(self.s, "n1", "2026-10-04")
        r2 = ss.ack_notice(self.s, "n1", "2026-10-05")
        self.assertTrue(r1["written"] and not r2["written"])
        self.assertEqual(self.get()["notices_acknowledged"], [{"id": "n1", "on": "2026-10-04"}])
        self.assertEqual(schema.validate(self.get(), "subjects"), [])
        self.assertIn("error", ss.ack_notice(self.s, "n2", "soon"))


class Note(Base):
    def test_note_is_normalised_bounded_and_signal_class(self):
        r = ss.write_note(self.s, "2026-10-04", "  Did   fractions.\n Next: common denominators.  ")
        self.assertTrue(r["written"])
        self.assertEqual(self.get()["last_session_summary"], "Did fractions. Next: common denominators.")
        self.assertIn("error", ss.write_note(self.s, "2026-10-04", "   "))
        self.assertIn("error", ss.write_note(self.s, "2026-10-04", "x" * 401))
        self.consent("limited")
        self.assertFalse(ss.write_note(self.s, "2026-10-04", "kept out")["written"])
        self.assertNotEqual(self.get()["last_session_summary"], "kept out")

    def test_progress_class_survives_limited_but_not_revoked(self):
        self.pending()
        self.consent("limited")
        self.assertTrue(ss.set_phase(self.s, "test")["written"])
        self.consent("revoked")
        self.assertFalse(ss.set_phase(self.s, "lesson")["written"])
        self.assertEqual(self.get()["current_phase"], "test")


class TestGate(Base):
    """B-04.5f: entering a stage test needs the evidence the cohort rule asks for."""

    def test_an_active_course_cannot_jump_to_its_test_and_nothing_is_written(self):
        before = self.get()
        r = ss.set_phase(self.s, "test")
        self.assertIn("test_pending_convergence", r["error"])
        self.assertEqual(self.get(), before)

    def test_lesson_and_practice_are_unrestricted_and_so_is_resuming_a_test(self):
        self.assertTrue(ss.set_phase(self.s, "lesson")["written"])
        self.assertTrue(ss.set_phase(self.s, "practice")["written"])
        self.edit(lambda d: d.update(roster_state="active", current_phase="test"))      # a test cut off earlier
        r = ss.set_phase(self.s, "test")                                                # resuming it: already in test, so no gate
        self.assertNotIn("error", r)
        self.assertEqual((r["old"], r["new"]), ("test", "test"))

    def test_the_cohort_must_have_converged(self):
        self.pending()
        mate = f"{self.fx['S']}/mathB.json"
        self.assertTrue(os.path.exists(mate))                                           # the fixture's second course: a missing file must fail, not skip
        self.edit(lambda d: d.update(cohort_id=2, roster_state="active"), mate)
        self.edit(lambda d: d.update(cohort_id=2))
        r = ss.set_phase(self.s, "test", self.fx["C"])
        self.assertIn("still waiting on mathB", r.get("error", ""), r)
        self.edit(lambda d: d.update(roster_state="test_pending_convergence"), mate)
        r = ss.set_phase(self.s, "test", self.fx["C"])
        self.assertEqual(r.get("gate"), "cohort converged", r)

    def test_without_a_findable_courses_folder_the_roster_rule_still_applies_and_the_gap_is_said(self):
        self.pending()
        r = ss.set_phase(self.s, "test")
        self.assertIn("not checked", r["gate"])
        self.assertTrue(r["written"])


class Cli(Base):
    def test_cli_and_ledger(self):
        self.pending()
        ok = gs.run_step("session_state.py", ["phase", "{S}/mathA.json", "test"], self.fx, self.tmp)
        self.assertEqual(ok["exit"], 0)
        self.assertEqual(gs.run_step("session_state.py", ["phase", "{S}/mathA.json", "nope"], self.fx, self.tmp)["exit"], 1)
        self.assertEqual(gs.run_step("session_state.py", ["frobnicate"], self.fx, self.tmp)["exit"], 2)
        p = subprocess.run([sys.executable, os.path.join(os.path.dirname(HERE), "scripts", "session_state.py"), "note", self.s, "2026-10-04"],
                           input='Said "hi"; $(touch PWNED)', capture_output=True, text=True, cwd=self.tmp)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertEqual(self.get()["last_session_summary"], 'Said "hi"; $(touch PWNED)')
        self.assertFalse([f for f in os.listdir(self.tmp) if f.startswith("PWNED")])
        self.assertIn("session_state.py", [e["script"] for e in ledger.read(self.fx["L"])])


if __name__ == "__main__":
    unittest.main()


class PassEndsTheWait(Base):
    """record_stage_result: a pass returns a waiting course to active, so it is not 'ready to test' for its NEXT stage."""

    def test_pass_resets_test_pending_convergence_but_fail_keeps_it(self):
        import record_stage_result as rsr
        ss.set_roster(self.s, "test_pending_convergence")
        r = rsr.apply(self.s, self.c, "S2", "fail")
        self.assertNotIn("roster_state_reset", r)
        self.assertEqual(self.get()["roster_state"], "test_pending_convergence")      # the failed course stays the bottleneck
        r = rsr.apply(self.s, self.c, "S2", "pass")
        self.assertEqual(r["roster_state_reset"], "active")
        self.assertEqual((self.get()["roster_state"], self.get()["current_stage"], self.get()["current_phase"]), ("active", "S3", "lesson"))

    def test_pass_does_not_touch_other_states(self):
        import record_stage_result as rsr
        rsr.apply(self.s, self.c, "S2", "pass")
        self.assertEqual(self.get()["roster_state"], "active")
        self.edit(lambda d: d.update(roster_state="dropped"))
        rsr.apply(self.s, self.c, "S3", "pass")
        self.assertEqual(self.get()["roster_state"], "dropped")

    def test_cohort_convergence_is_not_trivially_satisfied_after_a_pass(self):
        import cohort_status
        import record_stage_result as rsr
        ss.set_roster(self.s, "test_pending_convergence")
        peer = f"{self.fx['S']}/design.json"
        self.edit(lambda d: d.update(roster_state="active"), peer)      # a same-cohort peer still mid-lesson
        cohorts, _ = cohort_status.compute_cohorts(self.fx["S"], self.fx["C"])
        self.assertFalse(cohorts["2"]["converged"])
        rsr.apply(self.s, self.c, "S2", "pass")
        cohorts, _ = cohort_status.compute_cohorts(self.fx["S"], self.fx["C"])
        mathA = next(m for m in cohorts["2"]["members"] if m["course_id"] == "mathA")
        self.assertFalse(mathA["test_ready"])
