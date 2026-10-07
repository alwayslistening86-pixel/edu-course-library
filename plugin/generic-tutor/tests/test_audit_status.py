"""K-15: audit_status.py decides 'audit recommended'."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

import audit_status as au  # noqa: E402
import golden_support as gs  # noqa: E402
from tutorlib import version  # noqa: E402


class Status(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)
        self.engine = version.engine_version()

    def edit(self, cid, **kw):
        p = f"{self.fx['C']}/{cid}/course.json"
        d = gs.read_json(p)
        d.update(kw)
        with open(p, "w") as f:
            json.dump(d, f)

    def affected(self):
        return {a["course_id"]: a["reasons"] for a in au.audit_status(self.fx["C"])["affected"]}

    def test_fixture_courses_are_flagged_for_what_they_lack(self):
        a = self.affected()
        self.assertEqual(a["mathA"], ["never_audited"])
        self.assertEqual(a["old"], ["old_schema", "never_audited", "never_rechecked"])

    def test_audited_at_current_version_is_clean(self):
        current = ".".join(map(str, self.engine))
        self.edit("mathA", last_audited_plugin_version=current)
        self.assertNotIn("mathA", self.affected())

    def test_patch_difference_is_not_flagged_but_minor_is(self):
        major, minor, _ = self.engine
        self.edit("mathA", last_audited_plugin_version=f"{major}.{minor}.0")
        self.assertNotIn("mathA", self.affected())
        self.edit("mathA", last_audited_plugin_version=f"{major}.{max(minor - 1, 0)}.0" if minor else f"{major - 1}.9.0")
        self.assertEqual(self.affected()["mathA"], ["audited_earlier"])
        self.edit("mathA", last_audited_plugin_version="garbage")
        self.assertEqual(self.affected()["mathA"], ["audited_earlier"])

    def test_historical_course_needs_no_recheck(self):
        self.edit("solo", last_audited_plugin_version="9.9.9", last_live_recheck=None, currency="historical")
        self.assertNotIn("solo", self.affected())

    def test_unreadable_and_missing_dir(self):
        with open(f"{self.fx['C']}/mathB/course.json", "w") as f:
            f.write("{")
        self.assertEqual(self.affected()["mathB"], ["unreadable"])
        self.assertIn("error", au.audit_status(f"{self.tmp}/nope"))

    def test_read_only(self):
        before = gs.snapshot_files(["{C}/mathA/course.json"], self.fx, self.tmp)
        au.audit_status(self.fx["C"])
        self.assertEqual(before, gs.snapshot_files(["{C}/mathA/course.json"], self.fx, self.tmp))


if __name__ == "__main__":
    unittest.main()
