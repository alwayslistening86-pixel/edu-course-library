"""ADR 0012 build task B-04.5j (scenario S12): every script that writes consults the learner's consent, or says why it need not.

A static check, not a proof: it finds scripts whose source writes state (a JSON save, a history insert, a delete, a zip, a copy)
and requires either a call into `consent.` or an entry in EXEMPT with the reason. A new writer without either fails the build, so
a script cannot quietly persist data against a learner's choice, and an exemption cannot be added without a sentence of why.
Stdlib only.
"""
import os
import re
import unittest

SCRIPTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts")

WRITE_MARKERS = ("state.save(", "atomic_io.write_json(", "ledger.logged", "sqlite_store.log_", "sqlite_store.upsert_", "os.remove(",
                 "os.replace(", "shutil.rmtree", "shutil.copy", "zipfile.ZipFile(", "os.makedirs(")
WRITE_MODE = re.compile(r"open\([^)]*['\"][wa]b?['\"]")

# Scripts that write but do not consult consent, each with the reason. Keep this list short and honest.
EXEMPT = {
    "audit_run.py": "staff report written to a path the caller names; reads learner folders, writes no learner state",
    "backup_profile.py": "the learner's own right to a copy of their data (/backup); a zip outside the learner folder",
    "bootstrap_scripts.py": "deploys the engine's own scripts; touches no learner data",
    "confirm_access.py": "records the folder-access confirmation (access.json), not learner progress",
    "course_bundle.py": "moves course content; refuses learner-data file names by design",
    "erase_profile.py": "the learner's right to erasure; deletes, never records",
    "exam_to_bank.py": "course content authoring (staff); no learner data",
    "misconception_ids.py": "course content authoring (staff): adds ids to a course's misconceptions.json; no learner data",
    "export_profile.py": "the learner's own right to their data (/export); writes a zip outside the folder",
    "migrate_schema.py": "rewrites existing files to a newer shape after a backup; adds no new learner data",
    "publish_course.py": "course publishing (staff); no learner data",
    "purge_history.py": "the learner's right to delete selected history; deletes, never records",
    "record_grading.py": "writes only through sqlite_store.log_grading, whose _safe wrapper enforces SIGNAL consent (checked below)",
    "restore_profile.py": "the learner's own backup being put back (/restore); an explicit act",
    "verify_sources.py": "course source snapshots (staff); no learner data",
}


def writers():
    out = {}
    for name in sorted(os.listdir(SCRIPTS)):
        if not name.endswith(".py"):
            continue
        with open(os.path.join(SCRIPTS, name), encoding="utf-8") as f:
            src = f.read()
        if any(m in src for m in WRITE_MARKERS) or WRITE_MODE.search(src):
            out[name] = src
    return out


class ConsentCoverage(unittest.TestCase):
    def test_every_writer_consults_consent_or_is_exempt_with_a_reason(self):
        missing = [n for n, src in writers().items() if "consent." not in src and n not in EXEMPT]
        self.assertEqual(missing, [], "these scripts write but neither call consent nor appear in EXEMPT with a reason: " + ", ".join(missing))

    def test_exemptions_are_not_stale(self):
        w = writers()
        for name in EXEMPT:
            self.assertIn(name, w, f"{name} is exempt but no longer writes; remove it from EXEMPT")
            self.assertNotIn("consent.", w[name], f"{name} now consults consent; remove it from EXEMPT")
            self.assertGreater(len(EXEMPT[name]), 25, f"{name}: say why in a sentence")

    def test_the_history_database_wrapper_really_enforces_consent(self):
        with open(os.path.join(SCRIPTS, "sqlite_store.py"), encoding="utf-8") as f:
            src = f.read()
        body = src[src.index("def _safe("):]
        body = body[:body.index("\ndef ", 10)] if "\ndef " in body[10:] else body
        self.assertIn("consent.check(", body)
        self.assertIn("log_grading", src)
        i = src.index("def log_grading")
        self.assertIn("@_safe", src[max(0, i - 80):i], "log_grading must stay behind the consent wrapper")


if __name__ == "__main__":
    unittest.main()
