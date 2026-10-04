"""erase_profile.py, export_profile.py, tutorlib.ids / paths (K-27..K-29, S-13, E-08)."""
import contextlib
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import erase_profile  # noqa: E402
import error_log  # noqa: E402
import export_profile  # noqa: E402
from tutorlib import ids, paths  # noqa: E402


def _w(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.root = os.path.join(self.tmp, "profile")
        for u in ("amy", "bob"):
            _w(os.path.join(self.root, u, "student_profile.json"), {"learner_id": u, "consent": {"status": "granted"}})
            _w(os.path.join(self.root, u, "subjects", "c1.json"),
               {"schema_version": 5, "course_id": "c1", "error_patterns": [], "item_mastery": {}})
            _w(os.path.join(self.root, u, "subjects", "c1_review_deck.json"), {"cards": []})
        # creates tutor.sqlite3 with a real history row for amy
        error_log.append(os.path.join(self.root, "amy", "subjects", "c1.json"), "S1", "I1", "practice", "slip", "NONE", "note", 1)


class Ids(unittest.TestCase):
    def test_valid(self):
        for v in ("amy", "aqa_gcse_maths_8300", "7.01a", "S1", "a-b_c.d"):
            self.assertEqual(ids.validate(v), v)

    def test_invalid(self):
        for v in ("", "../x", "a/b", "a\\b", "..", "a..b", ".hidden", "x" * 65, "con", "NUL", "a b", "x;rm", None, 5, "trail."):
            with self.assertRaises(ids.InvalidId, msg=repr(v)):
                ids.validate(v)


class Paths(Base):
    def test_symlink_learner_dir_refused(self):
        outside = os.path.join(self.tmp, "outside")
        os.makedirs(outside)
        os.symlink(outside, os.path.join(self.root, "evil"))
        with self.assertRaises(paths.OutsideRoot):
            paths.learner_dir(self.root, "evil")

    def test_ensure_within(self):
        paths.ensure_within(self.root, os.path.join(self.root, "amy", "subjects"))
        with self.assertRaises(paths.OutsideRoot):
            paths.ensure_within(self.root, os.path.join(self.root, "..", "x"))


class Erase(Base):
    def test_dry_run_and_missing_confirm_delete_nothing(self):
        for kwargs in ({"dry_run": True}, {}, {"confirm": "erase amy"}, {"confirm": "ERASE bob"}):
            r = erase_profile.erase(self.root, "amy", **kwargs)
            self.assertFalse(r["erased"])
            self.assertTrue(os.path.isdir(os.path.join(self.root, "amy")))
        r = erase_profile.erase(self.root, "amy", dry_run=True)
        self.assertTrue(r["has_history_db"])
        self.assertEqual(r["required_confirmation"], "ERASE amy")

    def test_exact_phrase_erases_only_that_learner(self):
        r = erase_profile.erase(self.root, "amy", confirm="ERASE amy")
        self.assertTrue(r["erased"])
        self.assertFalse(os.path.exists(os.path.join(self.root, "amy")))
        self.assertTrue(os.path.isfile(os.path.join(self.root, "bob", "student_profile.json")))

    def test_traversal_ids_refused(self):
        for bad in ("..", "../profile", "amy/../bob"):
            r = erase_profile.erase(self.root, bad, confirm=f"ERASE {bad}")
            self.assertFalse(r["erased"])
        self.assertTrue(os.path.isdir(os.path.join(self.root, "bob")))

    def test_cli_exit_codes(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(erase_profile.main([self.root, "amy"]), 0)  # dry-run style report
            self.assertEqual(erase_profile.main([self.root, "amy", "--confirm", "nope"]), 1)
            self.assertEqual(erase_profile.main([self.root, "amy", "--confirm", "ERASE amy"]), 0)


class Export(Base):
    def test_export_contains_progress_decks_and_history(self):
        out = os.path.join(self.tmp, "amy.zip")
        r = export_profile.export(self.root, "amy", out)
        self.assertTrue(r["exported"], r)
        with zipfile.ZipFile(out) as z:
            names = set(z.namelist())
            self.assertIn("manifest.json", names)
            self.assertIn("student_profile.json", names)
            self.assertIn("subjects/c1.json", names)
            self.assertIn("subjects/c1_review_deck.json", names)
            self.assertIn("history/error_events.json", names)
            rows = json.loads(z.read("history/error_events.json"))
            self.assertEqual(len(rows), 1)
            manifest = json.loads(z.read("manifest.json"))
            import hashlib
            for f in manifest["files"]:
                self.assertEqual(hashlib.sha256(z.read(f["name"])).hexdigest(), f["sha256"])
            self.assertFalse(any("bob" in n for n in names))

    def test_output_inside_profile_refused(self):
        r = export_profile.export(self.root, "amy", os.path.join(self.root, "amy", "x.zip"))
        self.assertFalse(r["exported"])

    def test_export_works_without_history_db(self):
        r = export_profile.export(self.root, "bob", os.path.join(self.tmp, "bob.zip"))
        self.assertTrue(r["exported"])
        self.assertEqual(r["history_tables"], [])

    def test_unknown_or_bad_user(self):
        self.assertFalse(export_profile.export(self.root, "zed", os.path.join(self.tmp, "z.zip"))["exported"])
        self.assertFalse(export_profile.export(self.root, "../x", os.path.join(self.tmp, "z.zip"))["exported"])


if __name__ == "__main__":
    unittest.main()
