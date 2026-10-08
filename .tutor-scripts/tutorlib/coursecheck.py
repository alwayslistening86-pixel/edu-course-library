"""
Checks an error entry against the course it is about (ADR 0012 class 2, B-04.5c / B-04.5d): the voice proposes an item and a
misconception id; a script writes only what the course can confirm.

The course folder comes from an explicit path, else <data root>/courses/<course id> when the data root can be found (EDU_ROOT or the
deployed scripts' own location) and the course id is the subjects file's name. If no course folder is found the checks are skipped
and the result says so; nothing is refused for lack of something to check against.

  item        in an itemised course (curriculum_map.json has `_syllabus_items`) the item id must be one of them. An item that belongs to a
              different stage than the one given is accepted with a warning, because interleaved practice legitimately revisits earlier
              stages. A course that is not itemised, or an item id of NONE, is not checked.
  misconception  a non-NONE misconception id must be the `id` of an entry in stages/<stage>/misconceptions.json. A stage whose file has no
              ids (written before ids existed) accepts only NONE, and the refusal says how to add ids (misconception_ids.py).
"""
import json
import os

from tutorlib import paths

NONE_VALUES = (None, "", "NONE")


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def course_dir_for(subjects_path, explicit=None):
    """The course folder this progress file belongs to, or None when it cannot be found."""
    if explicit:
        return explicit if os.path.isdir(explicit) else None
    root = paths.resolve_root()
    if not root:
        return None
    course_id = os.path.splitext(os.path.basename(subjects_path))[0]
    cand = os.path.join(root, "courses", course_id)
    return cand if os.path.isdir(cand) else None


def check_entry(course_dir, stage_id, item_id, misconception_id):
    """(refusal or None, warnings[], note). `note` says what could not be checked."""
    if course_dir is None:
        return None, [], "not checked: the course folder was not found"
    warnings = []
    cmap = _load(os.path.join(course_dir, "curriculum_map.json"))
    items = [i.get("id") for i in (cmap or {}).get("_syllabus_items", []) if isinstance(i, dict)] if isinstance(cmap, dict) else []
    if items and item_id not in NONE_VALUES:
        if item_id not in items:
            return f"item {item_id!r} is not an item of this course; use an item id from next_items.py (or NONE)", warnings, None
        owner = [s for s, v in cmap.items() if not s.startswith("_") and isinstance(v, dict) and item_id in (v.get("covers_items") or [])]
        if owner and stage_id not in owner:
            warnings.append(f"item {item_id} belongs to stage {owner[0]}, logged under {stage_id}")
    if misconception_id not in NONE_VALUES:
        entries = _load(os.path.join(course_dir, "stages", stage_id, "misconceptions.json"))
        ids = [e["id"] for e in entries if isinstance(e, dict) and isinstance(e.get("id"), str)] if isinstance(entries, list) else []
        if misconception_id not in ids:
            if ids:
                return f"misconception id {misconception_id!r} is not in stage {stage_id}'s misconceptions.json (known: {', '.join(ids[:10])}); use one of those, or NONE for a new kind of mistake", warnings, None
            return f"stage {stage_id} lists no misconception ids, so only NONE can be recorded (misconception_ids.py adds ids to an existing file)", warnings, None
    return None, warnings, None
