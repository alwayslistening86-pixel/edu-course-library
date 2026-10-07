#!/usr/bin/env python3
"""
assemble_paper.py -- build a timed practice paper from a course's question bank (L-08, N-07).

    python3 assemble_paper.py <courses_dir> <course_id> [--marks N] [--minutes N] [--stages S1,S2] [--seed N]
                              [--calculator yes|no|any] [--exclude id1,id2]

Reads `<courses_dir>/<course_id>/question_bank.json` (schema `question_bank`; optional per course). Picks questions from the
chosen stages (default: every stage) until the paper's marks are within TOLERANCE of --marks (default 40), spreading questions
across stages and syllabus items first, then by difficulty, deterministically for a given --seed (default 0, so a paper can be
reproduced and a different seed gives a different paper). `--exclude` removes questions already used (e.g. an earlier mock).

Output: {course_id, seed, total_marks, minutes_suggested (the paper's marks x minutes-per-mark; default 1.2 min per mark, or --minutes),
questions[{id, stage_id, item_ids, marks, calculator, command_word, prompt}], items_covered, stages_covered, notes}.
The output deliberately carries NO mark scheme and NO model answers (they are read from the bank when marking), so a paper
can be shown to the learner as is. Grade boundaries are NOT estimated: boundaries are published per series by the board and
change, and this system holds none; `notes` says so. Read-only.
"""
import json
import os
import random
import sys

from tutorlib import cli, schema

DEFAULT_MARKS = 40
TOLERANCE = 3
MINUTES_PER_MARK = 1.2


def _shown(q):
    """What the learner may see of a question: never the answer key, but a multiple-choice question's options (the key holds them)."""
    out = {k: q.get(k) for k in ("id", "stage_id", "item_ids", "marks", "calculator", "command_word", "prompt")}
    key = q.get("key", {})
    if key.get("kind") == "mcq" and key["options"][0] not in q["prompt"]:         # an item written with its options in the prompt needs no second copy
        out["options"] = key["options"]
    return out


def assemble(courses_dir, course_id, marks=DEFAULT_MARKS, minutes=None, stages=None, seed=0, calculator="any", exclude=()):
    path = os.path.join(courses_dir, course_id, "question_bank.json")
    if not os.path.isfile(path):
        return {"error": f"course {course_id!r} has no question_bank.json (it is optional; the exam simulator needs one)"}
    errs = schema.validate_file(path, "question_bank")
    if errs:
        return {"error": f"question_bank.json is invalid: {errs[:3]}"}
    with open(path, encoding="utf-8") as f:
        bank = json.load(f)["questions"]
    pool = [q for q in bank if q["id"] not in set(exclude) and (not stages or q["stage_id"] in stages)
            and (calculator == "any" or q.get("calculator") in (None, calculator == "yes"))]
    if not pool:
        return {"error": "no questions match those filters"}
    rng = random.Random(seed)
    rng.shuffle(pool)                                  # seed decides ties; the sort below is stable
    covered_items, covered_stages, chosen, total = set(), {}, [], 0
    def novelty(q):
        new_items = len(set(q.get("item_ids", [])) - covered_items)
        return (-new_items, covered_stages.get(q["stage_id"], 0), q.get("difficulty", 3))

    while pool and total < marks - TOLERANCE:
        fits = [q for q in pool if total + q["marks"] <= marks + TOLERANCE]
        if not fits:
            break
        q = sorted(fits, key=novelty)[0]
        pool.remove(q)
        chosen.append(q)
        total += q["marks"]
        covered_items |= set(q.get("item_ids", []))
        covered_stages[q["stage_id"]] = covered_stages.get(q["stage_id"], 0) + 1
    if not chosen:
        return {"error": "could not fit any question within the requested marks"}
    chosen.sort(key=lambda q: (q["stage_id"], q["id"]))
    mins = minutes if minutes else round(total * MINUTES_PER_MARK)
    notes = ["Grade boundaries are published per series by the exam board and are not held here: this paper gives marks, not a grade.",
             "Time is advisory: the tutor cannot enforce it; the learner should note their own start and finish."]
    if abs(total - marks) > TOLERANCE:
        notes.append(f"The bank could not reach {marks} marks within +/-{TOLERANCE}; this paper has {total}.")
    return {"course_id": course_id, "seed": seed, "total_marks": total, "minutes_suggested": mins,
            "questions": [_shown(q) for q in chosen],
            "items_covered": sorted(covered_items), "stages_covered": sorted(covered_stages), "notes": notes}


def main(argv):
    args = list(argv)
    opts = {"--marks": str(DEFAULT_MARKS), "--minutes": None, "--stages": None, "--seed": "0", "--calculator": "any", "--exclude": ""}
    for k in list(opts):
        if k in args:
            i = args.index(k)
            if i + 1 >= len(args):
                print(json.dumps({"error": f"{k} needs a value"}))
                return 2
            opts[k] = args[i + 1]
            del args[i:i + 2]
    if len(args) != 2 or opts["--calculator"] not in ("yes", "no", "any"):
        print(json.dumps({"error": "usage: assemble_paper.py <courses_dir> <course_id> [--marks N] [--minutes N] [--stages S1,S2] [--seed N] [--calculator yes|no|any] [--exclude id,id]"}))
        return 2
    try:
        marks, seed = int(opts["--marks"]), int(opts["--seed"])
        minutes = int(opts["--minutes"]) if opts["--minutes"] else None
    except ValueError:
        print(json.dumps({"error": "--marks, --minutes and --seed must be integers"}))
        return 2
    stages = [s for s in (opts["--stages"] or "").split(",") if s] or None
    return cli.emit(assemble(args[0], args[1], marks, minutes, stages, seed, opts["--calculator"],
                             tuple(x for x in opts["--exclude"].split(",") if x)))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
