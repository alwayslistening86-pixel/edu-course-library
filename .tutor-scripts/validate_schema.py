#!/usr/bin/env python3
"""
validate_schema.py -- check a persisted file against its JSON Schema (S-05, S-06).

    python3 validate_schema.py <kind> <file>
    python3 validate_schema.py --kinds
    python3 validate_schema.py --course-dir <course_dir>

kind: student_profile | subjects | review_deck | course | curriculum_map | rubric
Output: {"kind", "file", "valid", "errors": [...]}. Exit 0 valid, 1 invalid/unreadable, 2 usage.

`--course-dir` checks every schema-covered file of one course in a single call: course.json, curriculum_map.json, rubric.json, each
stage's misconceptions.json and question_bank.json when present. Output: {"course_dir", "valid", "files_checked", "invalid": [{file, kind, errors[:5]}]}.
"""
import json
import os
import sys

from tutorlib import cli, schema


def check_course_dir(course_dir):
    if not os.path.isdir(course_dir):
        return {"error": f"FileNotFoundError: no such course folder {course_dir}"}
    targets = [("course.json", "course"), ("curriculum_map.json", "curriculum_map"), ("rubric.json", "rubric"), ("question_bank.json", "question_bank")]
    stages = os.path.join(course_dir, "stages")
    if os.path.isdir(stages):
        targets += [(f"stages/{st}/misconceptions.json", "misconceptions") for st in sorted(os.listdir(stages))]
    checked, invalid = 0, []
    for rel, kind in targets:
        path = os.path.join(course_dir, *rel.split("/"))
        if not os.path.isfile(path):
            if kind in ("course", "curriculum_map", "rubric"):
                invalid.append({"file": rel, "kind": kind, "errors": ["file is missing"]})
            continue
        checked += 1
        errors = schema.validate_file(path, kind)
        if errors:
            invalid.append({"file": rel, "kind": kind, "errors": errors[:5]})
    return {"course_dir": course_dir, "valid": not invalid, "files_checked": checked, "invalid": invalid}


def main(argv):
    if len(argv) == 2 and argv[0] == "--course-dir":
        return cli.emit(check_course_dir(argv[1]))
    if argv == ["--kinds"]:
        return cli.emit({"kinds": schema.kinds()})
    if len(argv) != 2 or argv[0] not in schema.kinds():
        print(json.dumps({"error": f"usage: validate_schema.py <{'|'.join(schema.kinds())}> <file> | --kinds | --course-dir <course_dir>"}))
        return 2
    errors = schema.validate_file(argv[1], argv[0])
    out = {"kind": argv[0], "file": argv[1], "valid": not errors, "errors": errors}
    print(json.dumps(out, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
