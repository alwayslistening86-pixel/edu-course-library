#!/usr/bin/env python3
"""
hook_guard.py -- the optional Claude Code hooks for generic-tutor (P-05, P-06, P-07, P-08). Claude Code only; Cowork has no hooks (ADR 0001).

Wired by `hooks/hooks.json`; one script, the event comes from the hook input on stdin (`hook_event_name`). Nothing depends on it: every script
already enforces consent, paths and ownership, so a missing hook costs a safety net, never correctness.

  SessionStart      deploys `.tutor-scripts/` (bootstrap_scripts) when the data root is found, and tells the model who the learners are and to run /run first.
  UserPromptSubmit  remembers the slash command this session is running (teaching or authoring), so the guard knows whether `courses/` is off limits.
  PreToolUse        denies, with a reason that says what to do instead:
                      - editing a script-owned file (student_profile.json, subjects/*.json, review decks, tutor.sqlite3, the session ledger, access.json);
                      - any write under `profile/<id>/` while that learner's consent is `revoked`;
                      - touching another learner's folder than the one this session started with (read, write or Bash);
                      - writing to `courses/` while a teaching command (/continue, /review, /mock ...) is running (/add-course and /audit may).
                    Running a deployed script (`python3 .../.tutor-scripts/<x>.py`) is always allowed: scripts own the writes.
  Stop              runs verify_session for the session's learner and shows what it found (never blocks, never repairs).

Input is JSON on stdin. Output is JSON on stdout (`permissionDecision`, `additionalContext`, `systemMessage`), exit 0. Any error inside the hook allows the call.
"""
import json
import os
import re
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from tutorlib import consent, paths  # noqa: E402

TEACHING = {"continue", "review", "mock", "readiness", "status", "plan", "run", "dashboard", "list-courses", "drop"}
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
OWNED_TOP = {"student_profile.json", ".session_ledger.jsonl"}
BASH_WRITE = re.compile(r"(>>?|\btee\b|\bsed\s+-i|\brm\b|\bmv\b|\bcp\b|\btruncate\b|\bdd\b|\bsqlite3\b|\bln\b)")
PROFILE_REF = re.compile(r"profile/([A-Za-z0-9][A-Za-z0-9._-]*)")
SCRIPT_CALL = re.compile(r"\.tutor-scripts/[\w./-]+\.py")


def _state_path(session_id):
    sid = re.sub(r"[^A-Za-z0-9_.-]", "_", session_id or "none")[:80]
    d = os.path.join(tempfile.gettempdir(), "generic-tutor-hooks")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, sid + ".json")


