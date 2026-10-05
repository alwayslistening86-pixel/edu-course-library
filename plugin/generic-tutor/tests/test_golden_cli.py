"""
E-01: golden-output characterisation of every script's CLI. See golden_support.py.

Each case = ordered CLI steps run against a fresh copy of the standard fixture, plus
the files whose final contents are snapshotted. Output is compared byte-for-byte
with tests/golden/<case>.json. Refactors must keep these green or change them
deliberately (UPDATE_GOLDEN=1, then review the diff).
"""
import difflib
import os
import tempfile
import unittest

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import golden_support as gs  # noqa: E402

SUBJ = "{S}/mathA.json"
DECK = "{S}/mathA_review_deck.json"

CASES = {
    "apply_capabilities_dry": ([("apply_capabilities.py", ["{P}/student_profile.json", "{C}/design/course.json", "{S}/design.json", "--dry-run"])], []),
    "cohort_status": ([("cohort_status.py", ["{S}", "{C}"])], []),
    "confidence_compute": ([("confidence_update.py", ["compute", "0.5", "pass_clean"]),
                            ("confidence_update.py", ["compute", "0.5", "fail", "--misconception"]),
                            ("confidence_update.py", ["compute", "0.5", "bogus"]),
                            ("confidence_update.py", [])], []),
    "confidence_apply": ([("confidence_update.py", ["apply", SUBJ, "pass_remediated", "7"])], [SUBJ]),
    "coverage_check": ([("coverage_check.py", ["{C}/mathA"]), ("coverage_check.py", ["{C}/nope"])], []),
    "diagnostic_gate": ([("diagnostic_gate.py", [SUBJ, "S1", "S1.1", "true", "false"]),
                         ("diagnostic_gate.py", [SUBJ, "S1", "S1.1", "false", "false"]),
                         ("diagnostic_gate.py", [SUBJ, "S1", "S1.1", "false", "true"])], []),
    "error_log_flow": ([("error_log.py", ["append", SUBJ, "S2", "S2.1", "practice", "misconception", "MC-1", "thinks x", "6"]),
                        ("error_log.py", ["append", SUBJ, "S2", "S2.1", "practice", "misconception", "NONE", "again", "7"]),
                        ("error_log.py", ["query", SUBJ]),
                        ("error_log.py", ["resolve", SUBJ, "S2.1", "8"]),
                        ("error_log.py", ["append", SUBJ, "S2", "S2.1", "bogus", "NONE", "x", "9"]),
                        ("error_log.py", [])], [SUBJ]),
    "gate_check_active": ([("gate_check.py", ["{C}/mathA/course.json", SUBJ, "{S}", "{C}", "2026-10-04"])], []),
    "gate_check_dormant": ([("gate_check.py", ["{C}/mathB/course.json", "{S}/mathB.json", "{S}", "{C}", "2026-10-04"])], []),
    "gate_check_new_enrol": ([("gate_check.py", ["{C}/solo/course.json", "NONE", "{S}", "{C}", "2026-10-04"])], []),
    "item_mastery_flow": ([("item_mastery.py", ["observe", SUBJ, "S1.1", "true", "5"]),
                           ("item_mastery.py", ["observe", SUBJ, "S1.1", "false", "6"]),
                           ("item_mastery.py", ["status", SUBJ]),
                           ("item_mastery.py", ["status", SUBJ, "S9.9"])], [SUBJ]),
    "migrate_course": ([("migrate_schema.py", ["course", "{C}/old/course.json"])], ["{C}/old/course.json"]),
    "migrate_subject": ([("migrate_schema.py", ["subject", SUBJ, "{C}/mathA/course.json"])], []),
    "postcompile_gate": ([("postcompile_gate.py", ["check", "{C}/mathA"]), ("postcompile_gate.py", ["check", "{C}/broken"])], []),
    "prereq_check": ([("prereq_check.py", ["{C}/mathA/course.json", "{S}", "{C}"])], []),
    "record_stage_result": ([("record_stage_result.py", ["apply", SUBJ, "{C}/mathA/course.json", "S2", "pass"]),
                             ("record_stage_result.py", ["apply", SUBJ, "{C}/mathA/course.json", "S3", "fail"])], [SUBJ]),
    "remediation_flow": ([("remediation_state.py", ["record", SUBJ, "S2", "misconception", "6"]),
                          ("remediation_state.py", ["record", SUBJ, "S2", "misconception", "7"]),
                          ("remediation_state.py", ["record", SUBJ, "S2", "slip", "8"]),
                          ("remediation_state.py", ["record", SUBJ, "S2", "slip", "9"]),
                          ("remediation_state.py", ["status", SUBJ, "S2"]),
                          ("remediation_state.py", ["reset", SUBJ, "S2"])], [SUBJ]),
    "resume_enrollment": ([("resume_enrollment.py", ["{S}/design.json", "{C}/design/course.json", "active", "2026-10-04"])], ["{S}/design.json"]),
    "review_compute": ([("review_math.py", ["1", "2.3", "0", "5", "true"]), ("review_math.py", ["4", "2.0", "1", "9", "false"])], []),
    "review_apply": ([("review_math.py", ["apply", DECK, "k1", "6", "true"]), ("review_math.py", ["apply", DECK, "nope", "6", "true"])], [DECK]),
    "roster_check": ([("roster_check.py", ["{P}", "{C}"]), ("roster_check.py", ["{P}", "{C}", "3"]),
                      ("roster_check.py", ["{P}", "{C}", "2", "--resume", "--course", "design"])], []),
    "slot_advance": ([("slot_advance.py", ["{P}/student_profile.json", "--min-gap-minutes", "0"]),
                      ("slot_advance.py", ["{P}/student_profile.json", "--min-gap-minutes", "99999"])], ["{P}/student_profile.json"]),
    "validate_structure": ([("validate_structure.py", ["{C}/mathA"]), ("validate_structure.py", ["{C}/broken"]),
                            ("validate_structure.py", ["{C}/nope"])], []),
    "erase_dry_run": ([("erase_profile.py", ["{R}", "amy", "--dry-run"])], []),
    "export_profile": ([("export_profile.py", ["{R}", "amy", "{T}/out.zip"])], []),
    "validate_schema": ([("validate_schema.py", ["subjects", SUBJ]), ("validate_schema.py", ["course", SUBJ]),
                         ("validate_schema.py", ["--kinds"]), ("validate_schema.py", ["nope", SUBJ])], []),
    "verify_session": ([("slot_advance.py", ["{P}/student_profile.json", "--min-gap-minutes", "0"]),
                        ("record_stage_result.py", ["apply", SUBJ, "{C}/mathA/course.json", "S2", "pass"]),
                        ("verify_session.py", ["{L}"]), ("verify_session.py", ["{L}", "--previous"]),
                        ("verify_session.py", ["{L}", "--slot", "999"])], []),
    "scan_untrusted": ([("scan_untrusted.py", ["{C}/mathA"]), ("scan_untrusted.py", ["{C}/nope"])], []),
    "review_select": ([("review_select.py", ["{L}", "{C}"]), ("review_select.py", ["{L}", "{C}", "--course", "mathA", "--limit", "1"])], []),
    "next_items": ([("next_items.py", ["{L}", "{C}", "mathA", "--count", "4"])], []),
    "readiness": ([("readiness.py", ["{L}", "{C}", "mathA"])], []),
    "plan_estimate": ([("plan_estimate.py", ["{L}", "{C}", "--today", "2026-10-04"])], []),
    "plan_target": ([("plan_target.py", ["set", SUBJ, "2026-12-01", "2026-10-04"]), ("plan_estimate.py", ["{L}", "{C}", "--today", "2026-10-04"]),
                     ("plan_target.py", ["clear", SUBJ]), ("plan_target.py", ["set", SUBJ, "2026-01-01", "2026-10-04"])], [SUBJ]),
    "assemble_paper": ([("assemble_paper.py", ["{C}", "mathA", "--marks", "12", "--seed", "2"]), ("assemble_paper.py", ["{C}", "solo"])], []),
    "record_mock": ([("record_mock.py", [SUBJ, "40", "30", "50", "2026-10-04", "S1-Q1"]), ("record_mock.py", [SUBJ, "10", "11", "5", "2026-10-04"])], [SUBJ]),
    "dashboard_html": ([("dashboard_html.py", ["{L}", "{C}", "{T}/exports/amy.html", "--today", "2026-10-04"])], []),
    "profile_set": ([("profile_set.py", ["{P}/student_profile.json", "preferences.style", "brief", "2026-10-04"]),
                     ("profile_set.py", ["{P}/student_profile.json", "preferences.tone", "loud", "2026-10-04"]),
                     ("profile_set.py", ["{P}/student_profile.json", "session_slot", "0", "2026-10-04"])], ["{P}/student_profile.json"]),
    "session_state": ([("session_state.py", ["phase", SUBJ, "test"]), ("session_state.py", ["phase", SUBJ, "exam"]),
                       ("session_state.py", ["roster", SUBJ, "test_pending_convergence"]), ("session_state.py", ["roster", SUBJ, "dormant"]),
                       ("session_state.py", ["notice", SUBJ, "n1", "2026-10-04"]), ("session_state.py", ["notice", SUBJ, "n1", "2026-10-04"]),
                       ("session_state.py", ["exam", SUBJ, "{C}/mathA/course.json", "available"])], [SUBJ]),
    "history_report": ([("item_mastery.py", ["observe", SUBJ, "S1.1", "true", "5"]), ("error_log.py", ["append", SUBJ, "S2", "S2.1", "practice", "slip", "NONE", "x", "6"]),
                        ("history_report.py", ["mastery", "{L}"]), ("history_report.py", ["errors", "{L}"]), ("history_report.py", ["ease", "{L}"]),
                        ("history_report.py", ["bogus", "{L}"])], []),
    "audit_status": ([("audit_status.py", ["{C}"]), ("audit_status.py", ["{T}/nope"])], []),
    "practice_pick": ([("practice_pick.py", ["next", SUBJ, "{C}/mathA/stages/S1/practice.md", "S1"]), ("practice_pick.py", ["used", SUBJ, "S1", "fixed", "1"]),
                       ("practice_pick.py", ["used", SUBJ, "S1", "fixed", "1"]), ("practice_pick.py", ["used", SUBJ, "S1", "generated"]),
                       ("practice_pick.py", ["next", SUBJ, "{C}/mathA/stages/S1/practice.md", "S1"]), ("practice_pick.py", ["used", SUBJ, "S1", "fixed", "0"])], [SUBJ]),
    "recent_activity": ([("recent_activity.py", ["{L}"]), ("record_stage_result.py", ["apply", SUBJ, "{C}/mathA/course.json", "S2", "pass"]),
                         ("recent_activity.py", ["{L}", "--last", "1"]), ("recent_activity.py", ["{L}", "--last", "0"])], []),
    "confirm_access": ([("confirm_access.py", ["{C}", "isolated", "2026-10-04"]), ("confirm_access.py", ["{C}", "shared", "2026-10-05"]), ("confirm_access.py", ["{C}", "maybe", "2026-10-05"]),
                         ("confirm_access.py", ["{T}/none", "isolated", "2026-10-05"])], ["{C}/access.json"]),
    "roster_apply": ([("roster_apply.py", ["lock", "{P}", "mathA"]), ("roster_apply.py", ["lock", "{P}", "design"]), ("roster_apply.py", ["advance", "{P}", "{C}"]),
                      ("roster_apply.py", ["drop", "{P}", "{C}", "solo"]), ("roster_apply.py", ["drop", "{P}", "{C}", "solo"]), ("roster_apply.py", ["drop", "{P}", "{C}", "ghost"])],
                     ["{S}/mathA.json", "{S}/solo.json", "{P}/student_profile.json"]),
    "enrol": ([("enrol.py", ["{P}", "{C}", "mathA", "active", "2026-10-05"]), ("enrol.py", ["{P}", "{C}", "ghost", "active", "2026-10-05"]), ("enrol.py", ["{P}", "{C}", "mathB", "maybe", "2026-10-05"]),
               ("enrol.py", ["{P}"])], []),
    "rubric_lint": ([("rubric_lint.py", ["{C}/mathA"]), ("rubric_lint.py", ["{C}/nope"])], []),
    "purge_history": ([("purge_history.py", ["{R}", "amy", "history"]), ("purge_history.py", ["{R}", "amy", "course", "mathA"]), ("purge_history.py", ["{R}", "amy", "course", "ghost"]),
                        ("purge_history.py", ["{R}", "amy", "history", "--confirm", "nope"]), ("purge_history.py", ["{R}", "amy"])], []),
    "status": ([("status.py", ["{L}", "{C}"])], []),
    "invariants": ([("invariants.py", ["{L}", "{C}"])], []),
    "resolve_root": ([("resolve_root.py", ["--root", "{T}"]), ("resolve_root.py", ["--root", "{T}/missing"])], []),
    "sqlite_check": ([("sqlite_store.py", ["check", "{L}"])], []),
    "sqlite_backfill": ([("sqlite_store.py", ["backfill", "{L}"])], []),
}

