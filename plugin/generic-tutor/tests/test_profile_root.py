"""B-01.2: learner folders can live outside the data root (EDU_PROFILE_ROOT / --profile-root); the default is unchanged."""
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
from test_hook_guard import Base  # noqa: E402
from tutorlib import paths  # noqa: E402


class Resolve(unittest.TestCase):
    def setUp(self):
        self.d = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)

    def test_default_is_under_the_root_and_env_beats_it(self):
        self.assertEqual(paths.profile_root("/r", env={}), os.path.join("/r", "profile"))
        self.assertEqual(paths.profile_root("/r", env={"EDU_PROFILE_ROOT": "/x/y"}), os.path.abspath("/x/y"))
        self.assertEqual(paths.profile_root("/r", "/a", env={"EDU_PROFILE_ROOT": "/x/y"}), os.path.abspath("/a"))
        self.assertIsNone(paths.profile_root(None, env={}))

    def test_layout_reports_the_separate_root(self):
        root = os.path.join(self.d, "EDU")
        for sub in ("courses", "profile", ".tutor-scripts"):
            os.makedirs(os.path.join(root, sub))
        self.assertFalse(paths.layout(root, None)["profile_separate"] or paths.layout(root).get("profile_separate"))
        other = os.path.join(self.d, "My Learner Data")                 # a path with spaces
        lay = paths.layout(root, other)
        self.assertEqual(lay["profile"], other)
        self.assertTrue(lay["profile_separate"])
        self.assertTrue(any("profile/" in p for p in lay["problems"]))   # not created yet
        os.makedirs(other)
        self.assertTrue(paths.layout(root, other)["valid"])

    def test_cli_flag(self):
        fx = gs.build_fixture(self.d)
        os.makedirs(os.path.join(self.d, ".tutor-scripts"))
        os.makedirs(os.path.join(self.d, "profile"), exist_ok=True)
        elsewhere = tempfile.mkdtemp(prefix="learner data ")
        self.addCleanup(shutil.rmtree, elsewhere, True)
        r = gs.run_step("resolve_root.py", ["--root", "{T}", "--profile-root", elsewhere], fx, self.d)
        self.assertEqual(r["exit"], 0, r)
        self.assertEqual(r["stdout"]["profile"], os.path.abspath(elsewhere))
        self.assertTrue(r["stdout"]["profile_separate"])
        self.assertEqual(gs.run_step("resolve_root.py", ["--profile-root"], fx, self.d)["exit"], 2)

    @unittest.skipUnless(os.name == "nt", "drive-letter paths only mean something on Windows")
    def test_windows_drive_path(self):
        self.assertTrue(paths.profile_root("C:\\EDU", "E:\\Learner Data").lower().startswith("e:\\"))


class GuardFollowsProfileRoot(Base):
    """The hook guard must protect learner data on the other drive exactly as it does under the root."""

    def setUp(self):
        super().setUp()
        self.prof = os.path.join(self.tmp, "stick", "Learner Data")
        shutil.copytree(os.path.join(self.root, "profile"), self.prof)
        shutil.rmtree(os.path.join(self.root, "profile"))
        self.env["EDU_PROFILE_ROOT"] = self.prof

    def test_script_owned_files_are_still_protected(self):
        d, why = self.tool("Write", file_path=os.path.join(self.prof, "ann", "student_profile.json"), content="x")
        self.assertEqual(d, "deny")
        self.assertIn("script", why)
        self.assertEqual(self.tool("Write", file_path=os.path.join(self.prof, "ann", "worksheet.md"), content="x")[0], "allow")

    def test_revoked_consent_is_found_on_the_other_drive(self):
        self.assertEqual(self.tool("Write", file_path=os.path.join(self.prof, "cy", "n.md"), content="x")[0], "deny")
        self.assertEqual(self.tool("Bash", command=f'echo hi > "{self.prof}/cy/n.txt"')[0], "deny")
        self.assertEqual(self.tool("Bash", command=f'echo hi > "{self.prof}/ann/student_profile.json"')[0], "deny")

    def test_session_start_lists_learners_from_there(self):
        out = self.fire("SessionStart")
        self.assertIn("ann", json.dumps(out))

    def test_without_the_variable_nothing_is_found_there(self):
        self.env.pop("EDU_PROFILE_ROOT")
        self.assertNotIn("ann", json.dumps(self.fire("SessionStart")))


if __name__ == "__main__":
    unittest.main()
