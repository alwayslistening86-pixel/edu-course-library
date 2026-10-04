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
        exempt = {"bootstrap_scripts.py"}  # covered by test_scripts/test_toolkit with temp deploys
        self.assertEqual([s for s in scripts if s not in covered and s not in exempt], [])


if __name__ == "__main__":
    unittest.main()
