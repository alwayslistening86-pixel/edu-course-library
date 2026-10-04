"""E-15: history DB schema versioning, newer-DB refusal, health check."""
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import sqlite_store  # noqa: E402


class Versioning(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.subj = self.fx["S"] + "/mathA.json"
        self.db = self.fx["L"] + "/tutor.sqlite3"
        self.entry = {"id": "e1", "stage_id": "S1", "source_phase": "practice", "cause": "slip", "slot": 1}

    def uv(self):
        con = sqlite3.connect(self.db)
        try:
            return con.execute("PRAGMA user_version").fetchone()[0]
        finally:
            con.close()

    def test_new_db_is_stamped(self):
        self.assertTrue(sqlite_store.log_error_event(self.subj, self.entry)["ok"])
        self.assertEqual(self.uv(), sqlite_store.DB_SCHEMA_VERSION)

    def test_legacy_unversioned_db_is_stamped_without_data_loss(self):
        sqlite_store.log_error_event(self.subj, self.entry)
        con = sqlite3.connect(self.db)
        con.execute("PRAGMA user_version = 0")
        con.commit()
        con.close()
        self.assertEqual(self.uv(), 0)
        self.assertTrue(sqlite_store.log_error_event(self.subj, {**self.entry, "id": "e2"})["ok"])
        self.assertEqual(self.uv(), sqlite_store.DB_SCHEMA_VERSION)
        self.assertEqual(sqlite_store.check(self.fx["L"])["row_counts"]["error_events"], 2)

    def test_newer_db_refused_and_untouched(self):
        sqlite_store.log_error_event(self.subj, self.entry)
        con = sqlite3.connect(self.db)
        con.execute("PRAGMA user_version = 99")
        con.commit()
        con.close()
        r = sqlite_store.log_error_event(self.subj, {**self.entry, "id": "e2"})
        self.assertFalse(r["ok"])
        self.assertIn("newer than this plugin understands", r["error"])
        self.assertEqual(self.uv(), 99)
        self.assertFalse(sqlite_store.check(self.fx["L"])["healthy"])

    def test_check_cli(self):
        r = gs.run_step("sqlite_store.py", ["check", "{L}"], self.fx, self.tmp)
        self.assertEqual((r["exit"], r["stdout"]), (0, {"exists": False}))
        sqlite_store.log_error_event(self.subj, self.entry)
        r = gs.run_step("sqlite_store.py", ["check", "{L}"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 0)
        self.assertTrue(r["stdout"]["healthy"])
        self.assertEqual(r["stdout"]["integrity"], ["ok"])

    def test_corrupt_file_reported_not_raised(self):
        with open(self.db, "wb") as f:
            f.write(b"this is not sqlite" * 100)
        r = sqlite_store.log_error_event(self.subj, self.entry)
        self.assertFalse(r["ok"])
        self.assertTrue(json.dumps(r))


if __name__ == "__main__":
    unittest.main()
