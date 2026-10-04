"""Consent enforcement matrix (E-05/E-06): every state writer x every consent status."""
import json
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import confidence_update  # noqa: E402
import error_log  # noqa: E402
import item_mastery  # noqa: E402
import record_stage_result  # noqa: E402
import remediation_state  # noqa: E402
import review_math  # noqa: E402
import slot_advance  # noqa: E402
import sqlite_store  # noqa: E402
from tutorlib import consent  # noqa: E402


def _w(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


def _r(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


class Base(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.root, True)
        self.learner = os.path.join(self.root, "profile", "amy")
        self.profile = os.path.join(self.learner, "student_profile.json")
        self.subj = os.path.join(self.learner, "subjects", "c1.json")
        self.deck = os.path.join(self.learner, "subjects", "c1_review_deck.json")
        self.course = os.path.join(self.root, "courses", "c1", "course.json")
        self.db = os.path.join(self.learner, "tutor.sqlite3")
        _w(self.subj, {"schema_version": 5, "course_id": "c1", "roster_state": "active", "cohort_id": 2,
                       "syllabus_status": {"S1": "unsat", "S2": "unsat"}, "current_stage": "S1",
                       "current_phase": "test", "confidence": 0.5, "error_patterns": [], "item_mastery": {},
                       "remediation": {}})
        _w(self.deck, {"schema_version": 1, "course_id": "c1", "cards": [
            {"id": "k1", "stage_id": "S1", "front": "f", "back": "b", "interval_sessions": 1, "due_at_slot": 2,
             "ease": 2.3, "lapses": 0}]})
        _w(self.course, {"stage_ladder": ["S1", "S2"]})

    def set_consent(self, status):
        if status is not None:
            _w(self.profile, {"consent": {"status": status}, "session_slot": 3})


class Matrix(Base):
    # (state under test) -> (progress writes persist?, scheduling persist?, signals persist?)
    EXPECT = {"granted": (True, True, True), "limited": (True, True, False), "revoked": (False, False, False)}

    def check_all(self, status):
        prog, sched, sig = self.EXPECT[status]
        self.set_consent(status)

        # SIGNAL writers
        before = _r(self.subj)
        r = confidence_update.apply(self.subj, "pass_clean", 1)
        self.assertEqual(r["written"], sig, (status, r))
        self.assertEqual(_r(self.subj)["confidence"] != before["confidence"], sig)
        self.assertIn("new_confidence", r)  # still computed for in-session use

        r = error_log.append(self.subj, "S1", "I1", "practice", "slip", "NONE", "n", 1)
        self.assertEqual(len(_r(self.subj)["error_patterns"]) == 1, sig, (status, r))
        r = item_mastery.observe(self.subj, "I1", True, 1)
        self.assertEqual("I1" in _r(self.subj)["item_mastery"], sig, (status, r))
        self.assertEqual(os.path.exists(self.db), sig, f"{status}: sqlite history")

        # PROGRESS writers
        r = record_stage_result.apply(self.subj, self.course, "S1", "pass")
        self.assertEqual(_r(self.subj)["syllabus_status"]["S1"] == "pass", prog, (status, r))
        remediation_state.record(self.subj, "S2", "slip", 2)
        self.assertEqual("S2" in _r(self.subj)["remediation"], prog)

        # SCHEDULING writers
        r = review_math.apply(self.deck, "k1", 4, True)
        self.assertEqual(_r(self.deck)["cards"][0]["interval_sessions"] != 1, sched, (status, r))
        r = slot_advance.advance(self.profile, min_gap_minutes=0)
        self.assertEqual(_r(self.profile)["session_slot"] == 4, sched, (status, r))

    def test_granted(self):
        self.check_all("granted")

    def test_limited(self):
        self.check_all("limited")

    def test_revoked(self):
        self.check_all("revoked")


class Edges(Base):
    def test_no_profile_means_granted(self):
        r = error_log.append(self.subj, "S1", "I1", "practice", "slip", "NONE", "n", 1)
        self.assertEqual(r["action"], "appended")

    def test_corrupt_profile_fails_closed(self):
        os.makedirs(self.learner, exist_ok=True)
        with open(self.profile, "w") as f:
            f.write("{not json")
        self.assertEqual(consent.status_for(self.subj), "revoked")
        r = record_stage_result.apply(self.subj, self.course, "S1", "pass")
        self.assertFalse(r["written"])
        self.assertEqual(_r(self.subj)["syllabus_status"]["S1"], "unsat")

    def test_unknown_status_fails_closed(self):
        self.set_consent("maybe")
        self.assertEqual(consent.status_for(self.subj), "revoked")

    def test_missing_consent_block_defaults_granted(self):
        _w(self.profile, {"session_slot": 0})
        self.assertEqual(consent.status_for(self.subj), "granted")

    def test_sqlite_helpers_gate_directly(self):
        self.set_consent("limited")
        r = sqlite_store.log_error_event(self.subj, {"id": "e", "stage_id": "S1", "source_phase": "practice",
                                                     "cause": "slip", "slot": 1})
        self.assertFalse(r["written"])
        self.assertFalse(os.path.exists(self.db))
        # scheduling-class card upsert is still allowed under limited
        r = sqlite_store.upsert_review_card(self.deck, _r(self.deck)["cards"][0])
        self.assertTrue(r.get("ok"))
        self.assertTrue(os.path.exists(self.db))


if __name__ == "__main__":
    unittest.main()
