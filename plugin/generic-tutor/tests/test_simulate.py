"""A-05: simulated learners. Checks the selection rule against simple alternatives, and that the simulator uses the engine's own ranking."""
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import next_items  # noqa: E402
from evals import simulate  # noqa: E402


class Simulation(unittest.TestCase):
    def test_deterministic_for_a_seed(self):
        self.assertEqual(simulate.simulate("weakest_first", 3), simulate.simulate("weakest_first", 3))

    def test_weakest_first_beats_random_and_round_robin_at_two_budgets(self):
        for steps in (40, 100):
            r = simulate.compare(seeds=150, steps=steps)
            for other in ("random", "round_robin"):
                self.assertGreater(r["weakest_first"]["known_fraction"], r[other]["known_fraction"] + 0.02, (steps, other))
                self.assertGreater(r["weakest_first"]["focus"], r[other]["focus"] + 0.05, (steps, other))

    def test_the_estimate_is_better_than_knowing_nothing(self):
        for pol in simulate.POLICIES:
            self.assertLess(simulate.compare(seeds=100, steps=100)[pol]["estimate_error"], 0.5, pol)

    def test_the_policy_ranks_with_the_engines_own_weakness(self):
        est, observed = [0.9, 0.2, 0.5, 0.2], [True, True, True, False]
        self.assertEqual(simulate.pick("weakest_first", None, est, observed, 0), 3)                     # unseen bonus breaks the tie with item 1
        self.assertEqual(next_items.weakness(0.2, False), next_items.weakness(0.2, True) + next_items.UNSEEN_BONUS)
        self.assertGreater(next_items.weakness(0.5, True, 2), next_items.weakness(0.5, True, 0))


if __name__ == "__main__":
    unittest.main()
