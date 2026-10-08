"""N-11: /list-courses shows where a course came from and how current it is."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import list_courses  # noqa: E402

FIX = os.path.join(ROOT, "evals", "fixtures", "courses", "fx_maths_fractions")
LOG = """# Change log - fx
## 2026-10-01 - built
First build from the sample specification.
## 2026-10-05 - Specification wording updated
**Found by:** recheck **Fixed:** item titles
"""


class Provenance(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.addCleanup(self._t.cleanup)
        self.courses = os.path.join(self._t.name, "courses")
        os.makedirs(self.courses)
        self.learner = os.path.join(self._t.name, "learner")
        os.makedirs(self.learner)
        self.path = os.path.join(self.courses, "fx")
        shutil.copytree(FIX, self.path)

    def row(self, **kw):
        rows = list_courses.build(self.learner, self.courses, **kw)["courses"]
        self.assertEqual(len(rows), 1)
        return rows[0]

    def test_a_course_with_a_change_log_reports_its_history(self):
        with open(os.path.join(self.path, "change.md"), "w", encoding="utf-8") as f:
            f.write(LOG)
        p = self.row()["provenance"]
        self.assertEqual((p["built_on"], p["changes"]), ("2026-10-01", 2))
        self.assertEqual(p["last_change"], {"date": "2026-10-05", "title": "Specification wording updated"})
        self.assertEqual(p["source_document"], "Self-authored sample specification")
        self.assertEqual((p["source_version"], p["itemised_on"]), ("1", "2026-10-06"))
        self.assertEqual(p["last_live_recheck"], "2026-10-06")

    def test_missing_pieces_are_null_not_errors(self):
        os.remove(os.path.join(self.path, "curriculum_map.json"))
        p = self.row()["provenance"]
        self.assertEqual((p["built_on"], p["last_change"], p["changes"], p["source_document"]), (None, None, 0, None))

    def test_a_very_long_source_description_is_capped_for_display(self):
        cm = os.path.join(self.path, "curriculum_map.json")
        with open(cm, encoding="utf-8") as f:
            data = json.load(f)
        data["_items_source"]["document"] = "Qualification " + "x" * 400
        with open(cm, "w", encoding="utf-8") as f:
            json.dump(data, f)
        doc = self.row()["provenance"]["source_document"]
        self.assertLessEqual(len(doc), 160)
        self.assertTrue(doc.endswith("…"))

    def test_the_compact_form_stays_compact(self):
        self.assertNotIn("provenance", self.row(compact=True))


if __name__ == "__main__":
    unittest.main()
