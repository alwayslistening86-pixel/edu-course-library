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

Usage (pure calculation, unchanged, still never touches a file):
    python3 review_math.py <old_interval_sessions> <old_ease> <old_lapses> \
        <current_slot> <correct: true|false>

Usage (read-modify-write, added in v1.10.0 — closes the write-back trust
gap named directly by the library owner: previously this script computed
new card fields and *trusted* the calling skill's prose instruction to
write them back onto the card, with no code ever checking that happened):
    python3 review_math.py apply <deck.json> <card_id> <current_slot> <correct: true|false>

`apply` loads the `*_review_deck.json` file, finds the card by `id` in its
`cards` list, calls the same `compute()` below using that card's current
interval_sessions/ease/lapses, writes the four returned fields back onto
the card object in place, saves the file, logs the pass and the card's new
state to sqlite_store's review_log/review_cards tables, and returns the
same shape as `compute()` plus `"written": true`. `review-scheduler.md`
calls `apply`, not "write its output straight back onto the card," from
this version on. The positional-args `compute`/`main()` form stays exactly
as it was, for testing and for any caller that genuinely wants the
arithmetic only.

Output: JSON to stdout with the new card fields.
"""
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sqlite_store  # noqa: E402
from tutorlib import atomic_io, cli, consent, filelock, ledger, state


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


def _load(path):
    return state.load(path, "review_deck")


def _save(path, data):
    atomic_io.write_json(path, data)


@ledger.logged("review_math.py", "deck_path")
@filelock.locked("deck_path")
def apply(deck_path, card_id, current_slot, correct):
    """Read-modify-write: loads the deck, finds the card, computes the new
    fields with compute(), writes them back onto the card, saves the file,
    and logs both the pass and the card's new state to sqlite_store. This
    is the script actually owning the write — see the module docstring."""
    d = _load(deck_path)
    cards = d.get("cards", [])
    card = next((c for c in cards if isinstance(c, dict) and c.get("id") == card_id), None)
    if card is None:
        return {"error": f"card_id {card_id!r} not found in {deck_path}"}

    old_interval = card.get("interval_sessions", 1)
    old_ease = card.get("ease", EASE_DEFAULT)
    old_lapses = card.get("lapses", 0)

    result = compute(old_interval, old_ease, old_lapses, current_slot, correct)

    card["interval_sessions"] = result["interval_sessions"]
    card["ease"] = result["ease"]
    card["lapses"] = result["lapses"]
    card["due_at_slot"] = result["due_at_slot"]
    allowed, cstatus = consent.check(deck_path, consent.SCHEDULING)
    if not allowed:
        result.update(consent.skipped(cstatus, consent.SCHEDULING))
        result["card_id"] = card_id
        return result
    _save(deck_path, d)

    log_result = sqlite_store.log_review_pass(
        deck_path, card_id, correct, int(old_interval), result["interval_sessions"],
        float(old_ease), result["ease"], current_slot,
    )
    upsert_result = sqlite_store.upsert_review_card(deck_path, card)

    result["card_id"] = card_id
    result["written"] = True
    result["sqlite"] = {"log_review_pass": log_result, "upsert_review_card": upsert_result}
    return result


def main():
    args = sys.argv[1:]
    if args and args[0] == "apply":
        if len(args) != 5:
            print(json.dumps({"error": "usage: review_math.py apply <deck.json> <card_id> <current_slot> <correct:true|false>"}))
            sys.exit(2)
        deck_path, card_id, current_slot, correct_s = args[1:5]
        correct = correct_s.strip().lower() == "true"
        try:
            result = apply(deck_path, card_id, current_slot, correct)
        except cli.EXPECTED_ERRORS as e:
            print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
            sys.exit(1)
        sys.exit(cli.emit(result))
        return

    if len(args) != 5:
        print(json.dumps({"error": "usage: review_math.py <old_interval> <old_ease> <old_lapses> <current_slot> <correct:true|false> | apply <deck.json> <card_id> <current_slot> <correct:true|false>"}))
        sys.exit(2)
    old_interval, old_ease, old_lapses, current_slot, correct_s = args
    correct = correct_s.strip().lower() == "true"
    result = compute(old_interval, old_ease, old_lapses, current_slot, correct)
    sys.exit(cli.emit(result))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
