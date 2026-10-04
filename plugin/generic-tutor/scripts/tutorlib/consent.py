"""
Consent enforcement in code (E-05).

profile-kernel defines three consent states for a learner:

  granted  everything persists
  limited  only progress and scheduling bookkeeping persist; learner "signals"
           (errors, confidence, mastery, summaries, history) are used in the
           session but never written
  revoked  nothing is written

Until now that was prose, honoured by the model and by exactly one script.
Every state-writing script now asks `check(path, kind)` before it writes.

Write kinds:
  PROGRESS    syllabus_status / current_stage / phase, roster state, remediation
              attempt counters (needed so a stage cannot loop forever), capability
              unlocks  -> allowed under granted, limited
  SCHEDULING  session_slot, review card interval/ease/lapses/due -> granted, limited
  SIGNAL      error_patterns, confidence, item_mastery, history DB rows,
              summaries -> granted only

Finding the profile: for a path inside `<learner>/subjects/` the profile is
`<learner>/student_profile.json`; for `<learner>/student_profile.json` itself
it is that file. A path with no profile beside it (bare fixtures, a course
folder) is treated as granted. A profile whose consent block cannot be read or
holds an unknown status fails CLOSED (treated as revoked).
"""
import json
import os

PROGRESS = "progress"
SCHEDULING = "scheduling"
SIGNAL = "signal"

_ALLOWED = {
    "granted": {PROGRESS, SCHEDULING, SIGNAL},
    "limited": {PROGRESS, SCHEDULING},
    "revoked": set(),
}


def profile_path_for(path):
    ap = os.path.abspath(path)
    d = os.path.dirname(ap)
    if os.path.basename(ap) == "student_profile.json":
        return ap
    if os.path.basename(d) == "subjects":
        return os.path.join(os.path.dirname(d), "student_profile.json")
    cand = os.path.join(d, "student_profile.json")
    return cand if os.path.isfile(cand) else None


def status_for(path):
    """Return 'granted' | 'limited' | 'revoked'. Fails closed on unreadable/unknown."""
    pp = profile_path_for(path)
    if pp is None or not os.path.isfile(pp):
        return "granted"
    try:
        with open(pp, encoding="utf-8") as f:
            status = (json.load(f).get("consent") or {}).get("status", "granted")
    except (OSError, ValueError, AttributeError):
        return "revoked"
    return status if status in _ALLOWED else "revoked"


def check(path, kind):
    """(allowed, status). Callers skip the write when not allowed."""
    status = status_for(path)
    return kind in _ALLOWED[status], status


def skipped(status, kind):
    return {"written": False, "skipped": f"consent {status}: {kind} writes are not persisted"}
