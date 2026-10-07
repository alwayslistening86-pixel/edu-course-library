#!/usr/bin/env python3
"""
release_notes.py -- print the CHANGELOG.md section for a version (R-12).

    python3 tools/release_notes.py <version>      # e.g. 1.22.0 (a leading 'v' is accepted)

Exit 1 if CHANGELOG.md has no '## [<version>]' section, so a release cannot be cut without notes.
"""
import os
import re
import sys


def section(text, version):
    version = version.lstrip("v")
    m = re.search(rf"^## \[{re.escape(version)}\][^\n]*\n(.*?)(?=^## \[|\Z)", text, re.M | re.S)
    return m.group(0).rstrip() + "\n" if m else None


def main(argv):
    if len(argv) != 1:
        print("usage: release_notes.py <version>", file=sys.stderr)
        return 2
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "CHANGELOG.md")
    with open(path, encoding="utf-8") as f:
        notes = section(f.read(), argv[0])
    if notes is None:
        print(f"no CHANGELOG.md section for {argv[0]}", file=sys.stderr)
        return 1
    print(notes, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
