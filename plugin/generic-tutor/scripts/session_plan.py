#!/usr/bin/env python3
"""
session_plan.py -- how a session fits the time the learner said they have, and where it may safely stop (L-20). Read-only.

    python3 session_plan.py <learner_dir> [--elapsed MINUTES] [--phase lesson|practice|test] [--available MINUTES]

`availability.session_minutes` is collected at intake and until now nothing used it. The tutor has no clock, so the minutes come from the
learner ("about 20 minutes in") or from `--available` when they say today is different; this script turns them into a plan and an answer.

  phase_minutes   the session split lesson / practice / test (35 / 40 / 25 per cent; the test never gets less than 8 minutes)
  remaining       available - elapsed
  advice          continue | wrap_up (5 minutes or less left: finish the current step, record, stop) | over_time (past the time: offer to stop)
                  | stop_before_test (practice is done but the time left is less than a test needs: stop at this point and start the next session with the test)
  stop_points     the places that leave state consistent: after the lesson, after practice, after a test result is recorded.
                  Never mid-test: a test left open is re-presented as the first attempt next time, so it is best finished.
Guidance only: nothing is written and nothing is blocked; the learner can always carry on.
"""
import json
import os
import sys

from tutorlib import cli

DEFAULT_MINUTES = 45
SPLIT = (("lesson", 0.35), ("practice", 0.40), ("test", 0.25))
TEST_MIN = 8
WRAP_UP_AT = 5
PHASES = ("lesson", "practice", "test")


def plan(available, elapsed=0, phase="lesson"):
    phase_minutes = {k: round(available * share) for k, share in SPLIT}
    phase_minutes["test"] = max(TEST_MIN, phase_minutes["test"])
    remaining = available - elapsed
    if elapsed >= available:
        advice = "over_time"
    elif phase == "practice" and remaining < phase_minutes["test"]:
        advice = "stop_before_test"
    elif remaining <= WRAP_UP_AT:
        advice = "wrap_up"
    else:
        advice = "continue"
    if phase == "test" and advice in ("wrap_up", "over_time"):
        advice = "finish_the_test"                       # a test is never left half done
    return {"available_minutes": available, "elapsed_minutes": elapsed, "remaining": remaining, "phase": phase, "phase_minutes": phase_minutes,
            "can_start_test": remaining >= phase_minutes["test"], "advice": advice,
            "stop_points": ["after the lesson", "after practice", "after a test result is recorded"]}


def run(learner_dir, elapsed=0, phase="lesson", available=None):
    if phase not in PHASES:
        return {"error": f"phase must be one of {PHASES}"}
    defaulted = False
    if available is None:
        try:
            with open(os.path.join(learner_dir, "student_profile.json"), encoding="utf-8") as f:
                available = ((json.load(f).get("availability") or {}).get("session_minutes"))
        except (OSError, ValueError) as e:
            return {"error": f"{type(e).__name__}: cannot read student_profile.json in {learner_dir}"}
        if not isinstance(available, int) or isinstance(available, bool) or available <= 0:
            available, defaulted = DEFAULT_MINUTES, True
    return {**plan(available, elapsed, phase), "minutes_defaulted": defaulted}


def main(argv):
    args, opts = [], {}
    i = 0
    while i < len(argv):
        if argv[i] in ("--elapsed", "--phase", "--available"):
            if i + 1 >= len(argv):
                print(json.dumps({"error": f"{argv[i]} needs a value"}))
                return 2
            opts[argv[i]] = argv[i + 1]
            i += 2
        else:
            args.append(argv[i])
            i += 1
    if len(args) != 1:
        print(json.dumps({"error": "usage: session_plan.py <learner_dir> [--elapsed MINUTES] [--phase lesson|practice|test] [--available MINUTES]"}))
        return 2
    try:
        elapsed = int(opts.get("--elapsed", 0))
        available = int(opts["--available"]) if "--available" in opts else None
    except ValueError:
        print(json.dumps({"error": "minutes must be whole numbers"}))
        return 2
    if elapsed < 0 or (available is not None and available <= 0):
        print(json.dumps({"error": "minutes must be positive"}))
        return 2
    return cli.emit(run(args[0], elapsed, opts.get("--phase", "lesson"), available))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
