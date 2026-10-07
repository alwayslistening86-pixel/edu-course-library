#!/usr/bin/env python3
"""
diagnostic_gate.py — decides whether the practice-phase diagnostic branch
should fire: the branch that doesn't exist anywhere in course-runner.md
before this script, where a learner can visibly flounder through
`practice.md` and get no adaptive response until a hard test fail.

This is a trigger-condition check, not a diagnosis. It never classifies
*why* an answer was wrong (that's error_log.py's `cause` field, a model
judgment) — it only decides *whether this moment is worth stopping to ask
about*, from facts that are either already on disk (error_log.py's own
data) or handed in by the calling skill because they can only be known
from the live exchange (explicit confusion, a right-answer-wrong-reasoning
catch). Deliberately narrow: firing on every wrong answer collapses this
back into "replay the lesson slower" for a different reason, just phrased
as a branch instead of a re-explanation — see the tutor-core adaptive-
teaching-gap scoping note's "What this costs, honestly" section. The cost
is real (more turns, more tokens per stage) and should only be paid when
one of these four conditions actually holds.

Four trigger conditions, any one is sufficient:
  (a) two consecutive misses on the same item, in this stage's unresolved
      error_patterns (computed here from error_log.py's own data — the
      caller doesn't need to re-scan the log by hand)
  (b) a recurring `cause` tag within this stage (3+ unresolved entries
      sharing one cause in the current stage — a pattern, not one bad day)
  (c) the learner explicitly said they're confused (external flag — this
      script cannot read a conversation, so the calling skill passes it in
      exactly like a graded verdict is passed into review_math.py)
  (d) a right answer reached with wrong or absent reasoning, whenever the
      exchange surfaces one (external flag, same reason as (c)) — the
      false-positive-mastery case, arguably the most important of the four
      because nothing else in this plugin ever catches it

When it fires, the response is always **elicit before explaining** — ask
what the learner did, don't just tell them what's wrong — because the
elicited reasoning is what lets error_log.py's `cause` get classified
against the five-cause taxonomy instead of guessed. This script returns
that taxonomy table so the calling skill always has it in the same
authoritative shape rather than re-typing it from memory each session.

**(v1.5.0) `item_mastery` is surfaced, not a fifth trigger.** When
item_mastery.py has an entry for this item, its current `p_mastery` and
`observations` are included in the output purely as context for whatever
response the calling skill gives once this gate has already fired for one
of the four reasons above — a low `p_mastery` explains *why* trigger (a) or
(b) fired, useful for tone, but it never fires this gate by itself. Adding
mastery-level as a fifth trigger condition would reopen exactly the
scope-creep this script was written to resist (see the four-trigger
rationale above) for a signal (a decaying, item-specific tracking
probability) whose exact threshold has never been validated; a persistently
low `p_mastery` will, in practice, keep re-triggering trigger (a)/(b) on its
own as further misses accumulate, so nothing is lost by not gating on it
directly. When no entry exists yet for this item, `item_mastery` is `null`
— a brand-new item, not an error condition.

Usage:
    python3 diagnostic_gate.py <subjects.json> <stage_id> <item_id> \
        <explicit_confusion: true|false> <reasoning_mismatch: true|false>

Output: JSON to stdout. Read-only — this script never writes anything;
logging the resulting diagnosis is error_log.py's job, after the model has
actually done the diagnosing this gate only decided was worth doing.
"""
import json
import os
import sys

from tutorlib import cli

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import item_mastery  # noqa: E402

TAXONOMY = {
    "slip": {
        "meaning": "knew it, executed wrong (careless, not conceptual)",
        "right_response": "a prompt to recheck their own work",
        "wrong_response": "re-explaining a concept they already have",
    },
    "missing_prerequisite": {
        "meaning": "a gap from an earlier stage or an earlier course",
        "right_response": "routing back to where it was first taught",
        "wrong_response": "repeating the current stage's lesson, which assumes the missing piece",
    },
    "misconception": {
        "meaning": "a specific wrong mental model, applied consistently",
        "right_response": "directly confronting the wrong model with a case that breaks it, "
                           "ideally matched to misconceptions.json",
        "wrong_response": "a generic 'let's go over this again' that never names the actual wrong belief",
    },
    "misapplied_procedure": {
        "meaning": "right idea, wrong steps or formula",
        "right_response": "a fresh worked example of the correct procedure, set beside theirs",
        "wrong_response": "re-explaining the underlying concept, which was never the problem",
    },
    "comprehension": {
        "meaning": "didn't parse what the question actually asked",
        "right_response": "practice decoding question wording",
        "wrong_response": "any subject re-teaching at all",
    },
}


def _load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def evaluate(subjects_path, stage_id, item_id, explicit_confusion, reasoning_mismatch):
    d = _load(subjects_path)
    entries = d.get("error_patterns", [])
    if not isinstance(entries, list):
        entries = []
    unresolved_stage = [e for e in entries if isinstance(e, dict) and e.get("stage_id") == stage_id and not e.get("resolved")]

    same_item_misses = sum(1 for e in unresolved_stage if e.get("item_id") == item_id)
    trigger_a = same_item_misses >= 2

    cause_counts = {}
    for e in unresolved_stage:
        c = e.get("cause")
        if c:
            cause_counts[c] = cause_counts.get(c, 0) + 1
    recurring_cause = next((c for c, n in cause_counts.items() if n >= 3), None)
    trigger_b = recurring_cause is not None

    reasons = []
    if trigger_a:
        reasons.append(f"two-or-more unresolved misses on item {item_id!r} in stage {stage_id!r} ({same_item_misses})")
    if trigger_b:
        reasons.append(f"recurring cause {recurring_cause!r} in stage {stage_id!r} ({cause_counts[recurring_cause]} unresolved entries)")
    if explicit_confusion:
        reasons.append("learner explicitly said they're confused")
    if reasoning_mismatch:
        reasons.append("right answer, wrong or absent reasoning (false-positive-mastery catch)")

    fire = bool(reasons)

    mastery_status = item_mastery.status(subjects_path, item_id)
    mastery_entry = mastery_status.get("mastery") if isinstance(mastery_status, dict) else None
    item_mastery_info = mastery_entry if mastery_entry and mastery_entry.get("observations", 0) > 0 else None

    return {
        "fire": fire,
        "reasons": reasons,
        "trigger_a_repeated_item": trigger_a,
        "trigger_b_recurring_cause": {"cause": recurring_cause, "count": cause_counts.get(recurring_cause, 0)} if trigger_b else None,
        "trigger_c_explicit_confusion": bool(explicit_confusion),
        "trigger_d_reasoning_mismatch": bool(reasoning_mismatch),
        "response_style": "elicit before explaining — ask what they did, don't just tell them what's wrong" if fire else None,
        "taxonomy": TAXONOMY,
        "item_mastery": item_mastery_info,
    }


def main():
    if len(sys.argv) != 6:
        print(json.dumps({"error": "usage: diagnostic_gate.py <subjects.json> <stage_id> <item_id> <explicit_confusion:true|false> <reasoning_mismatch:true|false>"}))
        sys.exit(2)
    subjects_path, stage_id, item_id, confusion_s, mismatch_s = sys.argv[1:6]
    try:
        confusion = cli.parse_bool(confusion_s, "explicit_confusion")
        mismatch = cli.parse_bool(mismatch_s, "reasoning_mismatch")
    except ValueError as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)
    try:
        result = evaluate(subjects_path, stage_id, item_id, confusion, mismatch)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        sys.exit(1)
    sys.exit(cli.emit(result))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