def load_state(session_id):
    try:
        with open(_state_path(session_id), encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_state(session_id, st):
    try:
        with open(_state_path(session_id), "w", encoding="utf-8") as f:
            json.dump(st, f)
    except OSError:
        pass


def find_root(cwd):
    root = paths.resolve_root()
    if root:
        return root
    d = os.path.abspath(cwd or os.getcwd())
    for _ in range(3):
        if os.path.isdir(os.path.join(d, "courses")) or os.path.isdir(os.path.join(d, "profile")):
            return d
        d = os.path.dirname(d)
    return None


def classify(path, root):
    """(area, learner, owned): where a path sits under the data root."""
    try:
        rel = os.path.relpath(os.path.realpath(path), os.path.realpath(root))
    except ValueError:
        return None, None, False
    parts = rel.split(os.sep)
    if parts[0] == "courses":
        return "courses", None, False
    if parts[0] == "profile" and len(parts) >= 2:
        if parts[1] == "access.json":
            return "profile", None, True
        rest = parts[2:]
        owned = bool(rest) and (rest[0] in OWNED_TOP or rest[0].startswith("tutor.sqlite3")
                                or (rest[0] == "subjects" and len(rest) == 2 and rest[1].endswith(".json")))
        return "profile", parts[1], owned
    return None, None, False


def _deny(reason):
    return {"decision": "deny", "reason": reason}


def decide_path(path, root, st, writing):
    area, learner, owned = classify(path, root)
    if area is None:
        return {"decision": "allow"}
    if learner:
        pinned = st.get("learner")
        if pinned and learner != pinned:
            return _deny(f"This session is working with learner '{pinned}'; '{learner}' is another learner's folder. Leave it alone (or start a new session for them).")
        if writing and consent.status_for(os.path.join(root, "profile", learner, "student_profile.json")) == "revoked":
            return _deny(f"Learner '{learner}' has revoked consent: nothing may be written under their folder.")
    if writing and owned:
        return _deny("This file is written by a script, never by hand. Use the script that owns it (see docs/DATA_MODEL.md), or ask for /doctor if it looks wrong.")
    if writing and area == "courses" and st.get("command") in TEACHING:
        return _deny(f"/{st['command']} is a teaching command and does not edit course files. Course content changes go through /add-course or /audit.")
    return {"decision": "allow", "learner": learner}


def decide_bash(command, root, st):
    command = command.replace("\\", "/")                      # Windows-style paths in a command read the same as forward-slash ones
    learners = set(PROFILE_REF.findall(command))
    pinned = st.get("learner")
    for lid in sorted(learners):
        if pinned and lid != pinned:
            return _deny(f"This session is working with learner '{pinned}'; '{lid}' is another learner's folder.")
    if SCRIPT_CALL.search(command):
        return {"decision": "allow", "learner": next(iter(learners), None) if len(learners) == 1 else None}
    if BASH_WRITE.search(command):
        for lid in learners:
            if consent.status_for(os.path.join(root, "profile", lid, "student_profile.json")) == "revoked":
                return _deny(f"Learner '{lid}' has revoked consent: nothing may be written under their folder.")
            if re.search(r"profile/" + re.escape(lid) + r"/(student_profile\.json|subjects/|tutor\.sqlite3|\.session_ledger)", command):
                return _deny("That file is written by a script, never by shell redirection or editing. Use the script that owns it.")
        if st.get("command") in TEACHING and re.search(r"\bcourses/", command):
            return _deny(f"/{st['command']} is a teaching command and does not edit course files.")
    return {"decision": "allow", "learner": next(iter(learners), None) if len(learners) == 1 else None}


def pre_tool(ev, root, st):
    tool, inp = ev.get("tool_name"), ev.get("tool_input") or {}
    if not root:
        return {"decision": "allow"}
    if tool in WRITE_TOOLS:
        r = decide_path(inp.get("file_path") or inp.get("notebook_path") or "", root, st, True)
    elif tool in ("Read", "Glob", "Grep"):
        r = decide_path(inp.get("file_path") or inp.get("path") or "", root, st, False)
    elif tool == "Bash":
        r = decide_bash(inp.get("command") or "", root, st)
    else:
        return {"decision": "allow"}
    return r


def command_of(prompt):
    m = re.match(r"\s*/(?:generic-tutor:)?([a-z][a-z-]*)", prompt or "")
    return m.group(1) if m else None


def learners_in(root):
    pd = os.path.join(root, "profile")
    try:
        return sorted(d for d in os.listdir(pd) if os.path.isfile(os.path.join(pd, d, "student_profile.json")))
    except OSError:
        return []


def session_start(ev, root):
    if not root:
        return {"additionalContext": "generic-tutor: no data folder found (no courses/ or profile/). Connect the EDU folder, then run /doctor."}
    plugin_json = os.path.join(os.path.dirname(HERE), ".claude-plugin", "plugin.json")
    note = ""
    if os.path.isfile(plugin_json):
        import bootstrap_scripts
        r = bootstrap_scripts.bootstrap(HERE, plugin_json, os.path.join(root, paths.DEPLOY_DIR_NAME))
        note = f" Scripts: {r.get('action') or r.get('error') or 'checked'}."
    ls = learners_in(root)
    who = f"Learners here: {', '.join(ls)}." if ls else "No learner profile yet: /add-profile creates one."
    return {"additionalContext": f"generic-tutor: data folder {root}.{note} {who} Run /run <name> before teaching."}


def stop(ev, root, st):
    lid = st.get("learner")
    if not root or not lid:
        return {}
    import verify_session
    from tutorlib import ledger
    learner_dir = os.path.join(root, "profile", lid)
    try:
        with open(os.path.join(learner_dir, "student_profile.json"), encoding="utf-8") as f:
            slot = int(json.load(f).get("session_slot", 0))
        findings = verify_session.verify(ledger.read(learner_dir), learner_dir, slot)
    except (OSError, ValueError):
        return {}
    missing = [f for f in findings if f["severity"] == "missing"]
    if not missing:
        return {}
    lines = "; ".join(f["message"] for f in missing[:3])
    return {"systemMessage": f"generic-tutor: this session may be missing state writes ({lines}). The next /run will offer to reconcile; nothing was changed."}


def handle(ev):
    name = ev.get("hook_event_name")
    sid = ev.get("session_id")
    root = find_root(ev.get("cwd"))
    st = load_state(sid)
    if name == "SessionStart":
        c = session_start(ev, root)
        return {"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": c["additionalContext"]}}
    if name == "UserPromptSubmit":
        cmd = command_of(ev.get("prompt"))
        if cmd:
            st["command"] = cmd
            save_state(sid, st)
        return {}
    if name == "PreToolUse":
        r = pre_tool(ev, root, st)
        if r.get("learner") and not st.get("learner"):
            st["learner"] = r["learner"]
            save_state(sid, st)
        if r["decision"] == "deny":
            return {"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": r["reason"]}}
        return {}
    if name == "Stop":
        return stop(ev, root, st)
    return {}


def main():
    try:
        ev = json.load(sys.stdin)
        out = handle(ev)
    except Exception:                      # a broken hook must never block the learner
        out = {}
    if out:
        print(json.dumps(out))
    return 0


if __name__ == "__main__":
    if "--help" in sys.argv[1:] or "-h" in sys.argv[1:]:
        print(__doc__)
        sys.exit(0)
    sys.exit(main())
