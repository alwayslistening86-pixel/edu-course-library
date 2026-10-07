#!/usr/bin/env python3
"""
scan_untrusted.py -- look for instruction-like text hidden in web-derived content (X-01, X-02).

    python3 scan_untrusted.py <file_or_dir>

Output {path, clean, blocking_count, advisory_count, files{<relative file>: [{rule, severity, line, excerpt}]}}.
Exit 0 always (it reports; the caller decides). See tutorlib/untrusted.py for the rules and
docs/UNTRUSTED_CONTENT.md for the policy around them.
"""
import json
import os
import sys

from tutorlib import cli, untrusted


def main(argv):
    if len(argv) != 1 or not os.path.exists(argv[0]):
        print(json.dumps({"error": "usage: scan_untrusted.py <existing file or directory>"}))
        return 2
    files = untrusted.scan_path(argv[0])
    allf = [f for fs in files.values() for f in fs]
    blocking = sum(1 for f in allf if f["severity"] == untrusted.BLOCKING)
    return cli.emit({"path": argv[0], "clean": not allf, "blocking_count": blocking,
                     "advisory_count": len(allf) - blocking, "files": files})


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
