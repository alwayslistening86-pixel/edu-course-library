"""
Fixed-seed subset of the composition fuzz (fuzz_lifecycle.py) so `unittest discover tests` covers
add / drop / resume / finish chained the way the skill prose prescribes. The full run is
`python3 tests/fuzz_lifecycle.py [sequences] [steps]` (3,000 x 25 is the reference run).
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fuzz_lifecycle  # noqa: E402


class CompositionFuzzTests(unittest.TestCase):
    SEQUENCES = 150
    STEPS = 25

    def _violations(self):
        found = []
        for seed in range(self.SEQUENCES):
            trace, errs = fuzz_lifecycle.run(seed, self.STEPS)
            if errs:
                found.append((seed, trace, errs))
        return found

    def test_no_invariant_violations_across_random_lifecycles(self):
        found = self._violations()
        self.assertEqual(found, [], f"first failing sequence (seed {found[0][0]}): {found[0][1]} -> {found[0][2]}" if found else "")

    def test_fuzz_detects_a_drop_that_does_not_wake(self):
        """Sensitivity: the harness must FAIL if /drop skips the wake step, or it proves nothing."""
        os.environ["NO_WAKE_ON_DROP"] = "1"
        try:
            self.assertTrue(self._violations(), "fuzz found nothing with the wake step removed")
        finally:
            del os.environ["NO_WAKE_ON_DROP"]


if __name__ == "__main__":
    unittest.main()
