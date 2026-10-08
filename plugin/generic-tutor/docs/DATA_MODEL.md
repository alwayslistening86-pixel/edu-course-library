# Data Model (S-01, S-10)

Inventory of every persisted file, derived from the **scripts** (the executable truth), cross-checked against the skills. `/EDU/` below is the install's data root. When a skill and a script disagree, the script wins and the skill is a bug (tracked as S-xx).

Machine-readable JSON Schemas (draft 2020-12) live in `plugin/generic-tutor/scripts/tutorlib/schemas/` (deployed with the scripts): `student_profile`, `subjects`, `review_deck`, `course`, `curriculum_map`, `rubric`, `misconceptions`, `question_bank`, `command_words`, `access`, `manifest`. `schemas/outputs/` holds shapes of script output that skills may quote (`plan_estimate`). Check any file with `validate_schema.py <kind> <file>`. `tests/test_schemas.py` validates every file the scripts write. This file explains ownership and intent; the schemas are the executable definition. `question_bank.json` questions may carry an optional `key` (kinds `mcq`, `numeric`, `short`; shapes and the marking rules in `tutorlib/marking.py`); a keyed question is marked by `mark_answer.py`, never by the model's judgment. Not schematised: `change.md` (checked by `change_log.py`), SQLite tables (checked by `sqlite_store.py`).

## Layout and ownership

```
/EDU/
  courses/<course_id>/                 shared content, one copy per qualification
    course.json            schema v4   written by: course-compiler (build), course-runner (last_live_recheck, grounding_status on vanish), course-auditor (grounding, coverage_status, migration)
    curriculum_map.json                written by: course-compiler; coverage_check.py reads
    rubric.json                        written by: course-compiler only; every entry sourced
    connectors.md                      written by: course-compiler (Step 6.5)
    exam_technique.md, command_words.json   optional; written by: course-compiler (Step 4.8) only where the board publishes guidance; read by validate_structure (`exam_guidance_status`), blocking at the gate only if present and malformed
    change.md                          written by: course-runner / course-auditor (free text today; S-11)
    stages/<stage_id>/{lesson,practice,test}.md, misconceptions.json (optional)
    exam/exam.md                       only if course.json.exam.enabled
  profile/               (or the folder named by $EDU_PROFILE_ROOT; learner folders can live on another drive, courses and scripts stay under the root)
    access.json            {"status": "isolated_confirmed|shared_confirmed", "confirmed_on"}   written by: confirm_access.py (profile/ and courses/ each)
    <user_id>/
      student_profile.json schema v2   written by: profile_init.py / profile_set.py (intake, /profile), slot_advance.py, resume_enrollment.py, roster_apply.py (highest_level_cleared)
      subjects/<course_id>.json  v5    created by enrol.py; field-level owners below
      subjects/<course_id>_review_deck.json  v1   written by: review_math.py apply (reschedule), deck_add.py (new cards)
      tutor.sqlite3                    append-only history; written only by sqlite_store.py
      .session_ledger.jsonl            one JSON line per state-changing script call (tutorlib/ledger.py); read by verify_session.py; written under granted/limited consent only
  .tutor-scripts/                      deployed copy of plugin scripts; written only by bootstrap_scripts.py
```

## `student_profile.json` (v2)

| Field | Type | Owner | Notes |
|---|---|---|---|
| `schema_version` | int | profile-kernel | 2 |
| `learner_id` | string | profile-kernel | = folder name |
| `consent.status` | `granted\|limited\|revoked` | profile-kernel | enforced in code by every writer via `tutorlib/consent.py` (v1.14.0) |
| `identity.{display_name,education_level,locale,home_language}` | string | intake, `/profile` | `locale` sets the spelling variant; `home_language` (optional) turns on glosses of key terms |
| `preferences.{style,tone,accessibility{dyslexia_mode,plain_language_mode,screen_reader_mode}}` | enums/bools | intake, `/profile` | |
| `learning_signals.{pace,working_memory_support_needed,verbal_load_sensitivity,spatial_support_needed,notes}` | enums/string | intake; cross-subject writes need learner OK | |
| `goals` | string[] | intake | |
| `availability.{sessions_per_week,session_minutes}` | int | intake, `/profile` | rate only, never dates |
| `roster.max_incomplete_courses` | int | intake, `/profile` | hard cap checked by `roster_check.py` |
| `highest_level_cleared` | int | journey-planner (raise), `resume_enrollment.py` (lower) | the one cumulative unlock ledger |
| `capabilities.share_images` | `{declared: bool, on: date}` | `/profile` | applied by `apply_capabilities.py` |
| `session_slot` | int (absent = 0) | `slot_advance.py` | advances once per `/run` |
| `session_slot_advanced_at` | ISO UTC timestamp | `slot_advance.py` | double-`/run` guard window; **undocumented in profile-kernel** (drift, fixed by this file) |
| `last_updated` | ISO date | writers | |

