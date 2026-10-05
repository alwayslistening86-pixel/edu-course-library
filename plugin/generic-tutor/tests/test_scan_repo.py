"""X-07: tools/scan_repo.py catches credentials, personal e-mail and private paths, and the real repo is clean."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(REPO, "tools"))
import scan_repo  # noqa: E402


def make_repo(files):
    d = tempfile.mkdtemp()
    subprocess.run(["git", "init", "-q", d], check=True)
    for rel, text in files.items():
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as f:
            f.write(text)
    subprocess.run(["git", "-C", d, "add", "-A"], check=True)
    return d


class Scan(unittest.TestCase):
    def test_real_repo_is_clean(self):
        self.assertEqual(scan_repo.scan(REPO), [])

    def test_seeded_problems_are_found_and_clean_text_is_not(self):
        key = "sk-ant-" + "a" * 30
        d = make_repo({
            "notes.md": f"token {key}\n",
            "docs/a.md": "contact someone.real@gmail.com or noreply@anthropic.com or test@example.com\n",
            "courses/x/course.json": "{}",
            "profile/amy/student_profile.json": "{}",
            "tests/h.sqlite3": "x",
            "ok.py": "print('hello')\n",
        })
        self.addCleanup(shutil.rmtree, d, True)
        kinds = sorted((rel, kind) for rel, _n, kind, _m in scan_repo.scan(d))
        self.assertIn(("notes.md", "anthropic-key"), kinds)
        self.assertIn(("docs/a.md", "email"), kinds)
        self.assertEqual(sum(1 for r, k in kinds if k == "email"), 1)           # only the real-looking address
        self.assertIn(("courses/x/course.json", "private-path"), kinds)
        self.assertIn(("profile/amy/student_profile.json", "private-path"), kinds)
        self.assertIn(("tests/h.sqlite3", "private-path"), kinds)
        self.assertFalse([k for k in kinds if k[0] == "ok.py"])


if __name__ == "__main__":
    unittest.main()
