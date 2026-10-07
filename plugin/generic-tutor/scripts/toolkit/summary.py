#!/usr/bin/env python3
"""
toolkit/summary.py -- the same one-screen summary `/status` gives, without opening a session (U-04). Read-only.

It calls the plugin's own `status.py` (the deployed sibling of this package) so the numbers can never differ from what `/status` shows:
roster occupancy, per-course stage progress, confidence, reviews due and the suggested next step. It computes and decides nothing itself.

Usage:
    python3 -m toolkit status <learner_id>
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
import core  # noqa: E402


def snapshot(learner_id, root=None):
    import status as status_script                 # the plugin script one folder up
    root = root or core.edu_root()
    pdir = core.profile_dir(learner_id, root)
    if not os.path.isdir(pdir):
        return {"error": f"no such learner profile: {pdir}"}
    return status_script.build(pdir, core.courses_dir(root))


def main():
    if len(sys.argv) != 2:
        print(json.dumps({"error": "usage: summary.py <learner_id>"}))
        sys.exit(2)
    result = snapshot(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(1 if "error" in result else 0)


if __name__ == "__main__":
    main()
