#!/usr/bin/env python3
"""
review_math.py — deterministic SM-2-lite spaced-repetition scheduling for
review-scheduler.md.

review-scheduler.md's own rule, made concrete:
  - New card: interval_sessions = 1.
  - Correct recall: interval_sessions grows "roughly x1.5-2, adjusted by
    ease"; due_at_slot moves forward by that many session-slots from now.
  - Incorrect recall: interval_sessions resets to 1, lapses increments,
    ease nudges down slightly, floored so a card can never spiral into
    effectively-never-reviewed.

Concrete formula (this is the one place the prose left "roughly" undefined -
made explicit and stable here rather than re-approximated by the model on
every review pass, which is exactly the kind of small compounding drift
methodology.md's Computation check exists to prevent):
  - ease starts at 2.3 (per review-scheduler.md's own example card).
  - On correct: growth = 1.7 * (ease / 2.3), clamped to [1.3, 2.5] — 1.7 is
    the midpoint of "roughly x1.5-2", scaled by how far this card's ease has
    drifted from the default. new_interval = max(old_interval + 1,
    floor(old_interval * growth + 0.5)). The old_interval + 1 floor is what
    guarantees a correct recall always moves the card forward: without it, a
    card whose ease had dropped to ~2.0 or below (two lapses from default) had
    growth < 1.5, so round(1 * growth) == 1 and it stayed at interval 1
    forever. Rounding is half-up, not Python's banker's round(). The result is
    capped at MAX_INTERVAL_SESSIONS so a well-known card is still revisited
    within a term rather than drifting out to a year (at the cap it stays put).
    Ease also recovers by EASE_RECOVERY on each correct recall (capped at
    EASE_CEIL), so a lapse is a setback rather than a permanent penalty.
  - On incorrect: new_interval = 1, lapses += 1, ease = max(1.3, ease - 0.2).
  - due_at_slot = current_slot + new_interval, always.

This script never decides whether an answer was correct — that's a real
grading judgment (free-text recall vs. a card's back), left entirely to the
model per review-scheduler.md. It only takes the correct/incorrect verdict
already reached and applies the arithmetic that follows from it.

Usage:
    python3 review_math.py <old_interval_sessions> <old_ease> <old_lapses> \
        <current_slot> <correct: true|false>

Output: JSON to stdout with the new card fields.
"""
import json
import math
import sys


EASE_DEFAULT = 2.3
EASE_FLOOR = 1.3
EASE_CEIL = 2.5
EASE_RECOVERY = 0.05
MAX_INTERVAL_SESSIONS = 30  # cap: ~15 weeks at 2 sessions/week; adjust here, nowhere else
GROWTH_MID = 1.7
GROWTH_FLOOR = 1.3
GROWTH_CEIL = 2.5


def compute(old_interval, old_ease, old_lapses, current_slot, correct):
    old_interval = int(old_interval)
    old_ease = float(old_ease)
    old_lapses = int(old_lapses)
    current_slot = int(current_slot)

    if correct:
        growth = GROWTH_MID * (old_ease / EASE_DEFAULT)
        growth = max(GROWTH_FLOOR, min(GROWTH_CEIL, growth))
        new_interval = min(MAX_INTERVAL_SESSIONS, max(old_interval + 1, math.floor(old_interval * growth + 0.5)))
        new_ease = old_ease + EASE_RECOVERY
        new_lapses = old_lapses
    else:
        new_interval = 1
        new_ease = max(EASE_FLOOR, old_ease - 0.2)
        new_lapses = old_lapses + 1

    new_ease = max(EASE_FLOOR, min(EASE_CEIL, new_ease))
    due_at_slot = current_slot + new_interval

    return {
        "interval_sessions": new_interval,
        "ease": round(new_ease, 3),
        "lapses": new_lapses,
        "due_at_slot": due_at_slot,
    }


def main():
    if len(sys.argv) != 6:
        print(json.dumps({"error": "usage: review_math.py <old_interval> <old_ease> <old_lapses> <current_slot> <correct:true|false>"}))
        sys.exit(2)
    old_interval, old_ease, old_lapses, current_slot, correct_s = sys.argv[1:6]
    correct = correct_s.strip().lower() == "true"
    result = compute(old_interval, old_ease, old_lapses, current_slot, correct)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
