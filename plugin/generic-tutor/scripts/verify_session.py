#!/usr/bin/env python3
"""
verify_session.py -- did the model make all the state writes a session implies? (V-03, V-06)

    python3 verify_session.py <learner_dir> [--slot N | --previous]

Reads `<learner_dir>/.session_ledger.jsonl` (written by every state-changing script) and checks
the lines for one session (= one session_slot; default the current slot, `--previous` = slot-1,
which is what /run uses to audit the LAST session) against rules of the form "A implies B":

  stage-pass-confidence   a stage pass was recorded but no pass_clean/pass_remediated confidence update followed
  stage-pass-cards        a stage pass was recorded but the course's review deck has no card for that stage
                          (stage-recap did not seed it)
  stage-fail-confidence   a stage fail was recorded without a `fail` confidence update
  stage-fail-remediation  a stage fail was recorded without a remediation attempt
  confidence-duplicated   more confidence updates than graded results (a retry applied twice)
  stage-result-duplicated the same stage result recorded twice in one session
  no-slot-advance         writes happened in a session whose slot was never advanced by /run

It reports; it NEVER writes grades or repairs state -- a missing write is shown to the learner and
decided by them (profile-kernel /run). Consent-skipped writes are not counted as writes.
Output: {slot, ledger_entries, ok, findings[{rule, severity, course_id, stage_id, message}]}. Exit 0.
"""
import json
import os
import sys

from tutorlib import cli, ledger

PASS_EVENTS = ("pass_clean", "pass_remediated")


def _deck_has_stage(learner_dir, course_id, stage_id):
    path = os.path.join(learner_dir, "subjects", f"{course_id}_review_deck.json")
    try:
        with open(path, encoding="utf-8") as f:
            cards = json.load(f).get("cards", [])
    except (OSError, ValueError):
        return False
    return any(isinstance(c, dict) and c.get("stage_id") == stage_id for c in cards)


def verify(entries, learner_dir, slot):
    mine = [e for e in entries if e.get("slot") == slot and "corrupt" not in e]
    wrote = [e for e in mine if e.get("written")]
    findings = []

    def add(rule, severity, course_id, stage_id, message):
        findings.append({"rule": rule, "severity": severity, "course_id": course_id, "stage_id": stage_id, "message": message})

    results = [e for e in wrote if e["script"] == "record_stage_result.py"]
    confs = [e for e in wrote if e["script"] == "confidence_update.py"]
    rems = [e for e in wrote if e["script"] == "remediation_state.py" and e["action"] == "record"]

    seen = {}
    for r in results:
        d, cid = r.get("detail", {}), r.get("course_id")
        stage, res = d.get("stage_id"), d.get("result")
        key = (cid, stage, res)
        seen[key] = seen.get(key, 0) + 1
        if seen[key] == 2:
            add("stage-result-duplicated", "warning", cid, stage, f"{res} for {stage} was recorded twice in this session")
        course_confs = [c for c in confs if c.get("course_id") == cid]
        if res == "pass":
            if not any(c["detail"].get("event") in PASS_EVENTS for c in course_confs):
                add("stage-pass-confidence", "missing", cid, stage,
                    f"{stage} was recorded as passed but confidence was not updated (confidence_update.py apply … pass_clean|pass_remediated)")
            if not _deck_has_stage(learner_dir, cid, stage):
                add("stage-pass-cards", "missing", cid, stage,
                    f"{stage} was recorded as passed but the review deck has no cards for it (stage-recap did not seed the deck)")
        elif res == "fail":
            if not any(c["detail"].get("event") == "fail" for c in course_confs):
                add("stage-fail-confidence", "missing", cid, stage,
                    f"{stage} was recorded as failed but confidence was not updated (confidence_update.py apply … fail)")
            if not any(m.get("course_id") == cid and m["detail"].get("stage_id") == stage for m in rems):
                add("stage-fail-remediation", "missing", cid, stage,
                    f"{stage} was recorded as failed but no remediation attempt was recorded (remediation_state.py record)")

    for cid in sorted({r.get("course_id") for r in results}):
        graded = sum(1 for r in results if r.get("course_id") == cid)
        updates = sum(1 for c in confs if c.get("course_id") == cid)
        if updates > graded:
            add("confidence-duplicated", "warning", cid, None, f"{updates} confidence updates for {graded} graded result(s)")

    if wrote and not any(e["script"] == "slot_advance.py" and e.get("written") for e in mine):
        add("no-slot-advance", "warning", None, None, "state was written in a session whose slot was never advanced (/run not executed this session?)")

    return findings


def main(argv):
    args = list(argv)
    mode, slot_arg = "current", None
    if "--previous" in args:
        args.remove("--previous")
        mode = "previous"
    if "--slot" in args:
        i = args.index("--slot")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--slot needs a number"}))
            return 2
        slot_arg = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1:
        print(json.dumps({"error": "usage: verify_session.py <learner_dir> [--slot N | --previous]"}))
        return 2
    learner_dir = args[0]
    try:
        with open(os.path.join(learner_dir, "student_profile.json"), encoding="utf-8") as f:
            current = int(json.load(f).get("session_slot", 0))
        slot = int(slot_arg) if slot_arg is not None else (current - 1 if mode == "previous" else current)
    except (OSError, ValueError) as e:
        return cli.emit({"error": f"{type(e).__name__}: {e}"})
    entries = ledger.read(learner_dir)
    findings = verify(entries, learner_dir, slot)
    return cli.emit({"slot": slot, "ledger_entries": sum(1 for e in entries if e.get("slot") == slot),
                     "ok": not any(f["severity"] == "missing" for f in findings), "findings": findings})


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
