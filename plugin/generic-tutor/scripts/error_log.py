#!/usr/bin/env python3
"""
error_log.py — deterministic bookkeeping for `error_patterns`, a field every
skill in this plugin references (tutor-core's pacing, course-runner's
remediation, review-scheduler's "a recurring miss surfaces here") but that,
before this script existed, no schema and no code ever actually defined.

The taxonomy this script enforces (`cause`, one of five) is the load-bearing
part — see tutor-core's "Diagnosing before remediating" section for what
each one means and how it changes the response. This script does not
diagnose; classifying *why* an answer was wrong is a real judgment call the
model makes from the exchange, exactly like grading itself. This script only
gives that judgment a durable, structured, queryable shape once it's made —
the same division of labour as gate_check.py (never decides *whether* to
grant a gate, only applies the rule once the facts are known) and
review_math.py (never decides *if* a recall was correct, only computes the
arithmetic that follows).

Each entry, appended to subjects/<course_id>.json's `error_patterns` list:
  {
    "id": "err_2026-09-29_S09_003",
    "stage_id": "S09",
    "item_id": "RM6",
    "source_phase": "practice" | "test",
    "cause": "slip" | "missing_prerequisite" | "misconception" |
             "misapplied_procedure" | "comprehension",
    "misconception_id": "MC-RM6-2" or null,
    "rubric_criterion": "M2" or null,
    "note": "free text — the specific wrong belief or mistake, in the
             model's own words",
    "slot": 214,
    "resolved": false,
    "resolved_at_slot": null
  }

`rubric_criterion` (added alongside the pre-existing `stage_id`/`item_id`)
names the specific rubric.json entry this error was graded against, when the
grading exchange ties to one — an M/A/B tag, a named criterion key, whatever
shape that stage's rubric actually uses. `stage_id` and `item_id` say
*where* and *what*; this says *against which mark* the answer fell down,
which is the level of detail a real cohort-wide rollup (course-auditor) or a
review card (stage-recap) can act on much more precisely than "somewhere in
this stage." Optional — pass `NONE` when the exchange doesn't cleanly tie to
one criterion (a lesson-phase conversational check, say); never invented to
fill the field.

Resolution is the other half of this script's job, and it matters as much
as logging: a later correct, confident recall of the same item flips
`resolved` to true rather than leaving a permanent black mark. Without that
decay, tutor-core's pacing rules would keep treating a learner as weak on
something they've since mastered — `resolve` is not an afterthought command,
it's what keeps this file honest over time.

**Both `append` and `resolve` also feed `item_mastery.py`** — an incorrect
BKT observation on every `append`, a correct one on every `resolve` — so
per-item mastery tracking updates automatically from data this script is
already collecting, rather than needing every teaching turn separately
instrumented for it. See `item_mastery.py`'s own docstring for why BKT, and
why piggy-backing on this signal specifically. This script's return value
includes the resulting `item_mastery` block so the caller sees both effects
of one call without a second script invocation.

Subcommands:
    append  <subjects.json> <stage_id> <item_id> <source_phase> <cause> \
            <misconception_id|NONE> <note> <current_slot> [rubric_criterion|NONE]
    resolve <subjects.json> <item_id> <current_slot> [cause|ANY]
    query   <subjects.json> [stage_id|ALL]

`append`'s output includes `recurring`: true once this exact (item_id, cause)
pair has two or more *unresolved* entries — this is one of diagnostic_gate.py's
own trigger conditions, computed once here rather than re-derived there.

Output: JSON to stdout. Writes the subjects file back in place (append,
resolve only); query is read-only.
"""
import json
import os
import sys
from tutorlib import atomic_io, cli, consent, filelock

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import item_mastery  # noqa: E402
import sqlite_store  # noqa: E402

CAUSES = ("slip", "missing_prerequisite", "misconception", "misapplied_procedure", "comprehension")


def _load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def _save(path, data):
    atomic_io.write_json(path, data)


def _next_id(entries, stage_id, today_iso):
    seq = 1 + sum(1 for e in entries if isinstance(e, dict) and e.get("id", "").startswith(f"err_{today_iso}_{stage_id}_"))
    return f"err_{today_iso}_{stage_id}_{seq:03d}"


@filelock.locked("subjects_path")
def append(subjects_path, stage_id, item_id, source_phase, cause, misconception_id, note, current_slot, rubric_criterion="NONE"):
    if cause not in CAUSES:
        return {"error": f"cause must be one of {CAUSES}, got {cause!r}"}
    if source_phase not in ("practice", "test"):
        return {"error": f"source_phase must be 'practice' or 'test', got {source_phase!r}"}

    d = _load(subjects_path)
    entries = d.setdefault("error_patterns", [])
    if not isinstance(entries, list):
        return {"error": f"error_patterns is not a list in {subjects_path} — needs migrate_schema.py first"}

    today_iso = _today_from_entries_or_env()
    entry_id = _next_id(entries, stage_id, today_iso)
    misc_id = None if misconception_id in (None, "NONE", "") else misconception_id
    criterion = None if rubric_criterion in (None, "NONE", "") else rubric_criterion

    entry = {
        "id": entry_id,
        "stage_id": stage_id,
        "item_id": item_id,
        "source_phase": source_phase,
        "cause": cause,
        "misconception_id": misc_id,
        "rubric_criterion": criterion,
        "note": note,
        "slot": int(current_slot),
        "resolved": False,
        "resolved_at_slot": None,
    }
    entries.append(entry)
    allowed, cstatus = consent.check(subjects_path, consent.SIGNAL)
    if not allowed:
        return {"action": "not_persisted", "entry": entry, **consent.skipped(cstatus, consent.SIGNAL)}
    _save(subjects_path, d)
    sqlite_result = sqlite_store.log_error_event(subjects_path, entry)

    unresolved_same_pair = sum(
        1 for e in entries
        if isinstance(e, dict) and e.get("item_id") == item_id and e.get("cause") == cause and not e.get("resolved")
    )
    cause_count_in_stage = sum(
        1 for e in entries
        if isinstance(e, dict) and e.get("stage_id") == stage_id and e.get("cause") == cause and not e.get("resolved")
    )
    mastery_result = item_mastery.observe(subjects_path, item_id, False, current_slot)
    return {
        "action": "appended",
        "entry": entry,
        "recurring": unresolved_same_pair >= 2,
        "unresolved_same_item_and_cause": unresolved_same_pair,
        "unresolved_same_cause_in_stage": cause_count_in_stage,
        "item_mastery": mastery_result,
        "sqlite": sqlite_result,
    }


