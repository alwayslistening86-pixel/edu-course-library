# B-05.2 — Script inventory and proposed roles

> Checked at v1.95.0: all 71 top-level scripts have a row (`mark_answer.py` was added after the first pass and sits at the end of Table 1), and every `file:line` citation points at a line that exists. Roles are proposals for owner review, not decisions; nothing here changes behaviour.

Status: **proposal for owner review** (7 Oct 2026). Nothing here changes behaviour. It feeds the B-05 policy table (`docs/TASKS.md`, B-05; `docs/adr/0010-proposed-roles-and-portable-profile.md`).

Source note: this is micro-task B-05.2 of `docs/WAVE7.md`; the research that produced it worked from `docs/TASKS.md` (B-03 to B-07) and ADR 0010 before that plan was merged. Every row below comes from the script's own docstring and code in `plugin/generic-tutor/scripts/` (71 top-level `.py` files; `scripts/toolkit/` and `scripts/tutorlib/` are not covered).

## How to read this

**Roles** (ADR 0010): `tutor-voice` = everyday study chat, never writes durable state. `examiner` = stage tests, grading, diagnosing causes, anything that moves progress. `staff` = installs, audit, course changes, backups/erase. `any` = pure read-only status, safe for all roles.

**Class** (what the most-writing mode of the script can do):
- **R** reads only (R* = reads only, but can write a derived output file the caller names, not learner state)
- **P** writes progress state (`profile/<id>/subjects/*.json`, review decks, `tutor.sqlite3`, ledger)
- **L** writes learner profile or consent (`student_profile.json`, `access.json`)
- **C** writes course content (`courses/...`)
- **B** writes backups or erases (backup/export zips, deletion)
- **I** installs or deploys (`.tutor-scripts/`, hooks)

**Caller**: "learner" = a skill/command that runs in a normal learner session (course-runner `/continue`, tutor-core, review-scheduler `/review`, exam-simulator `/mock`, journey-planner `/plan` `/drop`, health-status `/status` `/dashboard` `/readiness` `/doctor`, profile-kernel landing `/run` `/profile` `/add-profile`, stage-recap). "staff" = course-auditor (`/audit`), course-compiler (`/add-course`), install/deploy. Derived by grepping `skills/` and `commands/` for the script name.

**Role column** gives the roles allowed for the script as a whole. Where behaviour differs by sub-command or flag, the second table refines it. `needs owner decision` marks a row where I was unsure and chose the narrower set.

Consent classes in code (`tutorlib/consent.py`) are noted where relevant: progress and scheduling persist under `granted` and `limited`; signal persists under `granted` only.

## Table 1 — every script (71)

