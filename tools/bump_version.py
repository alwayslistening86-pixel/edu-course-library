#!/usr/bin/env python3
"""
bump_version.py -- change the plugin version in every place that carries it, once (R-13).

    python3 tools/bump_version.py <new X.Y.Z> [--changelog "one-line summary"] [--dry-run]

Edits `plugin/generic-tutor/.claude-plugin/plugin.json` (the source of truth), `.claude-plugin/marketplace.json` and `pyproject.toml`,
refuses a version that is not strictly higher, and refreshes `.tutor-scripts/` (the deployed copy records the version in its manifest).
With --changelog it also adds the `## [X.Y.Z]` heading CI requires, under a "Changed" line, when none exists yet. The docs lint still
fails if any file disagrees, so a hand edit that drifts is caught; this just removes the reason to make one.
"""
import datetime
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_JSON = os.path.join(ROOT, "plugin", "generic-tutor", ".claude-plugin", "plugin.json")
MARKETPLACE = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
PYPROJECT = os.path.join(ROOT, "pyproject.toml")
CHANGELOG = os.path.join(ROOT, "CHANGELOG.md")
_SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def parse(v):
    m = _SEMVER.match(v or "")
    return tuple(int(x) for x in m.groups()) if m else None


def current():
    with open(PLUGIN_JSON, encoding="utf-8") as f:
        return json.load(f)["version"]


def replace_in(path, old, new, pattern):
    with open(path, encoding="utf-8", newline="") as f:
        text = f.read()
    out, n = re.subn(pattern.format(old=re.escape(old)), lambda m: m.group(0).replace(old, new), text)
    return text, out, n


def bump(new, changelog=None, dry_run=False, root_scripts=True):
    old = current()
    if parse(new) is None:
        return {"error": f"{new!r} is not X.Y.Z"}
    if parse(new) <= parse(old):
        return {"error": f"{new} is not higher than the current version {old}"}
    plans = []
    for path, pat in ((PLUGIN_JSON, r'"version":\s*"{old}"'), (MARKETPLACE, r'"version":\s*"{old}"'), (PYPROJECT, r'(?m)^version\s*=\s*"{old}"')):
        text, out, n = replace_in(path, old, new, pat)
        if n != 1:
            return {"error": f"expected exactly one version string in {os.path.relpath(path, ROOT)}, found {n}"}
        plans.append((path, out))
    result = {"from": old, "to": new, "files": [os.path.relpath(p, ROOT) for p, _ in plans], "dry_run": dry_run}
    if dry_run:
        return result
    for path, out in plans:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(out)
    if changelog is not None:
        with open(CHANGELOG, encoding="utf-8") as f:
            text = f.read()
        if f"## [{new}]" not in text:
            marker = re.search(r"^## \[\d+\.\d+\.\d+\]", text, re.M)
            entry = f"## [{new}] — {datetime.date.today().isoformat()}\n### Changed\n- {changelog}\n\n"
            text = text[:marker.start()] + entry + text[marker.start():] if marker else text + "\n" + entry
            with open(CHANGELOG, "w", encoding="utf-8") as f:
                f.write(text)
            result["changelog"] = "entry added"
    if root_scripts:
        src = os.path.join(ROOT, "plugin", "generic-tutor", "scripts")
        subprocess.run([sys.executable, os.path.join(src, "bootstrap_scripts.py"), src, PLUGIN_JSON, os.path.join(ROOT, ".tutor-scripts")],
                       check=True, capture_output=True)
        result["deployed_copy"] = "refreshed"
    return result


def main(argv):
    args = [a for a in argv if a != "--dry-run"]
    dry = "--dry-run" in argv
    note = None
    if "--changelog" in args:
        i = args.index("--changelog")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--changelog needs a one-line summary"}))
            return 2
        note = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1:
        print(json.dumps({"error": 'usage: bump_version.py <X.Y.Z> [--changelog "summary"] [--dry-run]'}))
        return 2
    out = bump(args[0], note, dry)
    print(json.dumps(out, indent=2))
    return 1 if "error" in out else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
