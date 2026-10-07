"""N-14: only a folder with a valid course id and a course.json is a course; staging and stray folders are not."""
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import audit_run  # noqa: E402
import audit_status  # noqa: E402
import currency_report  # noqa: E402
import doctor  # noqa: E402
import enrich_plan  # noqa: E402
import list_courses  # noqa: E402
from tutorlib import paths  # noqa: E402

FIX = os.path.join(ROOT, "evals", "fixtures", "courses", "fx_maths_fractions")
STRAYS = (".import-fx_maths_fractions.tmp", "_scratch", "bad name", "-leading-dash", "con")


class CourseIds(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.addCleanup(self._t.cleanup)
        self.courses = os.path.join(self._t.name, "courses")
        os.makedirs(self.courses)
        shutil.copytree(FIX, os.path.join(self.courses, "fx_maths_fractions"))
        for s in STRAYS:  # each a complete copy, so only the name can disqualify it
            shutil.copytree(FIX, os.path.join(self.courses, s))
        with open(os.path.join(self.courses, "notes.md"), "w", encoding="utf-8") as f:
            f.write("not a course")
        os.makedirs(os.path.join(self.courses, "empty_folder"))
        self.learner = os.path.join(self._t.name, "learner")
        os.makedirs(self.learner)

    def test_helper_returns_only_real_course_ids(self):
        self.assertEqual(paths.course_ids(self.courses), ["fx_maths_fractions"])

    def test_every_scanner_ignores_the_strays(self):
        rows = list_courses.build(self.learner, self.courses)["courses"]
        self.assertEqual([r["course_id"] for r in rows], ["fx_maths_fractions"])
        self.assertEqual(sorted(audit_run.run(self.courses)["courses"]), ["fx_maths_fractions"])
        self.assertEqual(audit_status.audit_status(self.courses)["courses_checked"], 1)
        self.assertEqual(list(enrich_plan.run(self.courses)["courses"]), ["fx_maths_fractions"])
        self.assertTrue(all(r["course_id"] == "fx_maths_fractions" for r in currency_report.run(self.courses)["courses"]))
        check = doctor.check_courses(self.courses)       # the leftover import folder is reported, not counted as a course
        self.assertEqual(check["status"], "warn")
        self.assertIn(".import-fx_maths_fractions.tmp", check["detail"])
        shutil.rmtree(os.path.join(self.courses, ".import-fx_maths_fractions.tmp"))
        self.assertIn("1 course(s)", doctor.check_courses(self.courses)["detail"])

    def test_a_real_course_with_a_valid_but_unusual_id_is_still_listed(self):
        shutil.copytree(FIX, os.path.join(self.courses, "Law.101-2026_a"))
        self.assertIn("Law.101-2026_a", paths.course_ids(self.courses))


if __name__ == "__main__":
    unittest.main()