| # | Script | Purpose (from docstring) | Class | Writes (paths) | Caller | Proposed roles | Reason / flag |
|---|---|---|---|---|---|---|---|
| 1 | apply_capabilities.py | Brings one enrolment's practical-stage status (`withheld`/`unsat`) into line with the learner's declared capabilities | P | `subjects/<course>.json` (`syllabus_status`); `--dry-run` writes nothing | learner (course-runner on `/continue`, profile-kernel on declare); also compiler, auditor | examiner, staff | Moves `syllabus_status`, so not tutor-voice. `--dry-run` is read-only. Paired with the `capabilities.*` setting in profile_set |
| 2 | assemble_paper.py | Builds a timed practice paper from `question_bank.json` (no mark scheme in output) | R | none | learner (exam-simulator `/mock`) | examiner, staff | Read-only, but it is test material for a mock that the examiner marks and records; kept narrow |
| 3 | audit_run.py | Whole deterministic audit of the library as one JSON report, diffed with a previous one | R* | optional `--out <report.json>` | staff (`/audit`) | staff | Audit flow only; the report file is the only write |
| 4 | audit_status.py | Decides "an audit is recommended" per course | R | none | staff (course-auditor) | staff | Only the auditor calls it |
| 5 | backup_profile.py | Full physical backup of one learner as a checksummed zip | B | `<profile_root>/../backups/<id>-backup-<UTC>.zip` (or `--out`); reads the learner folder, SQLite via online backup | learner command `/backup` (backup-restore) | staff | Backups class. **needs owner decision**: it is the learner's own data and a learner-run command (see Q2) |
| 6 | bootstrap_scripts.py | Deterministic install/update of the shared `.tutor-scripts/` from the running plugin | I | `.tutor-scripts/` (copies, deletes stale files, rewrites manifest) | profile-kernel landing every session; hook_guard SessionStart | staff | Installs/deploys. **needs owner decision**: it runs on every landing, so a student-mode session needs it done by someone (Q2) |
| 7 | calibration.py | Opt-in check that the learner's "I'll pass" rating matches outcomes (L-15) | P | `subjects/<course>.json` (calibration opt-in and ratings; signal-class) | learner (course-runner) | examiner | Writes learner signal; `report` is read-only (see Table 2) |
| 8 | change_log.py | Reads a course's `change.md` as data | R | none | staff (course-auditor) | staff | Course-maintenance only |
| 9 | cohort_status.py | Deterministic cohort/convergence grouping and level walk | R | none | learner (course-runner, journey-planner) | any | Pure computation from files; the writes it informs are done by other scripts |
| 10 | confidence_update.py | `compute` (pure) and `apply` (read-modify-write) of the course `confidence` value | P | `apply`: `subjects/<course>.json` `confidence`; `tutor.sqlite3` `confidence_events` (signal-class) | learner (course-runner, tutor-core, profile-kernel) | examiner | `apply` moves a signal; `compute` is pure (Table 2) |
| 11 | confirm_access.py | Records the learner's one-time "isolated or shared connection" answer | L | `<courses or profile folder>/access.json` | learner (course-runner, profile-kernel) | examiner | Consent-type record that unlocks teaching for every course (gate_check accepts it). **needs owner decision** |
| 12 | course_bundle.py | Moves a course between libraries as one verified zip, no learner data | C | `export`: the named `.zip`; `import`: `courses/<id>/` (stage dir, replace aside) | none (no skill or command mentions it; CLI only) | staff | Course content. `--dry-run` on import writes nothing |
| 13 | coverage_check.py | Whether every itemised syllabus item is taught by some stage | R | none | staff (auditor, compiler); named in course-runner | examiner, staff | Read-only. Not `any` because its caller list is staff-led; tutor-voice sees coverage through `status.py` |
| 14 | currency_report.py | Which courses need their sources looked at again (reads snapshots) | R | none | staff (auditor) | staff | Auditor only |
| 15 | dashboard_html.py | Self-contained static HTML progress page for one learner | R* | the `<output.html>` path given | learner (health-status `/dashboard`) | examiner, staff | Writes no state, only a file the caller names. **needs owner decision** whether tutor-voice may create a file (Q3) |
| 16 | deck_add.py | The one place new review cards enter a deck (`add`, `retire`, `mature`) | P | `subjects/<course>_review_deck.json`; `tutor.sqlite3` card rows | learner (review-scheduler, stage-recap) | examiner | `add`/`retire` write (scheduling-class); `mature` is read-only (Table 2) |
| 17 | diagnostic_gate.py | Decides whether the practice-phase diagnostic branch should fire | R | none | learner (course-runner, tutor-core); auditor | any | A trigger check from the error log; it never classifies cause. The follow-up `error_log append` is examiner-only, so see Q1 |
| 18 | doctor.py | One-shot health check of an install | R* | creates and deletes a probe temp file in each learner folder (writability test) | learner (`/doctor`, health-status); backup-restore | examiner, staff | Not pure read-only (probe file). **needs owner decision** whether tutor-voice may run it |
| 19 | enrich_plan.py | What optional content layers each course still lacks | R | none | staff (auditor) | staff | Audit enrichment pass |
| 20 | enrol.py | Creates a learner's progress file for a course | P | `profile/<id>/subjects/<course>.json` (new, schema 5) | learner (course-runner defensive create; planner, exam-simulator mentions); staff (compiler, auditor) | examiner, staff | Creates progress state. **needs owner decision**: course-runner calls it mid-session |
| 21 | erase_profile.py | Irreversible deletion of one learner's data | B | deletes `profile/<id>/` (needs `--confirm "ERASE <id>"`); without it reports only | learner command `/erase` (data-erasure) | staff | Erase class. **needs owner decision** (Q2) |
| 22 | error_log.py | Bookkeeping for `error_patterns` (`append`, `resolve`, `query`) | P | `subjects/<course>.json` `error_patterns`; `tutor.sqlite3` `error_events` | learner (course-runner, tutor-core, exam-simulator, review-scheduler); auditor | examiner | Records a diagnosis (cause) = the B-04 problem; `query` is read-only (Table 2) |
| 23 | exam_guidance.py | What exam guidance a course holds (technique text, command words) | R | none | learner (tutor-core) | any | Reads published board guidance only |
| 24 | exam_to_bank.py | Turns `exam/exam.md` items into a `question_bank.json` proposal | C | `--write`: `<course>/question_bank.json`; default prints a proposal | staff (auditor) | staff | Course content with `--write` |
| 25 | export_profile.py | Bundles one learner's data into a single zip | B | `<output.zip>` (refused if inside the profile root) | learner command `/export` (data-export) | staff | Backups/export class. **needs owner decision** (Q2) |
| 26 | gate_check.py | Evaluates course-runner's five ordered gates | R | none | learner (course-runner, review-scheduler) | any | Read-only decision; reports whether testing is allowed |
| 27 | goal_map.py | Learner goals to prioritised syllabus items (`items`, `set`, `clear`, `report`) | P | `set`/`clear`: `subjects/<course>.json` `goal_map` (progress-class) | learner (journey-planner) | examiner | `items`/`report` read-only (Table 2). **needs owner decision**: goal-setting is chat (Q3) |
| 28 | history_report.py | Canned reports over the append-only history database | R | none (opens `tutor.sqlite3` read-only) | staff (auditor) | staff | Cross-session learner analytics for the auditor |
| 29 | hook_guard.py | Optional Claude Code hooks: SessionStart deploy, PreToolUse guard, Stop verify | I | SessionStart runs bootstrap; writes `<tmp>/generic-tutor-hooks/<session>.json`; no learner data | hooks only (`hooks/hooks.json`), never called by the model | any (hook; not role-called) | It is the natural place to enforce the role table (Q4). **needs owner decision** |
| 30 | invariants.py | Cross-file consistency checks for one learner | R | none | staff (auditor) | staff | Auditor only |
| 31 | item_mastery.py | Per-item Bayesian knowledge tracing (`observe`, `status`) | P | `observe`: `subjects/<course>.json` `item_mastery`; `tutor.sqlite3` mastery rows (signal) | learner (profile-kernel, tutor-core) | examiner | `observe` takes a correct/incorrect judgement. `status` read-only (Table 2) |
| 32 | list_courses.py | Every course with the learner's standing, filterable | R | none | learner (course-runner, `/list-courses`) | any | Status listing |
| 33 | migrate_schema.py | Mechanical schema-version migration (`course`, `subject`) | C | `course.json` or `subjects/*.json` in place, plus `<file>.pre-migrate-v<N>.bak`; `--dry-run` writes nothing | staff (auditor) | staff | Changes course files (and a learner file in `subject` mode) |
| 34 | next_items.py | Which syllabus items practice should focus on next | R | none | learner (course-runner, tutor-core) | any | Selection from existing measures; read-only |
| 35 | paraphrase_check.py | Does a course copy its sources instead of paraphrasing | R | none | staff (compiler) | staff | Compiler check |
| 36 | plan_estimate.py | Slots left, and feasibility before a target date | R | none | learner (journey-planner) | any | Read-only estimate |
| 37 | plan_target.py | Record or clear an optional target date (`set`, `clear`) | P | `subjects/<course>.json` `target` (progress-class) | learner (journey-planner) | examiner | Both sub-commands write. **needs owner decision** (Q3) |
| 38 | postcompile_gate.py | Combines structure and coverage checks into one `can_ship` verdict | R | none | staff (auditor, compiler) | staff | Compiler/auditor gate |
| 39 | practice_pick.py | Which practice item next, and a record of items already met (`next`, `used`) | P | `used`: `subjects/<course>.json` `practice_used` (progress-class) | learner (course-runner) | examiner | `next` is read-only (Table 2). `used` is written each time an item is served: **needs owner decision** (Q3) |
| 40 | prereq_check.py | Course prerequisites (`requires_complete`) check | R | none | staff (compiler) | staff | Same rule gate_check applies at teaching time |
| 41 | prereq_pointer.py | Where the learner should go back to when the cause is `missing_prerequisite` | R | none | learner (course-runner) | any | Read-only suggestions |
| 42 | profile_init.py | Creates a new learner profile from intake answers | L | `profile/<id>/student_profile.json` (new); ledger line | learner (profile-kernel `/add-profile`, first load) | examiner, staff | Creates the learner's record; not tutor-voice. **needs owner decision** whether student mode may create profiles (Q2) |
| 43 | profile_set.py | Changes one whitelisted setting in `student_profile.json` | L | `student_profile.json` field (incl. `consent.status`, `learning_signals.*`) | learner (profile-kernel `/profile`) | examiner | Splits by field (Table 2). **needs owner decision** (Q3) |
| 44 | publish_course.py | Makes a compiled course live only after the post-compile gate (`publish`, `discard`) | C | `courses/.build-<id>/` renamed to `courses/<id>/`; `discard` removes the build folder | staff (compiler) | staff | Course change |
| 45 | purge_history.py | Selective irreversible deletion short of `/erase` (`history`, `course`) | B | deletes `tutor.sqlite3` (+wal/shm) and `.session_ledger.jsonl`; `course` removes one course's progress, deck, history, ledger lines | learner command (data-erasure) | staff | Erase class. **needs owner decision** (Q2) |
| 46 | readiness.py | Bounded answer to "am I ready?" (evidence and band, never a grade) | R | none | learner (`/readiness`, course-runner, health-status) | any | Read-only status |
| 47 | recent_activity.py | Plain-language view of the write ledger | R | none | learner (health-status) | any | Read-only; ledger holds ids and numbers only |
| 48 | record_grading.py | Keeps, per stage test, which rubric criteria were met and marks (V-09) | P | `tutor.sqlite3` grading rows + ledger line (signal, `granted` only) | learner (course-runner) | examiner | Record of grading; examiner by definition |
| 49 | record_mock.py | Records the result of a mock paper | P | `subjects/<course>.json` `mock_results` (signal-class, last 20 kept) | learner (exam-simulator) | examiner | Practice record, never moves `syllabus_status` but is still a marking result |
| 50 | record_stage_result.py | Owns the stage pass/fail write-back and `current_stage` advancement | P | `subjects/<course>.json` `syllabus_status`, `current_stage`; ledger | learner (course-runner) | examiner | The core "moves progress" script |
| 51 | remediation_state.py | Caps remediation-after-fail and the escalation path (`record`, `reset`, `status`) | P | `subjects/<course>.json` remediation counters (progress-class) | learner (course-runner); auditor | examiner | `record`/`reset` write; `status` read-only (Table 2) |
| 52 | resolve_root.py | Reports where the data root is and whether it looks right | R | none | learner (profile-kernel landing) | any | Read-only; useful to the B-01 "valid profile" check |
| 53 | restore_profile.py | Puts a learner back from a `backup_profile.py` zip | B | `profile/<id>/` (swap in; `--replace` first writes a `-pre-restore` safety zip) | learner command `/restore` (backup-restore) | staff | Overwrites learner data. **needs owner decision** (Q2) |
| 54 | resume_enrollment.py | Flips a dropped enrolment back to live, touching nothing else | P | `subjects/<course>.json` `roster_state`; with `--reopen-profile`: `student_profile.json` `highest_level_cleared` (only lowers) | learner (journey-planner, profile-kernel docs); staff (compiler, auditor) | examiner, staff | Writes profile only with the flag (Table 2). **needs owner decision** |
| 55 | review_math.py | SM-2-lite scheduling: pure calc, or `apply` to a deck | P | `apply`: `<course>_review_deck.json`, `tutor.sqlite3` review rows | learner (course-runner, review-scheduler) | examiner | `apply` writes scheduling state; the pure form writes nothing (Table 2). **needs owner decision** (Q3) |
| 56 | review_select.py | Chooses and orders the cards for a review session | R | none | learner (course-runner, review-scheduler) | any | Deterministic selection |
| 57 | roster_apply.py | Roster and level-ledger changes (`drop`, `advance`, `lock`) | P | `subjects/*.json` `roster_state`; `advance` also `student_profile.json` `highest_level_cleared` | learner (journey-planner `/drop`); staff (compiler `lock`) | examiner, staff | See Table 2 (`--preview` read-only) |
| 58 | roster_check.py | Roster-cap and level-lock computation | R | none | learner (journey-planner); staff (compiler, auditor) | any | Read-only decision |
| 59 | rubric_lint.py | Are a course's rubric criteria observable enough to grade against | R | none | staff (auditor) | staff | Reads rubric (marking material) for course maintenance |
| 60 | scan_untrusted.py | Looks for instruction-like text hidden in web-derived content | R | none | learner (course-runner); staff (auditor) | any | Read-only safety check, exit 0 always |
| 61 | session_plan.py | Fits a session into the time the learner has and where it may stop | R | none | learner (course-runner) | any | Read-only |
| 62 | session_state.py | Per-session fields of the progress file (`phase`, `roster`, `exam`, `notice`, `note`) | P | `subjects/<course>.json` `current_phase`, `roster_state`, `exam_status`, `notices_acknowledged`, `last_session_summary` | learner (course-runner) | examiner | All five sub-commands write (note is signal-class) |
| 63 | slot_advance.py | The one place the persistent session-slot counter moves | L | `student_profile.json` `session_slot`, `session_slot_advanced_at` | learner (profile-kernel `/run`, review-scheduler) | examiner | Writes the profile file. **needs owner decision**: pure bookkeeping at every `/run`, yet tutor-voice cannot write (Q2) |
| 64 | sqlite_store.py | Library for the per-learner history DB; CLI only `backfill` and `check` | P | `backfill`: `tutor.sqlite3` (rebuilds history rows); `check`: read-only | imported by other writers; CLI not named in any skill | staff | `backfill` is a repair tool. `check` is read-only (Table 2) |
| 65 | status.py | One-screen summary of where a learner stands | R | none | learner (many skills, `/status`) | any | The canonical read-only status script |
| 66 | validate_schema.py | Checks a persisted file against its JSON Schema | R | none | staff (auditor); schema docs | staff | Used by the auditor only |
| 67 | validate_structure.py | Structural and sourcing-completeness checks for one course | R | none | staff (auditor, compiler) | staff | Course maintenance |
| 68 | verify_session.py | Did the model make all the state writes a session implies | R | none | learner (profile-kernel `/run` audit of last session; hook Stop) | any | Read-only ledger check |
| 69 | verify_sources.py | Are a course's cited sources still there and unchanged (network) | C | `--write`: `<course>/source_snapshots.json`; default writes nothing; only hashes kept | staff (auditor) | staff | Needs network; writes course metadata with the flag |
| 70 | worksheet_check.py | Does a take-home worksheet give away the stage test | R | none | learner (stage-recap) | examiner, staff | Reads the graded `test.md`; hold-back material, kept off tutor-voice |
| 71 | mark_answer.py | Marks one learner answer against a question's answer key, by script | R | none | learner (exam-simulator) | any | Pure marking; recording the result is a separate writing step (ADR 0012 class 1) |

