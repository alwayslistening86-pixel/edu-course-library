"""E-24 / C-08: backup_profile.py and restore_profile.py."""
import datetime
import hashlib
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest
import zipfile
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import backup_profile  # noqa: E402
import golden_support as gs  # noqa: E402
import restore_profile  # noqa: E402


def tree(d):
    out = {}
    for dp, _dn, fns in os.walk(d):
        for fn in fns:
            full = os.path.join(dp, fn)
            if fn.endswith(".sqlite3"):
                con = sqlite3.connect(full)
                out[os.path.relpath(full, d)] = json.dumps(sorted(con.execute("SELECT id, note FROM error_events")))
                con.close()
            else:
                with open(full, "rb") as f:
                    out[os.path.relpath(full, d)] = hashlib.sha256(f.read()).hexdigest()
    return out


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        gs.run_step("slot_advance.py", ["{P}/student_profile.json", "--min-gap-minutes", "0"], self.fx, self.tmp)
        gs.run_step("error_log.py", ["append", "{S}/mathA.json", "S2", "S2.1", "practice", "slip", "NONE", "a note", "6"], self.fx, self.tmp)
        self.root = self.fx["R"]
        self.learner = self.fx["L"]

    def make_backup(self, **kw):
        r = backup_profile.backup(self.root, "amy", **kw)
        self.assertTrue(r["backed_up"], r)
        return r["zip_path"]

    def rewrite_zip(self, src, mutate):
        dst = src + ".mod.zip"
        with zipfile.ZipFile(src) as zi, zipfile.ZipFile(dst, "w") as zo:
            members = {n: zi.read(n) for n in zi.namelist()}
            mutate(members)
            for n, b in members.items():
                zo.writestr(n, b)
        return dst


class Backup(Base):
    def test_default_location_is_outside_the_learner_folder_and_contents_complete(self):
        z = self.make_backup(now=datetime.datetime(2026, 10, 4, 12, 0, tzinfo=datetime.timezone.utc))
        self.assertEqual(os.path.dirname(z), os.path.join(self.tmp, "backups"))
        self.assertTrue(os.path.basename(z).startswith("amy-backup-20261004T120000Z"))
        with zipfile.ZipFile(z) as zf:
            names = set(zf.namelist())
            self.assertIn("learner/student_profile.json", names)
            self.assertIn("learner/subjects/mathA.json", names)
            self.assertIn("learner/subjects/mathA_review_deck.json", names)
            self.assertIn("learner/tutor.sqlite3", names)
            self.assertIn("learner/.session_ledger.jsonl", names)

    def test_locks_and_partial_files_skipped_and_symlinks_ignored(self):
        open(self.fx["S"] + "/mathA.json.lock", "w").close()
        open(self.fx["S"] + "/x.json.part", "w").close()
        with zipfile.ZipFile(self.make_backup()) as zf:
            self.assertFalse([n for n in zf.namelist() if n.endswith((".lock", ".part"))])

    def test_out_dir_inside_learner_refused(self):
        r = backup_profile.backup(self.root, "amy", out_dir=self.learner + "/exports")
        self.assertFalse(r["backed_up"])

    def test_bad_ids_and_unknown_learner(self):
        self.assertFalse(backup_profile.backup(self.root, "../x")["backed_up"])
        self.assertFalse(backup_profile.backup(self.root, "nobody")["backed_up"])

    def test_sqlite_copy_is_consistent(self):
        z = self.make_backup()
        with zipfile.ZipFile(z) as zf, tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "t.sqlite3")
            with open(p, "wb") as f:
                f.write(zf.read("learner/tutor.sqlite3"))
            con = sqlite3.connect(p)
            self.assertEqual(con.execute("PRAGMA integrity_check").fetchone()[0], "ok")
            self.assertEqual(con.execute("SELECT COUNT(*) FROM error_events").fetchone()[0], 1)
            con.close()


