"""
Path guards (E-08). Resolve symlinks before comparing so a link inside a
learner folder cannot be used to reach, read or delete something outside it.
"""
import os

from tutorlib import ids


class OutsideRoot(ValueError):
    pass


def ensure_within(base, path):
    """Return realpath(path) if it is `base` itself or inside it, else raise OutsideRoot."""
    rb, rp = os.path.realpath(base), os.path.realpath(path)
    if rp != rb and not rp.startswith(rb + os.sep):
        raise OutsideRoot(f"{path!r} resolves outside {base!r}")
    return rp


def learner_dir(profile_root, user_id):
    """<profile_root>/<user_id>, validated; refuses a learner folder that is itself a symlink."""
    ids.validate(user_id, "user_id")
    d = os.path.join(profile_root, user_id)
    if os.path.islink(d):
        raise OutsideRoot(f"{d!r} is a symlink")
    ensure_within(profile_root, d)
    return d