## Table 2 — sub-commands and flags whose write behaviour differs

| Script | Sub-command / flag | Writes? | What | Proposed roles | Note |
|---|---|---|---|---|---|
| calibration.py | `optin` | yes | opt-in flag in `subjects/<course>.json` (signal-class) | examiner | needs owner decision (Q3) |
| calibration.py | `record` | yes | rating plus pass/fail, signal-class | examiner | |
| calibration.py | `report` | no | | any | |
| confidence_update.py | `compute` | no | pure calculation | any | |
| confidence_update.py | `apply` | yes | `confidence` and `confidence_events` row | examiner | |
| deck_add.py | add (default, cards on stdin) | yes | new cards to review deck, `tutor.sqlite3` card rows | examiner | seeded by stage-recap after a genuine pass |
| deck_add.py | `retire` | yes | removes named cards from the deck | examiner | |
| deck_add.py | `mature` | no | lists mature cards | any | |
| error_log.py | `append` | yes | `error_patterns` entry plus `error_events` row (cause, note) | examiner | the B-04 diagnosis write |
| error_log.py | `resolve` | yes | marks entries resolved | examiner | |
| error_log.py | `query` | no | | any | |
| goal_map.py | `items` | no | | any | |
| goal_map.py | `set` | yes | `goal_map` | examiner | needs owner decision (Q3) |
| goal_map.py | `clear` | yes | removes goals | examiner | needs owner decision (Q3) |
| goal_map.py | `report` | no | | any | |
| item_mastery.py | `observe` | yes | `item_mastery` plus mastery history row | examiner | |
| item_mastery.py | `status` | no | | any | |
| plan_target.py | `set`, `clear` | yes | `target` | examiner | needs owner decision (Q3) |
| practice_pick.py | `next` | no | reads `practice.md` and `practice_used` | any | |
| practice_pick.py | `used` (`fixed` / `generated`) | yes | `practice_used[stage]` | examiner | needs owner decision (Q3) |
| remediation_state.py | `record`, `reset` | yes | remediation attempt counters | examiner | |
| remediation_state.py | `status` | no | | any | |
| review_math.py | pure form (4 numbers) | no | interval/ease calculation | any | |
| review_math.py | `apply` | yes | deck card and review history row | examiner | needs owner decision (Q3) |
| roster_apply.py | `drop --preview` | no (scratch copy of the profile in a temp dir) | consequence report | examiner, staff | copies learner data to temp |
| roster_apply.py | `drop` | yes | `roster_state` dropped, wakes dormant courses | examiner | |
| roster_apply.py | `advance` | yes | `student_profile.json` `highest_level_cleared`, wakes courses | examiner | profile write |
| roster_apply.py | `lock` | yes | marks listed courses dormant | staff, examiner | called by `/add-course` only |
| session_state.py | `phase`, `roster`, `exam`, `notice` | yes | progress-class fields | examiner | |
| session_state.py | `note` | yes | `last_session_summary` (signal-class, text on stdin) | examiner | the summary is tutor-written text (Q3) |
| profile_set.py | `consent.status` | yes | the learner's consent state (always allowed) | examiner | needs owner decision: learner's own control (Q2) |
| profile_set.py | `learning_signals.*` | yes | signal-class settings | examiner | |
| profile_set.py | `preferences.*`, `availability.*`, `roster.max_incomplete_courses`, `goals`, `identity.*` | yes | progress-class settings | examiner | needs owner decision: style/tone/accessibility changes happen in chat (Q3) |
| profile_set.py | `capabilities.share_images` | yes | then `apply_capabilities.py` moves progress | examiner | |
| profile_set.py | `--dry-run` | no | before/after report | any | |
| apply_capabilities.py | `--dry-run` | no | | examiner, staff | |
| resume_enrollment.py | default | yes | `roster_state` only | examiner, staff | |
| resume_enrollment.py | `--reopen-profile` with `--reopen-to` | yes | also `student_profile.json` `highest_level_cleared` (lowers only) | examiner, staff | profile write |
| publish_course.py | `publish` | yes | `courses/<id>/` goes live | staff | |
| publish_course.py | `discard` | yes (deletes) | build folder | staff | |
| course_bundle.py | `export` | yes | one zip, nothing in the library | staff | |
| course_bundle.py | `import` | yes | course folder in `courses/` | staff | `--dry-run` writes nothing |
| migrate_schema.py | `course` | yes | `course.json` plus `.bak` | staff | `--dry-run` writes nothing |
| migrate_schema.py | `subject` | yes | learner `subjects/*.json` plus `.bak` | staff | writes learner data in a staff tool |
| verify_sources.py | default | no (network fetch) | | staff | |
| verify_sources.py | `--write` | yes | `source_snapshots.json` | staff | |
| exam_to_bank.py | default | no | proposal only | staff | |
| exam_to_bank.py | `--write` | yes | `question_bank.json` | staff | |
| audit_run.py | `--out` | yes (a report file) | | staff | |
| sqlite_store.py | `backfill` | yes | rebuilds history rows | staff | |
| sqlite_store.py | `check` | no | | any | used by doctor |
| purge_history.py | `history`, `course` | yes (deletes) | | staff | |
| erase_profile.py | no `--confirm` / `--dry-run` | no | list of what would go | staff | |
| erase_profile.py | `--confirm "ERASE <id>"` | yes (deletes) | | staff | |
| restore_profile.py | `--dry-run` | no | | staff | |
| restore_profile.py | default / `--replace` | yes | learner folder (replace also writes a safety zip) | staff | |

