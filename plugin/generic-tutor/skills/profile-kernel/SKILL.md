---
name: profile-kernel
description: Multi-learner profile system for the tutor — handles /run, /add-profile, /profile, and the first-ever-load intake landing flow when /EDU/profile/ is completely empty. Owns the one cumulative unlock ledger (highest_level_cleared) and the roster capacity a learner has committed to.
---

# Profile Kernel (roster-capped, level-ledger, capability declarations, isolated by folder)

## Invocation
`/run <user_id>` activates a learner's profile for the session. `/profile` shows or updates the *currently active* learner's aggregated profile. `/add-profile <user_id>` creates a new learner alongside existing ones. None of this runs on inferred intent — see the landing logic below for the one deliberate exception.

## File layout (multi-learner, content and progress deliberately separated)
```
/EDU/courses/<course_id>/                 ← shared, canonical, one copy per real qualification (see course-compiler)
  course.json
  rubric.json
  curriculum_map.json
  ...

/EDU/profile/<user_id_1>/                 ← private, isolated by folder — this is the actual privacy boundary
  student_profile.json
  subjects/
    <course_id>.json                      ← this learner's own progress through a shared course
/EDU/profile/<user_id_2>/
  student_profile.json
  subjects/
    <course_id>.json
```
A learner's session may only ever read or write paths under their own currently-active `/EDU/profile/<user_id>/`. The only things ever read from outside that boundary are a shared course's own content files — and only `course-compiler` (at build time) and `course-runner` (at live-recheck time) ever *write* to `/EDU/courses/`, never a learner's own teaching session, and never another learner's folder.

## Folder access confirmation
`/EDU/profile/` deserves exactly the same access confirmation `course-compiler` requires for `/EDU/courses/<course_id>/` — having file access through a shared parent connection is not the same as the person having deliberately isolated it. On first-ever load, before intake begins, ask plainly: *"Do you want `/EDU/profile/` connected as its own isolated folder, or to proceed under the shared connection as-is?"* Record the answer in `/EDU/profile/access.json` (`{"status": "pending_confirmation | isolated_confirmed | shared_confirmed"}`) and don't proceed to intake until it's answered. This is one-time per installation, not per learner.

