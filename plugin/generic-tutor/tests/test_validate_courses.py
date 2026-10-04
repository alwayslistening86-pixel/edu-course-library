"""
Smoke tests for .github/scripts/validate_courses.py, the CI driver the private
courses repo runs cross-repo. Exercises its exit codes only (0 clean, 1 failing
course, 2 usage / nothing to check); the validators it wraps are tested elsewhere.
"""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(ROOT))
DRIVER = os.path.join(REPO, ".github", "scripts", "validate_courses.py")


class ValidateCoursesDriver(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.root, True)
        # The driver imports the validators from <root>/plugin/generic-tutor/scripts.
        os.makedirs(os.path.join(self.root, "plugin", "generic-tutor"))
        shutil.copytree(os.path.join(ROOT, "scripts"),
                        os.path.join(self.root, "plugin", "generic-tutor", "scripts"),
                        ignore=shutil.ignore_patterns("__pycache__"))

    def run_driver(self):
        return subprocess.run([sys.executable, DRIVER, self.root],
                              capture_output=True, text=True)

    def test_no_courses_is_usage_error(self):
        os.makedirs(os.path.join(self.root, "courses"))
        self.assertEqual(self.run_driver().returncode, 2)

    def test_broken_course_fails(self):
        c = os.path.join(self.root, "courses", "broken")
        os.makedirs(c)
        with open(os.path.join(c, "course.json"), "w") as f:
            f.write("{}")
        r = self.run_driver()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("[FAIL] broken", r.stdout)


if __name__ == "__main__":
    unittest.main()