## (a) Summary count (checked against Table 1: 71 rows, one per script)

| Class | Count | Scripts |
|---|---|---|
| R reads only | 33 | assemble_paper, audit_status, change_log, cohort_status, coverage_check, currency_report, diagnostic_gate, enrich_plan, exam_guidance, gate_check, history_report, invariants, list_courses, mark_answer, next_items, paraphrase_check, plan_estimate, postcompile_gate, prereq_check, prereq_pointer, readiness, recent_activity, resolve_root, review_select, roster_check, rubric_lint, scan_untrusted, session_plan, status, validate_schema, validate_structure, verify_session, worksheet_check |
| R* reads only, but writes a derived file or probe | 3 | audit_run (`--out` report), dashboard_html (HTML page), doctor (temporary probe file) |
| P writes progress state | 19 | apply_capabilities, calibration, confidence_update, deck_add, enrol, error_log, goal_map, item_mastery, plan_target, practice_pick, record_grading, record_mock, record_stage_result, remediation_state, resume_enrollment, review_math, roster_apply, session_state, sqlite_store |
| L writes learner profile or consent | 4 | confirm_access, profile_init, profile_set, slot_advance |
| C writes course content | 5 | course_bundle, exam_to_bank, migrate_schema, publish_course, verify_sources |
| B writes backups or erases | 5 | backup_profile, erase_profile, export_profile, purge_history, restore_profile |
| I installs or deploys | 2 | bootstrap_scripts, hook_guard |
| **Total** | **71** | |

