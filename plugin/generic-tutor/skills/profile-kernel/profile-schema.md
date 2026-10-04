# Profile schemas, ledger, and displaying a profile

Loaded by `/add-profile` and `/profile`. Moved verbatim from `SKILL.md`; the field-by-field owners are in `${CLAUDE_PLUGIN_ROOT}/docs/DATA_MODEL.md`.

## Global profile schema (`<user_id>/student_profile.json`)
```json
{
  "schema_version": 2,
  "learner_id": "string",
  "consent": { "status": "granted|revoked|limited" },
  "identity": {
    "display_name": "string?",
    "education_level": "string",
    "locale": "en-GB"
  },
  "preferences": {
    "style": "brief|detailed",
    "tone": "neutral|friendly|formal|playful",
    "accessibility": { "dyslexia_mode": false, "plain_language_mode": false }
  },
  "learning_signals": {
    "pace": "fast|standard|slow",
    "working_memory_support_needed": "none|some|significant",
    "verbal_load_sensitivity": "none|some|significant",
    "spatial_support_needed": "none|some|significant",
    "notes": "free text"
  },
  "goals": ["string"],
  "availability": {
    "sessions_per_week": 2,
    "session_minutes": 60
  },
  "roster": {
    "max_incomplete_courses": 2
  },
  "highest_level_cleared": 0,
  "capabilities": { "share_images": { "declared": true, "on": "ISO date" } },
  "session_slot": 0,
  "session_slot_advanced_at": "ISO UTC timestamp (slot_advance.py's double-/run guard)",
  "last_updated": "ISO date"
}
```

### `capabilities` — practical units by declaration (v1.3.0)
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
```json
{
  "schema_version": 5,
  "course_id": "aqa_gcse_maths_8300",
  "roster_state": "active | dormant | test_pending_convergence | dropped",
  "cohort_id": "integer — a cached copy of this course's own academic_level, written once by course-compiler at enrollment and never changed afterward; course-runner's phase-convergence gate groups by this field, not globally, so courses at different levels never block each other's testing. For a standalone course (v1.3.0) it is the string \"standalone:<course_id>\": each standalone enrolment is its own cohort",
  "syllabus_status": {
    "S1": "pass | fail | unsat | withheld"
  },
  "notices_acknowledged": [ { "id": "notice id", "on": "ISO date" } ],
  "current_stage": "S1",
  "current_phase": "lesson | practice | test",
  "exam_status": "locked | available | passed",
  "confidence": 0.5,
  "error_patterns": [
    { "id": "err_…", "stage_id": "S1", "item_id": "…", "source_phase": "practice|test",
      "cause": "slip|missing_prerequisite|misconception|misapplied_procedure|comprehension",
      "misconception_id": "string|null", "rubric_criterion": "string|null", "note": "string",
      "slot": 0, "resolved": false, "resolved_at_slot": null }
  ],
  "item_mastery": { "<item_id>": { "p_mastery": 0.0, "observations": 0 } },
  "remediation": { "<stage_id>": { "attempts": 0, "last_cause": "string|null", "escalated": false, "escalated_at_slot": null } },
  "last_session_summary": "one or two sentences",
  "last_updated": "ISO date"
}
```
Field ownership (code, not prose, owns these; never hand-edit): `confidence` (a number in [0, 1], default 0.5 = unknown) by `confidence_update.py`; `error_patterns` by `error_log.py`; `item_mastery` by `item_mastery.py`; `remediation` by `remediation_state.py`; `syllabus_status`/`current_stage` by `record_stage_result.py`. Authoritative field shapes are defined by those scripts and `migrate_schema.py` (`SUBJECT_SCHEMA_VERSION`).

Two things moved deliberately since the original single-file design:
- **`last_live_recheck` now lives on the shared `course.json`**, not here — currency is a fact about the content, true for every learner enrolled, and checking it once benefits everyone rather than being duplicated per learner for no reason.
- **`stage_progress` is replaced by the flatter `syllabus_status` tri-state map** (`pass | fail | unsat`, defaulting to `unsat`), which is what the roster, convergence, and journey-planner logic actually reads to decide readiness.
- **v1.3.0 adds a fourth value, `withheld`**. It is only ever written by `apply_capabilities.py`, and only on a practical stage whose capability the learner hasn't declared. It counts as done for completion, so the course can finish **theory-only**, and a theory-only completion satisfies prerequisites. `notices_acknowledged` records which course notices the learner has already been told.

## Displaying a full profile
When the learner asks to see their overall profile or progress, read the currently active learner's `student_profile.json` plus every file under their own `subjects/`, and present a combined, read-time-only view — never another learner's folder, even if their `user_id` is known. Always surface `highest_level_cleared` and current roster occupancy (e.g. "2 of 2 incomplete-course slots in use") plainly, since both directly determine what the learner can do next. Also show declared `capabilities`, and mark any course that is running theory-only. Standalone courses hold roster slots like any other unfinished course, but have no level and never affect `highest_level_cleared`; list them as "standalone". Something like:

> **Global:** [preferences, learning signals, highest level cleared: 2]
> **Roster:** 2 of 2 incomplete slots in use *(take this from `roster_check.py`'s `roster_occupancy`, which counts dormant level-locked courses as well as live ones)*
> **OU Contract Law:** S4 of 10, confidence: medium, roster state: active
> **GCSE Chemistry:** S2 of 8, confidence: high, roster state: test_pending_convergence

## Dropping a course
`/drop <course_id>` (mechanics defined in `journey-planner`) preserves `subjects/<course_id>.json` exactly as it stands and frees the roster slot it held — a pause, not a deletion. Re-adding the same course later resumes from wherever it was left, and re-enters the roster cap as if newly added. This is distinct from discarding a *suspended* (ungrounded) course, which a learner may choose to erase with genuinely no trace at all — see `course-auditor`.
