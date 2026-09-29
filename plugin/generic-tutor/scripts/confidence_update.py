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

Usage:
    python3 confidence_update.py <old_confidence> <event: pass_clean|pass_remediated|fail> [--misconception]

Output: JSON to stdout with the new confidence value. This script never
reads or writes a file — same as review_math.py, the caller (course-runner,
at the point syllabus_status is written) reads the old value from
subjects/<course_id>.json, calls this, and writes the returned value back.
"""
import json
import sys

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


def main():
    args = sys.argv[1:]
    misconception = "--misconception" in args
    args = [a for a in args if a != "--misconception"]
    if len(args) != 2:
        print(json.dumps({"error": "usage: confidence_update.py <old_confidence> <event: pass_clean|pass_remediated|fail> [--misconception]"}))
        sys.exit(2)
    old_confidence, event = args
    try:
        result = compute(old_confidence, event, misconception)
    except ValueError as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(2)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
