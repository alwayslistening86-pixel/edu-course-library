"""L-09: exam_guidance.py hands the tutor only what the course holds. Stdlib only."""
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

import exam_guidance  # noqa: E402
from golden_support import build_fixture  # noqa: E402
from test_exam_guidance import GOOD_TECH, GOOD_WORDS  # noqa: E402


class ExamGuidanceUse(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.course = os.path.join(build_fixture(self.tmp)["C"], "mathA")

    def write(self, name, text):
        with open(os.path.join(self.course, name), "w", encoding="utf-8") as f:
            f.write(text if isinstance(text, str) else json.dumps(text))

    def test_nothing_published(self):
        r = exam_guidance.guidance(self.course, "Explain")
        self.assertFalse(r["technique"]["available"])
        self.assertFalse(r["command_words"]["available"])
        self.assertEqual(r["lookup"], {"word": "Explain", "found": False})

    def test_present_files_and_lookup(self):
        self.write("exam_technique.md", GOOD_TECH)
        self.write("command_words.json", GOOD_WORDS)
        r = exam_guidance.guidance(self.course, "  explain ")
        self.assertTrue(r["technique"]["available"])
        self.assertIn("Examiner report", r["technique"]["source"])
        self.assertEqual(r["command_words"]["words"], ["Explain", "State"])
        self.assertTrue(r["lookup"]["found"])
        self.assertIn("cause to effect", r["lookup"]["meaning"])
        self.assertFalse(exam_guidance.guidance(self.course, "Evaluate")["lookup"]["found"])

    def test_malformed_is_unavailable_with_problems(self):
        self.write("command_words.json", {"source": "Board guide", "command_words": []})
        self.write("exam_technique.md", "# Exam technique\n")
        r = exam_guidance.guidance(self.course, "Explain")
        self.assertFalse(r["command_words"]["available"])
        self.assertTrue(r["command_words"]["problems"])
        self.assertFalse(r["technique"]["available"])
        self.assertTrue(r["technique"]["problems"])
        self.assertFalse(r["lookup"]["found"])

    def test_long_text_is_capped(self):
        self.write("exam_technique.md", GOOD_TECH + "Filler line about marks.\n" * 600)
        t = exam_guidance.guidance(self.course)["technique"]
        self.assertEqual(len(t["text"]), exam_guidance.MAX_TEXT)
        self.assertTrue(t["truncated"])

    def test_missing_folder(self):
        self.assertIn("error", exam_guidance.guidance(os.path.join(self.tmp, "nope")))


if __name__ == "__main__":
    unittest.main()
