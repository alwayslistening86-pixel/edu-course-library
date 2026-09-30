#!/usr/bin/env python3
"""
toolkit/core.py — shared foundation for the client-side toolkit: path
resolution, schema-aware loading, and thin wrappers around the plugin's own
scripts. Every other toolkit module goes through this file rather than
touching subjects.json, course.json, or the review deck directly.

DESIGN RULES THIS PACKAGE HOLDS ITSELF TO (do not violate these when adding
a new toolkit module):

  1. ONE-WAY DATA FLOW. The tutor (the LM, plus the plugin's own scripts
     under .tutor-scripts/, run from inside a live Claude session) is the
     only writer of tutoring state: subjects/<course_id>.json, course.json,
     student_profile.json, the review deck. This package only reads that
     state. It never calls item_mastery.observe(), never edits
     roster_state, confidence, syllabus_status, or review-card scheduling
     fields. The one exception is the toolkit's own side-log
     (profile/<learner_id>/toolkit_log/), which the tutor never reads for
     any gate, mastery, or grading decision — see backup.py/health.py for
     what, if anything, a given module writes there.
  2. NO PEDAGOGY HERE. No teaching, no re-grading, no "what to study next"
     judgment that overrides the runner. At most, this package surfaces
     what the tutor's own records already say.
  3. IMPORT THE PLUGIN'S SCRIPTS, NEVER REIMPLEMENT THEIR READS. Where a
     .tutor-scripts/*.py module already knows how to read a piece of state
     (item_mastery.status, error_log.query, validate_structure.validate,
     coverage_check.check, migrate_schema's schema-version constants), this
     package imports and calls it rather than re-parsing the JSON by hand.
     Re-parsing here would silently drift from the plugin's own schema the
     next time it migrates (subjects.json has already moved 4->5 in the
     time this toolkit was designed) — importing means it can't.
  4. SCHEMA-AWARE, VERSION-TOLERANT. Every subjects.json/course.json read
     checks schema_version against migrate_schema's current constants and
     reports (never silently guesses) when a file is on an older or newer
     version than this copy of the toolkit understands.
  5. OPTIONAL AND DISPOSABLE. The tutor works identically if this package
     is never opened. No skill depends on it existing.
  6. LOCAL ONLY. No network. No accounts. EDU_ROOT is resolved from where
     this package is actually deployed (see below), or overridden via the
     EDU_TOOLKIT_ROOT environment variable for a non-standard layout.
  7. ZERO-DEPENDENCY, WITH ONE NAMED EXCEPTION. Every module here is stdlib
     Python only, except export_anki.py, which needs the third-party
     `genanki` package to write a real, correct .apkg file (see that
     module's own docstring for why this one case is worth the exception).
     Every other module stays dependency-free; a missing genanki install
     only disables that one feature, cleanly, with a plain instruction
     rather than an exception.

WHERE THIS PACKAGE LIVES, AND WHY EDU_ROOT NEEDS NO CONFIG FILE
bootstrap_scripts.py deploys this whole package to
<EDU_ROOT>/.tutor-scripts/toolkit/ as a unit (see that script's v1.6.0
docstring section). That's a fixed relative position: this file always
ends up three directories below EDU_ROOT
(EDU_ROOT/.tutor-scripts/toolkit/core.py). So EDU_ROOT is resolved by
walking up from this file's own path — no config file needed for the
common case. EDU_TOOLKIT_ROOT overrides this, for testing or a
non-standard install.
"""
import json
import os
import sys

# --- path resolution -------------------------------------------------------

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))          # .../.tutor-scripts/toolkit
_TUTOR_SCRIPTS_DIR = os.path.dirname(_THIS_DIR)                  # .../.tutor-scripts
_DEFAULT_EDU_ROOT = os.path.dirname(_TUTOR_SCRIPTS_DIR)           # .../EDU

# Make the sibling .tutor-scripts/*.py modules importable (item_mastery,
# error_log, migrate_schema, validate_structure, coverage_check, review_math,
# gate_check, ...) without reimplementing what they already do.
if _TUTOR_SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _TUTOR_SCRIPTS_DIR)


def edu_root():
    """Resolve EDU_ROOT: EDU_TOOLKIT_ROOT env var if set, else the folder
    three levels above this file (see module docstring)."""
    override = os.environ.get("EDU_TOOLKIT_ROOT")
    return override if override else _DEFAULT_EDU_ROOT


def profile_dir(learner_id, root=None):
    return os.path.join(root or edu_root(), "profile", learner_id)


def subjects_dir(learner_id, root=None):
    return os.path.join(profile_dir(learner_id, root), "subjects")


