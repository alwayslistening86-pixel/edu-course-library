#!/usr/bin/env python3
"""
confidence_update.py — gives `confidence` a formula instead of a vibe, same
spirit as review_math.py's SM-2-lite: an exponentially-weighted running
value in [0, 1], nudged by each graded event rather than reconstructed from
however much of the session is still in context.

Before this script, `confidence` was a tracked field with no owner —
present in the micro-profile schema, read by tutor-core's pacing rules
("doing well -> move faster," "struggling -> slow down"), but nothing
computed or updated it. This is that owner, the same division of labour as
review_math.py: the model never hand-computes the delta, it calls this
script with the event that just happened and writes back what it returns.

Event -> base delta:
  pass_clean          +0.15   (passed with no remediation)
  pass_remediated     +0.05   (passed, but only after a remediation cycle —
                                real progress, credited less than a clean pass)
  fail                -0.10
An additional flag, --misconception, applies a further -0.05 on top of
whichever base delta fired — a new error_patterns entry tagged
`misconception` is the costliest cause to leave uncorrected (see
diagnostic_gate.py's taxonomy), so it's penalised beyond an ordinary fail.

Every delta is scaled by distance from the relevant bound so confidence can
never overshoot 1 or undershoot 0:
  - a positive delta is scaled by (1 - old_confidence): the closer to 1
    already, the smaller the further gain.
  - a negative delta is scaled by old_confidence: the closer to 0 already,
    the smaller the further loss.
This is the same shape of guarantee review_math.py's ease floor/ceiling
gives that field — a lapse is a setback, not a cliff, and a strong streak
approaches but never reaches certainty.

Usage (pure calculation, unchanged, still never touches a file):
    python3 confidence_update.py compute <old_confidence> <event: pass_clean|pass_remediated|fail> [--misconception]

Usage (read-modify-write, added in v1.10.0 — closes the write-back trust
gap named directly by the library owner: previously this script computed a
value and *trusted* the calling skill's prose instruction to write it back,
with no code ever checking that happened, unlike error_log.py/item_mastery.py
which have always owned their own writes):
    python3 confidence_update.py apply <subjects.json> <event: pass_clean|pass_remediated|fail> <current_slot> [--misconception]

`apply` loads subjects.json, reads the current `confidence` field (default
0.5 if absent — a fresh course with no graded events yet), calls the same
`compute()` below, writes `confidence` back into the file itself, logs the
event to sqlite_store's confidence_events history table, and returns the
same shape as `compute()` plus `"written": true`. `course-runner.md` calls
`apply`, not `compute` + a hand-written-back value, from this version on.
The `compute` subcommand stays exactly as it was, for testing and for any
caller that genuinely wants the arithmetic only.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sqlite_store  # noqa: E402
from tutorlib import cli, consent, filelock, ledger, state

BASE_DELTA = {
    "pass_clean": 0.15,
    "pass_remediated": 0.05,
    "fail": -0.10,
}
MISCONCEPTION_EXTRA = -0.05
DEFAULT_CONFIDENCE = 0.5  # a fresh subjects.json with no graded events yet — genuinely unknown, not "struggling"


def compute(old_confidence, event, misconception=False):
    old_confidence = float(old_confidence)
    if not (0.0 <= old_confidence <= 1.0):
        old_confidence = max(0.0, min(1.0, old_confidence))

    if event not in BASE_DELTA:
        raise ValueError(f"event must be one of {tuple(BASE_DELTA)}, got {event!r}")

    deltas_applied = []

    def _apply(confidence, delta):
        if delta > 0:
            actual = delta * (1.0 - confidence)
        elif delta < 0:
            actual = delta * confidence
        else:
            actual = 0.0
        return max(0.0, min(1.0, confidence + actual)), actual

    confidence = old_confidence
    d = BASE_DELTA[event]
    confidence, actual = _apply(confidence, d)
    deltas_applied.append({"reason": event, "base_delta": d, "actual_delta": round(actual, 4)})

    if misconception:
        confidence, actual = _apply(confidence, MISCONCEPTION_EXTRA)
        deltas_applied.append({"reason": "misconception_extra", "base_delta": MISCONCEPTION_EXTRA, "actual_delta": round(actual, 4)})

    return {
        "old_confidence": round(old_confidence, 4),
        "new_confidence": round(confidence, 4),
        "deltas_applied": deltas_applied,
    }


def _load(path):
    return state.load(path, "subjects")


def _save(path, data):
    state.save(path, data, "subjects")


@ledger.logged("confidence_update.py", "subjects_path")
@filelock.locked("subjects_path")
def apply(subjects_path, event, current_slot, misconception=False):
    """Read-modify-write: loads the current confidence, computes the new
    value with compute(), writes it back into subjects.json, and logs the
    event to sqlite_store. This is the script actually owning the write —
    see the module docstring for why that matters."""
    d = _load(subjects_path)
    old_confidence = d.get("confidence", DEFAULT_CONFIDENCE)
    result = compute(old_confidence, event, misconception)
    d["confidence"] = result["new_confidence"]
    allowed, cstatus = consent.check(subjects_path, consent.SIGNAL)
    if not allowed:
        result.update(consent.skipped(cstatus, consent.SIGNAL))
        return result
    _save(subjects_path, d)

    total_delta = round(result["new_confidence"] - result["old_confidence"], 4)
    sqlite_result = sqlite_store.log_confidence_event(
        subjects_path, event, misconception, total_delta, result["new_confidence"], current_slot
    )

    result["written"] = True
    result["sqlite"] = sqlite_result
    return result


def main():
    args = sys.argv[1:]
    misconception = "--misconception" in args
    args = [a for a in args if a != "--misconception"]

    # Back-compat: no recognized subcommand as args[0] means the old
    # positional form (<old_confidence> <event>), still supported as an
    # implicit "compute".
    if args and args[0] not in ("compute", "apply"):
        args = ["compute"] + args

    if not args:
        print(json.dumps({"error": "usage: confidence_update.py compute <old_confidence> <event> [--misconception] | apply <subjects.json> <event> <current_slot> [--misconception]"}))
        sys.exit(2)

    cmd = args[0]
    try:
        if cmd == "compute":
            if len(args) != 3:
                print(json.dumps({"error": "usage: confidence_update.py compute <old_confidence> <event: pass_clean|pass_remediated|fail> [--misconception]"}))
                sys.exit(2)
            old_confidence, event = args[1], args[2]
            result = compute(old_confidence, event, misconception)
        elif cmd == "apply":
            if len(args) != 4:
                print(json.dumps({"error": "usage: confidence_update.py apply <subjects.json> <event: pass_clean|pass_remediated|fail> <current_slot> [--misconception]"}))
                sys.exit(2)
            subjects_path, event, current_slot = args[1], args[2], args[3]
            result = apply(subjects_path, event, current_slot, misconception)
        else:
            print(json.dumps({"error": f"unknown subcommand {cmd!r}, expected compute|apply"}))
            sys.exit(2)
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        sys.exit(1)
    except ValueError as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(2)
    sys.exit(cli.emit(result))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    main()
