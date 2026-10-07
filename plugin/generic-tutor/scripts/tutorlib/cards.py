"""
Review-card types (L-06). One place that knows what each type needs and how it is shown.

basic        a question and its answer (the default; a card with no `card_type` is basic)
cloze        the front holds one or more `{{c1::answer}}` deletions; the learner fills the blank
explain_why  the front asks why or how; the back is the key reason, in a sentence or two
worked_step  the front shows a problem and the steps so far; the learner gives the next step

The checks are structural and blunt on purpose: they catch a card filed under the wrong type, not a badly written one.
"""
import re

TYPES = ("basic", "cloze", "explain_why", "worked_step")
CLOZE = re.compile(r"\{\{c\d+::([^{}]+?)\}\}")
BLANK = "[...]"


def type_of(card):
    """The card's type; anything missing or unknown reads as basic, so older decks keep working."""
    t = card.get("card_type") if isinstance(card, dict) else None
    return t if t in TYPES else "basic"


def check_type(card):
    """None if the card satisfies its declared type, else the reason it does not."""
    t = card.get("card_type")
    if t is None:
        return None
    if t not in TYPES:
        return f"card_type must be one of {', '.join(TYPES)}"
    front = card["front"]
    if t == "cloze" and not CLOZE.search(front):
        return "a cloze card needs a {{c1::...}} deletion in its front"
    if t == "explain_why" and not re.search(r"\b(why|how)\b", front, re.I):
        return "an explain_why card's front must ask why or how"
    if t == "worked_step" and not re.search(r"\bstep\b", front, re.I):
        return "a worked_step card's front must show the steps so far and ask for the next step"
    return None


def prompt_for(card):
    """What to show the learner: a cloze front with each deletion blanked, otherwise the front as written."""
    front = card.get("front") or ""
    return CLOZE.sub(BLANK, front) if type_of(card) == "cloze" else front


def answers_for(card):
    """The deleted text of a cloze card, in order (empty for other types)."""
    return [m.group(1).strip() for m in CLOZE.finditer(card.get("front") or "")] if type_of(card) == "cloze" else []
