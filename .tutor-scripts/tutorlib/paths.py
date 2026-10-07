"""
Path guards (E-08). Resolve symlinks before comparing so a link inside a
learner folder cannot be used to reach, read or delete something outside it.
"""
import os

from tutorlib import ids

DEPLOY_DIR_NAME = ".tutor-scripts"


class OutsideRoot(ValueError):
    pass


def ensure_within(base, path):
    """Return realpath(path) if it is `base` itself or inside it, else raise OutsideRoot."""
    rb, rp = os.path.realpath(base), os.path.realpath(path)
    if rp != rb and not rp.startswith(rb + os.sep):
        raise OutsideRoot(f"{path!r} resolves outside {base!r}")
    return rp


def course_ids(courses_dir):
    """Sorted ids of the folders in `courses_dir` that are courses: a valid course id holding a course.json.
    Anything else (a `.import-x.tmp` staging folder, `_scratch`, a stray folder) is not a course (CONTENT_CONTRACT.md)."""
    out = []
    for name in os.listdir(courses_dir):
        try:
            ids.validate(name, "course id")
        except ValueError:
            continue
        if os.path.isfile(os.path.join(courses_dir, name, "course.json")):
            out.append(name)
    return sorted(out)


def learner_dir(profile_root, user_id):
    """<profile_root>/<user_id>, validated; refuses a learner folder that is itself a symlink."""
    ids.validate(user_id, "user_id")
    d = os.path.join(profile_root, user_id)
    if os.path.islink(d):
        raise OutsideRoot(f"{d!r} is a symlink")
    ensure_within(profile_root, d)
    return d


def resolve_root(explicit=None, env=None, here=None):
    """Find the tutor data root ("/EDU/" in the skills) in code instead of in prose (E-07).

    Order: explicit argument -> $EDU_ROOT -> the folder that contains the deployed
    `.tutor-scripts/` this module is running from. Returns an absolute path or None.
    """
    env = os.environ if env is None else env
    if explicit:
        return os.path.abspath(explicit)
    if env.get("EDU_ROOT"):
        return os.path.abspath(env["EDU_ROOT"])
    here = os.path.dirname(os.path.dirname(os.path.abspath(here or __file__)))  # .../.tutor-scripts
    if os.path.basename(here) == DEPLOY_DIR_NAME:
        return os.path.dirname(here)
    return None


def layout(root):
    """Standard locations under a root, plus anything wrong with them."""
    problems = []
    out = {"root": root}
    if not root or not os.path.isdir(root):
        return {**out, "courses": None, "profile": None, "tutor_scripts": None, "valid": False,
                "problems": [f"data root not found: {root!r}"]}
    out.update({"courses": os.path.join(root, "courses"), "profile": os.path.join(root, "profile"),
                "tutor_scripts": os.path.join(root, DEPLOY_DIR_NAME)})
    if not os.path.isdir(out["courses"]):
        problems.append("no courses/ folder - connect the folder that contains your courses (or the private courses repo)")
    if not os.path.isdir(out["profile"]):
        problems.append("no profile/ folder yet - first run: /add-profile creates it")
    if not os.path.isdir(out["tutor_scripts"]):
        problems.append("scripts not deployed (.tutor-scripts/ missing) - run /run so the plugin can deploy them")
    return {**out, "valid": not problems, "problems": problems}
