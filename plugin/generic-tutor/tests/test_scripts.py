"""
Regression tests for the generic-tutor scripts. Stdlib only.

Run from the plugin root:
    python3 -m unittest discover tests -v

Each test builds its fixtures in a temp dir, so nothing here touches a real /EDU folder.
The tests are named after the defect they pin down (see DESIGN_NOTES.md, v1.1.2).
"""
import datetime
import json
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

import cohort_status  # noqa: E402
import gate_check  # noqa: E402
import resume_enrollment  # noqa: E402
import review_math  # noqa: E402
import roster_check  # noqa: E402
import slot_advance  # noqa: E402
import bootstrap_scripts  # noqa: E402


def _read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _load(path):
    return json.loads(_read(path))


def _write(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


class Learner:
    """A throwaway learner profile + courses dir."""

    def __init__(self, tmp, cap=2, cleared=0):
        self.profile = os.path.join(tmp, "profile")
        self.subjects = os.path.join(self.profile, "subjects")
        self.courses = os.path.join(tmp, "courses")
        os.makedirs(self.subjects)
        os.makedirs(self.courses)
        _write(os.path.join(self.profile, "student_profile.json"),
               {"roster": {"max_incomplete_courses": cap}, "highest_level_cleared": cleared})

    def course(self, cid, stages=3, level=2, exam=False, grounding="verified"):
        _write(os.path.join(self.courses, cid, "course.json"), {
            "stage_ladder": [f"S{i}" for i in range(stages)], "academic_level": level,
            "grounding_status": grounding, "exam": {"enabled": exam},
            "folder_access": {"status": "isolated_confirmed"}, "currency": "live",
            "last_live_recheck": "2026-09-18"})

    def enrol(self, cid, state, passed, stages=3, cohort=2, exam_status="locked"):
        _write(os.path.join(self.subjects, f"{cid}.json"), {
            "course_id": cid, "roster_state": state, "cohort_id": cohort, "current_stage": "S0",
            "syllabus_status": {f"S{i}": ("pass" if i < passed else "unsat") for i in range(stages)},
            "exam_status": exam_status, "confidence": "medium", "error_patterns": ["x"],
            "last_session_summary": "kept"})

    def cohort(self, cohort=2):
        cohorts, _ = cohort_status.compute_cohorts(self.subjects, self.courses)
        return cohorts[str(cohort)]

    def path(self, cid):
        return os.path.join(self.subjects, f"{cid}.json")

    def cpath(self, cid):
        return os.path.join(self.courses, cid, "course.json")


class TmpCase(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.tmp = self._td.name
        self.addCleanup(self._td.cleanup)
        self.L = Learner(self.tmp)


class CompletedCourseTests(TmpCase):
    def test_finished_course_is_not_a_bottleneck(self):
        L = self.L
        L.course("A"); L.enrol("A", "active", 3)
        L.course("B"); L.enrol("B", "test_pending_convergence", 2)
        c = L.cohort()
        self.assertTrue(c["converged"])
        self.assertIsNone(c["bottleneck"])
        self.assertEqual(c["waiting_on"], [])

    def test_finished_course_still_listed_as_member(self):
        L = self.L
        L.course("A"); L.enrol("A", "active", 3)
        m = {x["course_id"]: x for x in L.cohort()["members"]}
        self.assertTrue(m["A"]["complete"])
        self.assertFalse(m["A"]["eligible"])

    def test_finished_course_frees_roster_slot(self):
        L = self.L
        L.course("A"); L.enrol("A", "active", 3)
        L.course("B"); L.enrol("B", "test_pending_convergence", 2)
        r = roster_check.compute(L.profile, L.courses)
        self.assertEqual(r["roster_occupancy"], 1)
        self.assertTrue(r["can_add_course"])

    def test_exam_pending_is_not_complete(self):
        L = self.L
        L.course("A", exam=True); L.enrol("A", "active", 3, exam_status="available")
        self.assertFalse(L.cohort()["members"][0]["complete"])
        L.enrol("A", "active", 3, exam_status="passed")
        self.assertTrue(L.cohort()["members"][0]["complete"])

    def test_empty_ladder_is_never_complete(self):
        self.assertFalse(cohort_status.is_complete({"stage_ladder": []}, {"syllabus_status": {}}))


class LevelClearingTests(TmpCase):
    def test_dropped_unfinished_does_not_block_level_clearing(self):
        L = self.L
        for cid in "AB":
            L.course(cid); L.enrol(cid, "active", 3)
        L.course("C"); L.enrol("C", "dropped", 1)
        c = L.cohort()
        self.assertTrue(c["all_complete"])
        self.assertEqual(c["excluded_members"], [{"course_id": "C", "reason": "dropped, unfinished"}])
        self.assertEqual(c["blocking_members"], [])

    def test_suspended_unfinished_does_not_block(self):
        L = self.L
        L.course("A"); L.enrol("A", "active", 3)
        L.course("S", grounding="suspended_ungrounded"); L.enrol("S", "active", 1)
        c = L.cohort()
        self.assertTrue(c["all_complete"])
        self.assertEqual(c["excluded_members"][0]["course_id"], "S")

    def test_active_or_dormant_unfinished_blocks(self):
        L = self.L
        L.course("A"); L.enrol("A", "active", 3)
        L.course("B"); L.enrol("B", "active", 1)
        c = L.cohort()
        self.assertFalse(c["all_complete"])
        self.assertEqual(c["blocking_members"], ["B"])

    def test_nothing_complete_is_not_cleared(self):
        L = self.L
        L.course("C"); L.enrol("C", "dropped", 1)
        self.assertFalse(L.cohort()["all_complete"])

    def test_dropped_but_complete_still_counts(self):
        L = self.L
        L.course("A"); L.enrol("A", "dropped", 3)
        self.assertTrue(L.cohort()["all_complete"])


class ReviewMathTests(unittest.TestCase):
    def test_card_recovers_from_two_lapses(self):
        i, e, l = 1, 2.3, 0
        for _ in range(2):
            r = review_math.compute(i, e, l, 0, False)
            i, e, l = r["interval_sessions"], r["ease"], r["lapses"]
        self.assertEqual((i, e, l), (1, 1.9, 2))
        seen = []
        for _ in range(6):
            r = review_math.compute(i, e, l, 0, True)
            i, e, l = r["interval_sessions"], r["ease"], r["lapses"]
            seen.append(i)
        self.assertEqual(seen, sorted(set(seen)), "interval must strictly grow on every correct recall")

    def test_correct_always_grows_until_cap(self):
        cap = review_math.MAX_INTERVAL_SESSIONS
        for old in range(1, cap):
            for ease in (1.3, 1.5, 1.9, 2.1, 2.3, 2.5):
                new = review_math.compute(old, ease, 0, 0, True)["interval_sessions"]
                self.assertGreater(new, old, (old, ease))
                self.assertLessEqual(new, cap)

    def test_interval_is_capped(self):
        self.assertEqual(review_math.compute(review_math.MAX_INTERVAL_SESSIONS, 2.5, 0, 0, True)["interval_sessions"],
                         review_math.MAX_INTERVAL_SESSIONS)

    def test_lapse_resets_and_ease_floor(self):
        r = review_math.compute(20, 1.3, 4, 10, False)
        self.assertEqual((r["interval_sessions"], r["ease"], r["lapses"], r["due_at_slot"]), (1, 1.3, 5, 11))

    def test_ease_recovers_and_stays_in_bounds(self):
        self.assertGreater(review_math.compute(3, 1.9, 2, 0, True)["ease"], 1.9)
        self.assertLessEqual(review_math.compute(3, 2.5, 0, 0, True)["ease"], review_math.EASE_CEIL)

    def test_half_up_rounding(self):
        # 5 * 1.7 = 8.5 -> 9 (banker's round would give 8)
        self.assertEqual(review_math.compute(5, 2.3, 0, 0, True)["interval_sessions"], 9)


class SlotCounterTests(TmpCase):
    def _profile(self, **extra):
        p = os.path.join(self.tmp, "student_profile.json")
        _write(p, dict({"learner_id": "x"}, **extra))
        return p

    def test_missing_counter_starts_at_zero_and_advances(self):
        p = self._profile()
        r = slot_advance.advance(p)
        self.assertEqual((r["previous_slot"], r["current_slot"]), (0, 1))
        self.assertEqual(_load(p)["learner_id"], "x")

    def test_double_run_in_one_sitting_counts_once(self):
        p = self._profile()
        t0 = datetime.datetime(2026, 9, 18, 10, 0, tzinfo=datetime.timezone.utc)
        slot_advance.advance(p, now=t0)
        r = slot_advance.advance(p, now=t0 + datetime.timedelta(minutes=5))
        self.assertIn("skipped", r)
        self.assertEqual(r["current_slot"], 1)

    def test_next_day_counts_again(self):
        p = self._profile()
        t0 = datetime.datetime(2026, 9, 18, 10, 0, tzinfo=datetime.timezone.utc)
        slot_advance.advance(p, now=t0)
        r = slot_advance.advance(p, now=t0 + datetime.timedelta(days=1))
        self.assertEqual(r["current_slot"], 2)

    def test_guard_can_be_disabled(self):
        p = self._profile()
        slot_advance.advance(p)
        self.assertEqual(slot_advance.advance(p, min_gap_minutes=0)["current_slot"], 2)

    def test_revoked_consent_writes_nothing(self):
        p = self._profile(consent={"status": "revoked"}, session_slot=7)
        before = _read(p)
        r = slot_advance.advance(p)
        self.assertEqual((r["skipped"], r["current_slot"]), ("consent revoked", 7))
        self.assertEqual(_read(p), before)

    def test_future_timestamp_does_not_freeze_counter(self):
        now = datetime.datetime(2026, 9, 18, 10, 0, tzinfo=datetime.timezone.utc)
        for delta in (datetime.timedelta(days=365), datetime.timedelta(minutes=90), datetime.timedelta(seconds=1)):
            p = self._profile(session_slot=4, session_slot_advanced_at=(now + delta).isoformat().replace("+00:00", "Z"))
            r = slot_advance.advance(p, now=now)
            self.assertEqual(r["current_slot"], 5, delta)
            self.assertNotIn("skipped", r, delta)
            self.assertEqual(_load(p)["session_slot_advanced_at"], now.isoformat().replace("+00:00", "Z"))

    def test_guard_boundaries(self):
        now = datetime.datetime(2026, 9, 18, 10, 0, tzinfo=datetime.timezone.utc)
        stamp = lambda d: (now - d).isoformat().replace("+00:00", "Z")
        # same instant and just inside the window skip; exactly at the window advances
        self.assertIn("skipped", slot_advance.advance(self._profile(session_slot_advanced_at=stamp(datetime.timedelta(0))), now=now))
        self.assertIn("skipped", slot_advance.advance(self._profile(session_slot_advanced_at=stamp(datetime.timedelta(minutes=179))), now=now))
        self.assertNotIn("skipped", slot_advance.advance(self._profile(session_slot_advanced_at=stamp(datetime.timedelta(minutes=180))), now=now))

    def test_garbled_timestamp_does_not_freeze_counter(self):
        p = self._profile(session_slot_advanced_at="not-a-date")
        self.assertEqual(slot_advance.advance(p)["current_slot"], 1)


class GateThreeTests(TmpCase):
    def _gate(self, state, passed=1, subj=True):
        L = self.L
        L.course("B"); L.enrol("B", state, passed)
        return gate_check.evaluate(L.cpath("B"), L.path("B") if subj else "NONE", L.subjects, L.courses, "2026-09-18")

    def test_teachable_states_pass(self):
        for st in ("active", "test_pending_convergence"):
            self.assertTrue(self._gate(st)["can_proceed"], st)

    def test_dropped_dormant_unknown_and_complete_are_blocked(self):
        for st in ("dropped", "dormant", "weird"):
            r = self._gate(st)
            self.assertFalse(r["can_proceed"], st)
            self.assertEqual(r["first_blocking_gate"], "3_level_lock")
        self.assertFalse(self._gate("active", passed=3)["can_proceed"])

    def test_dropped_message_points_to_resume_path(self):
        self.assertIn("/add-course", self._gate("dropped")["gates"]["3_level_lock"]["detail"])

    def test_no_enrollment_yet_is_the_defensive_create_case(self):
        self.assertTrue(self._gate("active", subj=False)["can_proceed"])

    def test_current_slot_is_echoed(self):
        p = os.path.join(self.L.profile, "student_profile.json")
        d = _load(p); d["session_slot"] = 12; _write(p, d)
        self.assertEqual(self._gate("active")["current_slot"], 12)


class ResumeTests(TmpCase):
    def test_resume_changes_only_state_and_date(self):
        L = self.L
        L.course("B"); L.enrol("B", "dropped", 2)
        before = _load(L.path("B"))
        r = resume_enrollment.resume(L.path("B"), L.cpath("B"), "active", "2026-09-18")
        self.assertTrue(r["resumed"])
        after = _load(L.path("B"))
        self.assertEqual(after["roster_state"], "active")
        for k in before:
            if k not in ("roster_state", "last_updated"):
                self.assertEqual(before[k], after[k], k)
        self.assertEqual(r["preserved_pass_count"], 2)

    def test_resumed_course_passes_gate_three(self):
        L = self.L
        L.course("B"); L.enrol("B", "dropped", 1)
        resume_enrollment.resume(L.path("B"), L.cpath("B"), "active", "2026-09-18")
        self.assertTrue(gate_check.evaluate(L.cpath("B"), L.path("B"), L.subjects, L.courses, "2026-09-18")["can_proceed"])

    def test_dormant_target_allowed(self):
        L = self.L
        L.course("B"); L.enrol("B", "dropped", 1)
        self.assertEqual(resume_enrollment.resume(L.path("B"), L.cpath("B"), "dormant", "d")["roster_state"], "dormant")

    def test_refuses_anything_not_dropped_and_writes_nothing(self):
        L = self.L
        L.course("B"); L.enrol("B", "active", 2)
        before = _read(L.path("B"))
        self.assertFalse(resume_enrollment.resume(L.path("B"), L.cpath("B"), "active", "d")["resumed"])
        self.assertEqual(_read(L.path("B")), before)

    def test_refuses_when_ladder_changed_while_dropped(self):
        L = self.L
        L.course("B", stages=4); L.enrol("B", "dropped", 1, stages=3)
        before = _read(L.path("B"))
        r = resume_enrollment.resume(L.path("B"), L.cpath("B"), "active", "d")
        self.assertFalse(r["resumed"])
        self.assertEqual(r["only_in_course"], ["S3"])
        self.assertEqual(_read(L.path("B")), before)

    def test_rejects_bad_target(self):
        L = self.L
        L.course("B"); L.enrol("B", "dropped", 1)
        self.assertFalse(resume_enrollment.resume(L.path("B"), L.cpath("B"), "dropped", "d")["resumed"])


class ReopenOnResumeTests(TmpCase):
    """drop -> clear level -> resume must not be a free pass (v1.1.4)."""

    def _setup(self, cleared=4):
        L = self.L
        _write(os.path.join(L.profile, "student_profile.json"),
               {"roster": {"max_incomplete_courses": 3}, "highest_level_cleared": cleared})
        L.course("A", level=4); L.enrol("A", "active", 3, cohort=4)          # finished, level 4
        L.course("C", level=4); L.enrol("C", "dropped", 1, cohort=4)         # dropped unfinished, level 4
        L.course("D", level=6); L.enrol("D", "active", 0, cohort=6)          # woke when level 4 cleared
        return L

    def test_level_clears_while_dropped_course_is_excluded(self):
        L = self._setup()
        self.assertTrue(L.cohort(4)["all_complete"])

    def test_plain_candidate_check_is_a_free_pass_the_old_loophole(self):
        L = self._setup()
        r = roster_check.compute(L.profile, L.courses, 4)
        self.assertEqual(r["lock_consequence"], "joins_freely")

    def test_resume_check_reopens_level_and_relocks_higher_courses(self):
        L = self._setup()
        r = roster_check.compute(L.profile, L.courses, 4, resume=True)
        self.assertTrue(r["reopens_level"])
        self.assertEqual(r["effective_highest_level_cleared"], 3)
        self.assertEqual(r["lock_consequence"], "becomes_new_floor")
        self.assertEqual(r["courses_that_would_lock"], ["D"])

    def test_resume_of_a_level_that_is_not_cleared_is_unchanged(self):
        L = self._setup(cleared=3)
        r = roster_check.compute(L.profile, L.courses, 4, resume=True)
        self.assertFalse(r["reopens_level"])
        self.assertEqual(r["effective_highest_level_cleared"], 3)

    def test_resume_enrollment_lowers_the_ledger_and_only_the_ledger(self):
        L = self._setup()
        pp = os.path.join(L.profile, "student_profile.json")
        before = _load(pp)
        r = resume_enrollment.resume(L.path("C"), L.cpath("C"), "active", "2026-09-18", pp, 3)
        self.assertTrue(r["resumed"])
        self.assertEqual(r["reopened_level"], {"from": 4, "to": 3})
        after = _load(pp)
        self.assertEqual(after["highest_level_cleared"], 3)
        for k in before:
            if k != "highest_level_cleared":
                self.assertEqual(before[k], after[k], k)

    def test_resume_enrollment_never_raises_the_ledger(self):
        L = self._setup()
        pp = os.path.join(L.profile, "student_profile.json")
        for bad in (4, 5, -1):
            before_s, before_p = _read(L.path("C")), _read(pp)
            r = resume_enrollment.resume(L.path("C"), L.cpath("C"), "active", "d", pp, bad)
            self.assertFalse(r["resumed"], bad)
            self.assertEqual((_read(L.path("C")), _read(pp)), (before_s, before_p), "nothing written")

    def test_reopen_flags_must_come_together(self):
        L = self._setup()
        pp = os.path.join(L.profile, "student_profile.json")
        self.assertFalse(resume_enrollment.resume(L.path("C"), L.cpath("C"), "active", "d", pp, None)["resumed"])

    def test_after_reopen_the_level_clears_again_only_on_completion(self):
        L = self._setup()
        pp = os.path.join(L.profile, "student_profile.json")
        resume_enrollment.resume(L.path("C"), L.cpath("C"), "active", "d", pp, 3)
        self.assertFalse(L.cohort(4)["all_complete"])
        L.enrol("C", "active", 3, cohort=4)
        self.assertTrue(L.cohort(4)["all_complete"])


class ReopenEdgeCaseTests(TmpCase):
    """v1.1.5: same-level course active, completed-course resume, ledger walk."""

    def _profile(self, cleared, cap=5):
        _write(os.path.join(self.L.profile, "student_profile.json"),
               {"roster": {"max_incomplete_courses": cap}, "highest_level_cleared": cleared})
        return os.path.join(self.L.profile, "student_profile.json")

    def test_same_level_active_course_does_not_hide_the_relock(self):
        L = self.L
        self._profile(2)
        L.course("W", level=2); L.enrol("W", "active", 0, cohort=2)     # added after level 2 cleared
        L.course("Z", level=3); L.enrol("Z", "active", 0, cohort=3)
        L.course("X", level=2); L.enrol("X", "dropped", 1, cohort=2)    # being resumed
        r = roster_check.compute(L.profile, L.courses, 2, resume=True, resume_course_id="X")
        self.assertTrue(r["reopens_level"])
        self.assertEqual(r["level_lock_floor"], 2)                       # the floor is W's level ...
        self.assertEqual(r["lock_consequence"], "becomes_new_floor")     # ... and Z is still re-locked
        self.assertEqual(r["courses_that_would_lock"], ["Z"])

    def test_reopen_with_nothing_above_locks_nothing(self):
        L = self.L
        self._profile(2)
        L.course("X", level=2); L.enrol("X", "dropped", 1, cohort=2)
        r = roster_check.compute(L.profile, L.courses, 2, resume=True, resume_course_id="X")
        self.assertEqual((r["lock_consequence"], r["courses_that_would_lock"]), ("joins_freely", []))

    def test_completed_dropped_course_reopens_nothing(self):
        L = self.L
        pp = self._profile(2)
        L.course("X", level=2); L.enrol("X", "dropped", 3, cohort=2)     # fully passed
        L.course("Z", level=3); L.enrol("Z", "active", 0, cohort=3)
        r = roster_check.compute(L.profile, L.courses, 2, resume=True, resume_course_id="X")
        self.assertTrue(r["already_complete"])
        self.assertFalse(r["reopens_level"])
        self.assertEqual(r["courses_that_would_lock"], [])
        self.assertEqual(r["effective_highest_level_cleared"], 2)

    def test_resume_enrollment_skips_lowering_for_a_complete_course(self):
        L = self.L
        pp = self._profile(2)
        L.course("X", level=2); L.enrol("X", "dropped", 3, cohort=2)
        before = _read(pp)
        r = resume_enrollment.resume(L.path("X"), L.cpath("X"), "active", "d", pp, 1)
        self.assertTrue(r["resumed"])
        self.assertTrue(r["already_complete"])
        self.assertIsNone(r["reopened_level"])
        self.assertEqual(_read(pp), before, "ledger untouched")
        self.assertEqual(_load(L.path("X"))["roster_state"], "active")

    def test_complete_dropped_course_is_reported_complete_not_dropped(self):
        L = self.L
        self._profile(2)
        L.course("X", level=2); L.enrol("X", "dropped", 3, cohort=2)
        g = gate_check.evaluate(L.cpath("X"), L.path("X"), L.subjects, L.courses, "2026-09-18")
        self.assertFalse(g["can_proceed"])
        self.assertIn("complete", g["gates"]["3_level_lock"]["detail"])

    def test_unfinished_course_still_reopens_with_course_flag(self):
        L = self.L
        self._profile(2)
        L.course("X", level=2); L.enrol("X", "dropped", 2, cohort=2)
        L.course("Z", level=3); L.enrol("Z", "active", 0, cohort=3)
        r = roster_check.compute(L.profile, L.courses, 2, resume=True, resume_course_id="X")
        self.assertFalse(r["already_complete"])
        self.assertTrue(r["reopens_level"])
        self.assertEqual(r["courses_that_would_lock"], ["Z"])

    def _walk(self, ledger, levels):
        """levels: {level: [(course, state, passed), ...]}"""
        L = self.L
        self._profile(ledger)
        for lvl, members in levels.items():
            for cid, state, passed in members:
                L.course(cid, level=lvl); L.enrol(cid, state, passed, cohort=lvl)
        cohorts, _ = cohort_status.compute_cohorts(L.subjects, L.courses)
        return cohort_status.level_walk(cohorts, ledger)

    def test_ledger_climbs_back_through_still_complete_higher_levels(self):
        w = self._walk(1, {2: [("X", "active", 3)], 3: [("Y", "active", 3)], 4: [("Q", "active", 1)]})
        self.assertEqual((w["to"], w["cleared_cohorts"], w["stopped_at"]), (3, [2, 3], 4))
        self.assertEqual(w["blocking"], ["Q"])

    def test_walk_stops_at_first_incomplete_cohort_even_if_a_later_one_is_complete(self):
        w = self._walk(1, {2: [("X", "active", 1)], 3: [("Y", "active", 3)]})
        self.assertEqual((w["to"], w["cleared_cohorts"], w["stopped_at"]), (1, [], 2))

    def test_walk_never_lowers_and_skips_empty_levels(self):
        self.assertEqual(self._walk(3, {2: [("X", "active", 3)]})["to"], 3)

    def test_walk_skips_levels_with_no_cohort(self):
        self.assertEqual(self._walk(1, {2: [("X", "active", 3)], 4: [("Y", "active", 3)]})["to"], 4)

    def test_walk_counts_excluded_dropped_members_like_v113(self):
        w = self._walk(1, {2: [("X", "active", 3), ("D", "dropped", 1)]})
        self.assertEqual(w["to"], 2)

    def test_cli_reports_level_ledger(self):
        import subprocess
        L = self.L
        self._profile(1)
        L.course("X", level=2); L.enrol("X", "active", 3, cohort=2)
        L.course("Y", level=3); L.enrol("Y", "active", 3, cohort=3)
        out = json.loads(subprocess.check_output([sys.executable, os.path.join(SCRIPTS, "cohort_status.py"), L.subjects, L.courses]))
        self.assertEqual(out["level_ledger"]["suggested_highest_level_cleared"], 3)
        self.assertEqual(out["level_ledger"]["stored"], 1)

    def test_full_sequence_lower_then_climb_back(self):
        """levels 1-3 cleared; resume unfinished X at level 2; ledger -> 1; finish X; ledger -> 3 again."""
        L = self.L
        pp = self._profile(3)
        L.course("A", level=1); L.enrol("A", "active", 3, cohort=1)
        L.course("X", level=2); L.enrol("X", "dropped", 2, cohort=2)
        L.course("Y", level=3); L.enrol("Y", "active", 3, cohort=3)
        r = roster_check.compute(L.profile, L.courses, 2, resume=True, resume_course_id="X")
        self.assertTrue(r["reopens_level"])
        resume_enrollment.resume(L.path("X"), L.cpath("X"), "active", "d", pp, r["effective_highest_level_cleared"])
        self.assertEqual(_load(pp)["highest_level_cleared"], 1)
        L.enrol("X", "active", 3, cohort=2)                               # X finishes
        cohorts, _ = cohort_status.compute_cohorts(L.subjects, L.courses)
        self.assertEqual(cohort_status.level_walk(cohorts, 1)["to"], 3)


class VacuousLevelAndWakeTests(TmpCase):
    """v1.1.6: vacuous levels in the walk, candidate_state, wake-on-drop."""

    def _profile(self, cleared, cap=5):
        _write(os.path.join(self.L.profile, "student_profile.json"),
               {"roster": {"max_incomplete_courses": cap}, "highest_level_cleared": cleared})
        return os.path.join(self.L.profile, "student_profile.json")

    def _walk(self, ledger, levels):
        L = self.L
        self._profile(ledger)
        for lvl, members in levels.items():
            for cid, state, passed in members:
                L.course(cid, level=lvl, grounding="suspended_ungrounded" if state == "suspended" else "verified")
                L.enrol(cid, "active" if state == "suspended" else state, passed, cohort=lvl)
        cohorts, _ = cohort_status.compute_cohorts(L.subjects, L.courses)
        return cohort_status.level_walk(cohorts, ledger)

    # --- (a) vacuous level in the walk -------------------------------------------------------
    def test_walk_steps_over_a_level_holding_only_a_dropped_course(self):
        w = self._walk(0, {2: [("X", "dropped", 1)], 3: [("Z", "active", 3)]})
        self.assertEqual(w["to"], 3)
        self.assertIsNone(w["stopped_at"])
        self.assertEqual(w["cleared_cohorts"], [3])
        self.assertEqual(w["skipped_cohorts"], [{"cohort_id": 2, "excluded_members": ["X"]}])

    def test_walk_steps_over_a_level_holding_only_a_suspended_course(self):
        w = self._walk(0, {2: [("S", "suspended", 1)], 3: [("Z", "active", 3)]})
        self.assertEqual((w["to"], w["stopped_at"]), (3, None))

    def test_walk_still_stops_at_a_level_with_a_blocking_member(self):
        w = self._walk(0, {2: [("X", "dropped", 1), ("B", "active", 1)], 3: [("Z", "active", 3)]})
        self.assertEqual((w["to"], w["stopped_at"], w["blocking"]), (0, 2, ["B"]))

    def test_walk_still_stops_at_a_level_with_only_a_dormant_course(self):
        w = self._walk(0, {2: [("D", "dormant", 0)], 3: [("Z", "active", 3)]})
        self.assertEqual((w["to"], w["stopped_at"]), (0, 2))

    def test_vacuously_clear_flag_is_only_for_levels_with_nothing_finished_or_blocking(self):
        L = self.L
        L.course("A", level=2); L.enrol("A", "active", 3, cohort=2)               # finished: all_complete, not vacuous
        L.course("X", level=3); L.enrol("X", "dropped", 1, cohort=3)              # vacuous
        L.course("B", level=4); L.enrol("B", "active", 1, cohort=4)               # blocking
        cohorts, _ = cohort_status.compute_cohorts(L.subjects, L.courses)
        self.assertEqual([cohorts[k]["vacuously_clear"] for k in ("2", "3", "4")], [False, True, False])

    def test_cli_ledger_agrees_on_the_vacuous_level(self):
        import subprocess
        L = self.L
        self._profile(0)
        L.course("X", level=2); L.enrol("X", "dropped", 1, cohort=2)
        L.course("Z", level=3); L.enrol("Z", "active", 3, cohort=3)
        out = json.loads(subprocess.check_output([sys.executable, os.path.join(SCRIPTS, "cohort_status.py"), L.subjects, L.courses]))
        led = out["level_ledger"]
        self.assertEqual(led["suggested_highest_level_cleared"], 3)
        self.assertIsNone(led["stopped_at"])
        self.assertEqual(led["blocking"], [])

    # --- (b) candidate_state ------------------------------------------------------------------
    def test_candidate_above_the_floor_starts_dormant(self):
        L = self.L
        self._profile(0)
        L.course("A", level=2); L.enrol("A", "active", 0, cohort=2)
        r = roster_check.compute(L.profile, L.courses, 4)
        self.assertEqual((r["candidate_state"], r["locked_behind_level"]), ("dormant", 2))

    def test_candidate_above_a_dormant_only_floor_starts_dormant(self):
        L = self.L
        self._profile(0)
        L.course("D", level=2); L.enrol("D", "dormant", 0, cohort=2)
        r = roster_check.compute(L.profile, L.courses, 4)
        self.assertEqual((r["candidate_state"], r["locked_behind_level"]), ("dormant", 2))

    def test_candidate_at_or_below_the_floor_starts_active(self):
        L = self.L
        self._profile(0)
        L.course("A", level=2); L.enrol("A", "active", 0, cohort=2)
        for lvl in (1, 2):
            r = roster_check.compute(L.profile, L.courses, lvl)
            self.assertEqual((r["candidate_state"], r["locked_behind_level"]), ("active", None), lvl)

    def test_candidate_at_or_below_cleared_level_starts_active(self):
        L = self.L
        self._profile(3)
        L.course("A", level=4); L.enrol("A", "active", 0, cohort=4)
        r = roster_check.compute(L.profile, L.courses, 3)
        self.assertEqual(r["candidate_state"], "active")

    def test_candidate_with_empty_roster_starts_active(self):
        self._profile(0)
        self.assertEqual(roster_check.compute(self.L.profile, self.L.courses, 5)["candidate_state"], "active")

    def test_resumed_course_is_always_active(self):
        L = self.L
        self._profile(2)
        L.course("X", level=2); L.enrol("X", "dropped", 1, cohort=2)
        L.course("Z", level=3); L.enrol("Z", "active", 0, cohort=3)
        r = roster_check.compute(L.profile, L.courses, 2, resume=True, resume_course_id="X")
        self.assertEqual((r["candidate_state"], r["locked_behind_level"]), ("active", None))

    # --- (c) wake on drop ---------------------------------------------------------------------
    def test_dropping_the_floor_course_wakes_the_next_level(self):
        L = self.L
        self._profile(0)
        L.course("X", level=2); L.enrol("X", "active", 1, cohort=2)
        L.course("Z", level=3); L.enrol("Z", "dormant", 0, cohort=3)
        self.assertEqual(roster_check.compute(L.profile, L.courses)["wake_now"], [])   # X still holds the floor
        L.enrol("X", "dropped", 1, cohort=2)
        r = roster_check.compute(L.profile, L.courses)
        self.assertEqual(r["wake_now"], ["Z"])
        self.assertEqual(r["unfinished_level_floor"], 3)

    def test_drop_wakes_only_the_lowest_dormant_level(self):
        L = self.L
        self._profile(0)
        L.course("X", level=2); L.enrol("X", "dropped", 1, cohort=2)
        L.course("Z", level=3); L.enrol("Z", "dormant", 0, cohort=3)
        L.course("Q", level=4); L.enrol("Q", "dormant", 0, cohort=4)
        self.assertEqual(roster_check.compute(L.profile, L.courses)["wake_now"], ["Z"])

    def test_two_dormant_courses_at_the_lowest_level_both_wake(self):
        L = self.L
        self._profile(0)
        L.course("Z1", level=3); L.enrol("Z1", "dormant", 0, cohort=3)
        L.course("Z2", level=3); L.enrol("Z2", "dormant", 0, cohort=3)
        L.course("Q", level=4); L.enrol("Q", "dormant", 0, cohort=4)
        self.assertEqual(roster_check.compute(L.profile, L.courses)["wake_now"], ["Z1", "Z2"])

    def test_nothing_wakes_while_a_live_course_holds_a_lower_floor(self):
        L = self.L
        self._profile(0)
        L.course("X", level=2); L.enrol("X", "active", 0, cohort=2)
        L.course("Z", level=3); L.enrol("Z", "dormant", 0, cohort=3)
        self.assertEqual(roster_check.compute(L.profile, L.courses)["wake_now"], [])

    def test_dormant_course_at_or_below_the_cleared_level_wakes(self):
        L = self.L
        self._profile(3)
        L.course("Z", level=3); L.enrol("Z", "dormant", 0, cohort=3)
        self.assertEqual(roster_check.compute(L.profile, L.courses)["wake_now"], ["Z"])

    def test_suspended_and_finished_dormant_courses_are_not_woken_or_counted(self):
        L = self.L
        self._profile(0)
        L.course("S", level=3, grounding="suspended_ungrounded"); L.enrol("S", "dormant", 0, cohort=3)
        L.course("F", level=3); L.enrol("F", "dormant", 3, cohort=3)
        L.course("Q", level=4); L.enrol("Q", "dormant", 0, cohort=4)
        r = roster_check.compute(L.profile, L.courses)
        self.assertEqual((r["wake_now"], r["unfinished_level_floor"]), (["Q"], 4))

    def test_resuming_the_dropped_floor_course_relocks_the_woken_one(self):
        L = self.L
        self._profile(0)
        L.course("X", level=2); L.enrol("X", "dropped", 1, cohort=2)
        L.course("Z", level=3); L.enrol("Z", "active", 0, cohort=3)      # woken by the drop
        r = roster_check.compute(L.profile, L.courses, 2, resume=True, resume_course_id="X")
        self.assertEqual((r["lock_consequence"], r["courses_that_would_lock"]), ("becomes_new_floor", ["Z"]))

    # --- roster cap counts dormant courses ------------------------------------------------------
    def test_dormant_courses_hold_roster_slots(self):
        L = self.L
        self._profile(0, cap=2)
        L.course("A", level=2); L.enrol("A", "active", 0, cohort=2)
        L.course("D", level=3); L.enrol("D", "dormant", 0, cohort=3)
        r = roster_check.compute(L.profile, L.courses)
        self.assertEqual((r["roster_occupancy"], r["can_add_course"]), (2, False))

    def test_dormant_adds_cannot_bypass_the_cap(self):
        L = self.L
        self._profile(0, cap=2)
        L.course("A", level=2); L.enrol("A", "active", 0, cohort=2)
        L.course("D1", level=3); L.enrol("D1", "dormant", 0, cohort=3)
        self.assertFalse(roster_check.compute(L.profile, L.courses, 4)["can_add_course"])

    def test_waking_is_occupancy_neutral_and_locking_frees_nothing(self):
        L = self.L
        self._profile(0, cap=2)
        L.course("X", level=2); L.enrol("X", "active", 0, cohort=2)
        L.course("Z", level=3); L.enrol("Z", "dormant", 0, cohort=3)
        before = roster_check.compute(L.profile, L.courses)["roster_occupancy"]
        L.enrol("Z", "active", 0, cohort=3)                       # wake (or, reversed, lock)
        self.assertEqual(roster_check.compute(L.profile, L.courses)["roster_occupancy"], before)

    def test_dropped_complete_and_suspended_dormant_courses_hold_no_slot(self):
        L = self.L
        self._profile(0, cap=2)
        L.course("S", level=3, grounding="suspended_ungrounded"); L.enrol("S", "dormant", 0, cohort=3)
        L.course("F", level=3); L.enrol("F", "dormant", 3, cohort=3)
        L.course("X", level=2); L.enrol("X", "dropped", 1, cohort=2)
        r = roster_check.compute(L.profile, L.courses)
        self.assertEqual((r["roster_occupancy"], r["can_add_course"]), (0, True))

    def test_full_roster_message_can_name_live_and_dormant_courses(self):
        L = self.L
        self._profile(0, cap=2)
        L.course("A", level=2); L.enrol("A", "active", 0, cohort=2)
        L.course("D", level=3); L.enrol("D", "dormant", 0, cohort=3)
        r = roster_check.compute(L.profile, L.courses)
        self.assertFalse(r["can_add_course"])
        self.assertEqual([(c["course_id"], c["locked"]) for c in r["occupying_courses"]], [("A", False), ("D", True)])

    def test_roster_full_of_only_dormant_courses_still_names_them(self):
        L = self.L
        self._profile(0, cap=2)
        for cid in ("D1", "D2"):
            L.course(cid, level=3); L.enrol(cid, "dormant", 0, cohort=3)
        r = roster_check.compute(L.profile, L.courses)
        self.assertEqual((r["can_add_course"], r["eligible_courses"]), (False, []))
        self.assertEqual([c["course_id"] for c in r["occupying_courses"]], ["D1", "D2"])

    def test_over_cap_roster_after_upgrade_reports_excess_and_refuses_adds(self):
        L = self.L
        self._profile(0, cap=2)
        L.course("A", level=2); L.enrol("A", "active", 0, cohort=2)
        for cid in ("D1", "D2", "D3"):
            L.course(cid, level=3); L.enrol(cid, "dormant", 0, cohort=3)
        r = roster_check.compute(L.profile, L.courses)
        self.assertEqual((r["roster_occupancy"], r["max_incomplete_courses"], r["can_add_course"]), (4, 2, False))
        self.assertEqual(len(r["occupying_courses"]), 4)

    def test_wake_fields_present_with_no_dormant_courses(self):
        self._profile(0)
        r = roster_check.compute(self.L.profile, self.L.courses)
        self.assertEqual((r["wake_now"], r["dormant_courses"]), ([], []))


class BootstrapTests(TmpCase):
    def test_every_shipped_script_is_deployed(self):
        target = os.path.join(self.tmp, ".tutor-scripts")
        r = bootstrap_scripts.bootstrap(SCRIPTS, os.path.join(ROOT, ".claude-plugin", "plugin.json"), target)
        self.assertEqual(r["action"], "deployed_fresh")
        for name in ("slot_advance.py", "resume_enrollment.py", "cohort_status.py"):
            self.assertTrue(os.path.isfile(os.path.join(target, name)), name)


if __name__ == "__main__":
    unittest.main()