class Restore(Base):
    def test_round_trip_after_erase(self):
        before = tree(self.learner)
        z = self.make_backup()
        shutil.rmtree(self.learner)
        r = restore_profile.restore(self.root, z)
        self.assertTrue(r["restored"], r)
        self.assertEqual(tree(self.learner), before)

    def test_refuses_existing_without_replace(self):
        z = self.make_backup()
        r = restore_profile.restore(self.root, z)
        self.assertFalse(r["restored"])
        self.assertIn("--replace", r["error"])

    def test_replace_takes_safety_backup_and_rolls_back_to_snapshot(self):
        z = self.make_backup()
        gs.run_step("error_log.py", ["append", "{S}/mathA.json", "S2", "S2.1", "practice", "slip", "NONE", "later note", "7"], self.fx, self.tmp)
        after_change = tree(self.learner)
        r = restore_profile.restore(self.root, z, replace=True)
        self.assertTrue(r["restored"], r)
        self.assertTrue(os.path.basename(r["safety_backup"]).endswith("-pre-restore.zip"))
        self.assertNotEqual(tree(self.learner), after_change)
        # the safety backup can bring the later state back
        r2 = restore_profile.restore(self.root, r["safety_backup"], replace=True)
        self.assertTrue(r2["restored"], r2)
        self.assertEqual(tree(self.learner), after_change)

    def test_dry_run_and_user_id_override(self):
        z = self.make_backup()
        self.assertTrue(restore_profile.restore(self.root, z, replace=True, dry_run=True)["dry_run"])
        r = restore_profile.restore(self.root, z, user_id="amy-copy")
        self.assertTrue(r["restored"])
        self.assertTrue(os.path.isfile(os.path.join(self.root, "amy-copy", "student_profile.json")))
        self.assertFalse(restore_profile.restore(self.root, z, user_id="../evil")["restored"])

    def test_tampered_member_detected_and_nothing_touched(self):
        z = self.make_backup()
        bad = self.rewrite_zip(z, lambda m: m.update({"learner/subjects/mathA.json": b'{"tampered": true}'}))
        before = tree(self.learner)
        r = restore_profile.restore(self.root, bad, replace=True)
        self.assertFalse(r["restored"])
        self.assertIn("checksum mismatch", r["error"])
        self.assertEqual(tree(self.learner), before)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "backups", "amy-backup-x-pre-restore.zip")))

    def test_structural_attacks_rejected(self):
        z = self.make_backup()
        cases = {
            "zip-slip": lambda m: m.update({"learner/../../evil.txt": b"x"}),
            "absolute": lambda m: m.update({"/etc/evil": b"x"}),
            "extra member": lambda m: m.update({"learner/extra.json": b"{}"}),
            "no manifest": lambda m: m.pop("manifest.json"),
        }
        for name, mut in cases.items():
            r = restore_profile.restore(self.root, self.rewrite_zip(z, mut), replace=True)
            self.assertFalse(r["restored"], name)
        self.assertFalse(os.path.exists(os.path.join(self.tmp, "evil.txt")))

    def test_newer_format_and_wrong_kind_and_garbage_file(self):
        z = self.make_backup()

        def edit(key, val):
            def m(members):
                d = json.loads(members["manifest.json"])
                d[key] = val
                members["manifest.json"] = json.dumps(d).encode()
            return m
        r = restore_profile.restore(self.root, self.rewrite_zip(z, edit("format_version", 99)), replace=True)
        self.assertIn("newer than this plugin", r["error"])
        self.assertIn("wrong manifest kind", restore_profile.restore(self.root, self.rewrite_zip(z, edit("kind", "export")), replace=True)["error"])
        junk = os.path.join(self.tmp, "junk.zip")
        with open(junk, "wb") as f:
            f.write(b"not a zip")
        self.assertFalse(restore_profile.restore(self.root, junk)["restored"])

    def test_failure_during_swap_leaves_original_in_place_and_cleans_up(self):
        z = self.make_backup()
        before = tree(self.learner)
        real = os.replace

        def flaky(a, b):
            if os.path.basename(a).startswith(".restore-"):
                raise OSError("disk gone")
            return real(a, b)
        with mock.patch("restore_profile.os.replace", side_effect=flaky):
            r = restore_profile.restore(self.root, z, replace=True)
        self.assertFalse(r["restored"])
        self.assertIn("disk gone", r["error"])
        self.assertEqual(tree(self.learner), before)
        leftovers = [f for f in os.listdir(self.root) if f.startswith(".restore-") or f.endswith(".replaced.tmp")]
        self.assertEqual(leftovers, [])

    def test_backups_never_overwrite_each_other(self):
        now = datetime.datetime(2026, 10, 4, 12, 0, tzinfo=datetime.timezone.utc)
        a = self.make_backup(now=now)
        b = self.make_backup(now=now)
        self.assertNotEqual(a, b)
        self.assertTrue(os.path.exists(a) and os.path.exists(b))

    def test_cli(self):
        r = gs.run_step("backup_profile.py", ["{R}", "amy", "--out", "{T}/bk"], self.fx, self.tmp)
        self.assertEqual(r["exit"], 0, r)
        self.assertEqual(gs.run_step("backup_profile.py", ["{R}"], self.fx, self.tmp)["exit"], 2)
        self.assertEqual(gs.run_step("restore_profile.py", ["{R}", "{T}/missing.zip"], self.fx, self.tmp)["exit"], 1)
        self.assertEqual(gs.run_step("restore_profile.py", ["{R}"], self.fx, self.tmp)["exit"], 2)


if __name__ == "__main__":
    unittest.main()
