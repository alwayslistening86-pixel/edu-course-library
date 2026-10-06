"""E-10/E-11: --envelope wraps any script's output as {ok, data, warnings, error{code,message}}; codes are a closed set."""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.join(os.path.dirname(HERE), "scripts")
sys.path.insert(0, SCRIPTS)

from tutorlib import cli  # noqa: E402


def run(script, *args):
    p = subprocess.run([sys.executable, os.path.join(SCRIPTS, script), *args], capture_output=True, text=True, timeout=30)
    return p.returncode, json.loads(p.stdout)


class Codes(unittest.TestCase):
    def test_classification(self):
        cases = {
            ("usage: x", 2): "E_USAGE",
            ("consent revoked", 1): "E_CONSENT",
            ("LockTimeout: busy", 1): "E_LOCKED",
            ("StateError: file has schema_version 9", 1): "E_SCHEMA",
            ("FileNotFoundError: nope", 1): "E_NOT_FOUND",
            ("stage_id 'x' not found in ladder", 1): "E_NOT_FOUND",
            ("result must be pass or fail", 1): "E_INVALID_INPUT",
        }
        for (msg, code), want in cases.items():
            self.assertEqual(cli.error_code(msg, code), want, msg)
            self.assertIn(want, cli.ERROR_CODES)

    def test_envelope_shapes(self):
        ok = cli.envelope('{"a": 1, "warnings": ["w"]}', 0)
        self.assertEqual((ok["ok"], ok["data"]["a"], ok["warnings"], ok["error"]), (True, {"a": 1, "warnings": ["w"]}["a"], ["w"], None))
        bad = cli.envelope('{"error": "boom"}', 1)
        self.assertEqual((bad["ok"], bad["data"], bad["error"]["code"]), (False, None, "E_INVALID_INPUT"))
        crash = cli.envelope("Traceback ...", 1)
        self.assertEqual(crash["error"]["code"], "E_INTERNAL")
        decision = cli.envelope('{"valid": false}', 1)             # a failing result that is not an {"error"}
        self.assertFalse(decision["ok"])
        self.assertEqual(decision["data"], {"valid": False})


class EndToEnd(unittest.TestCase):
    def test_every_script_accepts_the_flag(self):
        for name in sorted(f for f in os.listdir(SCRIPTS) if f.endswith(".py") and f != "hook_guard.py"):   # hook_guard speaks the hook protocol, not the CLI one
            p = subprocess.run([sys.executable, os.path.join(SCRIPTS, name), "--envelope"], capture_output=True, text=True, timeout=30)
            try:
                out = json.loads(p.stdout)
            except ValueError:
                self.fail(f"{name} --envelope printed no JSON: {p.stdout[-200:]} {p.stderr[-200:]}")
            self.assertEqual(set(out), {"ok", "data", "warnings", "error"}, name)


    def test_flag_position_and_exit_status(self):
        code, out = run("plan_target.py", "--envelope")
        self.assertEqual((code, out["ok"], out["error"]["code"]), (2, False, "E_USAGE"))
        code, out = run("error_log.py", "query", "/nonexistent/x.json", "--envelope")
        self.assertEqual((code, out["error"]["code"]), (1, "E_NOT_FOUND"))
        with tempfile.TemporaryDirectory() as t:
            code, out = run("resolve_root.py", "--root", t)          # legacy output unchanged without the flag
        self.assertNotIn("ok", out)

    def test_ok_envelope_without_changing_legacy_output(self):
        code, legacy = run("review_math.py", "1", "2.3", "0", "5", "true")
        code2, env = run("review_math.py", "--envelope", "1", "2.3", "0", "5", "true")
        self.assertEqual((code, code2), (0, 0))
        self.assertTrue(env["ok"])
        self.assertEqual(env["data"], legacy)


if __name__ == "__main__":
    unittest.main()
