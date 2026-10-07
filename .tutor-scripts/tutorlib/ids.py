"""
Identifier rules (S-13, E-08 groundwork).

user_id, course_id, stage_id, item_id and card_id all end up inside file paths
or SQL parameters. Learners (or text a learner pastes) must never be able to
turn one into a path escape. One rule for all of them: 1-64 characters, first
character alphanumeric, then letters, digits, underscore, dot or hyphen; no
path separators, no "..", no Windows reserved device names.
"""
import re

_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,63}$")
_RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(1, 10)), *(f"lpt{i}" for i in range(1, 10))}


class InvalidId(ValueError):
    pass


def validate(value, what="id"):
    if not isinstance(value, str) or not _ID.match(value) or ".." in value or value.endswith("."):
        raise InvalidId(f"invalid {what} {value!r}: use 1-64 letters, digits, '_', '.', '-' (starting with a letter or digit)")
    if value.split(".")[0].lower() in _RESERVED:
        raise InvalidId(f"invalid {what} {value!r}: reserved name")
    return value
