#!/usr/bin/env python3
"""
profile_set.py -- change one setting in a learner's student_profile.json, safely (C-11).

    python3 profile_set.py <student_profile.json> <field> <value> <today YYYY-MM-DD> [--dry-run]

Until now `/profile` edits were free-hand JSON edits by the model. This script is the one write path for the settings a learner can
change, with a whitelist, validation, atomic write, file lock, ledger line, consent handling and a before/after report:

  preferences.style                         brief | detailed
  preferences.tone                          neutral | friendly | formal | playful
  preferences.accessibility.dyslexia_mode   true | false
  preferences.accessibility.plain_language_mode   true | false
  preferences.accessibility.screen_reader_mode    true | false
  learning_signals.pace                     fast | standard | slow
  learning_signals.working_memory_support_needed | verbal_load_sensitivity | spatial_support_needed    none | some | significant
  learning_signals.notes                    text (<= 500 characters)
  availability.sessions_per_week            1-21        availability.session_minutes   5-240
  roster.max_incomplete_courses             1-20 (lowering it never removes a course; it only limits future additions)
  goals                                     JSON list of strings (<= 10 items, each <= 120 characters)
  identity.display_name | identity.education_level    text (<= 80)        identity.locale   text (<= 20)
  identity.home_language                    text (<= 40; optional, the learner's first language)
  capabilities.share_images                 true | false   (stored as {declared, on}; then run apply_capabilities.py for each course)
  consent.status                            granted | limited | revoked   (the learner's own control: always allowed)

Anything else is refused ("not a setting"). Consent rules: `consent.status` can always be changed; learning_signals.* are learner
signals (kept under `granted` only); every other setting is progress-class (kept under `granted` and `limited`); `revoked` stores
nothing else. The result is validated against the student_profile JSON Schema before it is written.
"""
import datetime
import json
import sys

from tutorlib import cli, consent, filelock, ledger, schema, state

ENUMS = {
    "preferences.style": ("brief", "detailed"),
    "preferences.tone": ("neutral", "friendly", "formal", "playful"),
    "learning_signals.pace": ("fast", "standard", "slow"),
    "learning_signals.working_memory_support_needed": ("none", "some", "significant"),
    "learning_signals.verbal_load_sensitivity": ("none", "some", "significant"),
    "learning_signals.spatial_support_needed": ("none", "some", "significant"),
    "consent.status": ("granted", "limited", "revoked"),
}
BOOLS = {"preferences.accessibility.dyslexia_mode", "preferences.accessibility.plain_language_mode", "preferences.accessibility.screen_reader_mode", "capabilities.share_images"}
INTS = {"availability.sessions_per_week": (1, 21), "availability.session_minutes": (5, 240), "roster.max_incomplete_courses": (1, 20)}
TEXTS = {"learning_signals.notes": 500, "identity.display_name": 80, "identity.education_level": 80, "identity.locale": 20, "identity.home_language": 40}
ALLOWED = set(ENUMS) | BOOLS | set(INTS) | set(TEXTS) | {"goals"}


def parse_value(field, raw):
    if field in ENUMS:
        if raw not in ENUMS[field]:
            raise ValueError(f"{field} must be one of {list(ENUMS[field])}")
        return raw
    if field in BOOLS:
        if raw.lower() not in ("true", "false"):
            raise ValueError(f"{field} must be true or false")
        return raw.lower() == "true"
    if field in INTS:
        lo, hi = INTS[field]
        try:
            n = int(raw)
        except ValueError:
            raise ValueError(f"{field} must be a whole number") from None
        if not lo <= n <= hi:
            raise ValueError(f"{field} must be between {lo} and {hi}")
        return n
    if field in TEXTS:
        if len(raw) > TEXTS[field]:
            raise ValueError(f"{field} must be at most {TEXTS[field]} characters")
        return raw
    if field == "goals":
        try:
            goals = json.loads(raw)
        except ValueError:
            raise ValueError("goals must be a JSON list of strings") from None
        if not (isinstance(goals, list) and len(goals) <= 10 and all(isinstance(g, str) and 0 < len(g) <= 120 for g in goals)):
            raise ValueError("goals must be a JSON list of at most 10 non-empty strings of at most 120 characters")
        return goals
    raise ValueError(f"{field!r} is not a setting this tool changes (allowed: {sorted(ALLOWED)})")


def _get(d, dotted):
    for part in dotted.split("."):
        if not isinstance(d, dict) or part not in d:
            return None
        d = d[part]
    return d


def _set(d, dotted, value):
    parts = dotted.split(".")
    for part in parts[:-1]:
        d = d.setdefault(part, {})
    d[parts[-1]] = value


@ledger.logged("profile_set.py", "profile_path")
@filelock.locked("profile_path")
def set_value(profile_path, field, raw_value, today_iso, dry_run=False):
    try:
        datetime.date.fromisoformat(today_iso)
        value = parse_value(field, raw_value)
    except ValueError as e:
        return {"error": str(e)}
    data = state.load(profile_path, "student_profile")
    old = _get(data, field)
    stored = {"declared": value, "on": today_iso} if field == "capabilities.share_images" else value
    _set(data, field, stored)
    data["last_updated"] = today_iso
    problems = schema.validate(data, "student_profile")
    if problems:
        return {"error": f"the result would not be a valid profile: {problems[:3]}"}
    result = {"field": field, "old": old, "new": stored}
    if field == "capabilities.share_images":
        result["next_step"] = "run apply_capabilities.py for each enrolled course that has practical stages, then tell the learner which stages unlocked or are withheld"
    if field == "roster.max_incomplete_courses":
        result["note"] = "lowering the cap never removes a course; it only limits future /add-course"
    if dry_run:
        return {**result, "dry_run": True, "written": False}
    if field != "consent.status":
        kind = consent.SIGNAL if field.startswith("learning_signals.") else consent.PROGRESS
        allowed, status = consent.check(profile_path, kind)
        if not allowed:
            return {**result, **consent.skipped(status, kind)}
    state.save(profile_path, data, "student_profile")
    return {**result, "written": True}


def main(argv):
    args = [a for a in argv if a != "--dry-run"]
    if len(args) != 4:
        print(json.dumps({"error": "usage: profile_set.py <student_profile.json> <field> <value> <today YYYY-MM-DD> [--dry-run]"}))
        return 2
    try:
        return cli.emit(set_value(args[0], args[1], args[2], args[3], "--dry-run" in argv))
    except cli.EXPECTED_ERRORS as e:
        print(json.dumps({"error": f"{type(e).__name__}: {e}"}))
        return 1


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
