#!/usr/bin/env python3
"""
practice_pick.py -- which practice item next, and a record of which ones the learner has already met (L-13).

    python3 practice_pick.py next <subjects.json> <practice.md> <stage_id>
    python3 practice_pick.py used <subjects.json> <stage_id> fixed <item_number>
    python3 practice_pick.py used <subjects.json> <stage_id> generated

The real practice files hold very few items (1-2 for most stages, 3-5 where scenarios are listed), so a learner who repeats a
stage, or practises again after a failed test, would otherwise meet the same prompts every time. `next` reads the numbered items
under "## Practice items" or "## Practice scenarios" and the learner's `practice_used[stage_id]` and answers
  {fixed_total, used_fixed, unused_fixed, generated_count, recommendation}
where recommendation is `use_fixed:<n>` (the lowest unused item) or `generate_new` (every written item has been met: write a
fresh one of the same type and difficulty, never a repeat of an earlier one). `used` records the choice afterwards.
`next` is read-only. State lives in the subjects file as `practice_used: {stage_id: {"fixed": [n, ...], "generated": k}}`
(optional; absent = nothing used, so no schema migration). Consent class: progress. Atomic, locked, ledgered.
"""
import json
import re
import sys

from tutorlib import atomic_io, cli, consent, filelock, ledger, state

_SECTION = re.compile(r"^##\s+Practice (?:items|scenarios)[^\n]*\n(.*?)(?=^##\s|\Z)", re.M | re.S)
_ITEM = re.compile(r"^(\d+)[.)]\s", re.M)


def fixed_items(practice_text):
    """Item numbers (as written) at the top level of the practice section, in order."""
    m = _SECTION.search(practice_text)
    return [int(n) for n in _ITEM.findall(m.group(1))] if m else []


def next_item(subjects_path, practice_path, stage_id):
    data = state.load(subjects_path, "subjects")
    try:
        with open(practice_path, encoding="utf-8") as f:
            items = fixed_items(f.read())
    except OSError as e:
        return {"error": f"FileNotFoundError: cannot read {practice_path}: {e.strerror}"}
    rec = (data.get("practice_used") or {}).get(stage_id) or {}
    used = sorted(set(rec.get("fixed") or []))
    unused = [n for n in items if n not in used]
    return {"stage_id": stage_id, "fixed_total": len(items), "used_fixed": [n for n in used if n in items], "unused_fixed": unused,
            "generated_count": int(rec.get("generated") or 0),
            "recommendation": f"use_fixed:{unused[0]}" if unused else "generate_new"}


@ledger.logged("practice_pick.py", "subjects_path")
@filelock.locked("subjects_path")
def mark_used(subjects_path, stage_id, kind, number=None):
    if kind not in ("fixed", "generated"):
        return {"error": "kind must be 'fixed' or 'generated'"}
    if kind == "fixed" and (not isinstance(number, int) or number < 1):
        return {"error": "a fixed item needs its item number (a positive integer)"}
    data = state.load(subjects_path, "subjects")
    rec = data.setdefault("practice_used", {}).setdefault(stage_id, {"fixed": [], "generated": 0})
    if kind == "fixed":
        already = number in rec["fixed"]
        if not already:
            rec["fixed"] = sorted(rec["fixed"] + [number])
    else:
        already = False
        rec["generated"] = int(rec.get("generated") or 0) + 1
    allowed, cstatus = consent.check(subjects_path, consent.PROGRESS)
    if not allowed:
        return {"action": "used", "stage_id": stage_id, **consent.skipped(cstatus, consent.PROGRESS)}
    if kind == "fixed" and already:
        return {"action": "used", "stage_id": stage_id, "kind": kind, "already_recorded": True, "written": False}
    atomic_io.write_json(subjects_path, data)
    return {"action": "used", "stage_id": stage_id, "kind": kind, "fixed": rec["fixed"], "generated": rec["generated"], "written": True}


def main(argv):
    try:
        if len(argv) == 4 and argv[0] == "next":
            return cli.emit(next_item(argv[1], argv[2], argv[3]))
        if len(argv) == 5 and argv[0] == "used" and argv[3] == "fixed":
            try:
                n = int(argv[4])
            except ValueError:
                n = None
            return cli.emit(mark_used(argv[1], argv[2], "fixed", n))
        if len(argv) == 4 and argv[0] == "used" and argv[3] == "generated":
            return cli.emit(mark_used(argv[1], argv[2], "generated"))
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1
    print(json.dumps({"error": "usage: practice_pick.py next <subjects.json> <practice.md> <stage_id> | used <subjects.json> <stage_id> fixed <n> | used <subjects.json> <stage_id> generated"}))
    return 2


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
