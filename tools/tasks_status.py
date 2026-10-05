#!/usr/bin/env python3
"""
tasks_status.py -- counts for docs/TASKS.md derived from the task tables and the progress log, so they cannot rot.

    python3 tools/tasks_status.py            print the counts table
    python3 tools/tasks_status.py --write    replace the "## Task counts" section of docs/TASKS.md
    python3 tools/tasks_status.py --check    exit 1 if that section is out of date

A task's status is the LAST row for its id in the "## Progress" log (done / partial / deferred / dropped); a task with no
row is open. A task row in a workstream table whose id cell carries a tick counts as done, and one that says "partial" as partial.
"""
import os
import re
import sys

ORDER = "R E S K C P V L A U N X D".split()
NAMES = {"R": "Repo", "E": "Engine", "S": "Schemas", "K": "Skills", "C": "Commands", "P": "Plugin surface", "V": "Trust & verification",
         "L": "Learning design", "A": "Assessment & evals", "U": "Learner visibility", "N": "Content pipeline", "X": "Security & privacy", "D": "Documentation"}
_ID = re.compile(r"^\|\s*([A-Z])-(\d{2})\b([^|]*)\|(.*)$")
STATES = ("done", "partial", "deferred", "dropped", "open")


def _classify(cell):
    low = cell.lower()
    if "➖" in cell or "dropped" in low:
        return "dropped"
    if "⏸" in cell or "deferred" in low:
        return "deferred"
    if "ℹ" in cell:
        return None
    if "🟡" in cell or any(w in low for w in ("partial", "mostly", "infrastructure")):
        return "partial"
    return "done" if "✅" in cell else None


def parse(text):
    head, _, log = text.partition("\n## Progress")
    log, _, _ = log.partition("\n## Suggested first sprint")
    tasks, status = {}, {}
    for line in head.splitlines():
        m = _ID.match(line)
        if m and m.group(1) in ORDER:
            tid = f"{m.group(1)}-{m.group(2)}"
            tasks[tid] = True
            if "✅" in m.group(3):
                status[tid] = "partial" if "partial" in m.group(3).lower() else "done"
            elif "partial" in m.group(3).lower():
                status[tid] = "partial"
    for line in log.splitlines():
        m = _ID.match(line)
        if not m:
            continue
        tid = f"{m.group(1)}-{m.group(2)}"
        cls = _classify(m.group(4).split("|")[0].strip())
        if cls:
            status[tid] = cls
        tasks.setdefault(tid, True)
    return sorted(tasks), status


def counts(text):
    ids, status = parse(text)
    table = {ws: dict.fromkeys(STATES, 0) for ws in ORDER}
    for tid in ids:
        table[tid[0]][status.get(tid, "open")] += 1
    return table


def render(table):
    lines = ["## Task counts", "", "Derived by `tools/tasks_status.py` from the tables and the progress log above; regenerate with `--write`.", "",
             "| Workstream | Tasks | Done | Partial | Deferred / dropped | Open |", "|---|---|---|---|---|---|"]
    tot = dict.fromkeys(STATES, 0)
    for ws in ORDER:
        r = table[ws]
        n = sum(r.values())
        for k in STATES:
            tot[k] += r[k]
        lines.append(f"| {ws} {NAMES[ws]} | {n} | {r['done']} | {r['partial']} | {r['deferred'] + r['dropped']} | {r['open']} |")
    lines.append(f"| **Total** | **{sum(tot.values())}** | **{tot['done']}** | **{tot['partial']}** | **{tot['deferred'] + tot['dropped']}** | **{tot['open']}** |")
    return "\n".join(lines) + "\n"


def split(text):
    i = text.index("\n## Task counts")
    return text[:i + 1], text[i + 1:]


def main(argv):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs", "TASKS.md")
    with open(path, encoding="utf-8") as f:
        text = f.read()
    keep, current = split(text)
    new = render(counts(keep))
    if "--write" in argv:
        with open(path, "w", encoding="utf-8") as f:
            f.write(keep + new)
        print(new)
        return 0
    if "--check" in argv:
        if current != new:
            print("docs/TASKS.md task counts are out of date: run python3 tools/tasks_status.py --write")
            return 1
        return 0
    print(new)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