Proposed role sets (whole-script, Table 1): `any` 18, `examiner` 17, `staff` 25, `examiner + staff` 10. No script is proposed for `tutor-voice` alone, and none allows `tutor-voice` unless it is `any` (so tutor-voice may call only read-only scripts, plus the read-only sub-commands in Table 2). Of the 18 `any`, 17 are read-only status or decision scripts and one (hook_guard) is hook infrastructure, not model-called.

## (b) Scripts the learner session calls but that write profile data

These are the ones that matter for the tutor-voice role: the learner-session skills and commands invoke them, and each writes under `profile/<id>/` (or `access.json`). Under the proposal every one is examiner-only (or examiner + staff), so a tutor-voice model would have to hand the call to the examiner or leave it undone.

Writes the learner profile or consent (`student_profile.json`, `access.json`):
- profile_set.py (every field; consent.status, learning_signals.*, preferences, goals, capabilities) - profile-kernel `/profile`
- profile_init.py - profile-kernel `/add-profile`, first load
- slot_advance.py - profile-kernel at `/run`, review-scheduler
- confirm_access.py - course-runner, profile-kernel
- roster_apply.py `advance` - journey-planner (also writes `highest_level_cleared`)
- resume_enrollment.py with `--reopen-profile` - journey-planner / compiler

