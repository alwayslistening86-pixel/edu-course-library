"""B-05.1: the hook guard's shell check is a text match, not a lock. These results are documented in docs/wave7/B-05-threat-model.md;
if the guard is made stronger, this test fails and that note must be updated in the same change."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import hook_guard  # noqa: E402


class KnownLimits(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.root, True)
        os.makedirs(os.path.join(self.root, "profile", "ann"))
        with open(os.path.join(self.root, "profile", "ann", "student_profile.json"), "w") as f:
            json.dump({"consent": {"status": "granted"}}, f)
        self.state = {"learner": "ann", "command": "continue"}

    def decide(self, command):
        return hook_guard.decide_bash(command, self.root, self.state)["decision"]

    def test_a_plain_redirection_is_denied(self):
        self.assertEqual(self.decide("echo x > profile/ann/student_profile.json"), "deny")

    def test_the_documented_bypasses_are_still_allowed(self):
        for command in ("python3 -c \"open('profile/ann/student_profile.json','w').write('x')\"",
                        "EDU_ROLE=staff python3 .tutor-scripts/erase_profile.py profile/ann",
                        "p=profile; python3 -c \"open('$p/ann/student_profile.json','w')\""):
            self.assertEqual(self.decide(command), "allow", command)


if __name__ == "__main__":
    unittest.main()
