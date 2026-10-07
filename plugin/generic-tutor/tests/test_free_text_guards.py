"""ADR 0012 build tasks B-04.5h and B-04.5i: free text is capped and screened for contact details; remediation causes are the five. Stdlib only."""
import json
import os
import shutil
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

import error_log  # noqa: E402
import remediation_state  # noqa: E402
import session_state  # noqa: E402
from golden_support import build_fixture  # noqa: E402
from tutorlib import contact  # noqa: E402


class ContactDetails(unittest.TestCase):
    def test_finds_the_obvious_forms(self):
        cases = {
            "mail me at maya.patel@example.com": ["email address"],
            "see https://example.com/page": ["web address"],
            "www.example.org is the site": ["web address"],
            "call 07700 900123 after school": ["phone number"],
            "her number is +44 7700 900 123": ["phone number"],
            "0161-496-0000": ["phone number"],
        }
        for text, want in cases.items():
            self.assertEqual(contact.contact_details(text), want, text)

    def test_ordinary_maths_is_left_alone(self):
        for text in ("added 3/4 + 1/2 as 4/6", "wrote 0.75 as 75 percent of 100", "thought 12 x 12 = 124, carried the wrong digit",
                     "used 1234567 instead of 123456", "a date 2026-10-07", "x = 0.000001"):
            self.assertEqual(contact.contact_details(text), [], text)


class Notes(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.fx = build_fixture(self.tmp)
        self.subj = os.path.join(self.fx["S"], "mathA.json")

    def raw(self):
        with open(self.subj, "rb") as f:
            return f.read()

    def append(self, note):
        return error_log.append(self.subj, "S1", "S1.1", "practice", "slip", "NONE", note, 5)

    def test_error_note_is_capped_and_screened_and_refusals_write_nothing(self):
        before = self.raw()
        too_long = self.append("x" * (error_log.NOTE_MAX + 1))
        self.assertIn("keep it to", too_long["error"])
        phone = self.append("said call me on 07700 900123")
        self.assertIn("phone number", phone["error"])
        self.assertNotIn("07700", json.dumps(phone))
        self.assertEqual(self.raw(), before)

    def test_error_note_at_the_limit_and_ordinary_text_are_stored(self):
        ok = self.append("a" * error_log.NOTE_MAX)
        self.assertNotIn("error", ok)
        ok = self.append("added the denominators instead of finding a common one")
        self.assertNotIn("error", ok)

    def test_session_summary_is_screened(self):
        before = self.raw()
        r = session_state.write_note(self.subj, "2026-10-07", "Covered fractions; email is a@b.com")
        self.assertIn("email address", r["error"])
        self.assertEqual(self.raw(), before)
        self.assertNotIn("error", session_state.write_note(self.subj, "2026-10-07", "Covered adding fractions."))


class RemediationCause(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.subj = os.path.join(build_fixture(self.tmp)["S"], "mathA.json")

    def test_only_the_five_causes(self):
        with open(self.subj, "rb") as f:
            before = f.read()
        for bad in ("careless", "Slip", "", "other"):
            r = remediation_state.record(self.subj, "S2", bad, 3)
            self.assertIn("cause must be one of", r["error"], bad)
        with open(self.subj, "rb") as f:
            self.assertEqual(f.read(), before)
        for good in error_log.CAUSES:
            self.assertNotIn("error", remediation_state.record(self.subj, "S3", good, 4))
            remediation_state.reset(self.subj, "S3")


if __name__ == "__main__":
    unittest.main()
