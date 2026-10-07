"""
Simulated learners (A-05): does the practice-selection rule beat the obvious alternatives, and does the mastery estimate follow the truth?

No model is involved. A simulated learner has a hidden true state per syllabus item (known / not known). Each practice step the policy picks one
item; the learner answers correctly with probability 1 - slip if the item is known and `guess` if not; after each opportunity an unknown item becomes
known with probability `learn`. The estimate the engine keeps is the real BKT update (`item_mastery._update`), and the "weakest first" policy uses the
same weakness formula as `next_items.choose` (a test keeps the two in step).

What this can and cannot tell you. It checks that the selection and the estimate behave as designed when learners behave like the model says. It says
nothing about whether real people learn this way: every effect size here is an assumption of the simulator. Use it to catch a rule that is worse than
random or an estimate that drifts, not to claim learning gains.

Policies: weakest_first (the engine's rule), random, round_robin (items in order, ignoring evidence).
Metrics, averaged over seeds: known_fraction at the end, focus (share of practice steps spent on items that were not yet known), and estimate_error
(mean |p_mastery - truth| at the end; 0.5 everywhere would score 0.5).
"""
import random

import item_mastery
import next_items

POLICIES = ("weakest_first", "random", "round_robin")


def pick(policy, rng, est, observed, step):
    n = len(est)
    if policy == "random":
        return rng.randrange(n)
    if policy == "round_robin":
        return step % n
    return min(range(n), key=lambda i: (-next_items.weakness(est[i], observed[i]), i))


def simulate(policy, seed, items=20, steps=40, known0=0.3, learn=0.15, slip=0.1, guess=0.2):
    rng = random.Random(seed)
    known = [rng.random() < known0 for _ in range(items)]
    est = [item_mastery.P_INIT] * items
    observed = [False] * items
    on_unknown = 0
    for step in range(steps):
        i = pick(policy, rng, est, observed, step)
        on_unknown += not known[i]
        correct = rng.random() < ((1 - slip) if known[i] else guess)
        est[i] = item_mastery._update(est[i], correct)[0]
        observed[i] = True
        if not known[i] and rng.random() < learn:
            known[i] = True
    return {"known_fraction": sum(known) / items, "focus": on_unknown / steps,
            "estimate_error": sum(abs(e - (1.0 if k else 0.0)) for e, k in zip(est, known, strict=True)) / items}


def compare(seeds=300, **kw):
    out = {}
    for pol in POLICIES:
        runs = [simulate(pol, s, **kw) for s in range(seeds)]
        out[pol] = {k: round(sum(r[k] for r in runs) / seeds, 4) for k in runs[0]}
    return out


if __name__ == "__main__":
    import json
    print(json.dumps(compare(), indent=2))
