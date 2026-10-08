#!/usr/bin/env python3
"""
item_mastery.py — per-syllabus-item Bayesian Knowledge Tracing (BKT),
augmenting (not replacing) the course-level `confidence` scalar
confidence_update.py owns.

Why per-item, and why this over `confidence`: `confidence` is one number
for a whole course — useful for tutor-core's coarse pacing ("doing well ->
move faster"), but it can't answer "does this learner actually have item
RM6, specifically" the way `curriculum_map.json`'s own itemisation invites.
Every stage's syllabus items are already atomic and already the unit
`error_log.py` logs against (`item_id` on every entry) — this script is
what turns that existing per-item signal into an actual per-item mastery
probability, rather than adding a second, unrelated tracking scheme.

Why BKT and not a heavier model: this is a personal, single-learner (or
small handful of learners) system producing at most a few hundred graded
events a year per course. A neural sequence tracker (DKT) needs a training
corpus across many learners to be worth anything — there is no such corpus
here, and fitting one to this little data would be fitting noise, not
signal. BKT with fixed, sensible default parameters is the right tool at
this scale — same reasoning as review_math.py using a stated concrete
formula instead of a heavier adaptive scheme nobody could audit.

The model, per item, is the textbook four-parameter BKT:
  P(L0)   prior probability the item is already known before any evidence
  P(T)    probability of transitioning from not-known to known after an
          opportunity to learn (whether or not this observation was correct)
  P(S)    "slip" - probability of answering incorrectly despite knowing it
  P(G)    "guess" - probability of answering correctly despite not knowing it

On each observation (correct or incorrect), Bayes' rule updates the belief
about *current* mastery, then the learning transition is applied to project
forward to the *next* opportunity:
  correct:    posterior = P(L)*(1-S) / [P(L)*(1-S) + (1-P(L))*G]
  incorrect:  posterior = P(L)*S     / [P(L)*S     + (1-P(L))*(1-G)]
  new P(L)  = posterior + (1 - posterior) * T

Defaults used here (P(L0)=0.3, P(T)=0.15, P(S)=0.1, P(G)=0.2) are the same
order of magnitude as the parameters commonly reported in the BKT literature
(e.g. Corbett & Anderson's original cognitive-tutor fits average in this
range) — stated, fixed, and documented rather than invented per item, and
deliberately not fit to this library's own sparse data, which would be
overfitting a handful of observations per item.

Where the observations come from — deliberately piggy-backed on existing
signal, not a new instrumentation burden: `error_log.py`'s `append` (an
incorrect observation) and `resolve` (a correct one) already fire exactly
when a diagnosed error or its later correction happens, against a specific
`item_id`. Rather than require every teaching turn to separately call this
script — which would be a much larger behavioural change, more tokens per
exchange, for information most exchanges don't need — `error_log.py` calls
this script's `observe` itself on both `append` and `resolve`, so item
mastery updates automatically from data the plugin is already collecting.
A model may still call `observe` directly for a graded exchange that ties
cleanly to one item (e.g. a rubric criterion mapped to a single item_id) but
this is optional, not mandatory instrumentation.

State lives in subjects/<course_id>.json under `item_mastery`, keyed by
item_id:
  "item_mastery": {
    "RM6": {"p_mastery": 0.62, "observations": 3, "last_slot": 214, "last_correct": true}
  }

Subcommands:
    observe <subjects.json> <item_id> <correct:true|false> <current_slot>
    status  <subjects.json> <item_id|ALL>

Usage:
    python3 item_mastery.py observe <subjects.json> <item_id> <true|false> <current_slot>
    python3 item_mastery.py status <subjects.json> <item_id|ALL>

Output: JSON to stdout. `observe` writes the subjects file back in place;
`status` is read-only.
"""
import json
import os
import sys
from tutorlib import cli, consent, filelock, ledger, state

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sqlite_store  # noqa: E402

P_INIT = 0.3
P_TRANSIT = 0.15
P_SLIP = 0.1
P_GUESS = 0.2


def _load(path):
    return state.load(path, "subjects")


def _save(path, data):
    state.save(path, data, "subjects")


