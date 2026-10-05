"""E-21: properties of the learning maths over seeded random inputs (stdlib only; same seeds every run)."""
import os
import random
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

import confidence_update as cu  # noqa: E402
import item_mastery as im  # noqa: E402
import review_math as rm  # noqa: E402

N = 2000


class ReviewProperties(unittest.TestCase):
    def cases(self):
        rng = random.Random(21)
        for _ in range(N):
            yield rng.randint(1, rm.MAX_INTERVAL_SESSIONS), rng.uniform(rm.EASE_FLOOR, rm.EASE_CEIL), rng.randint(0, 9), rng.randint(0, 500)

    def test_bounds_and_due_slot(self):
        for interval, ease, lapses, slot in self.cases():
            for correct in (True, False):
                r = rm.compute(interval, ease, lapses, slot, correct)
                self.assertTrue(1 <= r["interval_sessions"] <= rm.MAX_INTERVAL_SESSIONS, (interval, ease, correct, r))
                self.assertTrue(rm.EASE_FLOOR <= r["ease"] <= rm.EASE_CEIL, r)
                self.assertEqual(r["due_at_slot"], slot + r["interval_sessions"])

    def test_correct_never_shrinks_wrong_resets(self):
        for interval, ease, lapses, slot in self.cases():
            ok = rm.compute(interval, ease, lapses, slot, True)
            self.assertGreaterEqual(ok["interval_sessions"], interval)
            self.assertEqual(ok["lapses"], lapses)
            bad = rm.compute(interval, ease, lapses, slot, False)
            self.assertEqual((bad["interval_sessions"], bad["lapses"]), (1, lapses + 1))
            self.assertLessEqual(bad["ease"], round(ease, 3) + 1e-9)

    def test_higher_ease_never_gives_a_shorter_interval(self):
        rng = random.Random(22)
        for _ in range(N):
            interval = rng.randint(1, rm.MAX_INTERVAL_SESSIONS)
            lo, hi = sorted((rng.uniform(rm.EASE_FLOOR, rm.EASE_CEIL), rng.uniform(rm.EASE_FLOOR, rm.EASE_CEIL)))
            self.assertLessEqual(rm.compute(interval, lo, 0, 0, True)["interval_sessions"], rm.compute(interval, hi, 0, 0, True)["interval_sessions"])

    def test_a_streak_of_correct_answers_reaches_the_cap_and_stays(self):
        interval, ease = 1, rm.EASE_DEFAULT
        for _ in range(60):
            r = rm.compute(interval, ease, 0, 0, True)
            interval, ease = r["interval_sessions"], r["ease"]
        self.assertEqual(interval, rm.MAX_INTERVAL_SESSIONS)


class MasteryProperties(unittest.TestCase):
    def test_bounds_and_direction(self):
        rng = random.Random(23)
        for _ in range(N):
            p = rng.random()
            for correct in (True, False):
                new_p, posterior = im._update(p, correct)
                self.assertTrue(0.0 <= new_p <= 1.0 and 0.0 <= posterior <= 1.0, (p, correct))
            up, up_post = im._update(p, True)
            down, down_post = im._update(p, False)
            self.assertGreaterEqual(up_post, p - 1e-12)          # a correct answer is evidence for mastery
            self.assertLessEqual(down_post, p + 1e-12)
            self.assertGreaterEqual(up, down)

    def test_extremes_do_not_divide_by_zero(self):
        for p in (0.0, 1.0):
            for correct in (True, False):
                new_p, _ = im._update(p, correct)
                self.assertTrue(0.0 <= new_p <= 1.0)

    def test_repeated_correct_is_monotone_and_converges_high(self):
        p = im.P_INIT
        for _ in range(30):
            new_p, _ = im._update(p, True)
            self.assertGreaterEqual(new_p, p - 1e-12)
            p = new_p
        self.assertGreater(p, 0.95)


class ConfidenceProperties(unittest.TestCase):
    def test_bounds_and_direction(self):
        rng = random.Random(24)
        for _ in range(N):
            c = rng.random()
            for event in cu.BASE_DELTA:
                for mis in (False, True):
                    r = cu.compute(c, event, mis)
                    self.assertTrue(0.0 <= r["new_confidence"] <= 1.0, r)
            self.assertGreaterEqual(cu.compute(c, "pass_clean")["new_confidence"], round(c, 4) - 1e-9)
            self.assertLessEqual(cu.compute(c, "fail")["new_confidence"], round(c, 4) + 1e-9)
            self.assertGreaterEqual(cu.compute(c, "pass_clean")["new_confidence"], cu.compute(c, "pass_remediated")["new_confidence"])
            self.assertLessEqual(cu.compute(c, "pass_clean", True)["new_confidence"], cu.compute(c, "pass_clean")["new_confidence"])

    def test_out_of_range_input_is_clamped(self):
        for c in (-5, 7, float("1e9")):
            self.assertTrue(0.0 <= cu.compute(c, "fail")["new_confidence"] <= 1.0)


if __name__ == "__main__":
    unittest.main()
