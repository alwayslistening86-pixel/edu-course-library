"""ADR 0012 build tasks B-04.5c and B-04.5d: an error entry must name an item of the course and a misconception that exists."""
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
from tutorlib import schema  # noqa: E402


class Base(unittest.TestCase):
    def setUp(self):
        self.d = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.d, True)
        self.fx = gs.build_fixture(self.d)
        self.course = os.path.join(self.fx["C"], "mathA")
        self.subj = os.path.join(self.fx["S"], "mathA.json")
        self.mfile = os.path.join(self.course, "stages", "S1", "misconceptions.json")

    def log(self, item="S1.1", misc="NONE", stage="S1", *extra):
        return gs.run_step("error_log.py", ["append", self.subj, stage, item, "practice", "slip", misc, "dropped a sign", "9", "NONE", *extra], self.fx, self.d)

    def errors(self):
        with open(self.subj, encoding="utf-8") as f:
            return json.load(f)["error_patterns"]

    def set_ids(self):
        with open(self.mfile, encoding="utf-8") as f:
            data = json.load(f)
        data[0]["id"] = "MC-S1-1"
        with open(self.mfile, "w", encoding="utf-8") as f:
            json.dump(data, f)


class ItemCheck(Base):
    def test_an_invented_item_is_refused_and_nothing_is_written(self):
        r = self.log("S9.9", "NONE", "S1", "--course-dir", self.course)
        self.assertEqual(r["exit"], 1, r)
        self.assertIn("not an item of this course", r["stdout"]["error"])
        self.assertEqual(self.errors(), [])

    def test_a_real_item_is_accepted(self):
        r = self.log("S1.1", "NONE", "S1", "--course-dir", self.course)
        self.assertEqual(r["exit"], 0, r)
        self.assertNotIn("warnings", r["stdout"])
        self.assertEqual(len(self.errors()), 1)

    def test_an_item_of_another_stage_is_accepted_with_a_warning_because_practice_interleaves(self):
        r = self.log("S2.1", "NONE", "S1", "--course-dir", self.course)
        self.assertEqual(r["exit"], 0, r)
        self.assertIn("belongs to stage S2", r["stdout"]["warnings"][0])

    def test_none_is_not_checked_and_a_course_that_is_not_itemised_is_not_checked(self):
        self.assertEqual(self.log("NONE", "NONE", "S1", "--course-dir", self.course)["exit"], 0)
        cmap = os.path.join(self.course, "curriculum_map.json")
        with open(cmap, encoding="utf-8") as f:
            data = json.load(f)
        data.pop("_syllabus_items")
        with open(cmap, "w", encoding="utf-8") as f:
            json.dump(data, f)
        self.assertEqual(self.log("anything", "NONE", "S1", "--course-dir", self.course)["exit"], 0)

    def test_without_a_findable_course_the_check_is_skipped_and_says_so(self):
        r = self.log("S9.9")
        self.assertEqual(r["exit"], 0, r)
        self.assertIn("not checked", r["stdout"]["course_check"])

    def test_the_data_root_is_used_when_it_can_be_found(self):
        import subprocess
        env = {**os.environ, "EDU_ROOT": self.d}
        p = subprocess.run([sys.executable, os.path.join(gs.SCRIPTS, "error_log.py"), "append", self.subj, "S1", "S9.9", "practice", "slip", "NONE", "n", "9"],
                           capture_output=True, text=True, env=env)
        self.assertEqual(p.returncode, 1, p.stdout)
        self.assertIn("not an item of this course", p.stdout)


