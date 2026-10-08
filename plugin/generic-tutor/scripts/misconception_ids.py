#!/usr/bin/env python3
"""
misconception_ids.py -- give the entries of a course's misconceptions.json stable ids (B-04.5d), so a logged misconception can be checked. Course content.

    python3 misconception_ids.py <course_dir> [--write]

For each stages/<stage>/misconceptions.json, entries without an `id` get `MC-<stage>-<n>`, where n is the smallest positive number not already used in
that file. Existing ids are never changed and entries are never reordered, so running it again changes nothing and ids learners' errors already carry
stay valid. Without --write it only reports what it would add; with --write each file is replaced atomically, and only if it is a list of objects that
still validates afterwards. A file that is not valid JSON, or already has a duplicate id, is reported and left alone.
Output: {course_dir, written, files: [{stage, added: [ids], total}], skipped: [{stage, reason}]}.
"""
import json
import os
import sys

from tutorlib import atomic_io, cli, schema


def assign(stage, entries):
    """New list with ids added; returns (entries, added_ids)."""
    used = {e["id"] for e in entries if isinstance(e.get("id"), str)}
    added, out = [], []
    for e in entries:
        if "id" not in e:
            n = 1
            while f"MC-{stage}-{n}" in used:
                n += 1
            e = {"id": f"MC-{stage}-{n}", **e}
            used.add(e["id"])
            added.append(e["id"])
        out.append(e)
    return out, added


def run(course_dir, write=False):
    if not os.path.isdir(course_dir):
        return {"error": f"FileNotFoundError: no such course folder {course_dir}"}
    stages = os.path.join(course_dir, "stages")
    files, skipped = [], []
    for stage in sorted(os.listdir(stages)) if os.path.isdir(stages) else []:
        path = os.path.join(stages, stage, "misconceptions.json")
        if not os.path.isfile(path):
            continue
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, ValueError) as e:
            skipped.append({"stage": stage, "reason": f"unreadable: {type(e).__name__}"})
            continue
        if not isinstance(data, list) or not all(isinstance(e, dict) for e in data):
            skipped.append({"stage": stage, "reason": "not a list of entries"})
            continue
        ids = [e["id"] for e in data if isinstance(e.get("id"), str)]
        if len(ids) != len(set(ids)):
            skipped.append({"stage": stage, "reason": "already has a duplicate id; fix by hand"})
            continue
        new, added = assign(stage, data)
        problems = schema.validate(new, "misconceptions")
        if problems:
            skipped.append({"stage": stage, "reason": f"would not validate after adding ids: {problems[:2]}"})
            continue
        if added and write:
            atomic_io.write_json(path, new)
        files.append({"stage": stage, "added": added, "total": len(new)})
    return {"course_dir": course_dir, "written": bool(write and any(f["added"] for f in files)), "files": files, "skipped": skipped}


def main(argv):
    args = [a for a in argv if a != "--write"]
    if len(args) != 1:
        print(json.dumps({"error": "usage: misconception_ids.py <course_dir> [--write]"}))
        return 2
    return cli.emit(run(args[0], "--write" in argv))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
