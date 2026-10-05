#!/usr/bin/env python3
"""
profile_init.py -- create a new learner profile (the safe write path for /add-profile and first-ever load).

    python3 profile_init.py <profile_root> <user_id> <today YYYY-MM-DD>  < answers.json

`answers.json` (on stdin, so learner words never pass through a shell argument) is a flat object whose keys are the same dotted
settings profile_set.py accepts, e.g.
    {"identity.education_level": "Year 11", "preferences.style": "brief", "availability.sessions_per_week": 3,
     "availability.session_minutes": 45, "roster.max_incomplete_courses": 2, "capabilities.share_images": true,
     "learning_signals.pace": "slow", "goals": ["GCSE maths"]}
Unknown keys are refused. Values are validated by the same rules as profile_set.py. Missing settings are simply left unset (the
intake says: "leave the rest unset rather than guessing"). The new profile starts with schema_version 2, `consent.status: granted`,
`session_slot: 0`, `highest_level_cleared: 0` and a `subjects/` folder. It refuses an invalid id, a symlinked or existing learner
folder, and writes the profile atomically; the result is validated against the student_profile JSON Schema.
"""
import json
import os
import sys

import profile_set
from tutorlib import atomic_io, cli, ledger, paths, schema


def create(profile_root, user_id, today_iso, answers):
    try:
        d = paths.learner_dir(profile_root, user_id)
    except ValueError as e:
        return {"created": False, "error": str(e)}
    if os.path.exists(d):
        return {"created": False, "error": f"a learner folder for {user_id!r} already exists; use /run {user_id} or pick another id"}
    if not isinstance(answers, dict):
        return {"created": False, "error": "answers must be a JSON object of dotted setting names to values"}
    profile = {"schema_version": 2, "learner_id": user_id, "consent": {"status": "granted"}, "session_slot": 0,
               "highest_level_cleared": 0, "last_updated": today_iso}
    for field, value in answers.items():
        raw = json.dumps(value) if isinstance(value, list) else str(value).lower() if isinstance(value, bool) else str(value)
        try:
            parsed = profile_set.parse_value(field, raw)
        except ValueError as e:
            return {"created": False, "error": str(e)}
        if field == "consent.status":
            return {"created": False, "error": "consent is set separately: a new profile starts as 'granted'; change it with /profile"}
        profile_set._set(profile, field, {"declared": parsed, "on": today_iso} if field == "capabilities.share_images" else parsed)
    problems = schema.validate(profile, "student_profile")
    if problems:
        return {"created": False, "error": f"the profile would not be valid: {problems[:3]}"}
    os.makedirs(os.path.join(d, "subjects"))
    path = os.path.join(d, "student_profile.json")
    atomic_io.write_json(path, profile)
    ledger.record(path, "profile_init.py", "create", None, True, None, {"user_id": user_id})
    return {"created": True, "user_id": user_id, "profile": path, "set": sorted(answers)}


def main(argv):
    if len(argv) != 3:
        print(json.dumps({"error": "usage: profile_init.py <profile_root> <user_id> <today YYYY-MM-DD>  (answers as JSON on stdin)"}))
        return 2
    try:
        raw = sys.stdin.read().strip()
        answers = json.loads(raw) if raw else {}
    except ValueError:
        return cli.emit({"created": False, "error": "stdin is not valid JSON"})
    try:
        import datetime
        datetime.date.fromisoformat(argv[2])
    except ValueError:
        return cli.emit({"created": False, "error": "today must be YYYY-MM-DD"})
    return cli.emit(create(argv[0], argv[1], argv[2], answers))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
