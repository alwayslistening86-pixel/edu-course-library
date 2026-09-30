#!/usr/bin/env python3
"""
toolkit/__main__.py — CLI entry point: `python -m toolkit <command> ...`.
Dispatches to each module's own main(); see this package's README.md for
the full command list and core.py for the design rules every module here
follows. The GUI launcher (gui.pyw) is a separate, optional entry point
that wires these same modules to on-demand windows instead of a terminal.
"""
import sys

COMMANDS = {
    "backup": "backup",
    "health": "health",
    "progress": "progress",
    "review-due": "review_due",
    "errors": "errors",
}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("usage: python -m toolkit <command> [args...]")
        print("commands: " + ", ".join(sorted(COMMANDS)))
        sys.exit(2)
    command = sys.argv[1]
    module_name = COMMANDS[command]
    sys.argv = [f"toolkit.{module_name}"] + sys.argv[2:]
    module = __import__(f"toolkit.{module_name}", fromlist=["main"])
    module.main()


if __name__ == "__main__":
    main()
