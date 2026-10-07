#!/usr/bin/env python3
"""
bank_pick.py -- choose the next keyed question-bank item for a stage, and remember it was met (B-02.4, ADR 0012 class 1).

    python3 bank_pick.py next <subjects.json> <question_bank.json> <stage_id> [--prefer item_id,item_id]
    python3 bank_pick.py used <subjects.json> <question_bank.json> <stage_id> <question_id>

`next` is read-only. It considers only questions of that stage that carry a `key` (tutorlib/marking.py), because only those can be
marked by script (`mark_answer.py`); unkeyed bank questions need the examiner and are not offered here. It skips questions already
recorded as used, and with `--prefer` puts questions covering any of those syllabus item ids first (pass the weakest items from
`next_items.py`); otherwise it keeps bank order. Output: {stage_id, keyed_total, used, remaining, question: {id, prompt, marks,
item_ids, command_word, options?} | null, recommendation}. The key is never printed; a multiple-choice question shows its options
unless its prompt already contains them. `recommendation` is `ask:<id>` or `none_left` (every keyed question has been met: use a
practice.md item, or the examiner) or `no_keyed_questions` (this stage's bank has none: the examiner or an adult marks it).

`used` records the id under `practice_used[stage].bank` (and `bank_last`, the question most recently served), progress-class consent,
atomic, locked, ledgered. It refuses an id that is not a keyed question of that stage, so a mistyped or invented id cannot be recorded.
Recording it again is a no-op. Marking the answer and logging any error are separate steps.
"""
import json
import sys

from tutorlib import cli, consent, filelock, ledger, schema, state


def _keyed(bank_path, stage_id):
    errors = schema.validate_file(bank_path, "question_bank")
    if errors:
        return None, {"error": f"question bank is invalid: {errors[:3]}"}
    with open(bank_path, encoding="utf-8") as f:
        bank = json.load(f)
    return [q for q in bank["questions"] if q["stage_id"] == stage_id and "key" in q], None


def _shown(q):
    out = {k: q.get(k) for k in ("id", "prompt", "marks", "item_ids", "command_word")}
    key = q["key"]
    if key["kind"] == "mcq" and key["options"][0] not in q["prompt"]:
        out["options"] = key["options"]
    return out


def next_question(subjects_path, bank_path, stage_id, prefer=()):
    keyed, err = _keyed(bank_path, stage_id)
    if err:
        return err
    data = state.load(subjects_path, "subjects")
    used = set(((data.get("practice_used") or {}).get(stage_id) or {}).get("bank") or [])
    left = [q for q in keyed if q["id"] not in used]
    if prefer:
        wanted = set(prefer)
        left = sorted(left, key=lambda q: 0 if wanted & set(q.get("item_ids") or []) else 1)       # stable: bank order inside each group
    out = {"stage_id": stage_id, "keyed_total": len(keyed), "used": len([q for q in keyed if q["id"] in used]), "remaining": len(left)}
    if not keyed:
        return {**out, "question": None, "recommendation": "no_keyed_questions"}
    if not left:
        return {**out, "question": None, "recommendation": "none_left"}
    return {**out, "question": _shown(left[0]), "recommendation": f"ask:{left[0]['id']}"}


@ledger.logged("bank_pick.py", "subjects_path")
@filelock.locked("subjects_path")
def mark_used(subjects_path, bank_path, stage_id, question_id):
    keyed, err = _keyed(bank_path, stage_id)
    if err:
        return err
    if question_id not in {q["id"] for q in keyed}:
        return {"error": f"{question_id!r} is not a keyed question of stage {stage_id!r} in this bank"}
    data = state.load(subjects_path, "subjects")
    rec = data.setdefault("practice_used", {}).setdefault(stage_id, {"fixed": [], "generated": 0})
    bank = rec.setdefault("bank", [])
    already = question_id in bank
    if not already:
        bank.append(question_id)
    rec["bank_last"] = question_id
    allowed, cstatus = consent.check(subjects_path, consent.PROGRESS)
    if not allowed:
        return {"action": "used", "stage_id": stage_id, **consent.skipped(cstatus, consent.PROGRESS)}
    state.save(subjects_path, data, "subjects")
    return {"action": "used", "stage_id": stage_id, "question_id": question_id, "bank": bank, "already_recorded": already, "written": True}


def main(argv):
    usage = {"error": "usage: bank_pick.py next <subjects.json> <question_bank.json> <stage_id> [--prefer item,item] | used <subjects.json> <question_bank.json> <stage_id> <question_id>"}
    args = list(argv)
    prefer = ()
    if "--prefer" in args:
        i = args.index("--prefer")
        if i + 1 >= len(args):
            print(json.dumps(usage))
            return 2
        prefer = tuple(x for x in args[i + 1].split(",") if x)
        del args[i:i + 2]
    try:
        if len(args) == 4 and args[0] == "next":
            return cli.emit(next_question(*args[1:], prefer))
        if len(args) == 5 and args[0] == "used" and not prefer:
            return cli.emit(mark_used(*args[1:]))
    except cli.EXPECTED_ERRORS as e:
        return cli.emit({"error": f"{type(e).__name__}: {e}"})
    print(json.dumps(usage))
    return 2


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