@filelock.locked("subjects_path")
def resolve(subjects_path, item_id, current_slot, cause_filter="ANY"):
    d = _load(subjects_path)
    entries = d.get("error_patterns", [])
    if not isinstance(entries, list):
        return {"error": f"error_patterns is not a list in {subjects_path}"}

    resolved_ids = []
    for e in entries:
        if not isinstance(e, dict):
            continue
        if e.get("item_id") != item_id or e.get("resolved"):
            continue
        if cause_filter != "ANY" and e.get("cause") != cause_filter:
            continue
        e["resolved"] = True
        e["resolved_at_slot"] = int(current_slot)
        resolved_ids.append(e["id"])

    mastery_result = None
    sqlite_result = None
    if resolved_ids:
        allowed, cstatus = consent.check(subjects_path, consent.SIGNAL)
        if not allowed:
            return {"action": "not_persisted", "item_id": item_id, "entries_resolved": resolved_ids,
                    "count": len(resolved_ids), **consent.skipped(cstatus, consent.SIGNAL)}
        _save(subjects_path, d)
        mastery_result = item_mastery.observe(subjects_path, item_id, True, current_slot)
        sqlite_result = sqlite_store.resolve_error_events(subjects_path, resolved_ids, current_slot)
    return {
        "action": "resolved",
        "item_id": item_id,
        "entries_resolved": resolved_ids,
        "count": len(resolved_ids),
        "item_mastery": mastery_result,
        "sqlite": sqlite_result,
    }


def query(subjects_path, stage_filter="ALL"):
    d = _load(subjects_path)
    entries = d.get("error_patterns", [])
    if not isinstance(entries, list):
        entries = []
    if stage_filter != "ALL":
        entries = [e for e in entries if isinstance(e, dict) and e.get("stage_id") == stage_filter]

    unresolved = [e for e in entries if isinstance(e, dict) and not e.get("resolved")]
    by_cause = {}
    for e in unresolved:
        by_cause[e.get("cause")] = by_cause.get(e.get("cause"), 0) + 1

    # recurring (item_id, cause) pairs among unresolved entries — the same signal `append` reports live.
    pair_counts = {}
    for e in unresolved:
        key = (e.get("item_id"), e.get("cause"))
        pair_counts[key] = pair_counts.get(key, 0) + 1
    recurring_pairs = [{"item_id": k[0], "cause": k[1], "count": v} for k, v in pair_counts.items() if v >= 2]

    return {
        "stage_filter": stage_filter,
        "total_entries": len(entries),
        "unresolved_count": len(unresolved),
        "unresolved_by_cause": by_cause,
        "recurring_pairs": recurring_pairs,
        "entries": entries,
    }


def _today_from_entries_or_env():
    # error_log.py is always called with today's context already established by the calling skill
    # (course-runner already threads today's ISO date through gate_check.py); rather than take it as
    # yet another positional arg on every call, this reads it the one place a running session always
    # has it available and consistent: the OS clock, in UTC, matching every other ISO date this plugin
    # writes (course.json.last_live_recheck, error_patterns entries elsewhere, change.md).
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).date().isoformat()


def main():
    if len(sys.argv) < 3:
        print(json.dumps({"error": "usage: error_log.py append|resolve|query <subjects.json> ..."}))
        sys.exit(2)
    cmd, subjects_path = sys.argv[1], sys.argv[2]
    try:
        if cmd == "append":
            if len(sys.argv) not in (10, 11):
                print(json.dumps({"error": "usage: error_log.py append <subjects.json> <stage_id> <item_id> <source_phase> <cause> <misconception_id|NONE> <note> <current_slot> [rubric_criterion|NONE]"}))
                sys.exit(2)
            result = append(subjects_path, *sys.argv[3:11])
        elif cmd == "resolve":
            if len(sys.argv) not in (5, 6):
                print(json.dumps({"error": "usage: error_log.py resolve <subjects.json> <item_id> <current_slot> [cause|ANY]"}))
                sys.exit(2)
            cause_filter = sys.argv[5] if len(sys.argv) == 6 else "ANY"
            result = resolve(subjects_path, sys.argv[3], sys.argv[4], cause_filter)
        elif cmd == "query":
            stage_filter = sys.argv[3] if len(sys.argv) > 3 else "ALL"
            result = query(subjects_path, stage_filter)
        else:
            print(json.dumps({"error": f"unknown subcommand {cmd!r}, expected append|resolve|query"}))
            sys.exit(2)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        sys.exit(1)
    sys.exit(cli.emit(result))


if __name__ == "__main__":
    main()
