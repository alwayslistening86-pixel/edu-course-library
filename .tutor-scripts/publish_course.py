#!/usr/bin/env python3
"""
publish_course.py -- make a compiled course live only once it has passed the post-compile gate (N-15).

    python3 publish_course.py publish <courses_dir> <course_id> [--override "<reason>"]
    python3 publish_course.py discard <courses_dir> <course_id>

The compiler writes a new course into `<courses_dir>/.build-<course_id>/`, a hidden folder: no listing, audit or enrolment sees
it (a course is a folder with a valid id, and `.build-...` is not one). `publish` then
  1. refuses if a live course of that id already exists (an existing course is resumed or audited, never overwritten),
  2. runs postcompile_gate on the build folder and, unless the gate says `can_ship` (or `--override` gives a reason, which is
     returned for the report), stops and returns the blocking reasons with the build folder untouched,
  3. renames the folder to `<courses_dir>/<course_id>/` in one step, so the course appears complete or not at all.
`discard` removes a leftover build folder (an interrupted or abandoned compile). It touches nothing but `.build-<course_id>`.
Output: {published, course_id, can_ship, overridden, override_reason?, blocking_reasons?, advisory_notes?} or {error}.
"""
import json
import os
import shutil
import sys

import postcompile_gate
from tutorlib import atomic_io, cli, ids, paths

PREFIX = ".build-"


def _build_dir(courses_dir, course_id):
    ids.validate(course_id, "course id")
    if not os.path.isdir(courses_dir):
        raise FileNotFoundError(f"no courses folder at {courses_dir}")
    build = os.path.join(courses_dir, PREFIX + course_id)
    paths.ensure_within(courses_dir, build)
    if os.path.islink(build):
        raise ValueError(f"{build!r} is a symlink")
    return build


def publish(courses_dir, course_id, override_reason=None):
    try:
        build = _build_dir(courses_dir, course_id)
    except (ValueError, OSError) as e:
        return {"published": False, "error": f"{type(e).__name__}: {e}"}
    if not os.path.isdir(build):
        return {"published": False, "error": f"no build folder {PREFIX}{course_id} under {courses_dir}: write the course there first"}
    target = os.path.join(courses_dir, course_id)
    if os.path.exists(target):
        return {"published": False, "error": f"course {course_id!r} already exists; resume or audit it, never overwrite (discard the build folder if it is stale)"}
    gate = postcompile_gate.check(build)
    overridden = False
    if not gate.get("can_ship"):
        if not (override_reason and override_reason.strip()):
            return {"published": False, "course_id": course_id, "can_ship": False, "overridden": False,
                    "blocking_reasons": gate.get("blocking_reasons", []), "advisory_notes": gate.get("advisory_notes", [])}
        overridden = True
    try:
        atomic_io.replace(build, target)
    except OSError as e:
        return {"published": False, "course_id": course_id, "error": f"could not move the build folder into place, nothing changed: {e}"}
    out = {"published": True, "course_id": course_id, "can_ship": bool(gate.get("can_ship")), "overridden": overridden,
           "advisory_notes": gate.get("advisory_notes", [])}
    if overridden:
        out["override_reason"] = override_reason
        out["blocking_reasons"] = gate.get("blocking_reasons", [])
    return out


def discard(courses_dir, course_id):
    try:
        build = _build_dir(courses_dir, course_id)
    except (ValueError, OSError) as e:
        return {"discarded": False, "error": f"{type(e).__name__}: {e}"}
    if not os.path.isdir(build):
        return {"discarded": False, "course_id": course_id, "note": "no build folder to discard"}
    shutil.rmtree(build)
    return {"discarded": True, "course_id": course_id}


def main(argv):
    args = list(argv)
    reason = None
    if "--override" in args:
        i = args.index("--override")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--override needs a reason"}))
            return 2
        reason = args[i + 1]
        del args[i:i + 2]
    if len(args) == 3 and args[0] == "publish":
        return cli.emit(publish(args[1], args[2], reason))
    if len(args) == 3 and args[0] == "discard" and reason is None:
        return cli.emit(discard(args[1], args[2]))
    print(json.dumps({"error": "usage: publish_course.py publish <courses_dir> <course_id> [--override \"<reason>\"] | discard <courses_dir> <course_id>"}))
    return 2


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
