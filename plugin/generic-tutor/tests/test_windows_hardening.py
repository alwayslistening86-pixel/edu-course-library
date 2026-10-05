"""Things that break on Windows but not on a Linux CI box: legacy console code pages and briefly locked files."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
from tutorlib import atomic_io  # noqa: E402


class Encoding(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)

    def run_script(self, script, args, stdin_bytes=None, encoding="cp1252"):
        env = dict(os.environ, PYTHONIOENCODING=encoding, PYTHONUTF8="0")
        return subprocess.run([sys.executable, os.path.join(gs.SCRIPTS, script)] + args, input=stdin_bytes, capture_output=True, env=env, cwd=self.tmp)

    def test_utf8_stdin_survives_a_legacy_console_code_page(self):
        text = "Revised: price £5 and café déjà vu — “quoted”"
        subj = f"{self.fx['S']}/mathA.json"
        p = self.run_script("session_state.py", ["note", subj, "2026-10-05"], text.encode("utf-8"))
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertEqual(gs.read_json(subj)["last_session_summary"], text)

    def test_cards_with_accents_round_trip(self):
        import json
        deck = f"{self.fx['S']}/solo_review_deck.json"
        cards = [{"front": "Quelle est la capitale de la Côte d'Ivoire?", "back": "Yamoussoukro (£0 — nothing)"}]
        p = self.run_script("deck_add.py", [deck, "solo", "S1"], json.dumps(cards, ensure_ascii=False).encode("utf-8"))
        self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
        self.assertEqual(gs.read_json(deck)["cards"][0]["back"], "Yamoussoukro (£0 — nothing)")

    def test_help_text_with_non_ascii_characters_never_crashes(self):
        for script in sorted(f for f in os.listdir(gs.SCRIPTS) if f.endswith(".py")):
            p = self.run_script(script, ["--help"], encoding="ascii")
            self.assertEqual(p.returncode, 0, f"{script}: {p.stderr[-200:]!r}")


class LockedFiles(unittest.TestCase):
    def test_replace_waits_out_a_brief_permission_error(self):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        target = os.path.join(d, "x.json")
        real = os.replace
        calls = {"n": 0}

        def flaky(src, dst):
            calls["n"] += 1
            if calls["n"] < 3:
                raise PermissionError("held by another process")
            return real(src, dst)

        with mock.patch("tutorlib.atomic_io.os.replace", side_effect=flaky), mock.patch("tutorlib.atomic_io.time.sleep"):
            atomic_io.write_json(target, {"a": 1})
        self.assertEqual(calls["n"], 3)
        self.assertEqual(gs.read_json(target), {"a": 1})

    def test_a_permanent_permission_error_is_raised_and_leaves_no_temp_file(self):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        target = os.path.join(d, "x.json")
        with mock.patch("tutorlib.atomic_io.os.replace", side_effect=PermissionError("locked")), mock.patch("tutorlib.atomic_io.time.sleep"):
            with self.assertRaises(PermissionError):
                atomic_io.write_json(target, {"a": 1})
        self.assertEqual(os.listdir(d), [])


if __name__ == "__main__":
    unittest.main()
