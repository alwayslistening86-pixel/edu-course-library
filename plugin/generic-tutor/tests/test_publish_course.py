"""N-15: a compile is published by rename, only after the gate passes."""
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import list_courses  # noqa: E402
import publish_course as pc  # noqa: E402
from tutorlib import paths  # noqa: E402

FIX = os.path.join(ROOT, "evals", "fixtures", "courses", "fx_maths_fractions")
CID = "fx_maths_fractions"


class Publish(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.addCleanup(self._t.cleanup)
        self.courses = os.path.join(self._t.name, "courses")
        os.makedirs(self.courses)
        self.build = os.path.join(self.courses, ".build-" + CID)
        shutil.copytree(FIX, self.build)

    def test_a_build_in_progress_is_invisible_then_appears_whole(self):
        self.assertEqual(paths.course_ids(self.courses), [])
        learner = os.path.join(self._t.name, "learner")
        os.makedirs(learner)
        self.assertEqual(list_courses.build(learner, self.courses)["courses"], [])
        r = pc.publish(self.courses, CID)
        self.assertTrue(r["published"] and r["can_ship"] and not r["overridden"], r)
        self.assertEqual(paths.course_ids(self.courses), [CID])
        self.assertFalse(os.path.exists(self.build))
        self.assertTrue(os.listdir(os.path.join(self.courses, CID, "stages")))

    def test_a_course_that_fails_the_gate_stays_hidden_and_untouched(self):
        os.remove(os.path.join(self.build, "rubric.json"))
        r = pc.publish(self.courses, CID)
        self.assertFalse(r["published"])
        self.assertTrue(r["blocking_reasons"])
        self.assertTrue(os.path.isdir(self.build))
        self.assertEqual(paths.course_ids(self.courses), [])

    def test_an_override_needs_a_reason_and_is_reported(self):
        os.remove(os.path.join(self.build, "rubric.json"))
        self.assertFalse(pc.publish(self.courses, CID, "   ")["published"])
        r = pc.publish(self.courses, CID, "one stage's source is still being tracked down")
        self.assertTrue(r["published"] and r["overridden"] and not r["can_ship"], r)
        self.assertIn("tracked down", r["override_reason"])
        self.assertTrue(r["blocking_reasons"])

    def test_an_existing_course_is_never_overwritten(self):
        os.makedirs(os.path.join(self.courses, CID))
        r = pc.publish(self.courses, CID)
        self.assertFalse(r["published"])
        self.assertIn("already exists", r["error"])
        self.assertTrue(os.path.isdir(self.build), "the build folder is kept for the caller to decide")

    def test_missing_build_and_bad_ids(self):
        self.assertIn("no build folder", pc.publish(self.courses, "other")["error"])
        for bad in ("../x", "a/b", ".hidden", "con"):
            self.assertIn("error", pc.publish(self.courses, bad), bad)
            self.assertIn("error", pc.discard(self.courses, bad), bad)
        self.assertIn("error", pc.publish(os.path.join(self._t.name, "nope"), CID))

    def test_discard_removes_only_the_build_folder(self):
        other = os.path.join(self.courses, "keep_me")
        shutil.copytree(FIX, other)
        self.assertTrue(pc.discard(self.courses, CID)["discarded"])
        self.assertFalse(os.path.exists(self.build))
        self.assertTrue(os.path.isdir(other))
        self.assertFalse(pc.discard(self.courses, CID)["discarded"])
        self.assertFalse(pc.discard(self.courses, "keep_me")["discarded"], "a live course is not a build folder")
        self.assertTrue(os.path.isdir(other))

    def test_doctor_flags_an_unfinished_build(self):
        import doctor
        self.assertEqual(doctor.check_courses(self.courses)["status"], "warn")
        self.assertIn(".build-" + CID, doctor.check_courses(self.courses)["detail"])
        pc.discard(self.courses, CID)
        self.assertEqual(doctor.check_courses(self.courses)["status"], "ok")

    def test_cli_usage(self):
        self.assertEqual(pc.main([]), 2)
        self.assertEqual(pc.main(["discard", self.courses, CID, "--override", "x"]), 2)
        self.assertEqual(pc.main(["publish", self.courses, CID, "--override"]), 2)


if __name__ == "__main__":
    unittest.main()
