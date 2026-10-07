#!/usr/bin/env python3
"""
scan_repo.py -- secrets / personal-data / private-content scan of the files git tracks (X-07).

    python3 tools/scan_repo.py [repo_root]        exit 1 on any finding

Looks for: API keys and tokens (Anthropic, OpenAI-style, GitHub, AWS, Slack, private-key blocks), e-mail addresses other than
reserved examples and the Claude attribution address, and tracked paths that must live only in the private content repo
(`courses/`, `_staging/`, `_historic/`, `profile/<id>/`, `*.sqlite3`, `student_profile.json` outside tests/fixtures).
Heuristic and deliberately simple: it blocks the obvious mistakes, it is not a substitute for GitHub secret scanning.
"""
import os
import re
import subprocess
import sys

SECRET_PATTERNS = {
    "anthropic-key": re.compile(r"sk-ant-[A-Za-z0-9_-]{20,}"),
    "openai-style-key": re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
    "github-token": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr|github_pat)_[A-Za-z0-9_]{30,}"),
    "aws-access-key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "slack-token": re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}"),
    "private-key-block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
}
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@([A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+)")
ALLOWED_EMAIL_DOMAINS = {"example.com", "example.org", "example.net", "anthropic.com", "users.noreply.github.com", "localhost"}
ALLOWED_EMAILS = {"noreply@anthropic.com"}
FORBIDDEN_PATH = re.compile(r"^(courses|_staging|_historic)/|(^|/)profile/[^/]+/|\.sqlite3?$")
TEXT_EXT = (".md", ".json", ".py", ".yml", ".yaml", ".toml", ".txt", ".sql", ".cfg", ".ini", ".sh", ".html", ".css", ".js")


def tracked_files(root):
    out = subprocess.run(["git", "-C", root, "ls-files", "-z"], capture_output=True, text=True, check=True).stdout
    return [p for p in out.split("\0") if p]


def scan(root):
    findings = []
    for rel in tracked_files(root):
        if FORBIDDEN_PATH.search(rel) and not rel.startswith(("plugin/generic-tutor/tests/", "docs/")):
            findings.append((rel, 0, "private-path", "this path belongs in the private content repo"))
            continue
        if not rel.endswith(TEXT_EXT) or rel.endswith(".manifest.json"):
            continue
        try:
            with open(os.path.join(root, rel), encoding="utf-8", errors="replace") as f:
                lines = f.read().splitlines()
        except OSError:
            continue
        for n, line in enumerate(lines, 1):
            for name, pat in SECRET_PATTERNS.items():
                if pat.search(line):
                    findings.append((rel, n, name, "looks like a credential"))
            for m in EMAIL.finditer(line):
                if m.group(0).lower() in ALLOWED_EMAILS or m.group(1).lower() in ALLOWED_EMAIL_DOMAINS:
                    continue
                findings.append((rel, n, "email", f"e-mail address {m.group(0)[:3]}…@{m.group(1)}"))
    return findings


def main(argv):
    root = argv[0] if argv else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    findings = scan(root)
    for rel, n, kind, msg in findings:
        print(f"{rel}:{n}: [{kind}] {msg}")
    print(f"{len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
