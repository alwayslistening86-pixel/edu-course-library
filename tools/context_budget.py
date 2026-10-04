#!/usr/bin/env python3
"""
context_budget.py -- how much text each command loads into the model's context (P-15).

    python3 tools/context_budget.py [--json] [--check]

A command file `@`-includes skill files; everything included is read into context every time the command
runs. Sizes are in characters and an approximate token count (characters / 4 -- a rough, tokenizer-free
estimate, good for comparing, not for billing). `--check` compares against tools/context_budget.json (a
ratchet: the committed numbers may only go DOWN without a deliberate edit to that file) and exits 1 on growth.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = os.path.join(ROOT, "plugin", "generic-tutor")
BUDGET_FILE = os.path.join(ROOT, "tools", "context_budget.json")


def measure():
    out = {}
    cmds = os.path.join(PLUGIN, "commands")
    for fn in sorted(os.listdir(cmds)):
        if not fn.endswith(".md"):
            continue
        with open(os.path.join(cmds, fn), encoding="utf-8") as f:
            text = f.read()
        chars, parts = len(text), []
        for rel in re.findall(r"@\$\{CLAUDE_PLUGIN_ROOT\}/(\S+)", text):
            path = os.path.join(PLUGIN, rel)
            if os.path.isfile(path):
                with open(path, encoding="utf-8") as f:
                    n = len(f.read())
                chars += n
                parts.append({"file": rel, "chars": n})
        out[fn[:-3]] = {"chars": chars, "tokens": round(chars / 4), "includes": parts}
    return out


def main(argv):
    data = measure()
    if "--check" in argv:
        with open(BUDGET_FILE, encoding="utf-8") as f:
            budget = json.load(f)
        over = {c: (v["chars"], budget.get(c)) for c, v in data.items() if budget.get(c) is None or v["chars"] > budget[c]}
        for c, (now, allowed) in sorted(over.items()):
            print(f"OVER BUDGET /{c}: {now} chars (allowed {allowed}) - trim the skills it includes, or raise tools/context_budget.json deliberately")
        print(f"{len(over)} command(s) over budget")
        return 1 if over else 0
    if "--json" in argv:
        print(json.dumps(data, indent=2))
        return 0
    width = max(len(c) for c in data) + 1
    for c, v in sorted(data.items(), key=lambda kv: -kv[1]["chars"]):
        print(f"/{c:<{width}} {v['chars']:>7} chars  ~{v['tokens']:>5} tokens  ({len(v['includes'])} skill file(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
