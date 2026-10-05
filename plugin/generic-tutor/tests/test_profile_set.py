"""C-11: profile_set.py - the one write path for learner settings."""
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
import profile_set  # noqa: E402
from tutorlib import ledger, schema  # noqa: E402

TODAY = "2026-10-04"


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.p = f"{self.fx['L']}/student_profile.json"

    def set(self, field, value, dry=False):
        return profile_set.set_value(self.p, field, value, TODAY, dry)

    def get(self):
        return gs.read_json(self.p)


class Settings(Base):
    def test_valid_changes_of_every_type(self):
        for field, value, check in (
            ("preferences.style", "brief", lambda d: d["preferences"]["style"] == "brief"),
            ("preferences.accessibility.dyslexia_mode", "true", lambda d: d["preferences"]["accessibility"]["dyslexia_mode"] is True),
            ("availability.sessions_per_week", "4", lambda d: d["availability"]["sessions_per_week"] == 4),
            ("learning_signals.pace", "slow", lambda d: d["learning_signals"]["pace"] == "slow"),
            ("identity.display_name", "Alex", lambda d: d["identity"]["display_name"] == "Alex"),
            ("goals", '["GCSE maths grade 6", "learn contract law"]', lambda d: len(d["goals"]) == 2),
            ("roster.max_incomplete_courses", "3", lambda d: d["roster"]["max_incomplete_courses"] == 3),
        ):
            r = self.set(field, value)
            self.assertTrue(r["written"], (field, r))
            self.assertTrue(check(self.get()), field)
            self.assertEqual(schema.validate(self.get(), "student_profile"), [], field)
        self.assertEqual(self.get()["last_updated"], TODAY)

    def test_report_shows_old_and_new(self):
        self.set("preferences.tone", "formal")
        r = self.set("preferences.tone", "playful")
        self.assertEqual((r["old"], r["new"]), ("formal", "playful"))

    def test_refusals_leave_the_file_untouched(self):
        with open(self.p, "rb") as f:
            before = f.read()
        for field, value in (("preferences.tone", "sarcastic"), ("availability.sessions_per_week", "0"), ("availability.sessions_per_week", "many"),
                             ("preferences.accessibility.dyslexia_mode", "maybe"), ("goals", "not json"), ("goals", '["' + "x" * 130 + '"]'),
                             ("learning_signals.notes", "n" * 501), ("highest_level_cleared", "9"), ("session_slot", "0"),
                             ("consent.granted", "x"), ("capabilities", "{}"), ("roster.max_incomplete_courses", "99")):
            r = self.set(field, value)
            self.assertIn("error", r, field)
        self.assertIn("error", profile_set.set_value(self.p, "preferences.style", "brief", "yesterday"))
        with open(self.p, "rb") as f:
            self.assertEqual(f.read(), before)

    def test_ledger_fields_cannot_be_set_through_here(self):
        for field in ("highest_level_cleared", "session_slot", "session_slot_advanced_at", "schema_version", "learner_id"):
            self.assertIn("not a setting", self.set(field, "1")["error"])

    def test_dry_run_changes_nothing(self):
        r = self.set("preferences.style", "brief", dry=True)
        self.assertEqual((r["dry_run"], r["written"]), (True, False))
        self.assertNotEqual(self.get().get("preferences", {}).get("style"), "brief")

    def test_capability_is_stored_with_the_date_and_points_to_the_follow_up(self):
        r = self.set("capabilities.share_images", "true")
        self.assertEqual(self.get()["capabilities"]["share_images"], {"declared": True, "on": TODAY})
        self.assertIn("apply_capabilities.py", r["next_step"])

    def test_lowering_the_roster_cap_is_explained(self):
        self.assertIn("never removes a course", self.set("roster.max_incomplete_courses", "1")["note"])

    def test_corrupt_or_newer_profile_is_an_error_not_a_traceback(self):
        d = self.get()
        d["schema_version"] = 99
        with open(self.p, "w") as f:
            json.dump(d, f)
        r = gs.run_step("profile_set.py", ["{P}/student_profile.json", "preferences.style", "brief", TODAY], self.fx, self.tmp)
        self.assertEqual(r["exit"], 1)


