#!/usr/bin/env python3
"""
Docs lint (D-07): keeps skills, commands, scripts, versions and links honest.

Errors (exit 1):
  - a `.tutor-scripts/<x>.py` / `scripts/<x>.py` reference in a skill or command that doesn't exist
  - a command that includes a skill file that doesn't exist, or a skill no command includes
  - a skill whose frontmatter `name` differs from its folder
  - a skill whose description is missing, over 400 characters, or names no /command (and doesn't say it has none)
  - a skill without a **Contract** block (Owns/Reads/Calls/Emits/Never), or one naming a script that doesn't exist
  - disagreeing versions between plugin.json, .tutor-scripts/.manifest.json and pyproject.toml
  - a command missing from commands/help.md's table
  - a relative markdown link (in repo docs) whose target doesn't exist
Warnings (printed, exit 0 unless --strict):
  - a skill heading carrying a private "vN" version (K-35)

Usage: python3 tools/lint_docs.py [repo_root] [--strict]
"""
import json
import os
import re
import sys

PLUGIN = os.path.join("plugin", "generic-tutor")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def lint(root):
    errors, warnings = [], []
    plug = os.path.join(root, PLUGIN)
    skills_dir, cmds_dir, scripts_dir = (os.path.join(plug, d) for d in ("skills", "commands", "scripts"))
    skills = sorted(d for d in os.listdir(skills_dir) if os.path.isfile(os.path.join(skills_dir, d, "SKILL.md")))
    cmds = sorted(f for f in os.listdir(cmds_dir) if f.endswith(".md"))

    # script references
    for kind, d, names in (("skill", skills_dir, [os.path.join(s, "SKILL.md") for s in skills]),
                           ("command", cmds_dir, cmds)):
        for n in names:
            text = _read(os.path.join(d, n))
            for ref in sorted(set(re.findall(r"(?:\.tutor-scripts|scripts)/([A-Za-z_][\w/]*\.py)", text))):
                if not os.path.isfile(os.path.join(scripts_dir, ref)):
                    errors.append(f"{kind} {n}: references missing script {ref}")

    # command <-> skill wiring
    included = set()
    for c in cmds:
        for s in re.findall(r"skills/([\w-]+)/SKILL\.md", _read(os.path.join(cmds_dir, c))):
            included.add(s)
            if s not in skills:
                errors.append(f"command {c}: includes missing skill {s}")
    for s in skills:
        if s not in included:
            errors.append(f"skill {s}: not included by any command")

    # reference files inside skill folders: includes must exist, and none may be orphaned
    included_files = set()
    for c in cmds:
        for sk, fn in re.findall(r"skills/([\w-]+)/([\w.-]+\.md)", _read(os.path.join(cmds_dir, c))):
            included_files.add((sk, fn))
            if not os.path.isfile(os.path.join(skills_dir, sk, fn)):
                errors.append(f"command {c}: includes missing file skills/{sk}/{fn}")
    for sk in skills:
        skill_text = _read(os.path.join(skills_dir, sk, "SKILL.md"))
        for fn in sorted(os.listdir(os.path.join(skills_dir, sk))):
            if fn.endswith(".md") and fn != "SKILL.md" and (sk, fn) not in included_files and fn not in skill_text:
                errors.append(f"skill {sk}: reference file {fn} is neither included by a command nor mentioned in SKILL.md")

    # help.md must list every command
    help_path = os.path.join(cmds_dir, "help.md")
    if os.path.isfile(help_path):
        help_text = _read(help_path)
        for c in cmds:
            if c != "help.md" and f"`/{c[:-3]}" not in help_text:
                errors.append(f"command {c}: not listed in commands/help.md")

    # frontmatter name + heading versions
    for s in skills:
        text = _read(os.path.join(skills_dir, s, "SKILL.md"))
        m = re.search(r"^name:\s*(.+)$", text, re.M)
        if not m or m.group(1).strip() != s:
            errors.append(f"skill {s}: frontmatter name {m.group(1).strip() if m else None!r} != folder")
        desc = re.search(r"^description:\s*(.+)$", text, re.M)
        if not desc or len(desc.group(1)) > 400:
            errors.append(f"skill {s}: description missing or longer than 400 characters (it is what routes the skill)")
        elif "/" not in desc.group(1) and "no command" not in desc.group(1).lower():
            errors.append(f"skill {s}: description names no /command and does not say it has none")
        if "**Contract**" not in text:
            errors.append(f"skill {s}: missing the **Contract** block (see docs/SKILL_CONTRACT.md)")
        else:
            block = text.split("**Contract**", 1)[1].split("\n## ", 1)[0]
            for field in ("Owns", "Reads", "Calls", "Emits", "Never"):
                if f"**{field}" not in block:
                    errors.append(f"skill {s}: Contract block lacks a '{field}' line")
            for ref in re.findall(r"`([A-Za-z_]+\.py)`", block):
                if not os.path.isfile(os.path.join(scripts_dir, ref)):
                    errors.append(f"skill {s}: Contract names missing script {ref}")
        h = re.search(r"^# .*\bv\d+\b", text, re.M)
        if h:
            warnings.append(f"skill {s}: private version in heading ({h.group(0)[:60]!r})")

    # versions
    versions = {"plugin.json": json.loads(_read(os.path.join(plug, ".claude-plugin", "plugin.json")))["version"]}
    man = os.path.join(root, ".tutor-scripts", ".manifest.json")
    if os.path.isfile(man):
        versions[".manifest.json"] = json.loads(_read(man))["plugin_version"]
    pp = os.path.join(root, "pyproject.toml")
    if os.path.isfile(pp):
        m = re.search(r'^version\s*=\s*"([^"]+)"', _read(pp), re.M)
        if m:
            versions["pyproject.toml"] = m.group(1)
    mkt = os.path.join(root, ".claude-plugin", "marketplace.json")
    if os.path.isfile(mkt):
        for entry in json.loads(_read(mkt)).get("plugins", []):
            if entry.get("name") == "generic-tutor" and entry.get("version"):
                versions["marketplace.json"] = entry["version"]
    if len(set(versions.values())) > 1:
        errors.append(f"version mismatch: {versions}")

    # relative markdown links in repo docs
    md_files = [os.path.join(root, f) for f in ("README.md", "CONTRIBUTING.md", "CLAUDE.md")]
    for base in (os.path.join(root, "docs"), plug):
        for dp, dn, fn in os.walk(base):
            dn[:] = [d for d in dn if d not in ("tests", "__pycache__", "_template")]
            md_files += [os.path.join(dp, f) for f in fn if f.endswith(".md")]
    for f in sorted(set(md_files)):
        if not os.path.isfile(f):
            continue
        for target in re.findall(r"\]\(([^)\s]+)\)", _read(f)):
            if re.match(r"^(https?:|mailto:|#)", target) or "${" in target:
                continue
            path = target.split("#")[0]
            if path and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), path))):
                errors.append(f"{os.path.relpath(f, root)}: broken link {target}")
    return errors, warnings


def main(argv):
    strict = "--strict" in argv
    args = [a for a in argv if not a.startswith("--")]
    root = args[0] if args else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    errors, warnings = lint(root)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors or (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
