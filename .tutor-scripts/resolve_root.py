#!/usr/bin/env python3
"""
resolve_root.py -- report where the tutor's data root is and whether it looks right (E-07).

    python3 resolve_root.py [--root <path>]

Resolution order: --root, $EDU_ROOT, or the folder containing the deployed .tutor-scripts/
this script runs from. Output: {root, courses, profile, tutor_scripts, valid, problems[]}.
Exit 0 when a root was found and is valid, 1 otherwise (problems explain what to fix).
"""
import json
import sys

from tutorlib import cli, paths


def main(argv):
    root = None
    if argv[:1] == ["--root"]:
        if len(argv) != 2:
            print(json.dumps({"error": "usage: resolve_root.py [--root <path>]"}))
            return 2
        root = argv[1]
    elif argv:
        print(json.dumps({"error": "usage: resolve_root.py [--root <path>]"}))
        return 2
    resolved = paths.resolve_root(root)
    result = paths.layout(resolved)
    if resolved is None:
        result["problems"] = ["no data root: pass --root, set EDU_ROOT, or run the deployed copy under <root>/.tutor-scripts/"]
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