def _update(p_l, correct, p_slip=P_SLIP, p_guess=P_GUESS, p_transit=P_TRANSIT):
    if correct:
        num = p_l * (1 - p_slip)
        den = num + (1 - p_l) * p_guess
    else:
        num = p_l * p_slip
        den = num + (1 - p_l) * (1 - p_guess)
    posterior = num / den if den > 0 else p_l
    new_p = posterior + (1 - posterior) * p_transit
    return max(0.0, min(1.0, new_p)), max(0.0, min(1.0, posterior))


@ledger.logged("item_mastery.py", "subjects_path")
@filelock.locked("subjects_path")
def observe(subjects_path, item_id, correct, current_slot):
    d = _load(subjects_path)
    mastery = d.setdefault("item_mastery", {})
    if not isinstance(mastery, dict):
        return {"error": "item_mastery is not an object — needs migrate_schema.py first"}

    entry = mastery.get(item_id)
    prior = entry["p_mastery"] if isinstance(entry, dict) and "p_mastery" in entry else P_INIT
    new_p, posterior = _update(prior, correct)

    observations = (entry.get("observations", 0) + 1) if isinstance(entry, dict) else 1
    prior_run = int(entry.get("consecutive_misses", 0) or 0) if isinstance(entry, dict) else 0
    consecutive_misses = 0 if correct else prior_run + 1                      # a miss needs no cause to be counted (B-04.5b)
    mastery[item_id] = {
        "p_mastery": round(new_p, 4),
        "observations": observations,
        "last_slot": int(current_slot),
        "last_correct": bool(correct),
        "consecutive_misses": consecutive_misses,
    }
    allowed, cstatus = consent.check(subjects_path, consent.SIGNAL)
    if not allowed:
        return {"item_id": item_id, "prior": round(prior, 4), "posterior_this_observation": round(posterior, 4),
                "new_p_mastery": round(new_p, 4), "observations": observations, "consecutive_misses": consecutive_misses,
                **consent.skipped(cstatus, consent.SIGNAL)}
    _save(subjects_path, d)
    sqlite_result = sqlite_store.log_item_mastery_observation(
        subjects_path, item_id, correct, prior, posterior, new_p, current_slot
    )

    return {
        "item_id": item_id,
        "prior": round(prior, 4),
        "posterior_this_observation": round(posterior, 4),
        "new_p_mastery": round(new_p, 4),
        "observations": observations,
        "consecutive_misses": consecutive_misses,
        "params": {"p_init": P_INIT, "p_transit": P_TRANSIT, "p_slip": P_SLIP, "p_guess": P_GUESS},
        "sqlite": sqlite_result,
    }


def status(subjects_path, item_filter="ALL"):
    d = _load(subjects_path)
    mastery = d.get("item_mastery", {})
    if not isinstance(mastery, dict):
        mastery = {}
    if item_filter != "ALL":
        entry = mastery.get(item_filter)
        return {"item_id": item_filter, "mastery": entry if entry else {"p_mastery": P_INIT, "observations": 0, "detail": "no observations yet — prior only"}}
    return {"items": mastery, "count": len(mastery)}


def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "usage: item_mastery.py observe|status <subjects.json> ..."}))
        sys.exit(2)
    cmd, subjects_path = sys.argv[1], sys.argv[2]
    try:
        if cmd == "observe":
            if len(sys.argv) != 6:
                print(json.dumps({"error": "usage: item_mastery.py observe <subjects.json> <item_id> <correct:true|false> <current_slot>"}))
                sys.exit(2)
            try:
                correct = cli.parse_bool(sys.argv[4], "correct")
            except ValueError as e:
                print(json.dumps({"error": str(e)}))
                sys.exit(1)
            result = observe(subjects_path, sys.argv[3], correct, sys.argv[5])
        elif cmd == "status":
            item_filter = sys.argv[3] if len(sys.argv) > 3 else "ALL"
            result = status(subjects_path, item_filter)
        else:
            print(json.dumps({"error": f"unknown subcommand {cmd!r}, expected observe|status"}))
            sys.exit(2)
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        sys.exit(1)
    sys.exit(cli.emit(result))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
