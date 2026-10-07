---
name: profile-kernel
description: Multi-learner profile system for the tutor — handles /run, /add-profile, /profile, and the first-ever-load intake landing flow when /EDU/profile/ is completely empty. Owns the one cumulative unlock ledger (highest_level_cleared) and the roster capacity a learner has committed to.
---

# Profile Kernel (roster-capped, level-ledger, capability declarations, isolated by folder)

**Contract**
- **Owns:** `student_profile.json` (created by `profile_init.py`, changed only by `profile_set.py`: intake answers, `/profile` edits, consent, capabilities), `access.json`, the session-slot advance (`slot_advance.py`), deployment of scripts (`bootstrap_scripts.py`); `highest_level_cleared` is raised only by `journey-planner` and lowered only by `resume_enrollment.py`.
- **Reads:** `resolve_root.py` (data root), `verify_session.py` (last session's completeness).
- **Calls:** `bootstrap_scripts.py`, `resolve_root.py`, `slot_advance.py`, `verify_session.py`, `apply_capabilities.py`, `profile_init.py` (create), `profile_set.py` (later changes), `confirm_access.py`.
- **Emits:** "Running profile: …", plain statements of what consent means and what will not be remembered, the last-session audit when something is missing.
- **Never:** reads or writes another learner's folder; guesses a close user id; creates a profile on `/run`; sets a capability or credit on the learner's behalf; back-fills a grade the audit found missing.
- **Failure modes:** data-root problems reported by `resolve_root.py` → tell the learner exactly and stop; unknown user id → offer `/add-profile`.

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
`/EDU/profile/` deserves exactly the same access confirmation `course-compiler` requires for `/EDU/courses/<course_id>/` — having file access through a shared parent connection is not the same as the person having deliberately isolated it. On first-ever load, before intake begins, ask plainly: *"Do you want `/EDU/profile/` connected as its own isolated folder, or to proceed under the shared connection as-is?"* Record the answer with `confirm_access.py <the /EDU/profile/ dir> isolated|shared <today>` (writes `access.json`) and don't proceed to intake until it's answered. One-time per installation, not per learner.

## Landing logic (what happens when this system is opened)
**Before even the `/EDU/profile/` check below, run the bootstrap script — don't hand-derive whether the deployed scripts need updating:**
```
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/bootstrap_scripts.py ${CLAUDE_PLUGIN_ROOT}/scripts ${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json <the resolved path to this install's /EDU/.tutor-scripts/>
```
**On resolving that last path — this is the one place in this whole file where it matters enough to say explicitly: `/EDU/` is never a literal path.** It's this plugin's name, everywhere, for whatever real folder this install has actually connected as its tutor data root — a different location on every machine (a different drive letter, a different OS, a different folder name even), exactly the same way `/EDU/courses/` and `/EDU/profile/` elsewhere in this file already resolve to wherever *this* install's real folder is, not to any one install's actual path. Resolve `/EDU/.tutor-scripts/` the identical way you'd resolve `/EDU/profile/` for the check right below this one, on this same machine, in this same session — never reuse a path seen on a different install or a different session's device listing.

The script itself decides whether anything needs writing — a plain semver comparison between what's already deployed (its own `.manifest.json`) and this running plugin's own `version` in `plugin.json`, done as a real tuple compare rather than eyeballed, because a naive string compare gets an update like `1.9.0` → `1.10.0` backwards. Its `action` field tells you what happened: `deployed_fresh` (nothing was there yet — this install's first time seeing this plugin), `updated` (an older deployed copy was replaced with this plugin's current one — report the version jump plainly, the same way `course-auditor`'s own schema migrations are always reported, never silent, even though this one needs no separate confirmation since it never touches any learner's own data), `up_to_date` (no-op), or `warning_target_newer_than_bundle` (left untouched — surface this to the learner/you rather than guessing which side is right). This closes the gap the previous "copy once, never touch again" version of this design left open: a real fix to one of these scripts' own logic now actually reaches an install that already has an older copy, instead of being silently stuck there forever.

**Check the data root in code, not by eye.** Once the scripts are deployed, run `python3 /EDU/.tutor-scripts/resolve_root.py` (it finds the root from its own location, `--root`, or `$EDU_ROOT`). If it reports `problems` (no `courses/`, scripts not deployed, wrong folder connected), tell the learner exactly what it says and stop until that is fixed; do not guess another folder.

**Then check `/EDU/profile/` first, before anything else, every time this system is opened.**

- **If `/EDU/profile/` is empty (no user folders at all)** — first-ever load. Skip `/run` entirely; there's nothing to run yet. Confirm folder access (above), run the intake conversation through question 7 (roster capacity, then the optional sharing-work question) and write `student_profile.json` with those fields set, *then* ask what subjects the learner wants to study (one `/add-course` per subject, confirmed individually — never silently looped; `course-compiler`'s Step -1 now has a real cap to check on every one of these). Once every chosen course exists, run `/plan` (journey-planner) once as the final onboarding step.
- **If `/EDU/profile/` has one or more user folders already** — `/run <user_id>` is required before `/continue`, `/profile`, `/plan`, or any teaching can proceed. If the learner tries to jump straight to teaching, ask them to `/run <user_id>` first (or `/add-profile` if new).

