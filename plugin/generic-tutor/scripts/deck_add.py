#!/usr/bin/env python3
"""
deck_add.py -- the one place new review cards enter a deck (K-22, K-23, K-25).

    python3 deck_add.py <deck.json> <course_id> <stage_id> [--max-per-stage N] <<'EOF'
    [{"front": "...", "back": "...", "item_id": "S1.1", "criterion": "M1"}, ...]
    EOF

Until now stage-recap appended cards to the deck by hand-editing JSON, so card quality, duplicates and deck size were
unchecked. Cards come on stdin (course text never goes on a command line). Each is checked; a card that fails is
rejected with its reason and the rest are still added:
  fields    front and back are non-empty strings; item_id / criterion optional (null when not derivable)
  length    front <= 200 characters, back <= 400
  one ask   a front holds one question (at most one "?"), and is not a bare list of answers ("a) ... b) ...")
  dedupe    a front already in the deck for this course (ignoring case, spacing and punctuation) is skipped
  caps      at most --max-per-stage new cards per call (default 12); at most 300 cards in a deck
New cards get interval 1, ease 2.3, lapses 0, due at the learner's session_slot + 1, and the id `<stage>-c<N>` (next free N).
The deck is created in the standard shape if missing. Consent: scheduling class (limited keeps it; revoked writes nothing).
Atomic, locked and ledgered like every other state writer.
"""
import json
import os
import re
import sys

from tutorlib import atomic_io, cli, consent, filelock, ledger, state
import sqlite_store

MAX_FRONT = 200
MAX_BACK = 400
DEFAULT_MAX_PER_STAGE = 12
MAX_DECK = 300
EASE_DEFAULT = 2.3


def _norm(text):
    return re.sub(r"[^a-z0-9]+", " ", str(text).lower()).strip()


def check_card(card):
    """Return None if the card is acceptable, else the reason it is not."""
    if not isinstance(card, dict):
        return "not an object"
    for key in ("front", "back"):
        if not isinstance(card.get(key), str) or not card[key].strip():
            return f"{key} must be a non-empty string"
    for key in ("item_id", "criterion"):
        if card.get(key) is not None and not isinstance(card[key], str):
            return f"{key} must be a string or null"
    if len(card["front"]) > MAX_FRONT:
        return f"front is {len(card['front'])} characters (max {MAX_FRONT})"
    if len(card["back"]) > MAX_BACK:
        return f"back is {len(card['back'])} characters (max {MAX_BACK})"
    if card["front"].count("?") > 1:
        return "front asks more than one question"
    if re.search(r"(^|\s)\(?a[).]\s.*\(?b[).]\s", card["front"], re.I | re.S):
        return "front is a multi-part list; split it into separate cards"
    return None


def _slot(deck_path):
    pp = consent.profile_path_for(deck_path)
    try:
        with open(pp, encoding="utf-8") as f:
            return int(json.load(f).get("session_slot", 0))
    except (OSError, ValueError, TypeError):
        return 0


@ledger.logged("deck_add.py", "deck_path")
@filelock.locked("deck_path")
def add(deck_path, course_id, stage_id, cards, max_per_stage=DEFAULT_MAX_PER_STAGE):
    if not isinstance(cards, list):
        return {"error": "stdin must be a JSON list of cards"}
    allowed, cstatus = consent.check(deck_path, consent.SCHEDULING)
    if not allowed:
        return {"action": "not_persisted", **consent.skipped(cstatus, consent.SCHEDULING)}

    if os.path.isfile(deck_path):
        deck = state.load(deck_path, "review_deck")
    else:
        deck = {"schema_version": 1, "course_id": course_id, "cards": []}
    existing = deck.setdefault("cards", [])
    seen = {_norm(c.get("front", "")) for c in existing if isinstance(c, dict)}
    taken = {c.get("id") for c in existing if isinstance(c, dict)}
    slot = _slot(deck_path)

    added, rejected = [], []
    n = 0
    for card in cards:
        reason = check_card(card)
        if reason is None and _norm(card["front"]) in seen:
            reason = "duplicate of a card already in the deck"
        if reason is None and len(added) >= max_per_stage:
            reason = f"over the per-call cap of {max_per_stage}"
        if reason is None and len(existing) + len(added) >= MAX_DECK:
            reason = f"deck is full ({MAX_DECK} cards); retire cards first"
        if reason is not None:
            rejected.append({"front": str(card.get("front", ""))[:60] if isinstance(card, dict) else None, "reason": reason})
            continue
        n += 1
        while f"{stage_id}-c{n}" in taken:
            n += 1
        new = {"id": f"{stage_id}-c{n}", "stage_id": stage_id, "item_id": card.get("item_id"), "criterion": card.get("criterion"),
               "front": card["front"].strip(), "back": card["back"].strip(), "interval_sessions": 1, "ease": EASE_DEFAULT,
               "lapses": 0, "due_at_slot": slot + 1}
        taken.add(new["id"])
        seen.add(_norm(new["front"]))
        added.append(new)

    result = {"added": [c["id"] for c in added], "rejected": rejected, "deck_size": len(existing) + len(added)}
    if added:
        existing.extend(added)
        atomic_io.write_json(deck_path, deck)
        result["written"] = True
        for c in added:
            sqlite_store.upsert_review_card(deck_path, c)
    else:
        result["written"] = False
    return result


def main():
    args = sys.argv[1:]
    cap = DEFAULT_MAX_PER_STAGE
    if "--max-per-stage" in args:
        i = args.index("--max-per-stage")
        try:
            cap = int(args[i + 1])
        except (IndexError, ValueError):
            print(json.dumps({"error": "--max-per-stage needs an integer"}))
            sys.exit(2)
        del args[i:i + 2]
    if len(args) != 3:
        print(json.dumps({"error": "usage: deck_add.py <deck.json> <course_id> <stage_id> [--max-per-stage N]  (cards as a JSON list on stdin)"}))
        sys.exit(2)
    try:
        cards = json.load(sys.stdin)
    except ValueError as e:
        print(json.dumps({"error": f"stdin is not valid JSON: {e}"}))
        sys.exit(1)
    try:
        out = add(args[0], args[1], args[2], cards, cap)
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        sys.exit(1)
    sys.exit(cli.emit(out))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
