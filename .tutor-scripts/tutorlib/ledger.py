"""
Session ledger (V-01): one JSON line per state-changing script call.

The residual risk the earlier hardening could not close is the model simply NOT calling a script
(DESIGN_NOTES v1.10.0): nothing then records that something should have happened. Every writer
now appends a line to `<learner>/.session_ledger.jsonl`; `verify_session.py` later checks that
the lines for a session form a complete set (a stage pass without its confidence update, for
example, is flagged). Cowork has no hooks (ADR 0001), so this lives inside the scripts.

A line: {"ts", "slot", "script", "action", "course_id", "written", "skipped", "detail"}.
`slot` is the learner's session_slot when the call happened (one session = one slot). The ledger
is operational metadata, not a learner signal: it is written under `granted` and `limited`
consent, never under `revoked`, and never for paths with no learner profile beside them.
"""
import datetime
import functools
import inspect
import json
import os

from tutorlib import consent, filelock

LEDGER_NAME = ".session_ledger.jsonl"
_ARG_KEYS = ("stage_id", "item_id", "event", "result", "cause", "card_id", "correct", "target_state", "misconception")
_RESULT_KEYS = ("action", "written", "skipped", "new_confidence", "resumed", "error", "count")


def ledger_path(any_path):
    pp = consent.profile_path_for(any_path)
    return os.path.join(os.path.dirname(pp), LEDGER_NAME) if pp else None


def _slot(any_path):
    pp = consent.profile_path_for(any_path)
    try:
        with open(pp, encoding="utf-8") as f:
            return int(json.load(f).get("session_slot", 0))
    except (OSError, ValueError, TypeError):
        return None


def record(any_path, script, action, course_id=None, written=True, skipped=None, detail=None, now=None):
    """Append one line. Never raises: a ledger failure must not break the write that already happened."""
    try:
        lp = ledger_path(any_path)
        if lp is None:
            return False
        allowed, _ = consent.check(any_path, consent.SCHEDULING)
        if not allowed:
            return False
        now = now or datetime.datetime.now(datetime.timezone.utc)
        line = {"ts": now.replace(microsecond=0).isoformat().replace("+00:00", "Z"), "slot": _slot(any_path),
                "script": script, "action": action, "course_id": course_id, "written": bool(written),
                "skipped": skipped, "detail": detail or {}}
        with filelock.file_lock(lp):
            with open(lp, "a", encoding="utf-8") as f:
                f.write(json.dumps(line, ensure_ascii=False, sort_keys=True) + "\n")
        return True
    except Exception:  # noqa: BLE001 - deliberately broad, see docstring
        return False


def read(learner_dir):
    lp = os.path.join(learner_dir, LEDGER_NAME)
    if not os.path.isfile(lp):
        return []
    out = []
    with open(lp, encoding="utf-8") as f:
        for raw in f:
            raw = raw.strip()
            if raw:
                try:
                    out.append(json.loads(raw))
                except ValueError:
                    out.append({"corrupt": raw[:200]})
    return out


def _course_id(path):
    base = os.path.basename(path)
    name = base[:-5] if base.endswith(".json") else base
    return name[: -len("_review_deck")] if name.endswith("_review_deck") else name


def logged(script, path_param):
    """Decorator: after the call, append a ledger line describing it (skipped writes are recorded too)."""
    def deco(fn):
        sig = inspect.signature(fn)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            try:
                bound = sig.bind(*args, **kwargs).arguments
                path = bound[path_param]
                if isinstance(result, dict) and "error" not in result:
                    detail = {k: bound[k] for k in _ARG_KEYS if k in bound}
                    detail.update({k: result[k] for k in _RESULT_KEYS if k in result and k not in ("written", "skipped")})
                    record(path, script, fn.__name__, _course_id(path), written=result.get("written", "skipped" not in result),
                           skipped=result.get("skipped"), detail=detail)
            except Exception:  # noqa: BLE001
                pass
            return result
        return wrapper
    return deco
