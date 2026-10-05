#!/usr/bin/env python3
"""
validate_schema.py -- check a persisted file against its JSON Schema (S-05, S-06).

    python3 validate_schema.py <kind> <file>
    python3 validate_schema.py --kinds

kind: student_profile | subjects | review_deck | course | curriculum_map | rubric
Output: {"kind", "file", "valid", "errors": [...]}. Exit 0 valid, 1 invalid/unreadable, 2 usage.
"""
import json
import sys

from tutorlib import cli, schema


def main(argv):
    if argv == ["--kinds"]:
        return cli.emit({"kinds": schema.kinds()})
    if len(argv) != 2 or argv[0] not in schema.kinds():
        print(json.dumps({"error": f"usage: validate_schema.py <{'|'.join(schema.kinds())}> <file> | --kinds"}))
        return 2
    errors = schema.validate_file(argv[1], argv[0])
    out = {"kind": argv[0], "file": argv[1], "valid": not errors, "errors": errors}
    print(json.dumps(out, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
