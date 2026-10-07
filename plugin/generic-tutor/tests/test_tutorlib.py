"""Tests for tutorlib: atomic_io (E-03) and filelock (E-04), incl. concurrent real script calls."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from unittest import mock

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

from tutorlib import atomic_io, filelock  # noqa: E402


class TmpCase(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.d, True)

    def p(self, name):
        return os.path.join(self.d, name)


class AtomicIO(TmpCase):
    def test_format_matches_legacy_writers(self):
        data = {"b": 1, "a": ["é", {"x": None}]}
        atomic_io.write_json(self.p("f.json"), data)
        legacy = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        with open(self.p("f.json"), encoding="utf-8") as f:
            self.assertEqual(f.read(), legacy)

    def test_failure_mid_write_keeps_old_file_and_leaves_no_temp(self):
        atomic_io.write_json(self.p("f.json"), {"v": 1})
        with mock.patch("tutorlib.atomic_io.json.dump", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                atomic_io.write_json(self.p("f.json"), {"v": 2})
        with open(self.p("f.json")) as f:
            self.assertEqual(json.load(f), {"v": 1})
        self.assertEqual(os.listdir(self.d), ["f.json"])

    def test_unserialisable_data_keeps_old_file(self):
        atomic_io.write_json(self.p("f.json"), {"v": 1})
        with self.assertRaises(TypeError):
            atomic_io.write_json(self.p("f.json"), {"v": object()})
        with open(self.p("f.json")) as f:
            self.assertEqual(json.load(f), {"v": 1})
        self.assertEqual(os.listdir(self.d), ["f.json"])

    def test_backup_keeps_previous_version(self):
        atomic_io.write_json(self.p("f.json"), {"v": 1})
        atomic_io.write_json(self.p("f.json"), {"v": 2}, backup=True)
        with open(self.p("f.json.bak")) as f:
            self.assertEqual(json.load(f), {"v": 1})
        with open(self.p("f.json")) as f:
            self.assertEqual(json.load(f), {"v": 2})


class FileLock(TmpCase):
    def test_reentrant_in_process(self):
        with filelock.file_lock(self.p("x.json")):
            with filelock.file_lock(self.p("x.json")):
                self.assertTrue(os.path.exists(self.p("x.json.lock")))
            self.assertTrue(os.path.exists(self.p("x.json.lock")))
        self.assertFalse(os.path.exists(self.p("x.json.lock")))

    def test_lock_removed_after_exception(self):
        with self.assertRaises(ValueError):
            with filelock.file_lock(self.p("x.json")):
                raise ValueError("boom")
        self.assertFalse(os.path.exists(self.p("x.json.lock")))

    def test_timeout_when_held_elsewhere(self):
        with open(self.p("x.json.lock"), "w") as f:
            f.write("other-process")
        with self.assertRaises(filelock.LockTimeout):
            with filelock.file_lock(self.p("x.json"), timeout=0.2):
                pass

    def test_stale_lock_is_broken(self):
        lp = self.p("x.json.lock")
        with open(lp, "w") as f:
            f.write("dead-process")
        old = time.time() - 3600
        os.utime(lp, (old, old))
        with filelock.file_lock(self.p("x.json"), timeout=1, stale=30):
            pass
        self.assertFalse(os.path.exists(lp))

    def _fail_first(self, name, n, exc):
        """Patch os.<name> to raise `exc` for the first n calls, then behave normally; return the call counter."""
        real, calls = getattr(os, name), {"n": 0}

        def flaky(*a, **kw):
            calls["n"] += 1
            if calls["n"] <= n:
                raise exc
            return real(*a, **kw)
        patcher = mock.patch.object(filelock.os, name, flaky)
        patcher.start()
        self.addCleanup(patcher.stop)
        return calls

    def test_windows_style_permission_error_while_creating_is_retried(self):
        self.addCleanup(setattr, filelock, "PERMISSION_IS_CONTENTION", filelock.PERMISSION_IS_CONTENTION)
        filelock.PERMISSION_IS_CONTENTION = True
        calls = self._fail_first("open", 3, PermissionError(13, "Access is denied"))
        with filelock.file_lock(self.p("x.json"), timeout=5):
            self.assertTrue(os.path.exists(self.p("x.json.lock")))
        self.assertGreater(calls["n"], 3)
        self.assertFalse(os.path.exists(self.p("x.json.lock")))

    def test_a_real_permission_error_elsewhere_still_surfaces_at_once(self):
        self.addCleanup(setattr, filelock, "PERMISSION_IS_CONTENTION", filelock.PERMISSION_IS_CONTENTION)
        filelock.PERMISSION_IS_CONTENTION = False
        self._fail_first("open", 99, PermissionError(13, "Permission denied"))
        with self.assertRaises(PermissionError):
            with filelock.file_lock(self.p("x.json"), timeout=5):
                pass

    def test_a_timeout_names_the_underlying_error(self):
        self.addCleanup(setattr, filelock, "PERMISSION_IS_CONTENTION", filelock.PERMISSION_IS_CONTENTION)
        filelock.PERMISSION_IS_CONTENTION = True
        self._fail_first("open", 10 ** 6, PermissionError(13, "Access is denied"))
        with self.assertRaises(filelock.LockTimeout) as cm:
            with filelock.file_lock(self.p("x.json"), timeout=0.2):
                pass
        self.assertIn("PermissionError", str(cm.exception))

    def test_a_brief_permission_error_while_unlocking_is_retried_so_no_lock_is_left_behind(self):
        with filelock.file_lock(self.p("x.json")):
            calls = self._fail_first("unlink", 2, PermissionError(13, "Access is denied"))
        self.assertGreaterEqual(calls["n"], 3)
        self.assertFalse(os.path.exists(self.p("x.json.lock")))

    def test_a_permanent_unlink_failure_does_not_raise(self):
        with filelock.file_lock(self.p("x.json")):
            self._fail_first("unlink", 10 ** 6, PermissionError(13, "Access is denied"))
        # the lock file is left for the stale-lock rule; the caller's work is not turned into an error

    def test_decorator_locks_named_argument(self):
        seen = []

        @filelock.locked("path")
        def f(a, path):
            seen.append(os.path.exists(path + ".lock"))
        f(1, self.p("y.json"))
        self.assertEqual(seen, [True])
        self.assertFalse(os.path.exists(self.p("y.json.lock")))


class ConcurrentScriptCalls(TmpCase):
    def test_parallel_error_log_appends_all_land(self):
        subj = self.p("course.json")
        with open(subj, "w") as f:
            json.dump({"schema_version": 5, "course_id": "c", "error_patterns": [], "item_mastery": {}}, f)
        script = os.path.join(SCRIPTS, "error_log.py")
        n = 12
        procs = [subprocess.Popen(
            [sys.executable, script, "append", subj, "S1", f"I{i}", "practice", "slip", "NONE", f"note {i}", str(i)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) for i in range(n)]
        outs = [p.communicate() for p in procs]
        for (out, err), p in zip(outs, procs, strict=True):
            self.assertEqual(p.returncode, 0, out + err)
        with open(subj) as f:
            d = json.load(f)
        self.assertEqual(len(d["error_patterns"]), n)
        self.assertEqual(len({e["id"] for e in d["error_patterns"]}), n)
        self.assertFalse(os.path.exists(subj + ".lock"))


if __name__ == "__main__":
    unittest.main()
