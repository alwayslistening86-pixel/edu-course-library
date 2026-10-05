"""N-02: courses may declare min_engine_version; gate_check blocks when the install is older."""
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
from tutorlib import schema, version  # noqa: E402


class Version(unittest.TestCase):
    def test_parse_and_compare(self):
        self.assertEqual(version.parse("1.26.0"), (1, 26, 0))
        self.assertIsNone(version.parse("1.2"))
        self.assertIsNone(version.parse("x.y.z"))
        self.assertTrue(version.parse("1.10.0") > version.parse("1.9.0"))   # tuple compare, never string compare

    def test_check_min(self):
        d = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, d, True)
        with open(os.path.join(d, ".manifest.json"), "w") as f:
            json.dump({"plugin_version": "1.10.0"}, f)
        self.assertEqual(version.check_min("1.9.0", d), (True, "1.10.0"))
        self.assertEqual(version.check_min("1.10.0", d), (True, "1.10.0"))
        self.assertEqual(version.check_min("1.11.0", d), (False, "1.10.0"))
        self.assertEqual(version.check_min(None, d), (True, None))
        self.assertEqual(version.check_min("1.11.0", os.path.join(d, "nowhere")), (True, None))   # unknown -> never block

    def test_running_from_source_reads_plugin_json(self):
        self.assertIsNotNone(version.engine_version())


class Gate(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = gs.build_fixture(self.tmp)

    def gate(self, required):
        p = f"{self.fx['C']}/mathA/course.json"
        d = gs.read_json(p)
        if required:
            d["min_engine_version"] = required
        with open(p, "w") as f:
            json.dump(d, f)
        return gs.run_step("gate_check.py", ["{C}/mathA/course.json", "{S}/mathA.json", "{S}", "{C}", "2026-10-04"], self.fx, self.tmp)["stdout"]

    def test_future_requirement_blocks_with_a_clear_reason(self):
        g = self.gate("99.0.0")
        self.assertFalse(g["can_proceed"])
        self.assertEqual(g["first_blocking_gate"], "0_engine_version")
        self.assertIn("update the plugin", g["gates"]["0_engine_version"]["detail"])

    def test_met_or_absent_requirement_changes_nothing(self):
        self.assertTrue(self.gate("1.0.0")["can_proceed"])
        g = self.gate(None)
        self.assertTrue(g["can_proceed"])
        self.assertNotIn("0_engine_version", g["gates"])

    def test_schema_accepts_semver_only(self):
        c = gs.read_json(f"{self.fx['C']}/mathA/course.json")
        c["min_engine_version"] = "1.26.0"
        self.assertEqual(schema.validate(c, "course"), [])
        c["min_engine_version"] = "latest"
        self.assertTrue(schema.validate(c, "course"))


if __name__ == "__main__":
    unittest.main()
