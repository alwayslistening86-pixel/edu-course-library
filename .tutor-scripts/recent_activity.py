#!/usr/bin/env python3
"""
recent_activity.py -- "what has the tutor written about me lately?" in plain language (V-10). Read-only.

    python3 recent_activity.py <learner_dir> [--last N]        (default 15, newest first)

Turns the learner's write ledger (`.session_ledger.jsonl`) into sentences a learner can check: which progress file or deck was
updated, in which session, for which course, and which writes were NOT saved because of the consent setting. The ledger holds ids
and numbers only (never answers, notes or free text), so this shows no more than the ledger does. Nothing is written.
"""
import json
import sys

from tutorlib import cli, ledger

# (script, function) -> template; {course}, {stage}, {item}, {cause}, {result}, {event} come from the ledger detail
_TEMPLATES = {
    ("record_stage_result.py", "apply"): "Recorded a {result} for stage {stage} in {course}.",
    ("error_log.py", "append"): "Logged a mistake on item {item} ({cause}) in {course}.",
    ("error_log.py", "resolve"): "Marked mistakes on item {item} as resolved in {course}.",
    ("item_mastery.py", "observe"): "Updated your mastery estimate for item {item} in {course}.",
    ("confidence_update.py", "apply"): "Updated your confidence in {course} after a {event}.",
    ("remediation_state.py", "record"): "Counted a remediation attempt on stage {stage} in {course}.",
    ("remediation_state.py", "reset"): "Cleared the remediation count for stage {stage} in {course}.",
    ("review_math.py", "apply"): "Rescheduled a review card in {course}.",
    ("deck_add.py", "add"): "Added review cards to the {course} deck.",
    ("record_grading.py", "record"): "Kept the per-criterion marks for a {course} stage test (no answer text).",
    ("deck_add.py", "retire"): "Retired review cards from the {course} deck.",
    ("session_state.py", "set_phase"): "Changed the phase of your current stage in {course}.",
    ("session_state.py", "set_roster"): "Changed the study state of {course}.",
    ("session_state.py", "set_exam"): "Changed the exam status of {course}.",
    ("session_state.py", "ack_notice"): "Noted that you had read a course notice for {course}.",
    ("session_state.py", "write_note"): "Saved a short summary of your last session in {course}.",
    ("plan_target.py", "set_target"): "Saved your target date for {course}.",
    ("plan_target.py", "clear_target"): "Removed your target date for {course}.",
    ("goal_map.py", "set_goal"): "Saved which topics one of your goals means in {course}.",
    ("goal_map.py", "clear_goal"): "Removed a goal's topic mapping in {course}.",
    ("record_mock.py", "record"): "Saved a mock-paper result for {course}.",
    ("practice_pick.py", "mark_used"): "Noted which practice question you were given in {course}.",
    ("resume_enrollment.py", "resume"): "Resumed {course}.",
    ("slot_advance.py", "advance"): "Counted this as a new study session.",
    ("profile_set.py", "set_value"): "Changed a setting in your profile.",
}


def sentence(entry):
    d = entry.get("detail") or {}
    key = (entry.get("script"), entry.get("action"))
    text = _TEMPLATES.get(key)
    course = entry.get("course_id") or "your course"
    if text is None:
        text = f"{entry.get('script', 'A script')} updated something ({entry.get('action', 'write')})."
    text = text.format(course=course, stage=d.get("stage_id", "?"), item=d.get("item_id", "?"), cause=d.get("cause", "unknown cause"),
                       result=d.get("result", "result"), event=(d.get("event") or "result").replace("_", " "))
    if not entry.get("written", True):
        why = entry.get("skipped") or "not saved"
        text += f" It was NOT saved ({why})."
    return text


def build(learner_dir, last=15):
    entries = ledger.read(learner_dir)
    shown = [e for e in entries if "corrupt" not in e][-last:][::-1]
    return {"total_writes_logged": len(entries), "showing": len(shown),
            "activity": [{"session": e.get("slot"), "when": e.get("ts"), "text": sentence(e)} for e in shown],
            "note": "Only ids and numbers are logged, never your answers or messages."}


def main(argv):
    last = 15
    if "--last" in argv:
        i = argv.index("--last")
        try:
            last = max(1, int(argv[i + 1]))
        except (IndexError, ValueError):
            print(json.dumps({"error": "--last needs a positive integer"}))
            return 2
        del argv[i:i + 2]
    if len(argv) != 1:
        print(json.dumps({"error": "usage: recent_activity.py <learner_dir> [--last N]"}))
        return 2
    return cli.emit(build(argv[0], last))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
