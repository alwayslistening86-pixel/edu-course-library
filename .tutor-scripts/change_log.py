#!/usr/bin/env python3
"""
change_log.py -- read a course's `change.md` as data (S-11, N-11). Read-only.

    python3 change_log.py <course_dir>

The real files already follow one shape, which this script now defines and checks:

    # Change log - <course_id>
    ## YYYY-MM-DD - <title>            (the dash may be -, – or —)
    free text, optionally with bold labels:  **Found by:** … **Fixed:** … **Revalidated:** …

Output: {entries[{date, title, labels[]}], entry_count, first_date, last_date, built_on, problems[]}. Problems are advisory:
`malformed_heading` (a `##` line that does not start with an ISO date), `out_of_order` (entries not in date order, oldest first),
`no_built_entry` (nothing titled "built"), `no_title_heading` (missing the `# Change log` line). A course with no change.md reports
`entry_count: 0` and no problems (the file is optional). Nothing is written and no learner data is involved.
"""
import json
import os
import re
import sys

from tutorlib import cli

_HEAD = re.compile(r"^##\s+(\d{4}-\d{2}-\d{2})\s*[-–—]\s*(.+?)\s*$")
_LABEL = re.compile(r"^\*\*([A-Za-z][A-Za-z ]{0,40}):\*\*", re.M)


def parse(text):
    entries, problems, current = [], [], None
    lines = text.splitlines()
    if not any(line.startswith("# ") for line in lines[:3]):
        problems.append({"rule": "no_title_heading", "detail": "first line should be '# Change log - <course_id>'"})
    for n, line in enumerate(lines, 1):
        if line.startswith("## "):
            m = _HEAD.match(line)
            if m:
                current = {"date": m.group(1), "title": m.group(2), "labels": [], "line": n, "_body": []}
                entries.append(current)
            else:
                current = None
                problems.append({"rule": "malformed_heading", "line": n, "detail": line[:70]})
        elif current is not None:
            current["_body"].append(line)
    for e in entries:
        e["labels"] = _LABEL.findall("\n".join(e.pop("_body")))
    dates = [e["date"] for e in entries]
    if dates != sorted(dates):
        problems.append({"rule": "out_of_order", "detail": "entries should run oldest first"})
    if entries and not any(e["title"].lower().startswith("built") for e in entries):
        problems.append({"rule": "no_built_entry", "detail": "no entry titled 'built'"})
    return entries, problems


def read(course_dir):
    path = os.path.join(course_dir, "change.md")
    if not os.path.isfile(course_dir) and not os.path.isdir(course_dir):
        return {"error": f"FileNotFoundError: no such course folder {course_dir}"}
    if not os.path.isfile(path):
        return {"course_dir": course_dir, "entry_count": 0, "entries": [], "first_date": None, "last_date": None, "built_on": None, "problems": []}
    with open(path, encoding="utf-8", errors="replace") as f:
        entries, problems = parse(f.read())
    built = next((e["date"] for e in entries if e["title"].lower().startswith("built")), None)
    return {"course_dir": course_dir, "entry_count": len(entries), "entries": entries, "first_date": entries[0]["date"] if entries else None,
            "last_date": entries[-1]["date"] if entries else None, "built_on": built, "problems": problems}


def main(argv):
    if len(argv) != 1:
        print(json.dumps({"error": "usage: change_log.py <course_dir>"}))
        return 2
    return cli.emit(read(argv[0]))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