def courses_dir(root=None):
    return os.path.join(root or edu_root(), "courses")


def toolkit_log_dir(learner_id, root=None):
    """The toolkit's own side-log directory. The tutor never reads this for
    any gate, mastery, or grading decision (design rule 1) — it exists so
    the toolkit can remember its own history (e.g. timed attempts) without
    ever touching a file the tutor's logic depends on."""
    return os.path.join(profile_dir(learner_id, root), "toolkit_log")


# --- safe loading ------------------------------------------------------------

def load_json(path):
    """Returns the parsed JSON, or a dict with "__error__" set — callers
    check for that key rather than letting a bad file crash the whole
    toolkit window. Never raises for a missing or malformed file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"__error__": f"not found: {path}"}
    except json.JSONDecodeError as e:
        return {"__error__": f"malformed JSON in {path}: {e}"}


def is_ok(loaded):
    return isinstance(loaded, dict) and "__error__" not in loaded


# --- learner / course discovery ---------------------------------------------

def list_learners(root=None):
    """Every subfolder of profile/ that has a student_profile.json. Returns
    learner_ids, sorted. An empty result means no real profile exists yet
    (or EDU_ROOT is resolved wrong) — callers should say so plainly, not
    treat it as an error."""
    pdir = os.path.join(root or edu_root(), "profile")
    if not os.path.isdir(pdir):
        return []
    out = []
    for name in sorted(os.listdir(pdir)):
        if os.path.isfile(os.path.join(pdir, name, "student_profile.json")):
            out.append(name)
    return out


def load_student_profile(learner_id, root=None):
    return load_json(os.path.join(profile_dir(learner_id, root), "student_profile.json"))


def current_session_slot(learner_id, root=None):
    """Reads student_profile.json.session_slot fresh from disk every call —
    never cached, per the same rule every plugin skill already follows
    (review-scheduler's SKILL.md: 'read it from disk, never estimate it')."""
    prof = load_student_profile(learner_id, root)
    if not is_ok(prof):
        return None
    return prof.get("session_slot", 0)


def list_enrolled_courses(learner_id, root=None):
    """course_ids this learner has a subjects/<course_id>.json for (the
    review-deck file's own _review_deck suffix is excluded)."""
    sdir = subjects_dir(learner_id, root)
    if not os.path.isdir(sdir):
        return []
    out = []
    for name in sorted(os.listdir(sdir)):
        if name.endswith(".json") and not name.endswith("_review_deck.json"):
            out.append(name[:-5])
    return out


def load_subject(learner_id, course_id, root=None):
    return load_json(os.path.join(subjects_dir(learner_id, root), f"{course_id}.json"))


def load_review_deck(learner_id, course_id, root=None):
    return load_json(os.path.join(subjects_dir(learner_id, root), f"{course_id}_review_deck.json"))


def load_course(course_id, root=None):
    return load_json(os.path.join(courses_dir(root), course_id, "course.json"))


def load_curriculum_map(course_id, root=None):
    return load_json(os.path.join(courses_dir(root), course_id, "curriculum_map.json"))


def course_dir_path(course_id, root=None):
    return os.path.join(courses_dir(root), course_id)


# --- schema-version checks (design rule 4) ----------------------------------

def schema_status(loaded, kind):
    """kind is "subject" or "course". Compares loaded.get("schema_version")
    against migrate_schema's current constant for that kind and reports the
    relationship — never silently treats an old or unexpectedly-new file as
    current. Import is done lazily (inside the function) so a toolkit
    module that never needs this doesn't pay for loading migrate_schema."""
    import migrate_schema  # noqa: E402  (sibling .tutor-scripts module)

    current = {
        "subject": migrate_schema.SUBJECT_SCHEMA_VERSION,
        "course": migrate_schema.COURSE_SCHEMA_VERSION,
    }.get(kind)
    if current is None:
        return {"status": "unknown_kind", "kind": kind}
    if not is_ok(loaded):
        return {"status": "unreadable"}
    found = loaded.get("schema_version")
    if found is None:
        return {"status": "no_schema_version_field", "expected": current}
    if found == current:
        return {"status": "current", "version": found}
    if isinstance(found, int) and found < current:
        return {"status": "older", "version": found, "current": current,
                "note": "run the plugin's /audit to migrate this file"}
    return {"status": "newer_than_this_toolkit", "version": found, "current": current,
            "note": "this copy of the toolkit is older than the data it's reading — "
                    "it may not show every field; safe to keep using, but consider "
                    "re-running the tutor once so bootstrap_scripts.py redeploys "
                    "the current toolkit version too"}
