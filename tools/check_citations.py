#!/usr/bin/env python3
"""
check_citations.py -- do the file:line citations in a document point at lines that exist? (Wave 7 inventories)

    python3 tools/check_citations.py docs/wave7/B-06-personal-data.md [more.md ...]

Finds citations of the form `name.ext:12`, `name.ext:12-30` or `name.ext:12,40-44` (also `~12`), resolves `name.ext` to a unique file
under the repository, and reports any line number past the end of the file, any file that cannot be found, and any name that matches
several files. It checks that a cited line EXISTS, not that it says what the document claims; a human still reads the rows. Exit 0 when
every citation resolves, 1 otherwise.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CITE = re.compile(r"([A-Za-z0-9_./-]+\.(?:py|md|json|yml|yaml|sh|txt)):~?(\d[\d,~-]*)")


def _files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split("\n")
    index = {}
    for rel in out:
        if rel and not rel.startswith(".tutor-scripts/"):  # the deployed copy is byte-identical (CI checks), so cite the source
            index.setdefault(os.path.basename(rel), []).append(rel)
    return index


def _numbers(spec):
    for part in re.split(r"[,]", spec):
        part = part.strip("~ ")
        if not part:
            continue
        for n in part.split("-"):
            n = n.strip("~")
            if n.isdigit():
                yield int(n)


def check(path, index):
    problems = []
    with open(path, encoding="utf-8") as f:
        text = f.read()
    for m in CITE.finditer(text):
        name, spec = m.group(1), m.group(2)
        base = os.path.basename(name)
        hits = [r for r in index.get(base, []) if r.endswith(name)]
        if not hits:
            problems.append(f"{name}:{spec}  no such file in the repository")
            continue
        if len(hits) > 1:
            problems.append(f"{name}:{spec}  ambiguous: {', '.join(hits[:3])}")
            continue
        with open(os.path.join(ROOT, hits[0]), encoding="utf-8", errors="replace") as f:
            length = sum(1 for _ in f)
        bad = [n for n in _numbers(spec) if n < 1 or n > length]
        if bad:
            problems.append(f"{name}:{spec}  line {bad[0]} is past the end ({hits[0]} has {length} lines)")
    return problems


def main(argv):
    if not argv:
        print("usage: check_citations.py <doc.md> [...]", file=sys.stderr)
        return 2
    index = _files()
    failed = 0
    for path in argv:
        problems = check(path, index)
        for p in problems:
            print(f"{path}: {p}")
        failed += len(problems)
    print(f"{failed} citation problem(s)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