## `subjects/<course_id>.json` (v5)

| Field | Type | Owner (never hand-edit) |
|---|---|---|
| `schema_version` | int (5) | `migrate_schema.py` |
| `course_id` | string | `enrol.py`, once |
| `roster_state` | `active\|dormant\|test_pending_convergence\|dropped` | `roster_apply.py` (`dropped`, wake, lock), `enrol.py` (initial), `session_state.py roster` (`active`↔`test_pending_convergence`; `record_stage_result.py` resets to `active` on a pass), course-compiler (initial) |
| `cohort_id` | int \| `"standalone:<course_id>"` | `enrol.py`, once |
| `syllabus_status` | `{stage_id: pass\|fail\|unsat\|withheld}` | `record_stage_result.py` (`withheld`: `apply_capabilities.py`) |
| `current_stage` / `current_phase` | string / `lesson\|practice\|test` | `record_stage_result.py` (stage, and `lesson` on advance); `session_state.py phase` |
| `exam_status` | `locked\|available\|passed` | `session_state.py exam` (refuses `available` until every stage is satisfied) |
| `confidence` | float in [0,1], default 0.5 | `confidence_update.py apply` |
| `error_patterns[]` | `{id, stage_id, item_id, source_phase, cause, misconception_id, rubric_criterion, note, slot, resolved, resolved_at_slot}` | `error_log.py` (`note` at most 400 characters, whitespace collapsed, and refused if it holds an email address, web address or phone number; `cause` one of five; an item id must be one of the course's syllabus items and a `misconception_id` must be the `id` of an entry in that stage's `misconceptions.json` (entries carry an optional stable `id`; `misconception_ids.py` adds them), checked against the course folder when it can be found; an optional `mock: true` when logged with `--mock` from a mock paper: the error is kept and still counts as unresolved, but moves no mastery and no diagnostic trigger) |
| `item_mastery{item_id}` | `{p_mastery, observations, consecutive_misses, …}` | `item_mastery.py` |
| `remediation{stage_id}` | `{attempts, last_cause, escalated, escalated_at_slot}` | `remediation_state.py` |
| `goal_map` | `[{goal, items[], set_on}]` — optional: which syllabus items each of the learner's goals means (the tutor's reading, confirmed with the learner); up to 60 items per goal | `goal_map.py set/clear` (progress class); read by `goal_map.py report` |
| `target` | `{date: YYYY-MM-DD, set_on}` — optional learner-stated deadline | `plan_target.py` (progress class); the only calendar date stored; read by `plan_estimate.py` |
| `grading_used{stage_id}` | integer: the latest `record_grading.py` attempt a stage result consumed — optional | `record_stage_result.py` (a pass needs a newer, unused grading record) |
| `practice_used{stage_id}` | `{fixed: [item numbers], generated: n}` — optional | `practice_pick.py used` |
| `calibration{enabled, entries[{stage_id, rating 1-5, result, on}]}` | optional, opt-in self-rating before tests, newest 50 | `calibration.py` (signal class) |
| `notices_acknowledged[]` | `{id, on}` | `session_state.py notice` |
| `last_session_summary` | string, ≤400 chars | `session_state.py note` (signal class) |
| `last_updated` | ISO date | writers |

`cause` enum (shared by JSON, SQLite CHECK, skills): `slip`, `missing_prerequisite`, `misconception`, `misapplied_procedure`, `comprehension`.

## `*_review_deck.json` (v1)

`{schema_version, course_id, cards[{id, stage_id, item_id|null, criterion|null, front, back, card_type?, interval_sessions, due_at_slot, ease, lapses}]}`. `card_type` is optional: `basic` (the default when absent), `cloze`, `explain_why` or `worked_step` (rules in `tutorlib/cards.py`; `deck_add.py` rejects a card that does not fit its type). New cards are written only by `deck_add.py` (front ≤200 / back ≤400 characters, one question per front, duplicate fronts skipped, ≤12 per stage and ≤300 per deck). Scheduling fields owned by `review_math.py apply`; cards created by stage-recap (new card: interval 1, ease 2.3, lapses 0, due = current slot + 1).

## `course.json` (v4)

Fields: `schema_version, name, requires_complete[(id | [any-of ids])], standalone, selected_options?, folder_access{status}, currency (live|historical), lifecycle? (live|retiring; absent = live), material_vintage, academic_level (int|null), level_source, level_basis (framework|declared|standalone), grounding_status (verified|suspended_ungrounded; `null` = unmigrated, set by `migrate_schema.py`, resolved by auditor Tier 3), last_live_recheck, coverage_status (full|partial|unverified; **derived** by `coverage_check.py`), stage_ladder[], linear, framework, practical_stages{stage_id: [capability]}, learner_notices[{id,text,stages,since}], exam{enabled, requires_all_stage_tests_passed}`; optional `suspension{…}` when suspended.

