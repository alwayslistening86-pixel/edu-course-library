"""
CLI conventions shared by every script (E-10, E-11).

Every script prints exactly one JSON document on stdout. Exit codes:

  0  success -- including a *decision* the caller must read (e.g. can_proceed: false,
     consent skipped); those are results, not failures
  1  operation failed: the JSON has an "error" key (bad input values, missing file,
     unexpected exception, refused deletion, ...)
  2  usage error: wrong argument count / unknown subcommand

Before this module, several scripts reported a failure as {"error": ...} but still
exited 0, so a caller checking only the exit status could not tell success from failure.
"""
import json

from tutorlib import filelock, state

# Failures a script reports as {"error": ...} with exit 1 instead of a traceback.
EXPECTED_ERRORS = (FileNotFoundError, json.JSONDecodeError, state.StateError, filelock.LockTimeout)


def emit(result):
    """Print `result` as JSON and return the process exit code (1 if it carries an error)."""
    print(json.dumps(result, indent=2))
    return 1 if isinstance(result, dict) and "error" in result else 0


def parse_bool(raw, name="value"):
    """True or False for the words `true` / `false` (any case, spaces ignored); anything else raises ValueError.
    A flag that is silently read as false when mistyped ("yes", "1", "ture") records a right answer as a wrong one (ADR 0012)."""
    text = str(raw).strip().lower()
    if text == "true":
        return True
    if text == "false":
        return False
    raise ValueError(f"{name} must be true or false, got {raw!r}")


ERROR_CODES = ("E_USAGE", "E_CONSENT", "E_SCHEMA", "E_LOCKED", "E_NOT_FOUND", "E_INVALID_INPUT", "E_INTERNAL")


def error_code(message, exit_code=1):
    """Stable machine-readable code for an {"error": ...} message (E-11). Order matters: first match wins."""
    m = str(message).lower()
    if exit_code == 2 or m.startswith("usage"):
        return "E_USAGE"
    if "consent" in m:
        return "E_CONSENT"
    if "locktimeout" in m or "lock " in m or "locked" in m:
        return "E_LOCKED"
    if "filenotfounderror" in m or "not found" in m or "does not exist" in m or "no such" in m:
        return "E_NOT_FOUND"
    if "schema_version" in m or "stateerror" in m or "schema" in m:
        return "E_SCHEMA"
    return "E_INVALID_INPUT"


def envelope(stdout_text, exit_code):
    """Wrap a script's legacy stdout and exit status as {ok, data, warnings, error{code,message}} (E-10)."""
    try:
        doc = json.loads(stdout_text)
    except ValueError:
        doc = None
    if doc is None and exit_code == 0:
        doc = {"output": stdout_text}
    err = None
    if exit_code != 0 or (isinstance(doc, dict) and "error" in doc):
        has_error = isinstance(doc, dict) and "error" in doc
        message = doc["error"] if has_error else f"exit status {exit_code}" if doc is not None else (stdout_text.strip()[-300:] or f"exit status {exit_code}")
        code = error_code(message, exit_code) if doc is not None else "E_INTERNAL"
        err = {"code": code, "message": str(message)}
    warnings = []
    if isinstance(doc, dict) and isinstance(doc.get("warnings"), list):
        warnings = [str(w) for w in doc["warnings"]]
    return {"ok": err is None, "data": None if err and isinstance(doc, dict) and "error" in doc else doc, "warnings": warnings, "error": err}


def _install_envelope():
    import atexit
    import io
    import sys
    real, buf = sys.stdout, io.StringIO()
    sys.stdout = buf
    state_ = {"code": 0}
    orig_exit = sys.exit

    def _exit(code=0):
        state_["code"] = code if isinstance(code, int) else (0 if code is None else 1)
        orig_exit(code)

    sys.exit = _exit

    def _flush():
        sys.stdout = real
        real.write(json.dumps(envelope(buf.getvalue(), state_["code"]), indent=2) + "\n")

    atexit.register(_flush)


def read_stdin():
    """All of stdin as text, decoded as UTF-8 whatever the platform's locale says (Windows pipes default to a legacy code page,
    which would mangle accents and currency signs in course or learner text). A leading BOM is dropped; bad bytes become U+FFFD."""
    import sys
    data = sys.stdin.buffer.read() if hasattr(sys.stdin, "buffer") else sys.stdin.read().encode("utf-8")
    return data.decode("utf-8-sig", errors="replace")


def strip_envelope():
    """Remove `--envelope` from sys.argv and, if it was there, wrap this process's output (E-10)."""
    import sys
    if "--envelope" in sys.argv[1:]:
        sys.argv.remove("--envelope")
        _install_envelope()


def handle_help(doc, argv=None):
    """Called first thing in every script's __main__ block. Also strips `--envelope` (wraps the output, see `envelope`).

    `--help` / `-h` as the sole first argument prints the script's usage as plain text and exits 0 (E-09).

    Shows the docstring's "Usage:" section when it has one, else the whole docstring (capped at 40 lines).
    """
    import sys
    argv = sys.argv if argv is None else argv
    for stream in (sys.stdout, sys.stderr):                      # usage text may contain characters a legacy console code page lacks
        try:
            stream.reconfigure(errors="replace")
        except (AttributeError, ValueError):
            pass
    if argv is sys.argv:
        strip_envelope()
    if len(argv) < 2 or argv[1] not in ("-h", "--help"):
        return
    text = (doc or "").strip("\n")
    i = text.find("Usage:")
    lines = (text[i:] if i >= 0 else text).splitlines()[:40]
    print("\n".join(lines))
    sys.exit(0)