UPDATE = bool(os.environ.get("UPDATE_GOLDEN"))


class GoldenCLI(unittest.TestCase):
    pass


def _make(name, steps, files):
    def test(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = os.path.realpath(tmp)
            fx = gs.build_fixture(tmp)
            actual = {"steps": [{"cmd": [s] + a, **gs.run_step(s, a, fx, tmp)} for s, a in steps],
                      "files_after": gs.snapshot_files(files, fx, tmp)}
            actual = gs.normalise(actual, tmp)
        diff = gs.compare(name, actual, UPDATE)
        if diff:
            exp, act = diff
            self.fail("golden mismatch for %s:\n%s" % (name, "".join(
                list(difflib.unified_diff(exp.splitlines(True), act.splitlines(True), "golden", "actual"))[:60])))
    test.__name__ = f"test_{name}"
    return test


for _n, (_steps, _files) in CASES.items():
    setattr(GoldenCLI, f"test_{_n}", _make(_n, _steps, _files))


class GoldenCoverage(unittest.TestCase):
    def test_every_script_has_a_golden_case(self):
        scripts = sorted(f for f in os.listdir(gs.SCRIPTS) if f.endswith(".py"))
        covered = {s for steps, _ in CASES.values() for s, _a in steps}
        # bootstrap: covered by deploy tests; doctor: output embeds the interpreter version, covered by test_doctor_status
        # backup/restore: output embeds a wall-clock file name, covered by test_backup_restore; profile_init and deck_add read stdin (test_profile_set.Init, test_deck_add)
        exempt = {"bootstrap_scripts.py", "doctor.py", "backup_profile.py", "restore_profile.py", "profile_init.py", "deck_add.py", "worksheet_check.py"}
        self.assertEqual([s for s in scripts if s not in covered and s not in exempt], [])


if __name__ == "__main__":
    unittest.main()
