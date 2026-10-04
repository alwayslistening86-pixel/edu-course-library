---
name: data-export
description: Bundles the active learner's profile, every course's progress, review decks and the full history database into one zip on request via /export. Done by export_profile.py; read-only with respect to the learner's data.
---

# Data Export

**Contract**
- **Owns:** producing one export zip (nothing in `/EDU/` is modified).
- **Reads:** the active learner's folder, only through `export_profile.py`.
- **Calls:** `export_profile.py`.
- **Emits:** one zip file and a plain list of what it contains.
- **Never:** runs on inferred intent; includes another learner's data; writes the zip inside `/EDU/profile/`.

## Invocation
`/export`, for the currently active learner only.

## Procedure
1. Choose an output path **outside** `/EDU/profile/` (the learner's chosen folder, or a sensible default such as their documents/downloads folder), named `<user_id>-export.zip`.
2. Run:
   ```
   python3 /EDU/.tutor-scripts/export_profile.py <the /EDU/profile/ dir> <active user_id> <output.zip>
   ```
3. Hand the zip over as a normal file. Tell the learner what is inside (from the result) and that it contains personal data — they should store it as carefully as the original.

## What is included
`student_profile.json`; every `subjects/<course_id>.json` including dropped courses; every `*_review_deck.json`; every table of the history database as `history/<table>.json`; and `manifest.json` (format version, plugin version, sha256 of each file).

## Not included
Shared course content (`/EDU/courses/`, same for every learner) and `change.md` entries (they describe the course, not the learner). If the learner wants a readable summary rather than raw data, offer to produce a document from the export with the environment's document tooling.
