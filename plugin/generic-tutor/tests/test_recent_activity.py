"""V-10: the write ledger reads back as plain sentences, and no logged write falls through to the generic wording."""
import os
import re
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import golden_support as gs  # noqa: E402
import recent_activity as ra  # noqa: E402


class Activity(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.s = f"{self.fx['S']}/mathA.json"
        self.c = f"{self.fx['C']}/mathA/course.json"

    def step(self, script, *args):
        return gs.run_step(script, list(args), self.fx, self.tmp)

    def test_every_logged_write_has_a_template(self):
        missing = []
        for fn in sorted(os.listdir(gs.SCRIPTS)):
            if not fn.endswith(".py"):
                continue
            with open(os.path.join(gs.SCRIPTS, fn), encoding="utf-8") as f:
                for m in re.finditer(r'@ledger\.logged\("([^"]+)",\s*"[^"]+"\)\n(?:@[^\n]+\n)*def (\w+)', f.read()):
                    if (m.group(1), m.group(2)) not in ra._TEMPLATES:
                        missing.append(m.groups())
        self.assertEqual(missing, [])

    def test_sentences_and_order(self):
        self.step("error_log.py", "append", self.s, "S2", "S2.1", "practice", "slip", "NONE", "x", "6")
        self.step("record_stage_result.py", "apply", self.s, self.c, "S2", "pass")
        r = ra.build(self.fx["L"])
        texts = [a["text"] for a in r["activity"]]
        self.assertEqual(texts[0], "Recorded a pass for stage S2 in mathA.")
        self.assertIn("Logged a mistake on item S2.1 (slip) in mathA.", texts)
        self.assertEqual(ra.build(self.fx["L"], last=1)["showing"], 1)

    def test_skipped_writes_say_so_and_free_text_never_appears(self):
        pf = f"{self.fx['L']}/student_profile.json"
        import json
        p = gs.read_json(pf)
        p["consent"]["status"] = "limited"
        with open(pf, "w") as f:
            json.dump(p, f)
        self.step("error_log.py", "append", self.s, "S2", "S2.1", "practice", "slip", "NONE", "SECRET-NOTE-TEXT", "6")
        r = ra.build(self.fx["L"])
        self.assertNotIn("SECRET-NOTE-TEXT", json.dumps(r))
        self.assertTrue(any("NOT saved" in a["text"] for a in r["activity"]), r)

    def test_empty_ledger(self):
        r = ra.build(self.fx["L"])
        self.assertEqual((r["total_writes_logged"], r["activity"]), (0, []))


if __name__ == "__main__":
    unittest.main()
