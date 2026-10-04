#!/usr/bin/env python3
"""
slot_advance.py — the one place the learner's persistent session-slot counter moves.

review-scheduler.md's cards carry `due_at_slot`, and "a card is due whenever the
learner's current session-slot count has reached or passed it" - but before this
script no field anywhere stored that count, so every session had to guess what
slot it was on. The counter lives in the learner's own student_profile.json as
`session_slot` (a plain integer; absent means 0, so no schema migration is
needed). It advances by exactly 1 per tutoring session, at /run activation -
never per course, never per /review call, never on a date.

Double-/run guard: /run can be typed twice in one sitting (or re-run after a
disconnect). To keep that from counting as two sessions, the script records
`session_slot_advanced_at` (an ISO-8601 UTC timestamp, pure bookkeeping - it is
never used to place anything on a calendar) and skips if the last advance was
less than --min-gap-minutes ago (default 180). A stamp in the future (a clock that
was once wrong) is treated like a missing one, never as "recent", so it cannot freeze
the counter. Pass --min-gap-minutes 0 to
disable the guard.

Usage:
    python3 slot_advance.py <student_profile.json path> [--min-gap-minutes N]

Writes the file back in place (all other fields preserved) and prints
{"previous_slot": N, "current_slot": N+1}. Skips, with a reason, when
consent.status is "revoked" (nothing may be written) or when inside the
double-/run window; either way "current_slot" is still reported.
"""
import argparse
import datetime
import json
from tutorlib import atomic_io, consent, filelock

DEFAULT_MIN_GAP_MINUTES = 180


def _now():
    return datetime.datetime.now(datetime.timezone.utc)


@filelock.locked("path")
def advance(path, min_gap_minutes=DEFAULT_MIN_GAP_MINUTES, now=None):
    now = now or _now()
    with open(path, "r", encoding="utf-8") as f:
        profile = json.load(f)
    previous = int(profile.get("session_slot", 0))
    allowed, cstatus = consent.check(path, consent.SCHEDULING)
    if not allowed:
        return {"skipped": f"consent {cstatus}", "current_slot": previous}

    last = profile.get("session_slot_advanced_at")
    if min_gap_minutes > 0 and last:
        try:
            last_dt = datetime.datetime.fromisoformat(last.replace("Z", "+00:00"))
            if last_dt.tzinfo is None:
                last_dt = last_dt.replace(tzinfo=datetime.timezone.utc)
            elapsed = now - last_dt
            # Only a stamp in the recent PAST means "same sitting". A stamp in the future
            # (a clock that was once wrong) is not evidence of anything: treat it exactly like
            # an unparseable one - advance, and overwrite it with a sane stamp - rather than
            # freezing the counter until the clock catches up.
            if datetime.timedelta(0) <= elapsed < datetime.timedelta(minutes=min_gap_minutes):
                return {"skipped": "already advanced this sitting", "current_slot": previous}
        except ValueError:
            pass  # unparseable stamp: treat as absent rather than blocking the counter forever

    profile["session_slot"] = previous + 1
    profile["session_slot_advanced_at"] = now.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    atomic_io.write_json(path, profile)
    return {"previous_slot": previous, "current_slot": previous + 1}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("profile_path")
    ap.add_argument("--min-gap-minutes", type=int, default=DEFAULT_MIN_GAP_MINUTES)
    args = ap.parse_args()
    print(json.dumps(advance(args.profile_path, args.min_gap_minutes), indent=2))


if __name__ == "__main__":
    main()
