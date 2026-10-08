#!/usr/bin/env python3
"""
resolve_root.py -- report where the tutor's data root is and whether it looks right (E-07).

    python3 resolve_root.py [--root <path>] [--profile-root <path>]

Profile folders default to <root>/profile; --profile-root or $EDU_PROFILE_ROOT puts them elsewhere (own drive).
Resolution order: --root, $EDU_ROOT, or the folder containing the deployed .tutor-scripts/
this script runs from. Output: {root, courses, profile, profile_separate, tutor_scripts, valid, problems[]}.
Exit 0 when a root was found and is valid, 1 otherwise (problems explain what to fix).
"""
import json
import sys

from tutorlib import cli, paths


USAGE = {"error": "usage: resolve_root.py [--root <path>] [--profile-root <path>]"}


def main(argv):
    root = profile = None
    args = list(argv)
    while args:
        flag = args.pop(0)
        if flag not in ("--root", "--profile-root") or not args:
            print(json.dumps(USAGE))
            return 2
        if flag == "--root":
            root = args.pop(0)
        else:
            profile = args.pop(0)
    resolved = paths.resolve_root(root)
    result = paths.layout(resolved, profile)
    if resolved is None:
        result["problems"] = ["no data root: pass --root, set EDU_ROOT, or run the deployed copy under <root>/.tutor-scripts/"]
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
