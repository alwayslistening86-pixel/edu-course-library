"""tutorlib.state: safe loading, newer-schema refusal (E-20, S-09 part)."""
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
import migrate_schema  # noqa: E402
from tutorlib import state  # noqa: E402


class State(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.subj = self.fx["S"] + "/mathA.json"

    def write(self, text):
        with open(self.subj, "w", encoding="utf-8") as f:
            f.write(text)

    def test_supported_versions_match_migrator(self):
        self.assertEqual(state.SUPPORTED["subjects"], migrate_schema.SUBJECT_SCHEMA_VERSION)
        self.assertEqual(state.SUPPORTED["course"], migrate_schema.COURSE_SCHEMA_VERSION)

    def test_load_ok_and_older_or_missing_version_allowed(self):
        self.assertEqual(state.load(self.subj, "subjects")["course_id"], "mathA")
        d = gs.read_json(self.subj)
        del d["schema_version"]
        self.write(json.dumps(d))
        state.load(self.subj, "subjects")
        d["schema_version"] = 3
        self.write(json.dumps(d))
        state.load(self.subj, "subjects")

    def test_errors_are_clear(self):
        for text, needle in (("{broken", "cannot read as JSON"), ("[1,2]", "expected a JSON object")):
            self.write(text)
            with self.assertRaises(state.StateError) as cm:
                state.load(self.subj, "subjects")
            self.assertIn(needle, str(cm.exception))
        with self.assertRaises(state.StateError):
            state.load(self.subj + ".missing", "subjects")

    def test_newer_schema_refused_and_file_untouched_by_writers(self):
        d = gs.read_json(self.subj)
        d["schema_version"] = 99
        self.write(json.dumps(d))
        before = open(self.subj, "rb").read()
        cases = [("error_log.py", ["append", "{S}/mathA.json", "S2", "S2.1", "practice", "slip", "NONE", "n", "6"]),
                 ("item_mastery.py", ["observe", "{S}/mathA.json", "S1.1", "true", "5"]),
                 ("confidence_update.py", ["apply", "{S}/mathA.json", "pass_clean", "7"]),
                 ("remediation_state.py", ["record", "{S}/mathA.json", "S2", "slip", "6"]),
                 ("record_stage_result.py", ["apply", "{S}/mathA.json", "{C}/mathA/course.json", "S2", "pass"])]
        for script, args in cases:
            r = gs.run_step(script, args, self.fx, self.tmp)
            self.assertEqual(r["exit"], 1, (script, r))
            self.assertIn("newer than this plugin understands", json.dumps(r["stdout"]), script)
        self.assertEqual(open(self.subj, "rb").read(), before)

    def test_review_deck_newer_schema_refused(self):
        deck = self.fx["S"] + "/mathA_review_deck.json"
        d = gs.read_json(deck)
        d["schema_version"] = 7
        with open(deck, "w") as f:
            json.dump(d, f)
        r = gs.run_step("review_math.py", ["apply", deck, "k1", "6", "true"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 1)


if __name__ == "__main__":
    unittest.main()


class SaveValidates(unittest.TestCase):
    """E-20: a write may not make a file worse than it was when loaded."""

    def setUp(self):
        import shutil
        import tempfile
        import golden_support as gs
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.path = f"{self.fx['S']}/mathA.json"

    def test_valid_change_is_written(self):
        d = state.load(self.path, "subjects")
        d["confidence"] = 0.7
        state.save(self.path, d, "subjects")
        self.assertEqual(state.load(self.path)["confidence"], 0.7)

    def test_a_change_that_introduces_a_schema_error_is_refused_and_nothing_is_written(self):
        d = state.load(self.path, "subjects")
        d["confidence"] = "very high"
        with self.assertRaises(state.StateError) as cm:
            state.save(self.path, d, "subjects")
        self.assertIn("refusing to write", str(cm.exception))
        self.assertEqual(state.load(self.path)["confidence"], 0.5)

    def test_a_legacy_quirk_present_at_load_does_not_block_unrelated_writes(self):
        import json
        raw = state.load(self.path)
        raw["confidence"] = "medium"                               # old-shape value that predates the numeric confidence
        with open(self.path, "w") as f:
            json.dump(raw, f)
        d = state.load(self.path, "subjects")
        d["current_phase"] = "test"
        state.save(self.path, d, "subjects")                       # the quirk was already there; this change adds nothing
        self.assertEqual(state.load(self.path)["current_phase"], "test")
        d["error_patterns"] = "not a list"                         # a NEW error is still refused
        with self.assertRaises(state.StateError):
            state.save(self.path, d, "subjects")

    def test_unknown_kind_and_new_files_are_not_blocked(self):
        target = os.path.join(self.tmp, "fresh.json")
        state.save(target, {"anything": 1}, "something-else")
        self.assertEqual(state.load(target), {"anything": 1})
