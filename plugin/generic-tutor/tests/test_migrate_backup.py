"""E-12: migrations keep the pre-migration file and support --dry-run."""
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


class Backup(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.old = f"{self.fx['C']}/old/course.json"

    def raw(self, p):
        with open(p, "rb") as f:
            return f.read()

    def test_migration_reports_whether_the_result_matches_the_schema(self):
        r = migrate_schema.migrate_course(self.old, dry_run=True)
        self.assertFalse(r["valid_after"])                                   # fields that need sourcing stay null: reported, not hidden
        self.assertIn("missing required 'exam'", " ".join(r["schema_errors_after"]))
        good = migrate_schema.migrate_course(f"{self.fx['C']}/mathA/course.json", dry_run=True)
        self.assertTrue(good["valid_after"])
        self.assertNotIn("schema_errors_after", good)
        subj = migrate_schema.migrate_subject(f"{self.fx['S']}/mathA.json", f"{self.fx['C']}/mathA/course.json", dry_run=True)
        self.assertTrue(subj["valid_after"])

    def test_backup_holds_the_exact_original_bytes(self):
        original = self.raw(self.old)
        r = migrate_schema.migrate_course(self.old)
        self.assertTrue(r["wrote"])
        self.assertEqual(self.raw(r["backup"]), original)
        self.assertTrue(r["backup"].endswith(".pre-migrate-vunversioned.bak"))
        self.assertNotEqual(self.raw(self.old), original)

    def test_oldest_backup_per_source_version_is_never_overwritten(self):
        first = migrate_schema.migrate_course(self.old)["backup"]
        kept = self.raw(first)
        d = gs.read_json(self.old)
        d.pop("schema_version")                              # force a second migration from the same source version label
        d["name"] = "changed after first migration"
        with open(self.old, "w") as f:
            json.dump(d, f)
        migrate_schema.migrate_course(self.old)
        self.assertEqual(self.raw(first), kept)

    def test_dry_run_changes_nothing_and_says_what_would_change(self):
        before = self.raw(self.old)
        r = migrate_schema.migrate_course(self.old, dry_run=True)
        self.assertEqual((r["wrote"], r["dry_run"], r["would_change"]), (False, True, True))
        self.assertEqual(self.raw(self.old), before)
        self.assertEqual([f for f in os.listdir(os.path.dirname(self.old)) if f.endswith(".bak")], [])

    def test_nothing_to_migrate_means_no_backup(self):
        r = migrate_schema.migrate_course(f"{self.fx['C']}/mathA/course.json")
        self.assertFalse(r["wrote"])
        self.assertNotIn("backup", r)

    def test_subject_migration_also_backs_up_and_cli_flag_works(self):
        subj = f"{self.fx['S']}/mathA.json"
        d = gs.read_json(subj)
        d["schema_version"] = 3
        d.pop("item_mastery")
        d.pop("remediation")
        with open(subj, "w") as f:
            json.dump(d, f)
        dry = gs.run_step("migrate_schema.py", ["subject", subj, "{C}/mathA/course.json", "--dry-run"], self.fx, self.tmp)
        self.assertEqual((dry["exit"], dry["stdout"]["dry_run"]), (0, True))
        self.assertFalse(os.path.exists(subj + ".pre-migrate-v3.bak"))
        real = gs.run_step("migrate_schema.py", ["subject", subj, "{C}/mathA/course.json"], self.fx, self.tmp)
        self.assertTrue(real["stdout"]["wrote"])
        self.assertTrue(os.path.isfile(subj + ".pre-migrate-v3.bak"))
        with open(subj + ".pre-migrate-v3.bak", encoding="utf-8") as f:
            self.assertEqual(json.load(f)["schema_version"], 3)


if __name__ == "__main__":
    unittest.main()
