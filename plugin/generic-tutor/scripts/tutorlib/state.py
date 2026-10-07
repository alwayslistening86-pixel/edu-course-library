"""
Reading persisted state safely (E-20, S-09 groundwork).

load() replaces six copies of `json.load(open(path))`. It adds three guards that
used to surface as tracebacks or, worse, silent misbehaviour:

  * unreadable / malformed JSON            -> StateError with the path and reason
  * a JSON document that is not an object  -> StateError
  * `schema_version` NEWER than this script understands (a file written by a later
    plugin version) -> StateError telling the user to update the plugin, instead of
    quietly rewriting a file in a shape this code does not know

Older or absent versions load normally; upgrading them is migrate_schema.py's job.
"""
import json
import os

from tutorlib import atomic_io, schema

# Highest schema_version each persisted kind is understood at (keep in step with migrate_schema.py
# and docs/DATA_MODEL.md).
SUPPORTED = {"subjects": 5, "student_profile": 2, "review_deck": 1, "course": 4}


class StateError(ValueError):
    pass


def check_version(data, kind, path="<data>"):
    supported = SUPPORTED.get(kind)
    version = data.get("schema_version") if isinstance(data, dict) else None
    if supported is not None and isinstance(version, int) and not isinstance(version, bool) and version > supported:
        raise StateError(
            f"{path}: schema_version {version} is newer than this plugin understands ({kind} v{supported}); "
            "update the generic-tutor plugin before touching this file")


def load(path, kind=None):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        raise StateError(f"{path}: cannot read as JSON ({type(e).__name__}: {e})") from e
    if not isinstance(data, dict):
        raise StateError(f"{path}: expected a JSON object, got {type(data).__name__}")
    if kind:
        check_version(data, kind, path)
        if kind in schema.kinds():
            _baseline[_key(path)] = frozenset(schema.validate(data, kind))
    return data


# Schema errors a file already had when it was loaded (older or hand-edited files may not be perfect). save() blocks only the errors a
# change INTRODUCES, so a legacy quirk never stops a learner's session but a script bug cannot make a file worse.
_baseline: dict[str, frozenset] = {}


def _key(path):
    return os.path.abspath(path)


def save(path, data, kind):
    """Validate-before-write (E-20): write `data` atomically unless doing so would add schema errors the file did not already have."""
    if kind in schema.kinds():
        base = _baseline.get(_key(path))
        if base is None:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    base = frozenset(schema.validate(json.load(f), kind))
            except (OSError, ValueError):
                base = frozenset()
        introduced = [e for e in schema.validate(data, kind) if e not in base]
        if introduced:
            raise StateError(f"{path}: refusing to write, this change would make the {kind} file invalid: " + "; ".join(introduced[:3]))
    atomic_io.write_json(path, data)
    if kind in schema.kinds():
        _baseline[_key(path)] = frozenset(schema.validate(data, kind))
