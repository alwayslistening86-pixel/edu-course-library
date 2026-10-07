#!/usr/bin/env python3
"""
deck_add.py -- the one place new review cards enter a deck (K-22, K-23, K-25).

    python3 deck_add.py <deck.json> <course_id> <stage_id> [--max-per-stage N] <<'EOF'
    [{"front": "...", "back": "...", "item_id": "S1.1", "criterion": "M1", "card_type": "cloze"}, ...]
    EOF
    python3 deck_add.py retire <deck.json> <card_id> [<card_id> ...]
    python3 deck_add.py mature <deck.json>

Until now stage-recap appended cards to the deck by hand-editing JSON, so card quality, duplicates and deck size were
unchecked. Cards come on stdin (course text never goes on a command line). Each is checked; a card that fails is
rejected with its reason and the rest are still added:
  fields    front and back are non-empty strings; item_id / criterion optional (null when not derivable)
  length    front <= 200 characters, back <= 400
  one ask   a front holds one question (at most one "?"), and is not a bare list of answers ("a) ... b) ...")
  dedupe    a front already in the deck for this course (ignoring case, spacing and punctuation) is skipped
  type      optional card_type: basic (default), cloze ({{c1::..}} in the front), explain_why (front asks why/how), worked_step
            (front shows the steps so far and asks for the next); a card that does not fit its declared type is rejected
  caps      at most --max-per-stage new cards per call (default 12); at most 300 cards in a deck
New cards get interval 1, ease 2.3, lapses 0, due at the learner's session_slot + 1, and the id `<stage>-c<N>` (next free N).
The deck is created in the standard shape if missing. Consent: scheduling class (limited keeps it; revoked writes nothing).
Atomic, locked and ledgered like every other state writer.

retire  removes the named cards from the deck (the learner asked to stop seeing them, or the deck is full); unknown ids are reported, nothing else
        changes. The history database keeps its record of them. Never deletes the deck file.
mature  read-only: cards the learner has known for a long time (interval at least MATURE_INTERVAL sessions, no lapses), the natural ones to retire.
"""
import json
import os
import re
import sys

from tutorlib import cards as cardtypes, cli, consent, filelock, ledger, state
import sqlite_store

MAX_FRONT = 200
MAX_BACK = 400
DEFAULT_MAX_PER_STAGE = 12
MAX_DECK = 300
EASE_DEFAULT = 2.3
MATURE_INTERVAL = 20


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
    bad_type = cardtypes.check_type(card)
    if bad_type:
        return bad_type
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
        if cardtypes.type_of(card) != "basic":
            new["card_type"] = card["card_type"]
        taken.add(new["id"])
        seen.add(_norm(new["front"]))
        added.append(new)

    result = {"added": [c["id"] for c in added], "rejected": rejected, "deck_size": len(existing) + len(added)}
    if added:
        existing.extend(added)
        state.save(deck_path, deck, "review_deck")
        result["written"] = True
        for c in added:
            sqlite_store.upsert_review_card(deck_path, c)
    else:
        result["written"] = False
    return result


@ledger.logged("deck_add.py", "deck_path")
@filelock.locked("deck_path")
def retire(deck_path, card_ids):
    allowed, cstatus = consent.check(deck_path, consent.SCHEDULING)
    if not allowed:
        return {"action": "not_persisted", **consent.skipped(cstatus, consent.SCHEDULING)}
    if not os.path.isfile(deck_path):
        return {"error": f"FileNotFoundError: no deck at {deck_path}"}
    deck = state.load(deck_path, "review_deck")
    cards = deck.get("cards", [])
    want = set(card_ids)
    kept = [c for c in cards if not (isinstance(c, dict) and c.get("id") in want)]
    gone = len(cards) - len(kept)
    found = {c.get("id") for c in cards if isinstance(c, dict)}
    result = {"retired": sorted(want & found), "unknown": sorted(want - found), "deck_size": len(kept)}
    if gone:
        deck["cards"] = kept
        state.save(deck_path, deck, "review_deck")
    result["written"] = bool(gone)
    return result


def mature(deck_path):
    if not os.path.isfile(deck_path):
        return {"error": f"FileNotFoundError: no deck at {deck_path}"}
    cards = state.load(deck_path, "review_deck").get("cards", [])
    old = [{"id": c["id"], "stage_id": c.get("stage_id"), "interval_sessions": c["interval_sessions"]} for c in cards
           if isinstance(c, dict) and c.get("interval_sessions", 0) >= MATURE_INTERVAL and c.get("lapses", 0) == 0]
    return {"mature": sorted(old, key=lambda c: (-c["interval_sessions"], c["id"])), "deck_size": len(cards)}


def main():
    args = sys.argv[1:]
    if args[:1] == ["retire"] and len(args) >= 3:
        try:
            sys.exit(cli.emit(retire(args[1], args[2:])))
        except cli.EXPECTED_ERRORS as e:
            print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
            sys.exit(1)
    if args[:1] == ["mature"] and len(args) == 2:
        sys.exit(cli.emit(mature(args[1])))
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
        print(json.dumps({"error": "usage: deck_add.py <deck.json> <course_id> <stage_id> [--max-per-stage N]  (cards as a JSON list on stdin) | retire <deck.json> <card_id>... | mature <deck.json>"}))
        sys.exit(2)
    try:
        cards = json.loads(cli.read_stdin())
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