Writes progress, scheduling or signal state (`subjects/*.json`, review decks, `tutor.sqlite3`, ledger):
- record_stage_result.py, record_grading.py, record_mock.py - tests and mocks (course-runner, exam-simulator)
- error_log.py `append`/`resolve`, item_mastery.py `observe`, confidence_update.py `apply`, remediation_state.py `record`/`reset` - the practice-judgement writes (course-runner, tutor-core, exam-simulator, review-scheduler)
- session_state.py (`phase`, `roster`, `exam`, `notice`, `note`) - course-runner
- practice_pick.py `used`, calibration.py `optin`/`record`, goal_map.py `set`/`clear`, plan_target.py `set`/`clear` - ordinary study and planning conversation
- review_math.py `apply`, deck_add.py `add`/`retire` - review-scheduler, stage-recap
- apply_capabilities.py, enrol.py, resume_enrollment.py (default), roster_apply.py `drop`/`lock` - enrolment and roster changes

Learner-run commands that change or remove profile data but are classed staff (backups/erase): backup_profile.py (`/backup`), restore_profile.py (`/restore`), export_profile.py (`/export`), erase_profile.py and purge_history.py (`/erase`).

## (c) Open questions for the owner

1. **Practice-phase judgements (B-04).** error_log `append`, item_mastery `observe`, confidence_update `apply`, remediation_state `record` and record_grading all write during ordinary practice, and diagnostic_gate (read-only, proposed `any`) is what triggers them. If they are examiner-only, who makes them mid-conversation: a separate examiner call, a script-checked proposal from tutor-voice, or deferral to the next test? This one choice decides about a third of the P class.
2. **Learner-owned data commands and landing.** `/backup`, `/restore`, `/export`, `/erase`, purge_history and profile consent changes are the learner's own rights but I classed them staff (the brief's definition). Should "student mode cannot install or edit" still let a learner export or erase their own data? Same for landing: bootstrap_scripts, slot_advance, profile_init and verify_session run at every `/run`. Who runs them in a student-mode session?
3. **Settings the learner states in chat.** profile_set (tone, style, accessibility), goal_map, plan_target, calibration, practice_pick `used`, review_math `apply`, session_state `note` and dashboard_html are natural in chat yet write durable state or files. Keep them examiner-only (safest, but every "make it brief" needs a hand-off), or add a fourth tier such as "learner-settings" that tutor-voice may write?
4. **Enforcement mechanism.** Scripts do not know which role is calling. Is a role passed as `--role`/`EDU_ROLE` and checked in each script (plus hook_guard), or only in the hook guard (Claude Code only; Cowork has no hooks, ADR 0001)? Table 2 shows the policy needs sub-command and flag granularity (for example `error_log query` vs `append`), not script granularity.
5. **Test and marking material.** assemble_paper, worksheet_check, rubric_lint, coverage_check read question banks, `test.md` or rubrics. I kept them off tutor-voice; confirm that a small local model must not see them.
6. **Staff tools that touch learner data.** migrate_schema `subject` rewrites a learner file, roster_apply `drop --preview` copies a learner profile to a temp dir, doctor creates a probe file in the learner folder, history_report reads full history. Acceptable under `staff`, or should staff flows be forbidden from learner folders?
7. **Unused or CLI-only scripts.** course_bundle.py and sqlite_store.py (CLI part) are not named in any skill or command; confirm they are staff-only tools and not candidates for a learner flow.
