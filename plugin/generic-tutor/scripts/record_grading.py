#!/usr/bin/env python3
"""
record_grading.py -- keep, per stage test, which rubric criteria were judged met and for how many marks (V-09). Signal-class: granted consent only.

    python3 record_grading.py <subjects.json> <course.json> <stage_id> <slot> <<'EOF'
    [{"criterion": 1, "met": true, "marks": 2, "of": 2}, {"criterion": 2, "met": false, "marks": 0, "of": 3}]
    EOF

A pass or fail on its own says nothing about *why*. This keeps the part of the reasoning that is safe to keep: for each criterion of the stage's
rubric entry (1-based, in the order `rubric.json` lists them), whether it was met, marks awarded out of marks available, and a hash of the rubric
entry the test was marked against, so a later audit can tell that a rubric changed under an old result. **Nothing else is stored:** not the learner's
answer, not a quotation, not the rubric's own wording (the course text stays in the course). Each call is one attempt; attempts are numbered per stage
by the history database. Run it before `record_stage_result.py`, from the same marking.

Checks, all before anything is written: every criterion index exists in the stage's rubric entry and appears once; `met` is true/false; marks are whole
numbers with 0 <= marks <= of; `of` is at least 1. Nothing is written for a stage the rubric does not contain.
Output: {stage_id, attempt, criteria, marks_awarded, marks_available, rubric_hash}. History only: it never changes `syllabus_status` or `confidence`.
"""
import hashlib
import json
import os
import sys

import sqlite_store
from tutorlib import cli, ledger


def rubric_hash(entry):
    return hashlib.sha256(json.dumps({"criteria": entry.get("criteria"), "pass_threshold": entry.get("pass_threshold")}, sort_keys=True,
                                     ensure_ascii=False).encode("utf-8")).hexdigest()[:16]


def record(subjects_path, course_path, stage_id, slot, results):
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(course_path)), "rubric.json"), encoding="utf-8") as f:
            rubric = json.load(f)
    except (OSError, ValueError) as e:
        return {"error": f"FileNotFoundError: cannot read rubric.json next to {course_path}: {e}"}
    entry = (rubric.get("stage_rubrics") or {}).get(stage_id)
    if not isinstance(entry, dict) or not isinstance(entry.get("criteria"), list):
        return {"error": f"{stage_id!r} has no rubric entry"}
    n = len(entry["criteria"])
    if not isinstance(results, list) or not results:
        return {"error": "stdin must be a non-empty JSON list of {criterion, met, marks, of}"}
    seen, rows = set(), []
    for r in results:
        if not isinstance(r, dict):
            return {"error": "each result must be an object"}
        i, met, marks, of = r.get("criterion"), r.get("met"), r.get("marks"), r.get("of")
        if not (isinstance(i, int) and not isinstance(i, bool) and 1 <= i <= n):
            return {"error": f"criterion must be a number from 1 to {n} (this stage has {n} criteria), got {i!r}"}
        if i in seen:
            return {"error": f"criterion {i} appears twice"}
        if not isinstance(met, bool):
            return {"error": f"criterion {i}: met must be true or false"}
        if not all(isinstance(x, int) and not isinstance(x, bool) for x in (marks, of)) or of < 1 or not 0 <= marks <= of:
            return {"error": f"criterion {i}: marks must be a whole number from 0 to 'of', and 'of' at least 1"}
        seen.add(i)
        rows.append((i, met, marks, of, rubric_hash(entry)))
    try:
        slot = int(slot)
    except (TypeError, ValueError):
        return {"error": "slot must be a whole number"}
    res = sqlite_store.log_grading(subjects_path, stage_id, rows, slot)
    if res.get("ok") is False:
        return {"error": res.get("error", "could not write the history")}
    out = {"stage_id": stage_id, "criteria": len(rows), "marks_awarded": sum(r[2] for r in rows), "marks_available": sum(r[3] for r in rows),
           "rubric_hash": rows[0][4]}
    if res.get("written") is False:
        return {**out, "written": False, "skipped": res.get("skipped")}
    ledger.record(subjects_path, "record_grading.py", "record", os.path.splitext(os.path.basename(subjects_path))[0], True, None,
                  {"stage_id": stage_id, "criteria": len(rows)})
    return {**out, "attempt": res["attempt"], "written": True}


def main(argv):
    if len(argv) != 4:
        print(json.dumps({"error": "usage: record_grading.py <subjects.json> <course.json> <stage_id> <slot>  (results as a JSON list on stdin)"}))
        return 2
    try:
        results = json.loads(cli.read_stdin())
    except ValueError as e:
        print(json.dumps({"error": f"stdin is not valid JSON: {e}"}))
        return 1
    return cli.emit(record(*argv, results))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
