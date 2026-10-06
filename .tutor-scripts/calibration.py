#!/usr/bin/env python3
"""
calibration.py -- does the learner's own sense of "I'll pass this" match what happens? (L-15) Opt-in, signal-class.

    python3 calibration.py optin  <subjects.json> yes|no
    python3 calibration.py record <subjects.json> <stage_id> <rating 1-5> <pass|fail> <today YYYY-MM-DD>
    python3 calibration.py report <subjects.json>

`confidence` (confidence_update.py) is the SYSTEM's number about the learner. Calibration is the other half: before a stage test the learner is
asked "how sure are you of passing, 1 to 5?" (only if they said yes to `optin`), and the rating is stored with the result.
`report` compares them: a rating maps to a probability (1 -> 0.1, 2 -> 0.3, 3 -> 0.5, 4 -> 0.7, 5 -> 0.9); `bias` is mean predicted minus the real pass rate.
  verdict   too_few (fewer than 5 rated tests) | overconfident (bias >= +0.2) | underconfident (bias <= -0.2) | well_calibrated
Stored in the subjects file as `calibration: {enabled, entries[{stage_id, rating, result, on}]}`, newest 50 kept, one entry per stage and result
(a repeated call replaces it). Signal-class: written only under `granted` consent; atomic, locked, ledgered. It never changes `confidence`,
gates or grades; it is something to talk about with the learner, in their own terms.
"""
import json
import sys

from tutorlib import cli, consent, filelock, ledger, state

PROB = {1: 0.1, 2: 0.3, 3: 0.5, 4: 0.7, 5: 0.9}
MIN_ENTRIES = 5
BIAS = 0.2
KEEP = 50


def _cal(data):
    c = data.get("calibration")
    return c if isinstance(c, dict) else {"enabled": False, "entries": []}


def _write(path, mutate, action, detail):
    allowed, status = consent.check(path, consent.SIGNAL)
    if not allowed:
        return {"written": False, **consent.skipped(status, consent.SIGNAL)}
    with filelock.file_lock(path):
        data = state.load(path, "subjects")
        cal = _cal(data)
        err = mutate(cal)
        if err:
            return {"error": err}
        data["calibration"] = cal
        state.save(path, data, "subjects")
    ledger.record(path, "calibration.py", action, data.get("course_id"), True, None, detail)
    return {"written": True, "enabled": cal["enabled"], "entries": len(cal["entries"])}


def optin(path, answer):
    if answer not in ("yes", "no"):
        return {"error": "answer must be yes or no"}

    def m(cal):
        cal["enabled"] = answer == "yes"
    return _write(path, m, "calibration_optin", {"enabled": answer == "yes"})


def record(path, stage_id, rating, result, today):
    try:
        rating = int(rating)
    except (TypeError, ValueError):
        return {"error": "rating must be a whole number from 1 to 5"}
    if rating not in PROB:
        return {"error": "rating must be a whole number from 1 to 5"}
    if result not in ("pass", "fail"):
        return {"error": "result must be pass or fail"}

    def m(cal):
        if not cal.get("enabled"):
            return "self-rating is not switched on for this course (the learner has not said yes)"
        cal["entries"] = [e for e in cal["entries"] if not (e["stage_id"] == stage_id and e["result"] == result)]
        cal["entries"].append({"stage_id": stage_id, "rating": rating, "result": result, "on": today})
        cal["entries"] = cal["entries"][-KEEP:]
    return _write(path, m, "calibration_record", {"stage_id": stage_id, "rating": rating, "result": result})


def report(path):
    cal = _cal(state.load(path, "subjects"))
    es = [e for e in cal["entries"] if isinstance(e, dict) and e.get("rating") in PROB]
    out = {"enabled": bool(cal.get("enabled")), "n": len(es)}
    if len(es) < MIN_ENTRIES:
        return {**out, "verdict": "too_few"}
    predicted = sum(PROB[e["rating"]] for e in es) / len(es)
    actual = sum(1 for e in es if e["result"] == "pass") / len(es)
    bias = round(predicted - actual, 3)
    verdict = "overconfident" if bias >= BIAS else "underconfident" if bias <= -BIAS else "well_calibrated"
    return {**out, "mean_predicted": round(predicted, 3), "pass_rate": round(actual, 3), "bias": bias, "verdict": verdict}


def main(argv):
    try:
        if len(argv) == 3 and argv[0] == "optin":
            return cli.emit(optin(argv[1], argv[2]))
        if len(argv) == 6 and argv[0] == "record":
            return cli.emit(record(*argv[1:]))
        if len(argv) == 2 and argv[0] == "report":
            return cli.emit(report(argv[1]))
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1
    print(json.dumps({"error": "usage: calibration.py optin <subjects.json> yes|no | record <subjects.json> <stage_id> <1-5> <pass|fail> <today> | report <subjects.json>"}))
    return 2


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
