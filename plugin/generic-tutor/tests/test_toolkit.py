"""
Tests for the v1.6.0 client-side toolkit: core.py's path resolution and
schema-awareness, bootstrap_scripts.py's new package-deployment support,
and each read-only module's pure logic (backup, health, progress,
review_due, errors). The GUI (gui.pyw) is wiring only over these same
functions and is smoke-tested manually (tkinter isn't available in this
test environment) — nothing here depends on a display.

    python3 -m unittest discover tests -v
"""
import json
import os
import shutil
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
TOOLKIT = os.path.join(SCRIPTS, "toolkit")
sys.path.insert(0, SCRIPTS)
sys.path.insert(0, TOOLKIT)

import bootstrap_scripts  # noqa: E402
import core  # noqa: E402
import backup  # noqa: E402
import health  # noqa: E402
import progress  # noqa: E402
import review_due  # noqa: E402
import errors  # noqa: E402


def _w(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


class FakeEduCase(unittest.TestCase):
    """Builds a minimal, real-shaped EDU_ROOT under a tmp dir for each test."""

    def setUp(self):
        self.root = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def make_learner(self, learner_id, session_slot=10, consent="granted"):
        _w(os.path.join(self.root, "profile", learner_id, "student_profile.json"), {
            "schema_version": 2, "learner_id": learner_id, "session_slot": session_slot,
            "consent": {"status": consent}, "highest_level_cleared": 0, "roster": {"max_incomplete_courses": 2},
        })

    def make_subject(self, learner_id, course_id, **extra):
        base = {"schema_version": 5, "course_id": course_id, "roster_state": "active",
                "current_stage": "S1", "confidence": 0.5, "error_patterns": [], "item_mastery": {}}
        base.update(extra)
        _w(os.path.join(self.root, "profile", learner_id, "subjects", f"{course_id}.json"), base)

    def make_review_deck(self, learner_id, course_id, cards):
        _w(os.path.join(self.root, "profile", learner_id, "subjects", f"{course_id}_review_deck.json"),
           {"schema_version": 1, "course_id": course_id, "cards": cards})

    def make_course(self, course_id, **extra):
        base = {"schema_version": 4, "standalone": True, "coverage_status": "unverified",
                "grounding_status": "verified"}
        base.update(extra)
        _w(os.path.join(self.root, "courses", course_id, "course.json"), base)


class TestCorePaths(FakeEduCase):
    def test_edu_root_env_override_used(self):
        self.assertEqual(core.edu_root(), os.environ.get("EDU_TOOLKIT_ROOT", core._DEFAULT_EDU_ROOT))

    def test_list_learners_empty_when_no_profiles(self):
        self.assertEqual(core.list_learners(self.root), [])

    def test_list_learners_finds_real_profile(self):
        self.make_learner("alex")
        self.assertEqual(core.list_learners(self.root), ["alex"])

    def test_list_learners_ignores_folder_without_student_profile(self):
        os.makedirs(os.path.join(self.root, "profile", "stray"))
        self.assertEqual(core.list_learners(self.root), [])

    def test_current_session_slot_reads_fresh(self):
        self.make_learner("alex", session_slot=7)
        self.assertEqual(core.current_session_slot("alex", self.root), 7)

    def test_load_json_missing_file_reports_error_not_raise(self):
        result = core.load_json(os.path.join(self.root, "nope.json"))
        self.assertFalse(core.is_ok(result))
        self.assertIn("__error__", result)

    def test_list_enrolled_courses_excludes_review_deck_files(self):
        self.make_subject("alex", "gcse_maths")
        self.make_review_deck("alex", "gcse_maths", [])
        self.assertEqual(core.list_enrolled_courses("alex", self.root), ["gcse_maths"])


class TestSchemaStatus(FakeEduCase):
    def test_current_subject_schema(self):
        self.make_subject("alex", "x")
        subj = core.load_subject("alex", "x", self.root)
        status = core.schema_status(subj, "subject")
        self.assertEqual(status["status"], "current")

    def test_older_subject_schema_flagged_not_migrated(self):
        subj = {"schema_version": 3}
        status = core.schema_status(subj, "subject")
        self.assertEqual(status["status"], "older")

    def test_newer_than_toolkit_flagged(self):
        subj = {"schema_version": 999}
        status = core.schema_status(subj, "subject")
        self.assertEqual(status["status"], "newer_than_this_toolkit")

    def test_unreadable_flagged(self):
        status = core.schema_status({"__error__": "boom"}, "subject")
        self.assertEqual(status["status"], "unreadable")


class TestBackup(FakeEduCase):
    def test_backup_zips_profile_and_logs(self):
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths")
        result = backup.create_backup("alex", root=self.root)
        self.assertNotIn("error", result)
        self.assertTrue(os.path.isfile(result["zip_path"]))
        self.assertGreater(result["files_written"], 0)
        log_path = os.path.join(self.root, "profile", "alex", "toolkit_log", "backups.jsonl")
        self.assertTrue(os.path.isfile(log_path))

    def test_backup_missing_learner_errors_cleanly(self):
        result = backup.create_backup("nobody", root=self.root)
        self.assertIn("error", result)

    def test_backup_never_touches_courses_unless_asked(self):
        self.make_learner("alex")
        self.make_course("gcse_maths")
        result = backup.create_backup("alex", root=self.root)
        self.assertEqual(result["included_courses"], [])

    def test_backup_includes_requested_course(self):
        self.make_learner("alex")
        self.make_course("gcse_maths")
        result = backup.create_backup("alex", root=self.root, include_courses=["gcse_maths"])
        self.assertEqual(result["included_courses"], ["gcse_maths"])

    def test_backup_default_location_is_outside_the_learner_folder(self):
        self.make_learner("alex")
        result = backup.create_backup("alex", root=self.root)
        self.assertEqual(os.path.dirname(result["zip_path"]), os.path.join(self.root, "backups"))

    def test_backup_does_not_rezip_its_own_exports(self):
        self.make_learner("alex")
        backup.create_backup("alex", root=self.root)
        result2 = backup.create_backup("alex", root=self.root)
        # second backup's zip should not contain the first backup's zip
        import zipfile
        with zipfile.ZipFile(result2["zip_path"]) as zf:
            names = zf.namelist()
        self.assertFalse(any(n.endswith(".zip") for n in names))


class TestHealth(FakeEduCase):
    def test_no_learners_reports_note_not_error(self):
        result = health.check_health(root=self.root)
        self.assertEqual(result["learners"], [])
        self.assertIn("note", result)

    def test_flags_off_current_schema(self):
        self.make_learner("alex")
        self.make_subject("alex", "old_course", schema_version=3)
        result = health.check_health(root=self.root, learner_id="alex")
        self.assertIn("old_course", result["learners"][0]["off_current_schema"])

    def test_course_needing_attention_flagged(self):
        self.make_course("suspended_course", grounding_status="suspended")
        self.make_learner("alex")
        result = health.check_health(root=self.root, learner_id="alex")
        self.assertIn("suspended_course", result["courses_needing_attention"])

    def test_deployed_scripts_version_reads_manifest(self):
        _w(os.path.join(self.root, ".tutor-scripts", ".manifest.json"),
           {"plugin_version": "1.6.0", "files": [], "packages": ["toolkit"]})
        result = health.check_health(root=self.root)
        self.assertEqual(result["deployed_scripts"]["plugin_version"], "1.6.0")


class TestProgress(FakeEduCase):
    def test_snapshot_basic_shape(self):
        self.make_learner("alex", session_slot=12)
        self.make_subject("alex", "gcse_maths", confidence=0.7)
        result = progress.snapshot("alex", root=self.root)
        self.assertEqual(result["session_slot"], 12)
        self.assertEqual(result["courses"][0]["confidence"], 0.7)

    def test_mastery_summary_reports_lowest_items(self):
        mastery = {"RM6": {"p_mastery": 0.2}, "RM7": {"p_mastery": 0.9}}
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths", item_mastery=mastery)
        result = progress.snapshot("alex", root=self.root)
        low = result["courses"][0]["mastery"]["lowest"]
        self.assertEqual(low[0]["item_id"], "RM6")

    def test_open_error_count_excludes_resolved(self):
        entries = [
            {"item_id": "RM6", "cause": "slip", "resolved": False},
            {"item_id": "RM7", "cause": "slip", "resolved": True},
        ]
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths", error_patterns=entries)
        result = progress.snapshot("alex", root=self.root)
        self.assertEqual(result["courses"][0]["open_error_count"], 1)


class TestReviewDue(FakeEduCase):
    def test_due_now_vs_upcoming_split(self):
        self.make_learner("alex", session_slot=10)
        self.make_subject("alex", "gcse_maths")
        cards = [
            {"id": "c1", "stage_id": "S1", "item_id": "RM6", "due_at_slot": 5},
            {"id": "c2", "stage_id": "S1", "item_id": "RM7", "due_at_slot": 12},
            {"id": "c3", "stage_id": "S1", "item_id": "RM8", "due_at_slot": 20},
        ]
        self.make_review_deck("alex", "gcse_maths", cards)
        result = review_due.due_cards("alex", root=self.root, within_slots=5)
        self.assertEqual([c["card_id"] for c in result["due_now"]], ["c1"])
        self.assertEqual([c["card_id"] for c in result["upcoming"]], ["c2"])

    def test_never_writes_anything(self):
        self.make_learner("alex")
        self.make_subject("alex", "gcse_maths")
        self.make_review_deck("alex", "gcse_maths", [{"id": "c1", "due_at_slot": 0}])
        deck_path = os.path.join(self.root, "profile", "alex", "subjects", "gcse_maths_review_deck.json")
        with open(deck_path) as f:
            before = f.read()
        review_due.due_cards("alex", root=self.root)
        with open(deck_path) as f:
            after = f.read()
        self.assertEqual(before, after)


class TestErrors(FakeEduCase):
    def test_aggregate_groups_by_cause(self):
        self.make_learner("alex")
        entries = [
            {"stage_id": "S1", "item_id": "RM6", "cause": "slip", "resolved": False, "id": "e1"},
            {"stage_id": "S1", "item_id": "RM6", "cause": "slip", "resolved": False, "id": "e2"},
            {"stage_id": "S1", "item_id": "RM7", "cause": "comprehension", "resolved": True, "id": "e3"},
        ]
        self.make_subject("alex", "gcse_maths", error_patterns=entries)
        result = errors.aggregate("alex", root=self.root)
        self.assertEqual(result["by_cause"]["slip"], 2)
        self.assertEqual(result["most_frequent_causes"][0]["cause"], "slip")

    def test_open_only_excludes_resolved(self):
        self.make_learner("alex")
        entries = [{"stage_id": "S1", "item_id": "RM7", "cause": "comprehension", "resolved": True, "id": "e3"}]
        self.make_subject("alex", "gcse_maths", error_patterns=entries)
        result = errors.aggregate("alex", root=self.root, open_only=True)
        self.assertEqual(result["total_entries"], 0)


class TestBootstrapPackages(unittest.TestCase):
    def setUp(self):
        self.src = tempfile.mkdtemp()
        self.target = tempfile.mkdtemp()
        self.plugin_json = os.path.join(self.src, "plugin.json")
        _w(self.plugin_json, {"version": "1.6.0"})
        with open(os.path.join(self.src, "solo.py"), "w") as f:
            f.write("# a flat script\n")
        pkg = os.path.join(self.src, "toolkit")
        os.makedirs(pkg)
        with open(os.path.join(pkg, "__init__.py"), "w") as f:
            f.write("")
        with open(os.path.join(pkg, "core.py"), "w") as f:
            f.write("VALUE = 1\n")

    def tearDown(self):
        shutil.rmtree(self.src, ignore_errors=True)
        shutil.rmtree(self.target, ignore_errors=True)

    def test_fresh_deploy_copies_package_as_unit(self):
        result = bootstrap_scripts.bootstrap(self.src, self.plugin_json, self.target)
        self.assertEqual(result["action"], "deployed_fresh")
        self.assertTrue(os.path.isfile(os.path.join(self.target, "toolkit", "__init__.py")))
        self.assertTrue(os.path.isfile(os.path.join(self.target, "toolkit", "core.py")))
        self.assertTrue(os.path.isfile(os.path.join(self.target, "solo.py")))

    def test_a_directory_without_init_is_not_treated_as_a_package(self):
        os.makedirs(os.path.join(self.src, "not_a_package"))
        with open(os.path.join(self.src, "not_a_package", "stray.py"), "w") as f:
            f.write("")
        bootstrap_scripts.bootstrap(self.src, self.plugin_json, self.target)
        self.assertFalse(os.path.isdir(os.path.join(self.target, "not_a_package")))

    def test_update_replaces_stale_package_wholesale(self):
        bootstrap_scripts.bootstrap(self.src, self.plugin_json, self.target)
        # simulate a stale file left in the deployed package from an older version
        with open(os.path.join(self.target, "toolkit", "old_module.py"), "w") as f:
            f.write("")
        _w(self.plugin_json, {"version": "1.7.0"})
        result = bootstrap_scripts.bootstrap(self.src, self.plugin_json, self.target)
        self.assertEqual(result["action"], "updated")
        self.assertFalse(os.path.isfile(os.path.join(self.target, "toolkit", "old_module.py")))
        self.assertTrue(os.path.isfile(os.path.join(self.target, "toolkit", "core.py")))

    def test_manifest_records_packages(self):
        bootstrap_scripts.bootstrap(self.src, self.plugin_json, self.target)
        with open(os.path.join(self.target, ".manifest.json")) as f:
            manifest = json.load(f)
        self.assertEqual(manifest["packages"], ["toolkit"])

    def test_up_to_date_does_not_touch_package(self):
        bootstrap_scripts.bootstrap(self.src, self.plugin_json, self.target)
        marker = os.path.join(self.target, "toolkit", "untouched.marker")
        with open(marker, "w") as f:
            f.write("x")
        result = bootstrap_scripts.bootstrap(self.src, self.plugin_json, self.target)
        self.assertEqual(result["action"], "up_to_date")
        self.assertTrue(os.path.isfile(marker))


if __name__ == "__main__":
    unittest.main()


class RootResolution(unittest.TestCase):
    def setUp(self):
        from toolkit import core
        self.core = core
        self.saved = (core._root_override, os.environ.get("EDU_TOOLKIT_ROOT"), os.environ.get("EDU_ROOT"))
        self.addCleanup(self.restore)
        core.set_root(None)
        os.environ.pop("EDU_TOOLKIT_ROOT", None)
        os.environ.pop("EDU_ROOT", None)

    def restore(self):
        self.core.set_root(self.saved[0])
        for key, val in zip(("EDU_TOOLKIT_ROOT", "EDU_ROOT"), self.saved[1:], strict=True):
            if val is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = val

    def test_precedence_flag_then_toolkit_env_then_plain_env_then_location(self):
        self.assertEqual(self.core.edu_root(), self.core._DEFAULT_EDU_ROOT)
        os.environ["EDU_ROOT"] = "/from/env"
        self.assertEqual(self.core.edu_root(), os.path.abspath("/from/env"))
        os.environ["EDU_TOOLKIT_ROOT"] = "/from/toolkit/env"
        self.assertEqual(self.core.edu_root(), os.path.abspath("/from/toolkit/env"))
        self.core.set_root("/from/flag")
        self.assertEqual(self.core.edu_root(), os.path.abspath("/from/flag"))

    def test_cli_root_flag_is_accepted_anywhere_and_used(self):
        import subprocess
        import tempfile
        root = tempfile.mkdtemp()
        self.addCleanup(__import__("shutil").rmtree, root, True)
        os.makedirs(os.path.join(root, "profile"))
        for argv in (["--root", root, "health"], ["health", "--root", root]):
            p = subprocess.run([sys.executable, "-m", "toolkit"] + argv, capture_output=True, text=True, cwd=SCRIPTS, timeout=60)
            self.assertNotIn("Traceback", p.stderr, argv)
            self.assertEqual(json.loads(p.stdout)["edu_root"], root, argv)
        p = subprocess.run([sys.executable, "-m", "toolkit", "--root"], capture_output=True, text=True, cwd=SCRIPTS)
        self.assertEqual(p.returncode, 2)
