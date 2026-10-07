#!/usr/bin/env python3
"""
exam_guidance.py -- what exam guidance does this course actually hold? (L-09) Read-only.

    python3 exam_guidance.py <course_dir> [--word WORD]

Reads the optional course-root `exam_technique.md` and `command_words.json` (written by the compiler only where the issuing body
publishes guidance, N-05) so the tutor quotes what is there and never improvises exam technique the board did not publish.
Output: {"course_dir", "technique": {"available", "source", "text"}, "command_words": {"available", "source", "count", "words"},
"caveat"}, plus, with --word, "lookup": {"word", "found", "meaning", "earns_marks_by"} (case-insensitive; found false says the
course holds no definition for it). A file that is absent or malformed (validate_structure's rule) reports available false and, when
malformed, "problems"; this script never repairs it. The text is the compiler's own-words summary of the guidance, capped at 6000 chars.
"""
import json
import os
import sys

from tutorlib import cli
import validate_structure

MAX_TEXT = 6000
CAVEAT = ("Own-words summary of what the issuing body published, as read by the compiler; not the board's wording, and not a promise of marks. "
          "Where a file is unavailable, say the course holds no board guidance on it rather than inventing any.")


def guidance(course_dir, word=None):
    if not os.path.isdir(course_dir):
        return {"error": f"FileNotFoundError: no such course folder {course_dir}"}
    status = validate_structure._exam_guidance_status(course_dir)
    tech, cw = status["exam_technique"], status["command_words"]
    out = {"course_dir": course_dir, "technique": {"available": False}, "command_words": {"available": False}, "caveat": CAVEAT}
    if tech.get("present") and not tech.get("well_formed"):
        out["technique"]["problems"] = tech["problems"]
    elif tech.get("present"):
        with open(os.path.join(course_dir, "exam_technique.md"), encoding="utf-8") as f:
            text = f.read()
        src = next((ln.split(":", 1)[1].strip() for ln in text.splitlines() if ln.strip().lower().startswith("source:")), "")
        out["technique"] = {"available": True, "source": src, "text": text[:MAX_TEXT], "truncated": len(text) > MAX_TEXT}
    entries = []
    if cw.get("present") and not cw.get("well_formed"):
        out["command_words"]["problems"] = cw["problems"]
    elif cw.get("present"):
        with open(os.path.join(course_dir, "command_words.json"), encoding="utf-8") as f:
            data = json.load(f)
        entries = data["command_words"]
        out["command_words"] = {"available": True, "source": data["source"], "count": len(entries), "words": [e["word"] for e in entries]}
    if word is not None:
        key = word.strip().lower()
        hit = next((e for e in entries if e["word"].strip().lower() == key), None)
        out["lookup"] = ({"word": word, "found": True, "meaning": hit["meaning"], "earns_marks_by": hit["earns_marks_by"]} if hit
                         else {"word": word, "found": False})
    return out


def main(argv):
    word, rest, i = None, [], 0
    while i < len(argv):
        if argv[i] == "--word" and i + 1 < len(argv):
            word = argv[i + 1]
            i += 2
        else:
            rest.append(argv[i])
            i += 1
    if len(rest) != 1:
        print(json.dumps({"error": "usage: exam_guidance.py <course_dir> [--word WORD]"}))
        return 2
    return cli.emit(guidance(rest[0], word))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