class Consent(Base):
    def status(self, s):
        d = self.get()
        d["consent"]["status"] = s
        with open(self.p, "w") as f:
            json.dump(d, f)

    def test_limited_keeps_progress_class_but_drops_learning_signals(self):
        self.status("limited")
        self.assertTrue(self.set("preferences.style", "brief")["written"])
        r = self.set("learning_signals.pace", "slow")
        self.assertFalse(r["written"])
        self.assertNotEqual(self.get().get("learning_signals", {}).get("pace"), "slow")

    def test_revoked_stores_nothing_but_consent_itself_can_always_be_changed(self):
        self.status("revoked")
        self.assertFalse(self.set("preferences.style", "brief")["written"])
        self.assertNotIn("style", self.get().get("preferences", {}))
        self.assertTrue(self.set("consent.status", "granted")["written"])
        self.assertEqual(self.get()["consent"]["status"], "granted")
        self.assertTrue(self.set("preferences.style", "brief")["written"])

    def test_ledger_records_changes(self):
        self.set("preferences.style", "brief")
        self.assertIn("profile_set.py", [e["script"] for e in ledger.read(self.fx["L"])])


class Cli(Base):
    def test_cli_codes(self):
        ok = gs.run_step("profile_set.py", ["{P}/student_profile.json", "preferences.style", "brief", TODAY], self.fx, self.tmp)
        self.assertEqual((ok["exit"], ok["stdout"]["written"]), (0, True))
        self.assertEqual(gs.run_step("profile_set.py", ["{P}/student_profile.json", "preferences.style", "loud", TODAY], self.fx, self.tmp)["exit"], 1)
        self.assertEqual(gs.run_step("profile_set.py", ["{P}/student_profile.json", "preferences.style"], self.fx, self.tmp)["exit"], 2)
        dry = gs.run_step("profile_set.py", ["{P}/student_profile.json", "preferences.tone", "formal", TODAY, "--dry-run"], self.fx, self.tmp)
        self.assertEqual(dry["stdout"]["dry_run"], True)


if __name__ == "__main__":
    unittest.main()


class Init(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.root = os.path.join(self.tmp, "profile")
        os.makedirs(self.root)
        self.fx = {"R": self.root, "T": self.tmp}

    def test_create_with_answers_and_defaults(self):
        import profile_init
        r = profile_init.create(self.root, "alex", TODAY, {"identity.education_level": "Year 11", "preferences.style": "brief",
                                                           "availability.sessions_per_week": 3, "roster.max_incomplete_courses": 2,
                                                           "capabilities.share_images": True, "goals": ["GCSE maths"]})
        self.assertTrue(r["created"], r)
        p = gs.read_json(f"{self.root}/alex/student_profile.json")
        self.assertEqual((p["schema_version"], p["consent"]["status"], p["session_slot"], p["highest_level_cleared"]), (2, "granted", 0, 0))
        self.assertEqual(p["capabilities"]["share_images"], {"declared": True, "on": TODAY})
        self.assertTrue(os.path.isdir(f"{self.root}/alex/subjects"))
        self.assertEqual(schema.validate(p, "student_profile"), [])

    def test_refusals_create_nothing(self):
        import profile_init
        for uid, answers in (("../x", {}), ("alex", {"preferences.style": "loud"}), ("alex", {"highest_level_cleared": 5}),
                             ("alex", {"consent.status": "revoked"}), ("alex", [1])):
            self.assertFalse(profile_init.create(self.root, uid, TODAY, answers)["created"], (uid, answers))
        self.assertEqual(os.listdir(self.root), [])
        profile_init.create(self.root, "alex", TODAY, {})
        self.assertIn("already exists", profile_init.create(self.root, "alex", TODAY, {})["error"])

    def test_cli_reads_answers_from_stdin_so_hostile_text_is_inert(self):
        import subprocess
        script = os.path.join(os.path.dirname(HERE), "scripts", "profile_init.py")
        note = '"; touch PWNED; $(touch PWNED2)'
        p = subprocess.run([sys.executable, script, self.root, "alex", TODAY], input=json.dumps({"learning_signals.notes": note}),
                           capture_output=True, text=True, cwd=self.tmp)
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertEqual(gs.read_json(f"{self.root}/alex/student_profile.json")["learning_signals"]["notes"], note)
        self.assertFalse([f for f in os.listdir(self.tmp) if f.startswith("PWNED")])
        bad = subprocess.run([sys.executable, script, self.root, "bob", TODAY], input="not json", capture_output=True, text=True)
        self.assertEqual(bad.returncode, 1)
        self.assertEqual(subprocess.run([sys.executable, script, self.root], capture_output=True, text=True).returncode, 2)
