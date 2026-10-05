"""E-09: every script answers --help with plain-text usage and exit 0, without touching anything."""
import os
import subprocess
import sys
import unittest

SCRIPTS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts")


class Help(unittest.TestCase):
    def test_every_script_has_help(self):
        names = sorted(f for f in os.listdir(SCRIPTS) if f.endswith(".py"))
        self.assertGreater(len(names), 30)
        for name in names:
            for flag in ("--help", "-h"):
                p = subprocess.run([sys.executable, os.path.join(SCRIPTS, name), flag], capture_output=True, text=True, timeout=30)
                self.assertEqual(p.returncode, 0, f"{name} {flag}: {p.stderr[-200:]}")
                self.assertIn(name, p.stdout, f"{name} {flag} should print its own usage")
                self.assertFalse(p.stdout.lstrip().startswith("{"), f"{name} {flag} printed JSON, not usage")


if __name__ == "__main__":
    unittest.main()
