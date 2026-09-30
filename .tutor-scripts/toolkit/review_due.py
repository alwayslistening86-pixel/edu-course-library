#!/usr/bin/env python3
"""
toolkit/review_due.py — which review-deck cards are due, relative to the
current session_slot. Read-only preview of what /review would run in a
live session; never advances a slot, marks a card reviewed, or changes
ease/interval — that stays review-scheduler's job, run through the tutor.

Usage:
    python3 -m toolkit review-due <learner_id> [--within-slots N]
"""
import json
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402


def due_cards(learner_id, root=None, within_slots=0):
    root = root or core.edu_root()
    current_slot = core.current_session_slot(learner_id, root)
    if current_slot is None:
        return {"error": "could not read session_slot for this learner"}

    due, upcoming = [], []
    for course_id in core.list_enrolled_courses(learner_id, root):
        deck = core.load_review_deck(learner_id, course_id, root)
        if not core.is_ok(deck):
            continue
        for card in deck.get("cards", []):
            if not isinstance(card, dict):
                continue
            due_at = card.get("due_at_slot")
            if due_at is None:
                continue
            entry = {
                "course_id": course_id,
                "card_id": card.get("id"),
                "stage_id": card.get("stage_id"),
                "item_id": card.get("item_id"),
                "criterion": card.get("criterion"),
                "due_at_slot": due_at,
                "overdue_by": max(0, current_slot - due_at),
            }
            if due_at <= current_slot:
                due.append(entry)
            elif within_slots and due_at <= current_slot + within_slots:
                upcoming.append(entry)

    due.sort(key=lambda c: -c["overdue_by"])
    upcoming.sort(key=lambda c: c["due_at_slot"])
    return {
        "learner_id": learner_id,
        "current_slot": current_slot,
        "due_now": due,
        "due_count": len(due),
        "upcoming": upcoming,
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "usage: review_due.py <learner_id> [--within-slots N]"}))
        sys.exit(2)
    learner_id = sys.argv[1]
    within_slots = 0
    if "--within-slots" in sys.argv:
        i = sys.argv.index("--within-slots")
        if i + 1 < len(sys.argv):
            within_slots = int(sys.argv[i + 1])
    print(json.dumps(due_cards(learner_id, within_slots=within_slots), indent=2))


if __name__ == "__main__":
    main()
