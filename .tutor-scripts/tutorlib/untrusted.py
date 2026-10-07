"""
Heuristic scanner for instruction-like text in content derived from the web (X-01, X-02).

The course compiler and the live source recheck read web pages and write the result into course
files (lessons, practice, tests, rubric, change.md, connectors.md) that later sessions load into
the model's context as trusted teaching material. A page that says "ignore your previous
instructions ..." must not be able to ride that path. This module cannot prove content safe; it
catches the common, blunt attempts so a human sees them before the course ships.

Rules and severity:
  BLOCKING  override-instruction  "ignore/disregard/forget ... previous/all/prior instructions"
            hidden-characters     zero-width / bidi-control characters (hide text from a reader)
            impersonation         "message/note from the system/administrator/Anthropic/user"
            system-prompt         references to the system prompt / developer message / new instructions
            exfiltration          "send/post/upload/forward ... (profile|learner|conversation|files|data) ... to"
  ADVISORY  tool-directive        shell/tool commands aimed at the reader (curl, rm -rf, sudo, bash -c, python3 ...)
            html-comment          HTML comment containing assistant/instruction wording
            encoded-blob          very long base64-looking token
            role-hijack           "you are now an AI/assistant/Claude"

Each finding: {rule, severity, line, excerpt}. Matching is case-insensitive and line-based.
"""
import os
import re

BLOCKING, ADVISORY = "blocking", "advisory"

_RULES = [
    ("override-instruction", BLOCKING,
     re.compile(r"\b(ignore|disregard|forget|override)\b[^\n]{0,40}\b(previous|prior|above|earlier|all|any|your)\b[^\n]{0,30}\b(instructions?|rules|prompts?|guidelines)\b", re.I)),
    ("impersonation", BLOCKING,
     re.compile(r"\b(message|note|instruction|notice)s?\s+(from|by)\s+(the\s+)?(system|administrator|admin|anthropic|developer|user|operator)\b", re.I)),
    ("system-prompt", BLOCKING,
     re.compile(r"\b(system\s+prompt|developer\s+message|new\s+instructions?\s*:|updated\s+instructions?\s*:)", re.I)),
    ("exfiltration", BLOCKING,
     re.compile(r"(?:^|[.!?;:]\s+|\b(?:must|should|need to|have to|will|now|then|and|please|also|just|immediately|first)\s+)"
                r"(send|post|upload|forward|email|exfiltrate|transmit)\b[^\n]{0,60}\b(profile|learner|student|conversation|chat|files?|credentials?|api[_ ]?keys?|tokens?)\b[^\n]{0,60}\b(to|at)\b", re.I)),
    ("tool-directive", ADVISORY,
     re.compile(r"(\bcurl\s+-|\bwget\s+http|\brm\s+-rf\b|\bsudo\s|\bbash\s+-c\b|\bpython3?\s+\S+\.py|\.tutor-scripts/|\bchmod\s+\+x\b)", re.I)),
    ("html-comment", ADVISORY,
     re.compile(r"<!--[^>]*\b(assistant|claude|instruction|ignore|system)\b[^>]*-->", re.I)),
    ("encoded-blob", ADVISORY, re.compile(r"[A-Za-z0-9+/]{80,}={0,2}")),
    ("role-hijack", ADVISORY, re.compile(r"\byou\s+are\s+now\s+(an?\s+|the\s+)?(ai|assistant|claude|chatbot|system)\b", re.I)),
]
# The engine's own stage-test template tells the tutor to record the result with this exact call; it is the one shipped
# directive, so it is not reported (any other script call, or the same call with other arguments, still is).
_TEMPLATE_CALL = re.compile(r"python3 /EDU/\.tutor-scripts/record_stage_result\.py apply <subjects\.json> <course\.json> \S+")
_HIDDEN = re.compile("[​-‏‪-‮⁠-⁤﻿]")
SCAN_EXTENSIONS = (".md", ".json", ".txt")


def scan_text(text):
    findings = []
    for n, line in enumerate(text.splitlines(), 1):
        if _HIDDEN.search(line):
            findings.append({"rule": "hidden-characters", "severity": BLOCKING, "line": n, "excerpt": "<line contains invisible/bidi control characters>"})
        for rule, severity, pat in _RULES:
            m = pat.search(_TEMPLATE_CALL.sub("", line) if rule == "tool-directive" else line)
            if m:
                s = max(0, m.start() - 20)
                findings.append({"rule": rule, "severity": severity, "line": n, "excerpt": line[s:m.end() + 40].strip()[:140]})
    return findings


def scan_path(path):
    """Scan one file, or every .md/.json/.txt under a directory. Returns {file: [findings]} (clean files omitted)."""
    targets = []
    if os.path.isdir(path):
        for dp, dn, fns in os.walk(path):
            dn[:] = [d for d in dn if d != "__pycache__"]
            targets += [os.path.join(dp, f) for f in sorted(fns) if f.endswith(SCAN_EXTENSIONS)]
    else:
        targets = [path]
    out = {}
    for t in sorted(targets):
        try:
            with open(t, encoding="utf-8", errors="replace") as f:
                found = scan_text(f.read())
        except OSError:
            continue
        if found:
            out[os.path.relpath(t, path).replace(os.sep, "/") if os.path.isdir(path) else os.path.basename(t)] = found
    return out
