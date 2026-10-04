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
    return data
