# Profile schemas, ledger, and displaying a profile

Loaded by `/add-profile` and `/profile`. The field-by-field owners are in `${CLAUDE_PLUGIN_ROOT}/docs/DATA_MODEL.md`.

## Global profile schema (`<user_id>/student_profile.json`)
The fields, types and owners are in `${CLAUDE_PLUGIN_ROOT}/docs/DATA_MODEL.md` and, executably, in `scripts/tutorlib/schemas/student_profile.json` (`validate_schema.py student_profile <file>`); `intake.md` maps each intake question to its key. Created only by `profile_init.py` and changed only by `profile_set.py`.

### `capabilities` — practical units by declaration
What the learner says they can do outside the conversation, which some courses' practical stages need (`course.json.practical_stages`). The only one defined today is `share_images`: the learner can share images of their own work, such as CAD screenshots, drawings or photos of a model. It's a declaration, not a check: ask plainly, record the learner's answer and the date, and never set it on their behalf or infer it. Absent means not declared. Ask about it at intake, or when a learner adds a course with practical stages, and let them change it any time through `/profile`.

**Whenever a capability is declared or withdrawn**, bring every one of the learner's enrolments into line. For each `subjects/<course_id>.json` whose course has `practical_stages`, run:
```
python3 /EDU/.tutor-scripts/apply_capabilities.py <student_profile.json> <courses/<course_id>/course.json> <subjects/<course_id>.json> --dry-run
```
- **If `reopens_completed_course` is true for any course**, declaring would turn a finished (theory-only) course back into an unfinished one with practical stages to do. Name those courses and ask for an explicit yes before running it again without `--dry-run`. If the learner says no, still record the declaration, but skip that one course.
- Otherwise run it again without `--dry-run`.
- Tell the learner which stages were unlocked or withheld.

Withdrawing a declaration never erases a stage already passed. A capability declaration never counts as a qualification and never moves the level ledger.

### `highest_level_cleared` — the one cumulative unlock ledger
A single scalar, never a set. It only ever increases by clearing — with one deliberate exception, below — and only when a course-runner/journey-planner check confirms every course at a given academic level has reached genuine `complete` status (every stage passed, exam passed if applicable) — never set directly, never by learner claim, never by attestation of prior credit earned outside this system. Clearing level *N* exempts everything **at or below** *N* from the level-lock forever after: "if 3 is cleared, anything at or below 3 will add; anything above 3 will still lock." See `course-compiler`'s level-lock section for the full mechanism, and note explicitly: **this system never accepts attestation of a prior qualification as a substitute for clearing it here.** The one exception to "only increases": a level can clear while an unfinished course at it sits **dropped** (dropped and suspended courses are excluded from clearing, see `journey-planner`), and if the learner later resumes that course while it is still unfinished, `resume_enrollment.py` **lowers** the value to one below that course's level (a course that is already complete reopens nothing, and `resume_enrollment.py` skips the lowering) — so a learner cannot drop a course, clear its level, unlock higher courses, and then resume the dropped course alongside them. The learner is told and must say yes first; when the resumed course completes, `journey-planner` walks the ledger back up — that level and any higher level whose courses are all still complete — in the ordinary way. Letting an unverifiable claim move a course between lock brackets would undermine the one thing the whole roster/lock model exists to keep honest — that progress recorded here reflects study actually done here.

### `roster.max_incomplete_courses`
Set once at intake, adjustable later via `/profile`. This is the hard cap `course-compiler` and `journey-planner` both check before a new course may be added. Raising the cap later doesn't retroactively unlock anything already gated by the level-lock — the two mechanisms are independent.

## Micro-profile schema (`<active_user_id>/subjects/<course_id>.json`)
Fields, types and owners: `DATA_MODEL.md` and `scripts/tutorlib/schemas/subjects.json`. Created only by `enrol.py`; every later change goes through the script that owns the field, never a hand edit (`confidence_update.py`, `error_log.py`, `item_mastery.py`, `remediation_state.py`, `record_stage_result.py`, `session_state.py`, `roster_apply.py`).

- **`cohort_id`** is a cached copy of the course's own `academic_level`, written once at enrolment; the phase-convergence gate groups by it, so courses at different levels never block each other's testing. A standalone course gets `"standalone:<course_id>"`: each standalone enrolment is its own cohort.
- **`syllabus_status`** maps each stage to `pass | fail | unsat | withheld`. `withheld` is written only by `apply_capabilities.py`, on a practical stage whose capability the learner has not declared; it counts as done, so the course can finish **theory-only**, and that still satisfies prerequisites.
- `last_live_recheck` lives on the shared `course.json`, not here: currency is a fact about the content.

## Displaying a full profile
When the learner asks to see their overall profile or progress, read the currently active learner's `student_profile.json` plus every file under their own `subjects/`, and present a combined, read-time-only view — never another learner's folder, even if their `user_id` is known. Always surface `highest_level_cleared` and current roster occupancy (e.g. "2 of 2 incomplete-course slots in use") plainly, since both directly determine what the learner can do next. Also show declared `capabilities`, and mark any course that is running theory-only. Standalone courses hold roster slots like any other unfinished course, but have no level and never affect `highest_level_cleared`; list them as "standalone". Something like:

> **Global:** [preferences, learning signals, highest level cleared: 2]
> **Roster:** 2 of 2 incomplete slots in use *(take this from `roster_check.py`'s `roster_occupancy`, which counts dormant level-locked courses as well as live ones)*
> **OU Contract Law:** S4 of 10, confidence: medium, roster state: active
> **GCSE Chemistry:** S2 of 8, confidence: high, roster state: test_pending_convergence

## Dropping a course
`/drop <course_id>` (mechanics defined in `journey-planner`) preserves `subjects/<course_id>.json` exactly as it stands and frees the roster slot it held — a pause, not a deletion. Re-adding the same course later resumes from wherever it was left, and re-enters the roster cap as if newly added. This is distinct from discarding a *suspended* (ungrounded) course, which a learner may choose to erase with genuinely no trace at all — see `course-auditor`.

## Creating and changing a profile (scripts, not hand edits)
- **New learner:** collect the intake answers, then write them to the script on stdin (a quoted heredoc, never inside shell quotes):
  `python3 /EDU/.tutor-scripts/profile_init.py <the /EDU/profile/ dir> <user_id> <today, ISO> <<'ANSWERS'` followed by a JSON object such as `{"identity.education_level": "Year 11", "preferences.style": "brief", "availability.sessions_per_week": 3, "availability.session_minutes": 45, "roster.max_incomplete_courses": 2, "capabilities.share_images": true}` and `ANSWERS`. It validates every value, refuses an existing id, and creates `student_profile.json` and `subjects/`. Leave unanswered settings out.
- **Any later change** (`/profile`): `python3 /EDU/.tutor-scripts/profile_set.py <student_profile.json> <field> <value> <today, ISO>`; add `--dry-run` to preview. Allowed fields are the settings listed in the script's header (preferences, learning signals, availability, roster cap, goals, identity, `capabilities.share_images`, `consent.status`). It reports old and new values and refuses anything else — `highest_level_cleared`, `session_slot` and ids are never settable here. After a capability change run `apply_capabilities.py` as described above. Consent can always be changed by the learner; with `limited` or `revoked` consent the other settings are not stored (the script says so — tell the learner).
- Never edit `student_profile.json` by hand, and tell the learner what you changed in plain words.
