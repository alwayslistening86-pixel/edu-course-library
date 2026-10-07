"""N-05: exam_technique.md and command_words.json are optional, but if present they must be well formed (non-blocking status in
validate_structure, blocking in the post-compile gate when malformed). Stdlib only."""
import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))

import postcompile_gate  # noqa: E402
import validate_schema  # noqa: E402
import validate_structure  # noqa: E402
from golden_support import build_fixture  # noqa: E402

GOOD_WORDS = {"source": "Board guide, section 3", "command_words": [
    {"word": "Explain", "meaning": "Give reasons that link cause to effect.", "earns_marks_by": "Each linked reason earns a mark."},
    {"word": "State", "meaning": "Give a short fact with no reasons needed.", "earns_marks_by": "One correct fact per mark."}]}
GOOD_TECH = "# Exam technique: Maths\n\nSource: Examiner report, June, section 2\n\n## How marks are earned\nMethod marks are given for working shown.\nAnswer marks need the right value.\n"


class ExamGuidance(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.courses = build_fixture(self.tmp)["C"]

    def course(self):
        return os.path.join(self.courses, "mathA")

    def write(self, name, text):
        with open(os.path.join(self.course(), name), "w", encoding="utf-8") as f:
            f.write(text if isinstance(text, str) else json.dumps(text))

    def status(self):
        return validate_structure.validate(self.course())["exam_guidance_status"]

    def test_absent_is_fine(self):
        st = self.status()
        self.assertEqual(st, {"exam_technique": {"present": False}, "command_words": {"present": False}})

    def test_well_formed_files(self):
        self.write("exam_technique.md", GOOD_TECH)
        self.write("command_words.json", GOOD_WORDS)
        st = self.status()
        self.assertTrue(st["exam_technique"]["well_formed"])
        self.assertTrue(st["command_words"]["well_formed"])
        self.assertEqual(st["command_words"]["count"], 2)

    def test_exam_technique_needs_source_and_content(self):
        self.write("exam_technique.md", "# Exam technique\n\n## Marks\n")
        st = self.status()["exam_technique"]
        self.assertFalse(st["well_formed"])
        self.assertEqual(len(st["problems"]), 2)

    def test_command_words_schema_and_duplicates(self):
        self.write("command_words.json", {"source": "x", "command_words": []})
        self.assertFalse(self.status()["command_words"]["well_formed"])
        dup = {"source": "Board guide", "command_words": GOOD_WORDS["command_words"] + [dict(GOOD_WORDS["command_words"][0], word="explain")]}
        self.write("command_words.json", dup)
        self.assertIn("more than once", self.status()["command_words"]["problems"][0])

    def test_schema_check_covers_course_dir(self):
        self.write("command_words.json", {"source": "Board guide", "command_words": [{"word": "Explain"}]})
        r = validate_schema.check_course_dir(self.course())
        self.assertFalse(r["valid"])
        self.assertEqual(r["invalid"][0]["kind"], "command_words")

    def test_gate_blocks_only_when_malformed(self):
        self.write("command_words.json", GOOD_WORDS)
        self.assertFalse(any("command_words" in r for r in postcompile_gate.check(self.course())["blocking_reasons"]))
        self.write("command_words.json", {"source": "Board guide", "command_words": []})
        res = postcompile_gate.check(self.course())
        self.assertFalse(res["can_ship"])
        self.assertTrue(any("command_words" in r for r in res["blocking_reasons"]))

if __name__ == "__main__":
    unittest.main()