## `/run <user_id>` — outcomes
- **Match found** → load that folder as active for the rest of the session, then advance the session-slot counter exactly once — `python3 /EDU/.tutor-scripts/slot_advance.py <that learner's student_profile.json>` — and confirm plainly ("Running profile: Alex"), proceed. The counter (`student_profile.json.session_slot`, absent = 0) is what `review-scheduler` compares every card's `due_at_slot` against; it advances once per session here and nowhere else (not per course, not per `/review`, never by date), so "what slot are we on" is always read from disk, never guessed. The script skips itself, and says why, if consent is `revoked` or if the last advance was under three hours ago (so typing `/run` twice in one sitting, or re-running it after a disconnect, is one session, not two) — in both cases it still reports the current slot, and that is the number to use.
- **Then audit the last session — once, right after the slot advances.** Run `python3 /EDU/.tutor-scripts/verify_session.py <that learner's folder> --previous`. It reads the session ledger (every state-changing script logs one line) and checks that the previous session's writes are complete (e.g. a stage pass without its confidence update or review cards). If `ok` is true and `findings` is empty, say nothing. If it lists findings, tell the learner plainly what the record shows ("last session recorded a pass for S2 but its review cards were never created") and offer to repair it by running the missing step; **never invent or back-fill a grade, and never repair without saying so**. Findings with severity `warning` are mentioned briefly. This exists because a script cannot make the model call it; the ledger makes a skipped call visible.
- **No match found** → do not create one, do not guess a close match. Say plainly: *"No profile found for '<user_id>'. Try again, or create a new profile with `/add-profile <user_id>`?"*

## Intake questions
The questions asked once per new learner (education level, explanation style, support needs, accessibility, availability, roster capacity, image sharing, goals) are in `intake.md` in this folder. `/add-profile` loads it; on a first-ever load, read it before starting intake. Ask conversationally, one thing at a time; record only what the learner gives.

## Profile schemas
The global profile schema (with `capabilities`, `highest_level_cleared`, roster cap), the per-course micro-profile schema, how to display a full profile and what dropping a course does are in `profile-schema.md` in this folder. `/add-profile` and `/profile` load it; read it before creating, showing or editing a profile. Authoritative field shapes: `${CLAUDE_PLUGIN_ROOT}/docs/DATA_MODEL.md` and the JSON Schemas.

## Consent — what each status actually does
**Enforced in code, not just here.** Every state-writing script checks the learner's consent itself (`tutorlib/consent.py`) and returns `{"written": false, "skipped": "consent …"}` instead of writing — so a missed instruction cannot leak data. Writes fall in three classes: *progress* (`syllabus_status`, `current_stage`/phase, roster state, remediation counters, capability unlocks) and *scheduling* (`session_slot`, review-card intervals) persist under `granted` and `limited`; *signals* (`error_patterns`, `confidence`, `item_mastery`, and every row of `tutor.sqlite3` except card scheduling state) persist only under `granted`; `revoked` persists nothing. A profile whose consent block is unreadable or unrecognised is treated as `revoked`. A skipped result still carries the computed values (e.g. the new confidence) for in-session use; treat `written: false` as "use it now, it will not be remembered".

- **`granted`** — normal operation; every field below writes and persists as designed.
- **`limited`** — teaching proceeds normally this session, but only `syllabus_status`, `current_stage`, and `current_phase` persist to `subjects/<course_id>.json` at session end. Scheduling bookkeeping is also kept, because it is not a learner signal and losing it would break spaced review: `session_slot` (in `student_profile.json`, advanced by `slot_advance.py`) and the review decks' `interval_sessions` / `ease` / `lapses` / `due_at_slot` fields. Softer signals — `error_patterns`, `confidence`, `last_session_summary`, and any update to global `learning_signals` — are used in-session to scaffold teaching well right now, but are discarded rather than written. Tell the learner plainly, before the session starts, what won't be remembered.
- **`revoked`** — don't write anything, to either the global profile or any subject file, for the rest of this session. To actually remove data already stored, see `data-erasure`.

## Write rules
- A course-facing skill may only write to the currently active learner's own `subjects/<course_id>.json` — never another course's file, never another learner's folder, never `student_profile.json` directly except through `profile_init.py` / `profile_set.py` (intake, `/profile`, capability declarations, consent), `slot_advance.py` (which touches only `session_slot` and its timestamp), or `resume_enrollment.py` when reopening a level (which touches only `highest_level_cleared`, and only lowers it).
- If something a course observes seems to generalize across subjects, surface it to the learner and ask before writing it to the global profile — don't write cross-subject signals silently.
- Append-only for `error_patterns` (entries are resolved, never deleted).
- Don't downgrade a `syllabus_status` entry on a single weak moment — only on a genuine test result. `confidence` moves only through `confidence_update.py`.
- `roster_state` transitions (`dormant`, `test_pending_convergence`, `dropped`) are owned by `journey-planner` and `course-runner` respectively; `profile-kernel` only ever reads them for display. `cohort_id` is owned by `course-compiler` alone, written once at enrolment and never touched again by any skill, including this one.

## What this deliberately avoids
No merge-scoring formulas, no confidence-weighted arbitration, no hash-chained audit, no placement diagnostic, no attestation of external prior credit (both explained fully in `course-compiler`, for the same underlying reason: this system can only trust what it verified itself). Cross-subject and cross-learner bleed is prevented structurally, by folder and file boundaries — not by an algorithm arbitrating conflicting signals after the fact.
