"""E-17: one definition of eligibility/suspension; no script re-derives it."""
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

import cohort_status  # noqa: E402


class Helpers(unittest.TestCase):
    def test_states(self):
        self.assertEqual(cohort_status.LIVE_STATES, ("active", "test_pending_convergence"))
        self.assertEqual(cohort_status.SLOT_STATES, ("active", "test_pending_convergence", "dormant"))

    def test_is_suspended(self):
        self.assertTrue(cohort_status.is_suspended("suspended_ungrounded"))
        for v in ("verified", None, "", "SUSPENDED_UNGROUNDED"):
            self.assertFalse(cohort_status.is_suspended(v))


class NoRederivation(unittest.TestCase):
    def test_literals_live_only_in_cohort_status(self):
        offenders = []
        for fn in sorted(os.listdir(SCRIPTS)):
            if not fn.endswith(".py") or fn == "cohort_status.py":
                continue
            with open(os.path.join(SCRIPTS, fn), encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    code = line.split("#", 1)[0]
                    # prose in docstrings is fine; flag only comparisons / tuples of state literals in code
                    if re.search(r'(==|!=|in|not in)\s*[\(\[]?[^\n]*"(suspended_ungrounded|test_pending_convergence)"', code) \
                            and not code.lstrip().startswith(('"', "'")):
                        offenders.append(f"{fn}:{i}: {line.strip()}")
        self.assertEqual(offenders, [])


if __name__ == "__main__":
    unittest.main()