## Landing logic (what happens when this system is opened)
**Before even the `/EDU/profile/` check below, run the bootstrap script — don't hand-derive whether the deployed scripts need updating:**
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/bootstrap_scripts.py ${CLAUDE_PLUGIN_ROOT}/scripts ${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json <the resolved path to this install's /EDU/.tutor-scripts/>
```
**On resolving that last path — this is the one place in this whole file where it matters enough to say explicitly: `/EDU/` is never a literal path.** It's this plugin's name, everywhere, for whatever real folder this install has actually connected as its tutor data root — a different location on every machine (a different drive letter, a different OS, a different folder name even), exactly the same way `/EDU/courses/` and `/EDU/profile/` elsewhere in this file already resolve to wherever *this* install's real folder is, not to any one install's actual path. Resolve `/EDU/.tutor-scripts/` the identical way you'd resolve `/EDU/profile/` for the check right below this one, on this same machine, in this same session — never reuse a path seen on a different install or a different session's device listing.

The script itself decides whether anything needs writing — a plain semver comparison between what's already deployed (its own `.manifest.json`) and this running plugin's own `version` in `plugin.json`, done as a real tuple compare rather than eyeballed, because a naive string compare gets an update like `1.9.0` → `1.10.0` backwards. Its `action` field tells you what happened: `deployed_fresh` (nothing was there yet — this install's first time seeing this plugin), `updated` (an older deployed copy was replaced with this plugin's current one — report the version jump plainly, the same way `course-auditor`'s own schema migrations are always reported, never silent, even though this one needs no separate confirmation since it never touches any learner's own data), `up_to_date` (no-op), or `warning_target_newer_than_bundle` (left untouched — surface this to the learner/you rather than guessing which side is right). This closes the gap the previous "copy once, never touch again" version of this design left open: a real fix to one of these scripts' own logic now actually reaches an install that already has an older copy, instead of being silently stuck there forever.

**Then check `/EDU/profile/` first, before anything else, every time this system is opened.**

- **If `/EDU/profile/` is empty (no user folders at all)** — first-ever load. Skip `/run` entirely; there's nothing to run yet. Confirm folder access (above), run the intake conversation through question 7 (roster capacity, then the optional sharing-work question) and write `student_profile.json` with those fields set, *then* ask what subjects the learner wants to study (one `/add-course` per subject, confirmed individually — never silently looped; `course-compiler`'s Step -1 now has a real cap to check on every one of these). Once every chosen course exists, run `/plan` (journey-planner) once as the final onboarding step.
- **If `/EDU/profile/` has one or more user folders already** — `/run <user_id>` is required before `/continue`, `/profile`, `/plan`, or any teaching can proceed. If the learner tries to jump straight to teaching, ask them to `/run <user_id>` first (or `/add-profile` if new).

## `/run <user_id>` — outcomes
- **Match found** → load that folder as active for the rest of the session, then advance the session-slot counter exactly once — `python3 /EDU/.tutor-scripts/slot_advance.py <that learner's student_profile.json>` — and confirm plainly ("Running profile: Alex"), proceed. The counter (`student_profile.json.session_slot`, absent = 0) is what `review-scheduler` compares every card's `due_at_slot` against; it advances once per session here and nowhere else (not per course, not per `/review`, never by date), so "what slot are we on" is always read from disk, never guessed. The script skips itself, and says why, if consent is `revoked` or if the last advance was under three hours ago (so typing `/run` twice in one sitting, or re-running it after a disconnect, is one session, not two) — in both cases it still reports the current slot, and that is the number to use.
- **No match found** → do not create one, do not guess a close match. Say plainly: *"No profile found for '<user_id>'. Try again, or create a new profile with `/add-profile <user_id>`?"*

## Intake questions (asked once per new profile, conversationally, not as a rigid form)
1. General education level / context.
2. Brief vs. detailed explanation preference.
3. Any known learning difficulty or support need (working memory, reading load, attention, spatial reasoning).
4. Any accessibility needs (dyslexia-friendly formatting, plain-language support, session-length sensitivity).
5. **Study availability**, for the journey planner: a *rate*, not a schedule — `sessions_per_week` and `session_minutes`. No days of the week, no calendar dates are ever collected here; the whole planning model is slot-based, not date-based (see journey-planner).
6. **Roster capacity**: how many courses the learner wants to be able to hold *incomplete* at once. State plainly that this is a real commitment — adding a course beyond this cap later requires completing or dropping one first — so the answer should reflect genuine bandwidth, not enthusiasm.
7. **Sharing work (v1.3.0, optional):** can they share images of their own work (drawings, CAD screenshots, photos of something they made) when a course asks for it? Record the answer under `capabilities.share_images` with today's date. If they're unsure, leave it unset: courses with practical stages then run theory-only until they declare it.
8. What are they hoping to study — this drives the `/add-course` prompts that follow immediately after, now that a real `roster.max_incomplete_courses` exists for `course-compiler`'s Step -1 to gate against. **This question is asked last, deliberately** — it's the one that triggers building, and building shouldn't start before the cap it must be checked against is known.

Fill in what you get; leave the rest unset rather than guessing.

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

## Consent — what each status actually does
**Enforced in code, not just here (v1.14.0).** Every state-writing script checks the learner's consent itself (`tutorlib/consent.py`) and returns `{"written": false, "skipped": "consent …"}` instead of writing — so a missed instruction cannot leak data. Writes fall in three classes: *progress* (`syllabus_status`, `current_stage`/phase, roster state, remediation counters, capability unlocks) and *scheduling* (`session_slot`, review-card intervals) persist under `granted` and `limited`; *signals* (`error_patterns`, `confidence`, `item_mastery`, and every row of `tutor.sqlite3` except card scheduling state) persist only under `granted`; `revoked` persists nothing. A profile whose consent block is unreadable or unrecognised is treated as `revoked`. A skipped result still carries the computed values (e.g. the new confidence) for in-session use; treat `written: false` as "use it now, it will not be remembered".

- **`granted`** — normal operation; every field below writes and persists as designed.
- **`limited`** — teaching proceeds normally this session, but only `syllabus_status`, `current_stage`, and `current_phase` persist to `subjects/<course_id>.json` at session end. Scheduling bookkeeping is also kept, because it is not a learner signal and losing it would break spaced review: `session_slot` (in `student_profile.json`, advanced by `slot_advance.py`) and the review decks' `interval_sessions` / `ease` / `lapses` / `due_at_slot` fields. Softer signals — `error_patterns`, `confidence`, `last_session_summary`, and any update to global `learning_signals` — are used in-session to scaffold teaching well right now, but are discarded rather than written. Tell the learner plainly, before the session starts, what won't be remembered.
- **`revoked`** — don't write anything, to either the global profile or any subject file, for the rest of this session. To actually remove data already stored, see `data-erasure`.

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

## Write rules
- A course-facing skill may only write to the currently active learner's own `subjects/<course_id>.json` — never another course's file, never another learner's folder, never `student_profile.json` directly except through `/profile` (including capability declarations), intake, `slot_advance.py` (which touches only `session_slot` and its timestamp), or `resume_enrollment.py` when reopening a level (which touches only `highest_level_cleared`, and only lowers it).
- If something a course observes seems to generalize across subjects, surface it to the learner and ask before writing it to the global profile — don't write cross-subject signals silently.
- Append-only for `error_patterns` (entries are resolved, never deleted).
- Don't downgrade a `syllabus_status` entry on a single weak moment — only on a genuine test result. `confidence` moves only through `confidence_update.py`.
- `roster_state` transitions (`dormant`, `test_pending_convergence`, `dropped`) are owned by `journey-planner` and `course-runner` respectively; `profile-kernel` only ever reads them for display. `cohort_id` is owned by `course-compiler` alone, written once at enrollment and never touched again by any skill, including this one.

## Dropping a course
`/drop <course_id>` (mechanics defined in `journey-planner`) preserves `subjects/<course_id>.json` exactly as it stands and frees the roster slot it held — a pause, not a deletion. Re-adding the same course later resumes from wherever it was left, and re-enters the roster cap as if newly added. This is distinct from discarding a *suspended* (ungrounded) course, which a learner may choose to erase with genuinely no trace at all — see `course-auditor`.

## Displaying a full profile
When the learner asks to see their overall profile or progress, read the currently active learner's `student_profile.json` plus every file under their own `subjects/`, and present a combined, read-time-only view — never another learner's folder, even if their `user_id` is known. Always surface `highest_level_cleared` and current roster occupancy (e.g. "2 of 2 incomplete-course slots in use") plainly, since both directly determine what the learner can do next. Also show declared `capabilities`, and mark any course that is running theory-only. Standalone courses hold roster slots like any other unfinished course, but have no level and never affect `highest_level_cleared`; list them as "standalone". Something like:

> **Global:** [preferences, learning signals, highest level cleared: 2]
> **Roster:** 2 of 2 incomplete slots in use *(take this from `roster_check.py`'s `roster_occupancy`, which counts dormant level-locked courses as well as live ones)*
> **OU Contract Law:** S4 of 10, confidence: medium, roster state: active
> **GCSE Chemistry:** S2 of 8, confidence: high, roster state: test_pending_convergence

## What this deliberately avoids
No merge-scoring formulas, no confidence-weighted arbitration, no hash-chained audit, no placement diagnostic, no attestation of external prior credit (both explained fully in `course-compiler`, for the same underlying reason: this system can only trust what it verified itself). Cross-subject and cross-learner bleed is prevented structurally, by folder and file boundaries — not by an algorithm arbitrating conflicting signals after the fact.
