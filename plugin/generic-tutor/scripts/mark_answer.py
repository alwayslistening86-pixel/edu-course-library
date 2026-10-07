#!/usr/bin/env python3
"""
mark_answer.py -- mark one learner answer against a question's answer key, without a model (B-02.3, ADR 0012). Read-only.

    python3 mark_answer.py <question_bank.json> <question_id> <answer>

The question needs a `key` (see tutorlib/marking.py for the three kinds: mcq, numeric, short). The script, not the voice, decides
correct or not; the voice only supplies what the learner said. Output: {"question_id", "kind", "correct": true|false|null,
"reason", "marks_available", "marks_awarded"}; correct null means the answer cannot be marked by script (empty or ambiguous):
ask the learner to rewrite it and record nothing. Marks are all-or-nothing for a keyed question. A question with no key, a
malformed key, or an unknown id is an error (exit 1): fall back to the examiner. This script writes nothing; recording the result
is a separate step (error_log.py, item_mastery.py) and stays with the caller.
"""
import json
import sys

from tutorlib import cli, marking, schema


def mark_question(bank_path, question_id, answer):
    errors = schema.validate_file(bank_path, "question_bank")
    if errors:
        return {"error": f"question bank is invalid: {errors[:3]}"}
    with open(bank_path, encoding="utf-8") as f:
        bank = json.load(f)
    q = next((q for q in bank["questions"] if q["id"] == question_id), None)
    if q is None:
        return {"error": f"no such question {question_id!r} in the bank"}
    if "key" not in q:
        return {"error": f"question {question_id!r} has no answer key: it needs the examiner, not a script"}
    verdict = marking.mark(q["key"], answer)
    awarded = q["marks"] if verdict["correct"] else 0
    return {"question_id": question_id, "kind": q["key"]["kind"], **verdict, "marks_available": q["marks"], "marks_awarded": awarded}


def main(argv):
    if len(argv) != 3:
        print(json.dumps({"error": "usage: mark_answer.py <question_bank.json> <question_id> <answer>"}))
        return 2
    return cli.emit(mark_question(*argv))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
