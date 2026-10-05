#!/usr/bin/env python3
"""
review_select.py -- choose and order the cards for a review session (L-04, L-05, part of L-03).

    python3 review_select.py <learner_dir> <courses_dir> [--course <id>] [--stage <id>] [--item <id>]
                             [--limit N] [--slot N]

Replaces "gather every due card and present them" with a deterministic selection:

  due        a card is due when its due_at_slot <= the current slot (default: the profile's session_slot)
  scope      only courses the learner may draw slots from (active / test_pending_convergence, not grounding-suspended,
             not complete); optionally narrowed with --course / --stage / --item
  priority   most overdue first; then cards whose item the learner knows least (item_mastery.p_mastery, unobserved = 0.3);
             then lowest ease; then most lapses; then id (so ordering is stable)
  interleave the ordered cards are dealt round-robin across courses, so one subject cannot monopolise a session
             (spacing is the benefit of review; blocking by subject loses the contrast)
  cap        --limit (default 20) cards; the rest are reported as `remaining_due`, not dropped

Each selected card is returned with its front/back so the caller does not need to open the deck files. Read-only.
Output: {slot, selected[{course_id, card_id, stage_id, item_id, front, back, overdue_by, item_mastery}], selected_count,
remaining_due, due_total, scope}.
"""
import json
import os
import sys

from cohort_status import LIVE_STATES, is_complete, is_suspended
from item_mastery import P_INIT
from tutorlib import cli

DEFAULT_LIMIT = 20


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def select(learner_dir, courses_dir, course=None, stage=None, item=None, limit=DEFAULT_LIMIT, slot=None):
    profile = _load(os.path.join(learner_dir, "student_profile.json"))
    if profile is None:
        return {"error": f"no readable student_profile.json in {learner_dir}"}
    if slot is None:
        slot = profile.get("session_slot", 0) if isinstance(profile.get("session_slot", 0), int) else 0
    sdir = os.path.join(learner_dir, "subjects")
    due, skipped = [], []
    for fn in sorted(os.listdir(sdir)) if os.path.isdir(sdir) else []:
        if not fn.endswith(".json") or fn.endswith("_review_deck.json"):
            continue
        subj = _load(os.path.join(sdir, fn))
        if not isinstance(subj, dict):
            continue
        cid = subj.get("course_id") or fn[:-5]
        if course and cid != course:
            continue
        c = _load(os.path.join(courses_dir, cid, "course.json")) or {}
        if subj.get("roster_state") not in LIVE_STATES or is_suspended(c.get("grounding_status")) or (c and is_complete(c, subj)):
            skipped.append(cid)
            continue
        deck = _load(os.path.join(sdir, f"{cid}_review_deck.json")) or {}
        mastery = subj.get("item_mastery") if isinstance(subj.get("item_mastery"), dict) else {}
        for card in deck.get("cards", []):
            if not isinstance(card, dict) or not isinstance(card.get("due_at_slot"), int) or card["due_at_slot"] > slot:
                continue
            if stage and card.get("stage_id") != stage or item and card.get("item_id") != item:
                continue
            m = mastery.get(card.get("item_id")) if card.get("item_id") else None
            p = m.get("p_mastery", P_INIT) if isinstance(m, dict) else P_INIT
            due.append({"course_id": cid, "card_id": card.get("id"), "stage_id": card.get("stage_id"), "item_id": card.get("item_id"),
                        "front": card.get("front"), "back": card.get("back"), "overdue_by": slot - card["due_at_slot"],
                        "item_mastery": round(p, 4), "_ease": card.get("ease", 2.3), "_lapses": card.get("lapses", 0)})
    due.sort(key=lambda c: (-c["overdue_by"], c["item_mastery"], c["_ease"], -c["_lapses"], c["course_id"], str(c["card_id"])))
    # deal round-robin across courses, keeping each course's own priority order
    queues = {}
    for c in due:
        queues.setdefault(c["course_id"], []).append(c)
    order, selected = sorted(queues), []
    while len(selected) < limit and any(queues.values()):
        for cid in order:
            if queues[cid] and len(selected) < limit:
                selected.append(queues[cid].pop(0))
    for c in selected:
        c.pop("_ease"), c.pop("_lapses")
    return {"slot": slot, "selected": selected, "selected_count": len(selected), "due_total": len(due),
            "remaining_due": len(due) - len(selected),
            "scope": {"course": course, "stage": stage, "item": item, "limit": limit, "courses_skipped_not_live": sorted(skipped)}}


def main(argv):
    args, opts = list(argv), {"--course": None, "--stage": None, "--item": None, "--limit": str(DEFAULT_LIMIT), "--slot": None}
    for k in list(opts):
        if k in args:
            i = args.index(k)
            if i + 1 >= len(args):
                print(json.dumps({"error": f"{k} needs a value"}))
                return 2
            opts[k] = args[i + 1]
            del args[i:i + 2]
    if len(args) != 2:
        print(json.dumps({"error": "usage: review_select.py <learner_dir> <courses_dir> [--course id] [--stage id] [--item id] [--limit N] [--slot N]"}))
        return 2
    try:
        limit, slot = int(opts["--limit"]), (int(opts["--slot"]) if opts["--slot"] is not None else None)
    except ValueError:
        print(json.dumps({"error": "--limit and --slot must be integers"}))
        return 2
    if limit < 1:
        print(json.dumps({"error": "--limit must be at least 1"}))
        return 2
    return cli.emit(select(args[0], args[1], opts["--course"], opts["--stage"], opts["--item"], limit, slot))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
