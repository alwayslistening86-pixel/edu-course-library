#!/usr/bin/env python3
"""
toolkit/export_anki.py — export a learner's review deck(s) to a real Anki
.apkg file, importable into the actual Anki app (desktop or mobile).

Read-only against tutor state, per every other module here (core.py design
rule 1): this only reads subjects/<course_id>_review_deck.json and writes a
.apkg file under profile/<learner_id>/exports/, plus one log line to this
package's own toolkit_log — the same footprint backup.py already has.
Never touches ease/interval/lapses/due_at_slot, and never marks a card
reviewed; Anki gets its own copy of the card content and schedules it with
its own algorithm from scratch. This is content portability, not state
migration — the two systems' scheduling states are deliberately never
synced back and forth in either direction.

ONE DELIBERATE, DOCUMENTED EXCEPTION TO CORE.PY'S "NO NEW THIRD-PARTY
DEPENDENCY" RULE: this module needs `genanki` (MIT-licensed, pure Python,
no compiled/C++ requirement — `pip install genanki`) to actually write the
.apkg binary format correctly. Hand-rolling Anki's SQLite-based collection
format was considered and rejected: it's a real, easy-to-get-subtly-wrong
format (field separators, per-model JSON, checksums, card queue/type
enums), with no way to verify a hand-rolled writer actually round-trips
through real Anki without a live Anki install to test against — whereas
genanki already is exactly that, widely used (2,700+ stars), and actively
maintained. Every OTHER toolkit module stays zero-dependency; this is the
one, explicit, opt-in exception, and the feature no-ops with a plain
install instruction if genanki isn't present rather than crashing anything
else in the toolkit.

Usage:
    python3 -m toolkit export-anki <learner_id> [--courses id1,id2] [--out DIR]
"""
import datetime
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402

try:
    import genanki
    GENANKI_AVAILABLE = True
except ImportError:
    GENANKI_AVAILABLE = False

NOT_INSTALLED_MESSAGE = (
    "genanki is not installed, so Anki export is unavailable. "
    "Run: pip install genanki"
)


def _stable_id(*parts):
    """A deterministic id from a fixed string, sized for genanki's model/deck
    id space, so re-exporting the same course updates the same Anki deck on
    re-import instead of creating a duplicate every time."""
    h = hashlib.sha256("::".join(parts).encode("utf-8")).hexdigest()
    return int(h[:8], 16)


def _model():
    return genanki.Model(
        _stable_id("generic-tutor", "basic-model", "v1"),
        "generic-tutor basic",
        fields=[{"name": "Front"}, {"name": "Back"}],
        templates=[{
            "name": "Card 1",
            "qfmt": "{{Front}}",
            "afmt": '{{FrontSide}}<hr id="answer">{{Back}}',
        }],
    )


def export_decks(learner_id, root=None, course_ids=None, out_dir=None):
    if not GENANKI_AVAILABLE:
        return {"error": NOT_INSTALLED_MESSAGE}

    root = root or core.edu_root()
    pdir = core.profile_dir(learner_id, root)
    if not os.path.isdir(pdir):
        return {"error": f"no such learner profile: {pdir}"}

    courses = course_ids or core.list_enrolled_courses(learner_id, root)
    model = _model()
    decks = []
    exported_courses = []
    skipped_courses = []
    total_cards = 0

    for course_id in courses:
        deck_data = core.load_review_deck(learner_id, course_id, root)
        if not core.is_ok(deck_data):
            skipped_courses.append(course_id)
            continue
        cards = [
            c for c in deck_data.get("cards", [])
            if isinstance(c, dict) and c.get("front") and c.get("back")
        ]
        if not cards:
            skipped_courses.append(course_id)
            continue

        anki_deck = genanki.Deck(_stable_id("generic-tutor", "deck", course_id), f"EDU export::{course_id}")
        for card in cards:
            tags = [str(t) for t in (course_id, card.get("stage_id"), card.get("item_id"), card.get("criterion")) if t]
            anki_deck.add_note(genanki.Note(model=model, fields=[card["front"], card["back"]], tags=tags))
        decks.append(anki_deck)
        exported_courses.append(course_id)
        total_cards += len(cards)

    if not decks:
        return {
            "error": "no exportable cards found across the requested courses",
            "skipped_courses": skipped_courses,
        }

    out_dir = out_dir or os.path.join(pdir, "exports")
    os.makedirs(out_dir, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    apkg_path = os.path.join(out_dir, f"{learner_id}_anki_export_{stamp}.apkg")

    genanki.Package(decks).write_to_file(apkg_path)

    result = {
        "learner_id": learner_id,
        "apkg_path": apkg_path,
        "courses_exported": exported_courses,
        "skipped_courses": skipped_courses,
        "deck_count": len(decks),
        "card_count": total_cards,
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    _log_export(learner_id, root, result)
    return result


def _log_export(learner_id, root, result):
    log_dir = core.toolkit_log_dir(learner_id, root)
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "anki_exports.jsonl")
    entry = {k: result[k] for k in ("apkg_path", "deck_count", "card_count", "created_at")}
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "usage: export_anki.py <learner_id> [--courses id1,id2] [--out DIR]"}))
        sys.exit(2)
    learner_id = sys.argv[1]
    course_ids = None
    out_dir = None
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == "--courses" and i + 1 < len(args):
            course_ids = [c for c in args[i + 1].split(",") if c]
            i += 2
        elif args[i] == "--out" and i + 1 < len(args):
            out_dir = args[i + 1]
            i += 2
        else:
            i += 1
    result = export_decks(learner_id, course_ids=course_ids, out_dir=out_dir)
    print(json.dumps(result, indent=2))
    sys.exit(1 if "error" in result else 0)


if __name__ == "__main__":
    main()