class MisconceptionCheck(Base):
    def test_an_unknown_id_is_refused_naming_the_known_ones(self):
        self.set_ids()
        r = self.log("S1.1", "MC-S1-9", "S1", "--course-dir", self.course)
        self.assertEqual(r["exit"], 1, r)
        self.assertIn("MC-S1-1", r["stdout"]["error"])
        self.assertEqual(self.errors(), [])

    def test_a_known_id_is_accepted_and_recorded(self):
        self.set_ids()
        r = self.log("S1.1", "MC-S1-1", "S1", "--course-dir", self.course)
        self.assertEqual(r["exit"], 0, r)
        self.assertEqual(self.errors()[0]["misconception_id"], "MC-S1-1")

    def test_a_stage_with_no_ids_accepts_only_none_and_says_how_to_add_them(self):
        r = self.log("S1.1", "MC-RM6-2", "S1", "--course-dir", self.course)
        self.assertEqual(r["exit"], 1, r)
        self.assertIn("misconception_ids.py", r["stdout"]["error"])
        self.assertEqual(self.log("S1.1", "NONE", "S1", "--course-dir", self.course)["exit"], 0)

    def test_an_id_of_another_stage_is_not_accepted(self):
        self.set_ids()
        r = self.log("S2.1", "MC-S1-1", "S2", "--course-dir", self.course)
        self.assertEqual(r["exit"], 1, r)


class Schema(Base):
    def test_id_is_optional_checked_for_shape_and_must_be_unique(self):
        with open(self.mfile, encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(schema.validate(data, "misconceptions"), [])
        data[0]["id"] = "MC-S1-1"
        self.assertEqual(schema.validate(data, "misconceptions"), [])
        data[0]["id"] = "has spaces"
        self.assertTrue(schema.validate(data, "misconceptions"))
        data[0]["id"] = "MC-S1-1"
        data.append(dict(data[0]))
        self.assertTrue(any("more than once" in e for e in schema.validate(data, "misconceptions")))


class Backfill(Base):
    def run_it(self, *extra):
        return gs.run_step("misconception_ids.py", [self.course, *extra], self.fx, self.d)

    def test_dry_run_changes_nothing_and_write_adds_ids_once(self):
        with open(self.mfile, "rb") as f:
            before = f.read()
        r = self.run_it()
        self.assertEqual((r["exit"], r["stdout"]["written"], r["stdout"]["files"][0]["added"]), (0, False, ["MC-S1-1"]))
        with open(self.mfile, "rb") as f:
            self.assertEqual(f.read(), before)
        r = self.run_it("--write")
        self.assertTrue(r["stdout"]["written"])
        with open(self.mfile, encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual(data[0]["id"], "MC-S1-1")
        self.assertEqual(schema.validate(data, "misconceptions"), [])
        again = self.run_it("--write")["stdout"]
        self.assertFalse(again["written"])
        self.assertEqual(again["files"][0]["added"], [])

    def test_existing_ids_and_order_are_kept(self):
        with open(self.mfile, "w", encoding="utf-8") as f:
            json.dump([{"pattern": "first wrong idea about it", "correction": "first correction text", "source": "plausible, not board-documented"},
                       {"id": "MC-S1-1", "pattern": "second wrong idea about it", "correction": "second correction text", "source": "plausible, not board-documented"},
                       {"pattern": "third wrong idea about it", "correction": "third correction text", "source": "plausible, not board-documented"}], f)
        self.run_it("--write")
        with open(self.mfile, encoding="utf-8") as f:
            data = json.load(f)
        self.assertEqual([e["id"] for e in data], ["MC-S1-2", "MC-S1-1", "MC-S1-3"])
        self.assertEqual([e["pattern"][:5] for e in data], ["first", "secon", "third"])

    def test_a_broken_or_duplicated_file_is_left_alone(self):
        with open(self.mfile, "w", encoding="utf-8") as f:
            f.write("{not json")
        r = self.run_it("--write")["stdout"]
        self.assertEqual((r["files"], r["skipped"][0]["stage"]), ([], "S1"))
        with open(self.mfile, "w", encoding="utf-8") as f:
            json.dump([{"id": "A", "pattern": "x" * 12, "correction": "y" * 12, "source": "s" * 6}, {"id": "A", "pattern": "x" * 12, "correction": "y" * 12, "source": "s" * 6}], f)
        r = self.run_it("--write")["stdout"]
        self.assertIn("duplicate", r["skipped"][0]["reason"])

    def test_usage_and_missing_folder(self):
        self.assertEqual(gs.run_step("misconception_ids.py", [], self.fx, self.d)["exit"], 2)
        self.assertEqual(gs.run_step("misconception_ids.py", [os.path.join(self.d, "nope")], self.fx, self.d)["exit"], 1)


if __name__ == "__main__":
    unittest.main()