`_template/course.json` is a skeleton: every value to fill is a `{{PLACEHOLDER}}`, and the post-compile gate blocks any left in a course (N-13).

## `curriculum_map.json`

Keys starting `_` are metadata (`_meta`, `_items_source{document,url,version,itemised_on}`, `_syllabus_items[{id,title,topic_area,tier?}]`, `_declared_exclusions[{id,reason}]`); every other key is a stage id → `{covers_syllabus_refs[], syllabus_topic, covers_items[]}`. `coverage_check.py` is the sole authority on coverage.

## `rubric.json`

`{stage_rubrics{stage_id:{criteria[], pass_threshold, pass_percent?, source{issuing_body, document, reference}}}, exam_rubric{criteria, pass_threshold, source}}`. Every entry sourced; compiler never authors criteria. `pass_threshold` is prose; the optional integer `pass_percent` (1 to 100) is written only where the issuing body publishes a numeric pass mark, never invented, and `record_stage_result.py` refuses a pass whose recorded marks fall below it.

## `tutor.sqlite3`

Append-only history, never read back into teaching decisions (JSON is authoritative). Tables: `error_events`, `item_mastery`, `item_mastery_log`, `review_cards`, `review_log`, `confidence_events`, `grading_results` (per stage test, per rubric criterion: met, marks awarded and available, a hash of the rubric entry; indexes and numbers only, never answer text; written by `record_grading.py`). `PRAGMA user_version` is 3 (history schema; a newer database is refused; v3 only adds `grading_results`). v2 keys `error_events` and `review_cards` by `(course_id, id)` and records `course_id` on `review_log`; v1 keyed them by `id` alone, so two courses producing the same id overwrote each other. A v1 database is migrated in place on first use (`sqlite_store._migrate_v1_to_v2`, tested in `tests/test_history_keys.py`). Included in `/export`; removed by `/erase`; `purge_history.py` can clear it without erasing progress.

## Versioning policy (S-10)

- Each file type has its own integer `schema_version`; bump it only when a field is added, removed, renamed or its meaning changes.
- Every bump ships a mechanical migration in `migrate_schema.py` (never invents values; unknowns become `null` and are reported under `needs_sourcing`) plus a test that migrates a fixture from every earlier version.
- Deployed scripts and plugin version move together (`bootstrap_scripts.py`, semver tuple compare). A script must refuse, with a clear message, a file whose `schema_version` is newer than it understands.
- Docs describe the **current** shape only; history belongs in the changelog.

## Discrepancies found while compiling this inventory

| # | Finding | Status |
|---|---|---|
| 1 | `profile-kernel` documented `confidence` as `low|medium|high` and `error_patterns` as strings; scripts use numeric / structured | fixed (S-02) |
| 2 | `profile-kernel` omitted `item_mastery`, `remediation` and `session_slot_advanced_at` | fixed in skill (first two) / this file |
| 3 | `consent` was enforced in code by one script out of nine writers | fixed in v1.14.0 (E-05, E-06) |
| 4 | `tutor.sqlite3` absent from `/export` and from every skill | open (K-28) |
| 5 | Template `course.json` has the same key set as the skill schema and `migrate_schema.py` (checked), but placeholder prose in value positions makes it a skeleton, not a valid instance | key sets reconciled (S-03); validity open (N-13) |
| 6 | No script refused a newer `schema_version` than it understands | fixed for the six state-writing scripts in v1.17.0 (`tutorlib/state.py`); readers such as `gate_check` still open (S-09/E-20) |

## Repeat-call behaviour (E-13)

What a second identical call does. Pinned by `tests/test_idempotency.py`.

| Script / subcommand | Second call | Why |
|---|---|---|
| `session_state.py notice` | no-op (`written: false`) | acknowledgements are a set |
| `session_state.py phase\|roster\|exam`, `plan_target.py set` | same value, rewritten | assignments |
| `slot_advance.py` | skipped inside the sitting window | one session = one slot |
| `record_stage_result.py apply … pass` | same state; a replay for an *earlier* stage never moves `current_stage` backwards (v1.30.1) | a pass is a fact, not an event |
| `error_log.py resolve` | resolves nothing (`count: 0`) | only open entries resolve |
| `error_log.py append` | a second entry (new id) | each error is an event |
| `confidence_update.py apply`, `item_mastery.py observe`, `remediation_state.py record`, `review_math.py apply`, `record_mock.py` | counts again | each call is one real observation; callers must call once per event |
