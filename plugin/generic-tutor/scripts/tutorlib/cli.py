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
