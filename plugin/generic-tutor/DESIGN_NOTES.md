# generic-tutor — v0.3.0 → v1.0.0 design notes

This plugin was substantially redesigned from the originally uploaded v0.3.0. This
file records *why*, so a future edit doesn't accidentally undo a deliberate choice.
It is not read by any skill at runtime — it's for humans (and future Claude sessions)
editing this plugin.

## What changed, and why

**Course content and learner progress are now separate.**
v0.3.0 stored a learner's progress inside each course's own folder implicitly, which
meant N learners studying the same qualification could end up on N separately-compiled
copies — wasteful, and a real correctness risk if two compiles of "the same" GCSE Maths
drifted from each other. Now `/EDU/courses/<course_id>/` holds one canonical copy;
`/EDU/profile/<user_id>/subjects/<course_id>.json` holds one learner's progress through
it. `course-compiler` checks for an existing canonical match before ever building fresh.

**Enrollment is gated three ways, outer to inner:**
1. **Level-lock** — the lowest academic level among a learner's *chosen* courses must
   fully complete before anything above it activates. This is a consequence of the
   learner's own course choices, not an asserted prerequisite chain the system invents.
   `highest_level_cleared` is a single cumulative ledger (clearing level N frees
   everything at or below N, forever) — never set by attestation or self-report.
2. **Roster cap** — a fixed number of simultaneously-incomplete courses, committed to
   at intake. Adding beyond it requires completing or dropping one first.
3. **Phase-convergence** — within the active cohort, no course tests until every course
   in the cohort is test-ready. Modeled on how a real school term actually works
   (everyone sits exams in the same window). A course waiting on the rest of its cohort
   fills its slots with spaced review, not idle time or a sneak preview of new content.

**No placement diagnostic, no attestation of prior credit, anywhere, ever.**
Both would let a learner skip stages the system never actually verified — inventing a
diagnostic instrument would violate the compiler's own no-invented-rubric rule, and
attestation would break the honesty the entire slot/level model depends on. The only
way to skip a course here is to have genuinely completed it here.

**Planning is slot-based, never calendar-based.**
`journey-planner` allocates weekly session capacity across active courses using a rate
(`sessions_per_week`) and a sequence of session slots — no days of the week, no dates,
no drift-reconciliation to maintain. A missed week just means the next slot happens
whenever it happens.

**Stage-recap produces one tracked output and one deliberately untracked one.**
On a genuine stage pass: flashcards feed `review-scheduler`'s spaced-repetition deck
(tracked, in-system). A take-home worksheet with an answer key is generated and handed
off as a file (untracked, forgotten by the system the moment it's handed over) — the
one deliberate exception to "everything here eventually feeds back into some piece of
state." It exists purely as an optional extra, never expected to be done.

**course-auditor exists so plugin upgrades never strand existing courses.**
Every `course.json` and `subjects/<course_id>.json` carries `schema_version`; `/audit`
walks anything behind the current schema forward through defined migrations. Grounding
failures (a rubric source that's gone dead) are never silently patched — they suspend
the course, at no cost to the learner's roster capacity, with the learner free to hold
it indefinitely or discard it with no trace at all.

## Deliberately not included
- **Guardian-oversight** — this is a single-user, self-hosted tool: nobody else's
  account, roster, or child is using this instance. The engine's code is public and
  MIT-licensed (as of the CI work in this repo), but that's not the same as a
  multi-tenant deployment with unknown users, which is the scenario guardian-oversight
  controls exist for; that concern doesn't apply here and was cut rather than built
  speculatively.
- **A calendar/reminder integration** — would need real dates, which the slot-based
  model deliberately avoids everywhere.

## 30 Sep 2026 — ts-fsrs and the SQLite schema, checked against LearnOS

No version bump, no code shipped — this closes out the "review LearnOS" thread from the
infra backlog with an actual decision on its two concrete questions, rather than leaving
them open indefinitely.

**`ts-fsrs` (a maintained open-source FSRS spaced-repetition library, used by LearnOS)
— considered, declined for `review_math.py`.** Three real mismatches, not one:
1. FSRS's forgetting-curve math is built on real elapsed *time* since last review — the
   whole model is "how much have you forgotten over these actual days." This system's
   scheduling is deliberately slot-based, never date-based, everywhere else (see
   profile-kernel's `session_slot`, journey-planner's whole design) specifically so
   nothing here has to reason about calendar time. Feeding "elapsed slots" into FSRS in
   place of "elapsed days" breaks the model's own premise: five sessions in one
   afternoon and five sessions over five weeks would be treated identically, when
   FSRS's entire value is telling those two apart.
2. FSRS schedules from a graded recall (Again/Hard/Good/Easy), not a binary
   correct/incorrect. Adopting it would mean asking the model for a finer-grained
   judgment on every review, not just swapping the arithmetic underneath
   `review_math.py` — a real change to `review-scheduler.md`'s own grading contract,
   not a drop-in.
3. FSRS's real advantage over SM-2-family formulas is parameter fitting across large
   populations of real review logs (that's how Anki's own default parameters were
   derived). This is a single-learner (or a handful of learners) system generating at
   most a few hundred graded events a year per course — the same "not enough data to
   fit a heavier model" reasoning `item_mastery.py`'s own docstring already gives for
   choosing BKT over a neural tracker applies here just as directly. There's no
   population to fit against, and no per-learner series long enough to make FSRS's own
   per-user optimization pay for itself either.

`review_math.py`'s existing SM-2-lite formula stays as-is: simple, deterministic,
already tested, and it was built slot-based on purpose rather than by omission. No
action taken.

**SQLite schema — revised, still not wired in.** `schema_design.sql` (drafted 29 Sep,
before error_log.py/item_mastery.py/confidence_update.py existed) was stale against
what those scripts actually ship today. Revised to match their real field shapes
exactly, and to add two tables borrowed directly from reviewing LearnOS's own
`db/schema.sql`: `item_mastery_log` and `review_log`, both append-only observation
histories sitting alongside the existing current-state tables (`item_mastery`,
`review_cards`) — the same current-state/history split LearnOS uses for its own
flashcards/flashcard_reviews pair. Both are genuine new capability, not a straight port
of existing JSON: today's JSON only ever holds the latest belief or the latest card
state, so "has this item's mastery actually been trending up" or "how has this card's
ease moved over a term" aren't answerable at all right now. Everything else in
LearnOS's schema — users/auth, XP/streaks/badges, a social course-sharing registry — is
either already handled elsewhere in this system's own design or deliberately out of
scope, and none of it made it into the revised design. Still just a design reference:
`profile/` holds close to no real usage data yet, so there is no urgency and no
migration has been scheduled.

Separately: cross-checked item_mastery.py's update equations against CAHLR/pyBKT (github.com/CAHLR/pyBKT), the standard peer-reviewed Python BKT reference implementation. They match the standard Corbett & Anderson formulation exactly. No change made; this is an external correctness check, not a new finding.

## Version history
- **v0.3.0** — original upload: profile-kernel, course-compiler, course-runner,
  tutor-core. Per-learner course copies, no roster/level gating, no convergence,
  no spaced repetition, no audit suite.
- **v1.0.0** — this redesign: shared canonical courses, level-lock + roster cap +
  phase-convergence enrollment gating, `journey-planner`, `review-scheduler`,
  `stage-recap`, `course-auditor`, `data-export`, `data-erasure`.
- **v1.0.1** — stress-test fixes, no new features:
  - **Cohort scoping fixed.** `cohort_id` existed in the schema but was never used;
    `course-runner`'s phase-convergence gate defined "cohort" as every active course
    globally, which meant courses at genuinely different, unrelated academic levels
    could end up blocking each other's testing. `cohort_id` is now a real, load-bearing
    field: a cached copy of a course's own `academic_level`, written once at enrollment
    by `course-compiler`, and convergence/bottleneck logic in `course-runner` and
    `journey-planner` now groups by it instead of pooling everything together.
  - **Enrollment-file creation unified.** `course-compiler`'s two paths (dedupe-match
    reuse vs. fresh build) disagreed about who creates `subjects/<course_id>.json` —
    the dedupe path created it immediately, the fresh-build path claimed `course-runner`
    would create it on first `/continue`. Both paths now create it the same way, at the
    same step, with `cohort_id` set at creation; `course-runner` keeps a defensive
    fallback in case the file is ever missing.
  - **Grounding-suspension exemption actually enforced.** `course-auditor` claimed a
    `suspended_ungrounded` course stops counting against the roster cap and drops out
    of cohort convergence "from the moment it suspends," but nothing checked
    `grounding_status` in either `course-compiler`'s Step -1 count or `course-runner`'s
    cohort definition — both now explicitly exclude it, since `roster_state` alone
    never carries a "suspended" value to key off.
  - **Intake reordered.** Roster capacity and availability are now asked (and written
    to `student_profile.json`) *before* the subject-selection question that triggers
    the first `/add-course` calls — previously the subject question came first, so the
    very first onboarding course additions ran before `course-compiler`'s roster-cap
    check (Step -1) had a real cap to check against.
  - **Schema-version wording fixed.** `course-auditor`'s migration-table example
    described a `v2→v3` step that would have contradicted the shipped templates, which
    already carry `syllabus_status` at `schema_version: 2`. Clarified that `course.json`
    and `subjects/<course_id>.json` version independently, and that the only real
    migration this tier performs today is `v0.3.0`'s `schema_version: 1` straight to
    today's `v2` shape.
- **v1.1.0** — deterministic logic extracted from prose into real code, via
  `system-architect`'s methodology. Every v1.0.x skill re-derived its state-machine
  operations from markdown on every invocation, including exactly the cohort-grouping
  and grounding-exclusion logic the v1.0.1 entry above records as having drifted once
  already — narration surviving one bug-fix pass isn't evidence it won't drift again.
  Six scripts now own the correctness-critical arithmetic and structural checks:
  `gate_check.py` (all 5 `course-runner` gates), `cohort_status.py` (cohort grouping/
  convergence, used by both `course-runner` and `journey-planner`), `review_math.py`
  (SM-2-lite interval/ease/lapses arithmetic), `migrate_schema.py` (the Tier 2 schema
  walk), `roster_check.py` (roster-cap occupancy and level-lock floor, used by both
  `course-compiler` and `journey-planner`), `validate_structure.py` (Tier 1 structural
  checks plus Tier 3's rubric-coverage completeness — the same logic that caught
  Latin's unwired stage content during a manual audit, now run automatically). Pure
  judgment — pedagogy (`tutor-core`, untouched), grading a learner's free-text answer,
  and all source/level discovery research — stays prose, unchanged, on purpose.
  **Shipped inside the bundle**, at `scripts/`, and deployed to `/EDU/.tutor-scripts/`
  by `profile-kernel`'s landing logic on every open, via a seventh script
  (`bootstrap_scripts.py`) that version-gates the deploy against the running
  plugin's own `plugin.json` version rather than either always overwriting (which
  would silently clobber a script a prior session already deployed on every unrelated
  plugin update) or never overwriting once deployed (which was this feature's first
  cut, and turned out to mean a genuine bug fix to a script's own logic would never
  reach an install that already had an older copy — see v1.1.1 below). This is a
  deliberate deviation from the `proper-dm` plugin's precedent (inline one-off
  snippets at point of use, no persistent shipped scripts): this logic is shared
  across multiple skills and had already drifted once when duplicated in prose (see
  v1.0.1 above), so a single shared, versioned file per operation was chosen instead.
- **v1.1.1** — fixed the v1.1.0 bootstrap mechanism, in response to a real gap the
  user caught in the first cut before it had even seen a second machine: "copy to
  `/EDU/.tutor-scripts/` only if missing" protected an already-deployed script from
  being silently clobbered by an unrelated plugin update, but also meant a genuine fix
  to a script's own logic could never reach an install that already had it deployed —
  and the deploy target must never be a literal path in the first place, since a
  fresh install on a different machine (different drive, different OS, sometimes a
  differently-named folder entirely) resolves `/EDU/.tutor-scripts/` to somewhere
  else, the same way `/EDU/courses/` and `/EDU/profile/` already do everywhere else in
  this plugin. `bootstrap_scripts.py` now does a real version-gated update — a tuple
  semver compare against a `.manifest.json` written at the deploy target, not a
  string compare (which gets `1.9.0` → `1.10.0` backwards) and not left to a model to
  eyeball each session. `profile-kernel`'s landing logic runs it before anything else,
  every time, and reports whatever it did (`deployed_fresh` / `updated` / `up_to_date`
  / a `warning` if the target is somehow ahead of the running plugin) — following the
  same "auto-applied, always reported" discipline `course-auditor`'s own Tier 2
  already established for schema migrations, since this never touches learner data
  and so doesn't need that tier's extra confirmation gate.
  - **Review-deck reset added to duplicate-merge handling.** The <60%-progress
    duplicate-merge path reset `syllabus_status`/`current_stage` but never mentioned
    the learner's `review-scheduler` deck, whose cards are tagged with `stage_id`s from
    the losing copy's own ladder. The deck is now explicitly cleared on that reset path,
    alongside a `cohort_id` re-sync to the canonical course's `academic_level`.

- **v1.1.2** — four defects found by external review and reproduced against the shipped
  scripts before fixing; no new features.
  - **A finished course blocked its own cohort and kept its roster slot.** `roster_state`
    has no `complete` value, and `cohort_status.py` / `roster_check.py` only looked at
    `roster_state`, so a course with every stage (and the exam) passed stayed an eligible
    "not ready" bottleneck (`converged: false`) and still counted against
    `roster.max_incomplete_courses`. Fixed by deriving completeness from `syllabus_status`
    + `exam_status` in one shared helper (`is_complete`) rather than adding a stored state
    that a skill could forget to write. Complete members stay in a cohort's `members`
    (flagged) so the `highest_level_cleared` check can still see the whole cohort.
  - **Spaced repetition could stall at interval 1.** Two lapses drop ease to 1.9;
    growth = 1.7 x 1.9/2.3 = 1.40, and round(1 x 1.40) = 1, so the card never advanced
    (and every miss reset it to 1). `review_math.py` now floors the new interval at
    `old + 1`, rounds half-up (Python's `round` is banker's), and recovers ease by 0.05
    per correct recall (capped) so lapses aren't permanent.
  - **No persistent slot counter.** `due_at_slot` / `current_slot` were central to
    `review-scheduler` but no field stored the count. Added `student_profile.json.session_slot`
    (absent = 0, so no migration), advanced once per session at `/run` by the new
    `slot_advance.py`, and echoed by `gate_check.py` as `current_slot`.
  - **A dropped course could still be taught.** Gate 3 only blocked `dormant`, so
    `/continue` on a `dropped` course returned `can_proceed: true` and sidestepped the roster
    cap. Gate 3 is now an allowlist (`active` / `test_pending_convergence`, or no enrollment
    file yet); `dropped`, `dormant`, complete and unrecognised states block.
- **v1.1.3** — follow-up fixes to v1.1.2 from a second review pass; also the first `tests/`.
  - *Resuming a dropped course.* Gate 3 now sends a dropped course to `/add-course`, but
    the compiler's dedupe branch only ever created a fresh all-`unsat` enrollment - which
    would have overwritten the preserved progress. Step -0.5 now checks for an existing
    enrollment first: none -> create; `dropped` -> resume (roster cap already checked,
    level-lock consequence re-checked, then `resume_enrollment.py` flips `roster_state`
    only, refusing if the course's ladder changed while dropped); anything else -> already
    enrolled, do not touch. `resume_enrollment.py` is new.
  - *A dropped or suspended course must not hold a level hostage.* `all_complete` now means
    "at least one member complete, none blocking"; unfinished dropped/suspended members are
    reported in `excluded_members` rather than blocking, and the learner is told plainly when
    a level clears with exclusions. Rationale: `roster_check.py` already ignores dropped
    courses for the lock floor, and `/drop` is a pause with no other way out; the cost is
    that a learner can drop a hard course to clear a level, which is accepted and surfaced
    rather than hidden. If a stricter policy is ever wanted, move `dropped` from the
    excluded branch to `blocking` in `cohort_status.py` - it is one line.
  - *One place decides completeness.* `journey-planner`'s clearing step now reads
    `all_complete` / `blocking_members` / `excluded_members` from `cohort_status.py`
    instead of re-deriving completeness in prose.
  - *Spaced-repetition ceiling.* With ease recovery, healthy cards grew 1,2,3,5,9,17,31,57,105
    sessions; `review_math.py` now caps the interval at 30 sessions.
  - *Double `/run`.* `slot_advance.py` records `session_slot_advanced_at` and skips inside a
    three-hour window (`--min-gap-minutes 0` disables it).
  - *`tests/`.* First test directory: `python3 -m unittest discover tests` from the plugin
    root reproduces each defect above against fixtures built on the fly.
- **v1.1.4** — two defects found by review of v1.1.3.
  - **A future-dated `session_slot_advanced_at` froze the counter.** The double-`/run` guard
    skipped whenever `now - last < gap`, and a negative difference satisfies that, so a stamp
    written by a clock that was once wrong (a year ahead, or even 1.5 hours ahead) reported
    "already advanced this sitting" until the clock caught up. The guard now skips only when
    `0 <= elapsed < gap`; a future stamp is treated like an unparseable one - advance and
    overwrite it.
  - **Resume made the level-lock dodgeable, permanently.** With dropped courses excluded from
    level clearing (v1.1.3), a learner could drop a course, clear its level, unlock higher
    courses, then resume the dropped course, and `roster_check.py` returned `joins_freely`
    because the level was at or below `highest_level_cleared`. Two options were considered.
    (a) *Strict:* count dropped courses as blocking. Closes the loophole but creates a trap -
    an abandoned course holds every higher level hostage forever, and `/drop` is a pause with
    no way to discard one enrolment. (b) *Reopen on resume* (chosen): resuming an unfinished
    course whose level was already cleared reopens that level - `roster_check.py --resume`
    computes the lock as if `highest_level_cleared` were one below the course's level, the
    learner confirms the re-lock of the named higher courses, and `resume_enrollment.py
    --reopen-profile ... --reopen-to N` lowers the stored value. This is the only place the
    scalar is ever lowered; completing the course clears the level again the ordinary way. It
    keeps the escape hatch for a course the learner genuinely walks away from, while removing
    the payoff for gaming it (concurrent study of the higher level). One residual: courses
    that woke when the level cleared can have progressed before the resume re-locks them;
    that progress is kept, only further study is gated. If the strict policy is preferred
    instead, move `dropped` from `excluded` to `blocking` in `cohort_status.py` and the
    `--resume` machinery becomes unreachable but harmless.
- **v1.1.5** — three edge cases in the v1.1.4 resume/reopen mechanism, found by review.
  - **A same-level course already active hid the re-lock.** Reopening level 2 (resume X) with W
    (level 2) and Z (level 3) both active put the floor at W's level; `roster_check.py` only
    computed locks when the candidate was *below* the floor, so it said `joins_freely` with
    nothing to lock and Z stayed live. When `reopens_level` is true the script now locks every
    eligible course above the candidate's level, floor or no floor.
  - **Resuming a completed course reopened its level for good.** `roster_check --resume` only
    saw a level number and `resume_enrollment.py` didn't check completeness, so resuming a fully
    passed course lowered the ledger and locked higher courses - and clearing only fires when a
    course *becomes* complete, so nothing would ever re-clear it. `roster_check.py --resume
    --course <id>` now checks completeness itself (`already_complete`, no reopen, no locks);
    `resume_enrollment.py` skips the lowering for a complete course even if told to (belt and
    braces) and still takes it out of `dropped`. `gate_check.py` now reports a complete course as
    complete before it reports it as dropped, so a finished dropped course can't loop the learner
    between "resume it" and "dropped".
  - **The ledger couldn't climb back.** The only raise was `max(current, cohort_id)` for the
    cohort that just finished, so after a reopen (ledger 3 -> 1) finishing the level-2 course set
    it to 2 and level 3 - still fully complete - stayed stranded. `cohort_status.py` now also
    reports `level_ledger` (from `student_profile.json` beside `subjects/`), walking up from the
    stored value through each next cohort while it is `all_complete`, and `journey-planner`
    writes `suggested_highest_level_cleared`. The walk never lowers the ledger, stops at the
    first incomplete cohort, and skips levels with no cohort (vacuously clear).
- **v1.1.6** — a regression in the v1.1.5 walk, and two older gaps in the level-lock, found by review.
  - **The ledger walk stalled on a level with only excluded members.** `level_walk` stepped over
    levels with no cohort, but stopped at any cohort that wasn't `all_complete`, and
    `all_complete` needs at least one complete member. A level whose only course was dropped
    (X at 2, Z at 3 finished, ledger 0) therefore stopped at level 2 with `blocking: []` and
    suggested 0 where v1.1.4's `max(current, cohort)` would have written 3. A cohort with no
    complete member and no blocking member is now `vacuously_clear` and the walk steps over it
    like an empty level, reporting it in `skipped_cohorts`. A level with a blocking member, or
    only a dormant one, still stops the walk.
  - **A new course above the floor had no signal to start dormant.** `lock_consequence` only says
    whether the candidate locks *other* courses. `roster_check.py` now also returns
    `candidate_state` (`active|dormant`) and `locked_behind_level`, computed against the lowest
    unfinished level over live *and* dormant courses (`unfinished_level_floor`); `course-compiler`
    creates the enrolment with that state (both the new-course and the dedupe-match paths).
  - **Dropping the floor course stranded the courses above it.** With X (2) active and Z (3)
    dormant, `/drop X` left nothing live and no floor, and the only dormant->active step was the
    ledger-clearing step, so Z stayed locked behind a course that no longer counted.
    `roster_check.py` now returns `wake_now` (dormant, unfinished, non-suspended courses at or
    below the cleared level or at `unfinished_level_floor`) and `journey-planner`'s `/drop` runs
    it and wakes exactly those - one level, not every dormant level. Safe because the v1.1.4/5
    resume re-lock puts Z back to dormant if X is resumed (tested).
  - The prose steps that consume these fields (`/drop`, ledger clearing, course creation) are
    instructions Claude follows, not code; the scripts and their tests are what is verified.
- **v1.1.7** — one-line fix to a gap 1.1.6's `candidate_state` exposed, found by review.
  - **The roster cap ignored dormant courses.** `roster_occupancy` was `len(eligible)`, and
    `eligible` excludes dormant courses, so with `candidate_state` making above-floor adds start
    dormant they went uncounted: cap 2, one live course and four dormant ones read as occupancy 1,
    and one `/drop` could wake three courses against a cap of 2. Occupancy is now live + dormant
    (unfinished, non-suspended), matching the "N of M incomplete slots in use" display: locking a
    course never frees a slot and waking one is occupancy-neutral.
- **v1.1.8** — the "roster is full" message named only live courses.
  - Step -1 told Claude to name the occupying courses from `eligible_courses`, which excludes
    dormant ones: cap 2 with live A and dormant D refused but named only A, and with only dormant
    D1 and D2 it named nothing. `roster_check.py` now returns `occupying_courses` (live + dormant,
    each with `locked`) and Step -1 names from that, says a locked course can be dropped to free a
    slot, and explains an over-cap roster (learners upgrading from before 1.1.7 who already hold
    more incomplete courses than the cap: nothing is forced down, they just can't add).
- **v1.1.9** — tests only: `tests/fuzz_lifecycle.py` (reviewer-supplied composition fuzz) plus
  `tests/test_fuzz.py`. Several earlier bugs came from scripts chained in prose (add -> lock, drop ->
  wake, resume -> reopen, finish -> walk), which per-script tests can't see. The fuzz runs the real
  scripts in the order the prose prescribes over random add/drop/resume/finish sequences and checks
  five invariants after every step (live courses above the ledger sit at the lowest unfinished level;
  nothing that should have woken is still dormant; occupancy never exceeds the cap; the ledger only
  falls on a resume; no dormant course sits at or below the ledger). Reference run 3,000 x 25 steps:
  0 violations on 1.1.8; the 1.1.6 scripts fail 113 (all the cap bypass) and 1.1.8 with `/drop` not
  waking fails 624 (all a dormant course left asleep). `test_fuzz.py` runs 150 fixed-seed sequences
  under `unittest discover` and asserts the no-wake variant is caught. Scope: one stage ladder, no
  exams, no suspension, no consent modes, no convergence testing, one learner - and it follows the
  prose as read, so it cannot show Claude follows the prose in a live session. No script changed.
- **v1.2.0** — whole-syllabus coverage becomes a checkable property (requirement from the 2026-09-19 audit
  session; the first minor version bump since 1.0.0 because `course.json` moves to schema 3).
  - **The gap.** A course is only worth a learner's time if it teaches the whole specification it claims to be
    built on, and nothing checked that. `curriculum_map.json` held only `covers_syllabus_refs` +
    `syllabus_topic` (an index of broad areas); the runner's live recheck asked only whether a ref still
    *resolved*; `validate_structure.py` asked only whether stage files and rubric sources *existed*. Measured on
    the 28-course library that day: most GCSE/vocational stages had ~220-260 words of lesson, a whole GCSE
    Maths course ~2,100 words - a representative slice of each area, not the syllabus (e.g. Maths S5 Graphs vs
    OCR section 7's 7.01a-7.04c). The claim "this course covers the specification" was unfalsifiable.
  - **The model (index + itemised coverage, in the same file).** `curriculum_map.json` keeps its index role
    and gains `_syllabus_items` (the spec broken into its own atomic items, spec's own numbering as `id`,
    paraphrased `title`), `_items_source` (document/url/version/date - the provenance `/audit` re-fetches to
    detect drift), `_declared_exclusions` (item + mandatory reason: unselected option, out-of-tier), a
    `covers_items` list on each stage, and a `_meta` block stating what the file does and does not claim.
    Top-level `_` keys are metadata, never stages (`_note` already followed this in five maps). No
    weightings, hours, difficulty or dependency fields were added, deliberately: the file stays a map, not a
    second specification, and it does not invent precision the source does not publish.
  - **`coverage_check.py` (new).** Deterministic. Says every item is taught iff it is mapped to a stage AND
    that stage's `lesson.md` names the item's id (a map cannot claim what a lesson never mentions), or is
    declared excluded with a reason. Also reports unknown ids, duplicate ids, stages with no `covers_items`,
    missing provenance, items taught by several stages (reported, not penalised) and lesson word counts
    (reported, never judged - a short lesson is not by itself a defect). Output `computed_status`:
    `full` / `partial` / `unverified` (never itemised).
  - **`course.json` schema 3 adds `coverage_status`.** It is *derived* - the value the script computes -
    never set by hand and separate from `grounding_status` on purpose: thin coverage does not suspend a course
    (suspension is for sources that can no longer be verified) and changes no roster cap, level-lock or
    cohort. `migrate_schema.py` moves every schema 1 or 2 course to 3 in one hop with
    `coverage_status: "unverified"` (a true, stated default) and lists it under `needs_sourcing`; it can never
    write `full`. Enrolment files stay at schema 2 (unchanged).
  - **Audit (`course-auditor` v2): a Tier 3 coverage pass on every course, on every audit.** Unitemised
    course -> re-fetch the live spec, itemise it, map each existing stage to the items it *actually* teaches
    (conservatively; never to flatter the numbers), and **report before writing**. Already itemised ->
    re-derive and diff against `_items_source`, log to `change.md`, correct any stale `full`. A gap is never
    auto-filled: the audit writes no lessons, practice or tests, only annotations naming items a lesson
    already addresses. Remedies are offered, not applied - and appending stages to a ladder that has
    enrolments is called out as a migration of those enrolments (new `unsat` entries, a completed course stops
    being complete, `resume_enrollment.py` refuses a ladder mismatch), to be handled like a duplicate merge.
  - **Compiler (v6).** Step 4.5 now itemises the whole spec first and sizes the ladder to it; every item is
    taught or excluded with a reason; each lesson opens with "Syllabus items taught here"; the status is
    whatever `coverage_check.py` says; step 8 reports the coverage and any uncovered items.
  - **Runner (v6) - disclosure, not a block.** `gate_check.py` adds a non-blocking `coverage` block computed
    from the files each run (so a stale stored `full` cannot silence it): `effective_status`
    `disclose_to_learner`, item counts. When not `full` the runner says so in one plain line at the start of a
    session and `/list-courses` shows each course's status. It is *not* a gate: making it one would make every
    pre-1.2.0 course unteachable until audited, which strands learners rather than protecting them. If a hard
    block is wanted later it is one line in `_evaluate_gates` (block when `effective_status != "full"`); that
    is a policy choice left open here. The runner also treats a stage's `covers_items` as the checklist of what
    the lesson must teach, with `lesson.md` as plan and floor rather than ceiling, expanding from the source
    spec where the file is thin.
  - **Deliberately not done / limits.** (1) There is no per-item learner progress: a stage pass is still one
    test against the rubric, which samples the stage, so a pass does not show every item was mastered (the
    runner is told not to say it does). (2) `full` is *declared* coverage - itemised, mapped, named in the
    lessons; it does not verify the items match the live spec (that is the audit's real-world lookup) nor how
    well a lesson teaches an item, nor what Claude actually says in a session. (3) Directionality of a
    many-to-many relation (introduced in stage A, consolidated in B) is not modelled; only "which stages claim
    this item" is recorded. (4) Lessons are still thin until an audit-driven extension makes them thicker;
    this release makes the gap visible and measurable, it does not close it. (5) Itemising 28 courses is a
    model-driven, per-course task by design - the next `/audit` after upgrading produces it, reported first.
  - **Tests.** `tests/test_coverage.py` (37): every problem class of `coverage_check.py`, the whole-token id
    match (`1.01` is not satisfied by `1.01a`), gate_check's block (non-blocking; stale `full` does not
    silence it; a stored `partial` is never upgraded), migration (v1 and v2 -> 3, idempotent, never `full`,
    subject schema unchanged) and template sanity. Mutation-checked: removing the lesson-names-the-item
    check, accepting a reason-less exclusion, trusting the stored status in the gate, or ignoring
    `problems` in `clean` each fail the suite. Full suite 123 tests, OK.
- **v1.3.0** — standalone courses, list prerequisites, practical units by declaration, learner notices,
  level labels (requirements from the library owner's 2026-09-26 roadmap review).
  - **Standalone courses.** `course.json.standalone: true` = no academic level at all: programming-language
    certifications, AAT, CILEX and the SQE. `roster_check.py` accepts the literal `standalone` as a candidate
    (always `joins_freely` / `active`, locks nothing) and forces a standalone course's level to None in the
    lock arithmetic even if the file carries one; a dormant standalone course always wakes. `cohort_status.py`
    puts each standalone enrolment in its own cohort `standalone:<course_id>` (non-numeric, so `level_walk()`
    never treats it as a level and it never moves `highest_level_cleared`). Standalone courses **do** hold a
    roster slot while unfinished (owner decision: they still use session time).
  - **Prerequisites.** `requires_complete` is a list: ids (all required) and any-of lists. It is the owner's
    statement of the courses needed to *understand* a course - there is deliberately no abstract
    "Level N cleared" rule (considered and rejected 2026-09-26: prerequisites are about content, the level-lock
    about sequencing, and they stay separate). New `prereq_check.py` for /add-course; `gate_check.py` Gate 3
    re-checks before teaching (a prerequisite can be reopened later by a capability declaration). A theory-only
    completion satisfies a prerequisite (owner decision). Pre-1.3.0 single strings still read correctly.
  - **Practical units by declaration.** `course.json.practical_stages` maps a stage to the capabilities it needs
    (only `share_images` today); `student_profile.json.capabilities` records the learner's declaration. New
    `apply_capabilities.py` sets such stages `withheld` (missing capability, never over a real `pass`) or back to
    `unsat` (capability declared), reports `reopens_completed_course` so the caller asks first, and has
    `--dry-run`. `is_complete()` counts `withheld` as done **only on a stage the course marks practical**, so a
    theory-only learner can finish. `gate_check.py` adds a non-blocking `practical` block with the syllabus items
    withheld *for this learner* (items also taught in an open stage are not counted) - coverage itself stays a
    fact about the course and `coverage_check.py` is unchanged.
  - **Learner notices.** `course.json.learner_notices` = `[{id, text, stages|null, since}]`; `gate_check.py`
    returns the ones due for the current stage and not yet in the enrolment's `notices_acknowledged`; the runner
    reads each once and records it. First use: GCSE Latin's Component 3A set texts (2026-27 exams only).
  - **Level labels.** `level_basis` = framework | declared | standalone, shown by /list-courses so a declared
    level is never presented as a framework level.
  - **Schema.** course.json 3 -> 4, subjects 2 -> 3. Mechanical only: the migration never makes a course
    standalone, never adds a prerequisite, practical stage or notice, and leaves an ambiguous `level_basis` null
    and reported. Library decisions go through the auditor's new "Library decisions" section, reported first.
  - **Validator.** `validate_structure.py` adds `v13_problems` (reported, never auto-fixed), including
    `missing_prerequisite_courses` - a prerequisite naming a course that has not been built.
  - **Deferred.** A read-only reference mode for courses kept outside discovery (`/EDU/_historic/`).
  - **Tests.** `tests/test_v130.py` (34). Mutation-checked: 13 single-line breakages of the new rules (withheld
    counted on a non-practical stage, standalone cohort not forced, standalone level not ignored, standalone
    candidate branch removed, dormant standalone not woken, gate prerequisite check removed, acknowledged
    notices repeated, withheld items counted though taught elsewhere, a real pass overwritten by `withheld`,
    any-of treated as all-of, standalone/declared `level_basis` not inferred, missing prerequisite courses not
    reported) each fail the suite. Four 1.2.0 migration tests pinned the old target versions and now assert the
    current constants instead. Full suite 157 tests, OK.
- **v1.4.0** — the tutor-core adaptive-teaching layer: diagnosing during practice (not only after a failed
  test), a real taxonomy for wrong answers, a capped remediation path with escalation, a computed `confidence`,
  and sourced `misconceptions.json` (scoped by the library owner's 2026-09-29 tutor-core scoping review, built
  same day per the owner's explicit go-ahead).
  - **Why this came before the plugin upgrade proper.** The upgrade will presumably touch schema and
    course-facing structure again (the way 1.3.0 added notices, practical stages, prerequisites). Landing the
    adaptive layer first means that upgrade migrates a real, working adaptive layer instead of migrating the
    placeholder fields (`confidence`, `error_patterns`) that had sat undefined in the schema since long before
    1.3.0, and then having to redesign them again immediately after.
  - **The gap this closes.** Before this version, `course-runner`'s only adaptive response was remediation
    after a hard test fail — a learner could visibly flounder through `practice.md`, still attempt the test,
    fail, and only then get any response tailored to what went wrong. `error_patterns` and `confidence` were
    both referenced across `tutor-core`/`course-runner`/`review-scheduler` and defined nowhere. Remediation had
    no cap: nothing stopped a stuck learner cycling remediate→retest→fail indefinitely, and nothing routed
    "this isn't working" anywhere. Test grading checked the final answer against `rubric.json`, never the
    reasoning behind it — a learner could bank a genuine `syllabus_status: pass` by a coincidentally-cancelling
    wrong method or the right option for the wrong reason, and nothing downstream ever revisited it.
  - **Four new scripts, same division of labour as everywhere else in this plugin: the model diagnoses, a
    script owns the bookkeeping.** `error_log.py` gives `error_patterns` an actual shape (five-cause taxonomy —
    slip, missing_prerequisite, misconception, misapplied_procedure, comprehension — each entry linkable to a
    `misconceptions.json` id), computes recurrence, and resolves an entry on a later confident recall so a
    learner isn't permanently marked weak on something they've since mastered. `diagnostic_gate.py` decides
    *whether* a moment is worth stopping for (two misses on one item, a recurring cause in-stage, explicit
    confusion, or a right-answer-wrong-reasoning catch) — deliberately narrow, since firing on every wrong
    answer is just "replay the lesson slower" wearing a different hat; it never diagnoses *why*, only whether
    to ask. `remediation_state.py` is the missing cap: attempt 1 same-framework re-explanation, attempt 2 a
    genuinely different approach plus an earlier-stage check, past attempt 2 `escalate` rather than a silent
    third loop — the stage stays `test_pending_convergence`, logged for the auditor's rollup, never a soft
    pass. `confidence_update.py` is an EWMA-style running value in [0, 1] (pass_clean +0.15, pass_remediated
    +0.05, fail -0.10, an extra -0.05 for a misconception-tagged event), every delta scaled by distance from
    the bound it's approaching so it can never overshoot — same guarantee `review_math.py`'s ease floor/ceiling
    gives that field.
  - **False-positive-mastery.** `course-runner`'s test grading now explicitly calls for grading the method
    (`rubric.json`'s M/A/B tags), not just the final answer, wherever the rubric gives a structured breakdown;
    a reasoning mismatch is itself a `diagnostic_gate.py` trigger, run *before* the grade is recorded, not after.
  - **`misconceptions.json`** (v1.4.0, new, optional, non-blocking): 2-4 sourced entries per stage
    (`{"pattern", "correction", "source"}`), authored by `course-compiler` from real examiner-report /
    specification-commentary sources — the same sourcing discipline as `rubric.json`, including the explicit
    "plausible, not board-documented" escape hatch for a plausible-but-unsourced entry, so a course never reads
    as if a board said something it didn't. Not frozen at compile time: `course-auditor`'s new Tier 3 rollup
    proposes (never auto-writes) a new entry when the same unmatched `misconception`-caused pattern recurs
    across learners in the library's own `error_patterns` data.
  - **Schema.** `subjects/<course_id>.json` 3 → 4: `error_patterns: []`, `confidence: 0.5`, `remediation: {}`
    added as mechanical defaults (all three judgment-free — `0.5` states "no graded event yet," never a guess).
    `course.json` unchanged. `validate_structure.py` adds a non-blocking `misconceptions_status` per course
    (present/well-formed/count per stage) — absence is never a validation failure, since the file is new.
  - **Deliberately not done.** No new content-authoring wave (existing courses' `misconceptions.json` files are
    backfilled by audit, not by a build pass). No change to phase-convergence/cohort-testing. `tutor-core`'s
    pacing prose stays prose — reading a real `confidence` number instead of an impression, not becoming a
    script itself. Existing courses are not retrofitted with `misconceptions.json` content in this release;
    the field is additive and every check around it is non-blocking by design.
  - **Tests.** `tests/test_v140.py` (40): every new script's core behavior (taxonomy validation, recurrence,
    resolve-on-recall, all four `diagnostic_gate.py` triggers including that resolved entries stop counting,
    the full attempt-1/attempt-2/escalate/never-a-fourth-loop remediation path, stage independence, reset,
    `confidence_update.py`'s bounds and event ordering including the misconception surcharge and delta-shrinks-
    near-the-ceiling behavior, the 3→4 subject migration and its idempotence, and `misconceptions_status`
    including the non-blocking guarantee on both absence and malformation). One `test_v130.py` assertion that
    had pinned the old subject schema version literal now asserts the current constant instead (same pattern as
    the 1.2.0→1.3.0 transition). Full suite 197 tests, OK.
- **v1.5.0** — per-item BKT mastery, rubric-criterion-tagged errors and review cards, and a blocking
  post-compile structural gate (the three-part project the library owner and I agreed on after reviewing and
  narrowing a third party's — Grok's — five upgrade suggestions on 2026-09-29; two of Grok's five, multi-model
  routing and predicting misconceptions before the learner answers, were explicitly shelved as disproportionate
  to a single-learner system, not built).
  - **Why BKT over DKT.** A neural sequence tracker (DKT) needs a training corpus across many learners to be
    worth anything; this is a personal, single-learner-scale system producing at most a few hundred graded
    events a year per course. Fitting DKT here would be fitting noise, not signal. `item_mastery.py` uses
    textbook four-parameter Bayesian Knowledge Tracing instead, with fixed, documented, never-fit-to-this-
    library's-own-data parameters (`P(L0)=0.3, P(T)=0.15, P(S)=0.1, P(G)=0.2` — the same order of magnitude
    commonly reported in the BKT literature), the same "stated formula over an unauditable adaptive scheme"
    reasoning `review_math.py` already used for spaced-repetition scheduling.
  - **Augments `confidence`, never replaces it.** `confidence_update.py`'s course-level scalar is untouched —
    it's still what `tutor-core`'s pacing section paces the whole subject by. `item_mastery.py` is new,
    additional, per-item state for the finer-grained question "does this learner actually have item RM6" that
    one course-wide number was never meant to answer.
  - **Piggy-backed on existing signal, not new instrumentation.** Rather than requiring every teaching turn to
    separately call `item_mastery.py`, `error_log.py`'s existing `append` (an incorrect observation) and
    `resolve` (a correct one) — which already fire against a specific `item_id` — now call `item_mastery.observe()`
    themselves and fold its result into their own return value. Mastery tracking updates automatically from data
    the plugin was already collecting; no new behavioral discipline demanded of any calling skill.
  - **`rubric_criterion` closes the same-taxonomy loop.** `error_log.py` entries can now optionally carry the
    specific `rubric.json` criterion an error was graded against (an M/A/B tag or whatever shape that stage's
    rubric uses), alongside the pre-existing `stage_id`/`item_id`. `stage-recap`'s review cards carry the same
    `item_id`/`criterion` pair when derivable — reusing an error entry's own tags rather than re-deriving them —
    so a graded error, a review card, and a mastery estimate can all be traced to the same item/criterion instead
    of three separate ad-hoc labels. All three fields stay independently optional; `stage_id` remains the floor
    every entry and every card always carries.
  - **`diagnostic_gate.py` surfaces `item_mastery`, deliberately not a fifth trigger.** The four existing trigger
    conditions (two misses on one item, a recurring cause, explicit confusion, a reasoning mismatch) are
    unchanged — adding mastery-level as a new firing condition would reopen exactly the scope-creep the four-
    trigger design was written to resist, for a threshold that's never been validated. A persistently low
    `p_mastery` will in practice keep re-triggering the existing triggers as further misses accumulate, so
    nothing is lost by only surfacing it as context once the gate has already fired for a real reason.
    `tutor-core`'s pacing prose gained one parallel paragraph: `item_mastery` is for choosing *which* items
    within an otherwise-fine stage deserve slower treatment, `confidence` is still the one number the whole
    subject is paced by.
  - **`postcompile_gate.py` — the compiler's advisory report becomes one blocking verdict.** Before this version,
    `course-compiler`'s Step 8 ran `validate_structure.py` and `coverage_check.py` and then "reported back
    honestly" — a real structural problem (a missing `test.md`, a rubric entry with no source, a 1.3.0 field
    inconsistency) was disclosed in prose but never stopped the course from being written and enrolled anyway.
    `postcompile_gate.py` combines both checks into one `can_ship` verdict, classifying their fields as
    BLOCKING (missing stage files, an unreadable or missing-entry rubric, an empty source citation, any 1.3.0
    field inconsistency — all data-integrity bugs, not content-quality gaps) or ADVISORY (orphaned stage dirs,
    misconceptions status, coverage below `full` — all already explicitly, deliberately non-blocking by earlier
    design and left exactly that way here). `course-compiler`'s new Step 7.5 refuses to proceed to enrollment
    (Step 8) on a `false` verdict unless `postcompile_gate.py override <course_dir> "<reason>"` is called
    explicitly, with the reason recorded in the verdict and required in Step 9's report — an override is never
    silent, it's a deliberate, disclosed exception, not a bypass.
  - **Schema.** `subjects/<course_id>.json` 4 → 5: `item_mastery: {}` added as a mechanical default (an empty
    object means no item has an observation yet, never a guess). `course.json` unchanged.
  - **Deliberately not done.** Multi-model routing for diagnostic/grading turns (shelved: no evidenced problem,
    no clean routing layer inside Claude/Cowork, disproportionate to what it would fix). Predicting a
    misconception before the learner answers (shelved: over-engineered for single-learner scale — reacting to
    an actual wrong answer, which this plugin already does well, costs far less than trying to anticipate one).
    No retrofitting of existing courses' review decks with `item_id`/`criterion` tags — additive going forward,
    same as `misconceptions.json` in 1.4.0.
  - **Tests.** `tests/test_v150.py` (25): `item_mastery.py`'s update formula against a hand-verified sequence,
    monotonic climb and saturation-at-1.0 behavior, status lookups for both observed and never-observed items;
    `error_log.py`'s automatic mastery feed on both `append` (incorrect) and `resolve` (correct, including the
    "nothing resolved → no mastery call" case), `rubric_criterion` storage/defaulting/`NONE`-normalization;
    `diagnostic_gate.py` surfacing mastery without it ever forcing a fire and never overriding a real trigger;
    the 4→5 subject migration and its idempotence; and `postcompile_gate.py`'s blocking/advisory classification
    for every field it reads plus the override path. One `test_v140.py` assertion that had pinned the old
    subject schema version literal now asserts the current constant instead (same pattern as the 1.2.0→1.3.0 and
    1.3.0→1.4.0 transitions). Full suite 222 tests, OK.
- **v1.6.0** — an optional, read-only client-side toolkit (`scripts/toolkit/`), scoped down from a much larger
  proposal (a third party's — again Grok's — 13-tool CLI catalogue) after two rounds of "what's actually
  value-add here" with the library owner. Runs entirely outside a Claude session, on the owner's own machine.
  - **What survived the scoping, and why the rest didn't.** Kept: `backup` (elevated to the highest priority of
    anything here — `.gitignore` deliberately excludes `profile/*/` from version control, so this is currently
    the *only* backup path for a learner's irreplaceable history/mastery/errors; courses can be recompiled, this
    can't), `health`, `progress` (with a gate-visibility note folded in rather than a separate tool), `review_due`,
    `errors`. Cut entirely, not just deferred: `session` (a thin wrapper over `progress`+`review_due` that risked
    becoming a second front door around the real gating/teaching logic, which only lives in a live session),
    `export_cornell` (extractive-only note-taking without an LM produces something worse than reading `lesson.md`
    directly — a content-generation tool, categorically different from every other read-only module here, not a
    fit for this package's own rules), `diff` and `log` (solving a problem nobody's had yet — same
    provisioning-for-a-scale-that-doesn't-exist instinct the original infra review already named), `focus`
    (zero connection to any tutor data). `coverage`'s content folded into `health`'s course section rather than
    a standalone tool.
  - **Design rules, stricter than the plugin's own scripts.** One-way data flow: the tutor (the LM + the
    plugin's own `.tutor-scripts/*.py`, run only from inside a live session) is the sole writer of tutoring
    state; this package only reads it, with one narrow exception — its own `toolkit_log/` side-log (currently
    just a record of backups taken), which the tutor never reads for any gate, mastery, or grading decision.
    No pedagogy, no re-diagnosis, no "what to study next" that overrides the runner.
  - **Import the plugin's scripts, never reimplement their reads.** `core.py` calls `item_mastery.status()`,
    `error_log.query()`, and reads `migrate_schema`'s schema-version constants directly rather than re-parsing
    `subjects.json` by hand — the subjects schema has already moved twice (4→5 this same release cycle) while
    this toolkit was being scoped, which is exactly the drift risk a hand-rolled parser would have walked into.
    `schema_status()` reports (never guesses) when a file is older or newer than what this toolkit understands.
  - **GUI over CLI, by explicit request, with one hard rule.** The owner asked for something closer to a
    lightweight desktop app than more terminal scripts — `gui.pyw` (stdlib `tkinter` only, no new dependency,
    no web server) opens one small control-panel window; nothing else opens until a button is clicked, and no
    window auto-refreshes in the background (a Refresh button re-reads on demand instead). This is deliberate:
    the point is a status check beside the Claude window, not a second place to actually study, and every window
    says as much in its own footer text so it can't be mistaken for one. `gui.pyw` is wiring only — every button
    calls straight into the same tested functions the CLI (`__main__.py`, `python -m toolkit <command>`) uses.
  - **A real compiled `.exe` was considered and deliberately deferred, not ruled out.** PyInstaller can't
    cross-build a Windows binary from this plugin's Linux build environment, so packaging one would be a step
    the owner runs once, themselves, in a real Windows terminal (`pyinstaller --onefile --windowed gui.pyw`).
    Writing `gui.pyw` stdlib-only keeps that option open with zero rework if it's ever wanted; the `.pyw`
    double-click experience already delivers the actual ask (click, small native windows, no browser tab) without
    needing it.
  - **Deployment needed a real change to `bootstrap_scripts.py`, not just new files.** The existing bootstrap
    only flat-copies `.py` files directly inside `scripts/` into `.tutor-scripts/` on every `/run` — it doesn't
    walk subdirectories, so a Python *package* (`toolkit/__init__.py`, `toolkit/core.py`, ...) would have
    silently never been deployed. `bootstrap()` now also detects any immediate subdirectory of the source that
    contains an `__init__.py` and deploys it wholesale via `shutil.copytree`, replacing whatever's at the target
    on a genuine version-gated update (never a partial merge of old and new package files) — same
    fresh/updated/up-to-date/newer-than-bundle logic as every flat script, just extended to packages. The
    manifest now also records `packages`.
  - **Deliberately not done.** No network, no accounts, no new third-party dependency of any kind. No tool here
    computes or overrides a mastery, confidence, or gate value. No retrofitting `export_cornell`/`session`/`diff`
    — they were cut on their merits, not deferred as a backlog.
  - **Tests.** `tests/test_toolkit.py` (32): `core.py`'s path resolution and schema-version classification
    (current/older/newer/unreadable) against a fake, real-shaped `EDU_ROOT`; `backup`'s zip contents, its
    own-exports exclusion, its side-log write, and clean failure on a missing learner; `health`'s schema-drift
    and suspended-course flagging plus reading the deployed-scripts manifest; `progress`'s mastery summary and
    open-error counting; `review_due`'s due/upcoming split and its guarantee of never writing to the deck;
    `errors`' cause aggregation and open-only filtering; and five tests against `bootstrap_scripts.py`'s new
    package-deployment path (fresh deploy, a non-package directory correctly ignored, a stale package file
    correctly replaced wholesale on update, the manifest recording `packages`, and an up-to-date check leaving
    a deployed package untouched). `gui.pyw` itself was smoke-tested manually (constructed under Xvfb with a
    real `tkinter`, every window opened against fake data) since this test environment has no display and no
    `tkinter`-dependent test belongs in a suite that must run headless in CI. Full suite 254 tests, OK.
- **v1.7.0** — one new toolkit module, `export_anki.py`, no other functional change:
  - **Anki export.** Writes a real `.apkg` file from a learner's review deck(s), one Anki
    sub-deck per course, tagged with course_id/stage_id/item_id/criterion. Importable
    straight into the real Anki app on any device. This is content portability, not a
    scheduling sync: Anki schedules its own copy from scratch with its own algorithm;
    this system's own SM-2-lite state (`interval_sessions`/`ease`/`lapses`/`due_at_slot`)
    is read, never written, and never touched by anything that happens in Anki afterward.
  - **The one deliberate, documented exception to "zero third-party dependency."** Every
    other toolkit module is stdlib-only (core.py design rule 7, added this version).
    `export_anki.py` needs `genanki` (MIT, pure Python, no C++/compiled requirement) to
    write the `.apkg` binary format correctly. Hand-rolling Anki's SQLite-based collection
    format was considered and rejected: it's a real, easy-to-get-subtly-wrong format
    (field separators, per-model JSON, checksums, card queue/type enums), with no way to
    verify a hand-rolled writer round-trips through real Anki without a live Anki install
    to test against — whereas genanki already is exactly that, at 2,700+ stars and
    actively maintained. A missing genanki install disables only this one feature, with a
    plain `pip install genanki` instruction, and never affects any other toolkit module.
  - **Prompted by reviewing LearnOS a second time** (see the 30 Sep entry above): their
    review deck ships `ts-fsrs` for scheduling, which this system declined for its own
    reasons, but the adjacent idea of genuine flashcard-app interoperability (a learner
    reviewing on their phone in the actual app millions of people already use) stood on
    its own merits regardless of which scheduler either system uses internally.
  - **Tests.** `tests/test_export_anki.py` (11): deterministic ID generation, the
    genanki-missing error path (forced, not dependent on the test environment actually
    lacking it), a real `.apkg` file written and reopened as an actual zip containing a
    real `collection.anki2`, multi-course export producing multiple decks, the
    `--courses` filter, a missing review deck skipped rather than fatal, the one
    toolkit-log line written, and cards with and without `item_id`/`criterion` both
    exporting cleanly. Full suite 265 tests, OK.

## 30 Sep 2026 — Safety idea taken from uk-agents/uk-legal-plugins (Apache-2.0), tutor-core updated

Following the BAILII MCP review, its author's broader work was checked: `paulieb89/uk-legal-mcp`
(the flagship UK legal research MCP — case law, legislation, Hansard, HMRC) and
`uk-agents/uk-legal-plugins`, an 11-plugin Apache-2.0 Claude marketplace for UK legal
practice. Both read for safety before starring (clean — see the roadmap doc for the
detail) and starred, but the marketplace itself was not installed: per the explicit
decision this session, we take ideas piecemeal from its source under its Apache-2.0
licence rather than adding the whole plugin, keeping the other 10 practice-area plugins
bookmarked in case a future reason (CILEX's practical-practice side was raised as one
candidate) makes installing more of it worthwhile.

One idea from its `law-student-uk` plugin was genuinely missing from this system and got
adopted: **`irac-practice`'s "real-matter check."** That skill stops and redirects to a
real solicitor/clinic/Citizens Advice if a student's practice question describes an
actual situation (a real name, address, pound amount, deadline, "my landlord/employer")
rather than a hypothetical — because an AI grading a "hypo" that's actually someone's
real legal problem is answering with advice, not teaching. Checked this system's own
`tutor-core/SKILL.md`: the existing `## Safety` section only covered physical-risk
supervision (labs, tools, food safety, exercise) — nothing caught a real-situation
question sliding into being treated as advice. Since this system already has multiple
courses in regulated professions beyond just law (`aat_*`, `acca_applied_knowledge`,
`icaew_cfab` for accountancy, alongside `sqe1`/`sqe2`/`cilex_level3_diploma`/`llb`), the
rule was generalised rather than written law-specific: added a "Real situations, not
hypotheticals" subsection to `## Safety` covering any of these courses, with the same
trigger list (real name/address/amount/deadline/letter) and the same redirect (keep
teaching the concept, decline to answer as if the situation were real).

This is a pedagogy-layer change (`tutor-core`, shared by every course), not a script
change — no version bump on its own logic, but it ships with the next release since it's
a real behavioural addition every learner in a regulated-profession course benefits from.

**Not adopted from the same review, left open:**
- The "verify before formatting" citation discipline (`oscola-build-citation`,
  `find-case-by-party-verify` — never report a case/statute citation without resolving it
  against a live source first) is a genuinely good idea for `sqe1`/`sqe2`/
  `cilex_level3_diploma`/`llb`, but implementing it properly means actually connecting
  `uk-legal-mcp` (or `bailii-mcp`) as a live grounding source for those courses' content
  and rubrics — a bigger step than a text change, and still an open decision (see
  roadmap doc).
- The IRAC/CILAC grading rubric structure (issue-spotting / rule-accuracy /
  application-mapping / organisation, pass–borderline–not-yet banding, max one labelled
  example phrasing, session-over-session pattern tracking) is well-designed and close to
  what `item_mastery`/`error_log`'s rubric-criterion tagging already does in spirit, but
  checking whether `sqe1`/`sqe2`/`llb`/`cilex_level3_diploma`'s actual rubrics already
  reach this granularity (and improving them if not) is real course-content work, not a
  pedagogy-layer text change — left as a flagged idea, not actioned.

## 30 Sep 2026 — uk-legal-mcp / govuk-mcp wired in as suggested connectors (v1.9.0)

Following the round-4 review (uk-legal-mcp/govuk-mcp read and starred, both clean --
see the earlier entry this same day), this makes them real, discoverable suggestions
rather than just a roadmap note. Two changes:

- **`connectors.md` rewritten** for the four legal courses (`sqe1`, `sqe2`,
  `cilex_level3_diploma`, `llb`) -- each previously said "no relevant connector was
  found in the searched registry," true at the time those courses were built, before
  either server existed. Now each lists both, with status `suggested, not yet
  connected` -- per `course-compiler`'s own connector rule ("never connect anything
  without explicit permission"), this file records the suggestion; it does not flip a
  course to actually using the connector. That flip is the learner's call, made when
  they're actually running the course, the same as it would be for a connector
  suggested at original build time.
- **New `plugin/generic-tutor/.mcp.json`** at the plugin root, declaring both servers
  (following the same `mcpServers` manifest shape `uk-agents/uk-legal-plugins` uses for
  its own `law-student-uk` plugin) so they're actually offerable through whatever MCP
  client the plugin is running in, rather than existing only as a paragraph in
  `connectors.md` that nothing surfaces. This does not auto-connect anything --
  approval still happens in the client, same as any MCP server.

No script changes, no schema change. `sqe1`'s `connectors.md` previously noted "the
SRA's own specification pages were fetched directly instead" -- that's still true for
sourcing the syllabus itself; this addition is about grounding *citations used during
teaching* (a case name, a neutral citation, a statute section), not resourcing the
course build.

## 30 Sep 2026 — PhET/GeoGebra links added to 29 stages across 6 courses (course content, no version bump)

The other flagged "Open next steps" item: `alevel_physics`/`alevel_chemistry`/`alevel_biology`
each declared practical/apparatus work "out of scope," and `alevel_mathematics`/
`alevel_further_mathematics`/`gcse_mathematics` had no visual/interactive component at all.
PhET (MIT, explicitly free for educational use) and GeoGebra (GPL, UK-curriculum-standard)
were starred earlier this session as the fix; this makes it real.

**What was done.** Every PhET sim and GeoGebra app referenced was individually verified with
`WebFetch` against its real, canonical URL before being added anywhere -- not assumed from a
sim's name or a search result. 8 PhET sims for physics (Wave Interference, Projectile Motion,
Circuit Construction Kit: DC, Gravity and Orbits, Charges and Fields, Capacitor Lab: Basics,
Faraday's Law, Alpha Decay), 5 for chemistry (Molecule Shapes, Reactions & Rates, Reversible
Reactions, pH Scale, Acid-Base Solutions), 3 for biology (Gene Expression Essentials, Neuron,
Natural Selection), and GeoGebra's own stable apps (Graphing Calculator, Geometry, 3D
Calculator, Classic's Probability Calculator) for maths -- each matched to a specific stage
whose actual content it visualises (e.g. Wave Interference on S05's interference/diffraction
content specifically, not stationary waves in S04; Faraday's Law on the induction stage, not
static fields). 29 stage `lesson.md` files across `alevel_physics`, `alevel_chemistry`,
`alevel_biology`, `alevel_mathematics`, `alevel_further_mathematics`, and `gcse_mathematics`
each got one new `## Further resources (optional)` section appended, listing the matched
resource(s) with a one-line note on what it actually lets a learner do differently (drag a
point, run a collision, rotate a solid) -- not a generic "here's a sim" link.

**Link, not embed.** These are markdown lesson files read by the tutor during a live session,
not rendered web pages -- there is no embedding mechanism to decide between. A link is the
same mechanism already used for citations and sources elsewhere in this library.

**Deliberately optional, deliberately not graded.** Every section says plainly that nothing in
it is required to pass the stage and that it isn't part of the syllabus content itself --
consistent with `tutor-core`'s coverage-honesty rule (a lesson's real content is what's taught
and testable; supplementary visualisation is exactly that, supplementary). No `coverage_check.py`
item is claimed to be taught by a resource link; `covers_items` on these stages is unchanged.

**Not a course-content build in the "new course" sense** -- no new stages, no schema change, no
version bump (this is existing stages gaining an optional pointer, the same class of change as
a `connectors.md` edit, not new taught material) -- so it ships as a plain commit against
`courses/`, not a plugin release.

`validate_structure.py` run against all six touched courses after the edit: 0 problems.

**Not done, left for a future pass if it's ever wanted:** the remaining stages in these six
courses that don't have as clean a sim/applet match (e.g. `alevel_physics`'s S12 circular
motion/SHM, S19-21 astrophysics -- PhET has relevant sims but none were verified this pass);
any course outside these six; GeoGebra's own curated per-topic "Materials" library (only the
four generic, always-available apps were used, since verifying individual community-submitted
Materials pages one by one for correctness is a much bigger and lower-confidence task than
verifying PhET's own maintained sims).

## 30 Sep 2026 — curated UK-channel video links added to 17 stages across 6 courses (course content, no version bump)

Closes the third and last of this session's three flagged build ideas. Follows directly
from the `Curriculum-Engine` review earlier in the session: that repo's live-YouTube-
search-and-rank mechanism was declined as the wrong shape for this library, but the
underlying need (a spoken/visual explanation for topics that benefit from one) and the
right mechanism (named, reputable channels, hand-picked per stage, exactly like every
other source in this library) were kept as an open item. This does that.

**Verification method.** Every candidate video was found via `WebSearch` restricted to
`youtube.com`, then verified with YouTube's `oembed` endpoint
(`https://www.youtube.com/oembed?url=...&format=json`), which returns the real title and
`author_name` for a given video id without needing to scrape the full watch page (which
rate-limited/blocked `WebFetch` directly with 429s). A video was only used once its
`author_name` matched the intended channel (Freesciencelessons, Craig'n'Dave, or
corbettmaths) -- this is the same discipline applied to the PhET/GeoGebra links two
entries above: never assume a URL or title, verify against the source itself.

**Board-matching mattered for computer science.** `gcse_computer_science` is AQA 8525
and `alevel_computer_science` is AQA 7517 (checked against each course's own
`course.json`, not assumed) -- Craig'n'Dave publishes separate video series per exam
board with different terminology and spec numbering, so the AQA-specific videos were
used throughout, not the OCR J277 ones that surface just as readily in search (both were
found and verified; the OCR ones were discarded once the board mismatch was caught).

**What was added.** 17 stage `lesson.md` files across `gcse_physics` (Half Life,
Properties of Waves, Permanent and Induced Magnets), `gcse_chemistry` (Ionic Bonding,
Introducing Electrolysis, Reversible Reactions), `gcse_biology` (Digestive Enzymes, The
Nervous System + Homeostasis, Evolution by Natural Selection), `gcse_computer_science`
(AQA Bubble sort, Truth tables, Von Neumann architecture, SQL), `alevel_computer_science`
(AQA Fetch-decode-execute cycle + Interrupts, Functional programming list operations),
and `gcse_mathematics` (Surds, Tree Diagrams) -- all Freesciencelessons/Craig'n'Dave/
Corbettmaths, all board-matched where a board applies. Two stages (`gcse_mathematics`'s
S05 and S27) had no PhET/GeoGebra link from the earlier pass, so this is their first
`## Further resources (optional)` section; the others are new sections on stages the
earlier pass didn't touch (no course/stage overlaps between the two passes).

**Same rules as the PhET/GeoGebra pass:** linked, not embedded; explicitly optional and
ungraded; no `coverage_check.py` claim changed; plain commit against `courses/`, no
schema change, no plugin version bump. `validate_structure.py`: 0 problems across all six
touched courses.

**Not done, left open if ever wanted:** the other three courses PhET/GeoGebra already
touched (`alevel_physics`, `alevel_chemistry`, `alevel_biology`, `alevel_mathematics`,
`alevel_further_mathematics`) have no video links yet -- Cognito Chemistry/Cognito
Biology and further Corbettmaths/ExamSolutions-style channels for A-level maths were not
researched this pass; any course outside the eleven now touched across both passes
(PhET/GeoGebra + video links) has neither.

## 30 Sep 2026 — v1.10.0: SQLite history wired in for real, and a write-back trust gap closed

Two things shipped together, deliberately, in response to a direct question: "we still
technically live on a single assumption -- that the LM will always write back and not
just say it did."

**1. `schema_design.sql` finally wired in, and found to have been orphaned.** The
five-table per-learner history schema (`error_events`, `item_mastery` +
`item_mastery_log`, `review_cards` + `review_log`, `confidence_events`) existed only as a
deployed file at `.tutor-scripts/schema_design.sql` on the runtime target -- it was never
actually committed to this repo, despite the roadmap backlog calling it "designed,
revised." New `scripts/sqlite_store.py` (~420 lines) creates and writes it for real, one
`tutor.sqlite3` per learner, sitting alongside `subjects/`. JSON stays the live source of
truth for *current* state, exactly as designed -- nothing here is ever read back into a
teaching decision. It's purely additive history a human or a future `course-auditor` pass
can query later ("is this item actually trending up", "how has this card's ease moved
over a term") that a snapshot-only JSON file can't answer. Every write function is
wrapped in a `_safe` decorator: a SQLite failure (disk full, lock, corruption) returns
`{"ok": false, "error": ...}` and never raises, never blocks, never rolls back the JSON
write, which stays authoritative. `error_log.py`'s `append`/`resolve` and
`item_mastery.py`'s `observe` now call the matching `sqlite_store` function right after
their existing `_save`, and surface the result under a new `"sqlite"` key in their
returned JSON. `bootstrap_scripts.py` needed no change -- it already deploys any flat
`.py` file in `scripts/`, version-gated, so `sqlite_store.py` is picked up automatically.
A one-time `sqlite_store.py backfill <learner_dir>` migrates an existing learner folder,
current-state tables only (`item_mastery`, `review_cards`) plus the full `error_events`
list (already a durable list, not a snapshot) -- it deliberately does *not* fabricate
synthetic rows into the three log/history tables, since that history was never actually
recorded and inventing it would be dishonest.

**2. The write-back trust gap, found by reading the actual source, not assumed.**
Investigating where to hook `sqlite_store` in surfaced a real asymmetry: `error_log.py`
and `item_mastery.py` have always owned their JSON writes outright (load, mutate, save,
all in the same script). But `confidence_update.py` and `review_math.py` were pure
calculators -- verified by reading both in full -- that never touched a file. Per their
own docstrings and per `course-runner.md`/`review-scheduler.md`'s prose, persisting
`confidence` and a review card's `interval_sessions`/`ease`/`lapses`/`due_at_slot` was
**100% prose-trust**: the calling skill was merely instructed in markdown to "write the
returned value back," with no code anywhere that performed or verified it. This is the
literal, concrete instance of the question that prompted this work -- and it directly
parallels this session's own earlier failures (an unpersisted roadmap edit, an unexecuted
unstarring) that were claimed done but weren't.

**The fix:** both scripts gained a new `apply` subcommand that performs the full
read-modify-write itself, the same way `error_log.py`/`item_mastery.py` always have --
`confidence_update.py apply <subjects.json> <event> <current_slot> [--misconception]` and
`review_math.py apply <deck.json> <card_id> <current_slot> <correct>`. Each also logs to
the matching `sqlite_store` table and returns `"written": true` plus the sqlite result.
The old pure-calculator forms (`confidence_update.py compute <old_confidence> <event>`
and `review_math.py`'s positional-args form) are unchanged and still exist, for testing
and for any caller that genuinely wants the arithmetic only. `course-runner.md` and
`review-scheduler.md` were updated to call `apply` instead of "write the returned value
back" -- the field-ownership claim in `course-runner.md` ("`confidence` by
`confidence_update.py` -- write only through those scripts") is now literally true rather
than aspirational.

**Honest limit of this fix, worth naming plainly rather than overclaiming:** this closes
the gap for the two fields that were pure prose-trust -- once `apply` is called, the write
happens in code, not by hand-copying a returned value. It does **not**, and structurally
cannot, guarantee the model always *calls* `apply` in the first place during a live
session instead of skipping the step or improvising. That residual risk -- an omitted
tool call, not an unenforced one -- is a different, harder problem (closer to a runtime
audit/verification layer than a script change) and is explicitly not solved here.

**Tests.** New `tests/test_v1100.py`, 21 tests: `sqlite_store.py`'s db creation, every
logging/upsert function, backfill's current-state-only guarantee, and that a forced
failure returns `{"ok": false}` rather than raising; `error_log.py`/`item_mastery.py`'s
new sqlite side effects; and `confidence_update.py apply`/`review_math.py apply`'s full
read-modify-write-plus-log behaviour, including that `apply` and `compute` agree on the
arithmetic for identical inputs. Full suite: 286 tests, 0 failures (265 pre-existing + 21
new), run via `python3 -m unittest discover tests -v`.

**Not done, deliberately held per instruction:** the PhET/GeoGebra/video-link course
coverage from the two entries above this one is explicitly *not* being expanded further
right now -- that's deferred to a future `course-auditor` pass rather than pursued
alongside infra work.

## 30 Sep 2026 — v1.11.0: fixed the passed/not_passed bug, and closed the syllabus_status/current_stage write-back gap

Prompted by an independent code review (external Copilot-based review, then independently
re-verified line-by-line rather than trusted): every one of 1253 `stages/<id>/test.md` files
told the model how to record a stage's result, and 445 of them said "Record `passed` or
`not_passed`... into this course's micro-profile" -- but `syllabus_status` has only ever
meant `"pass"`/`"fail"`/`"unsat"`/`"withheld"`. Every script that reads it
(`cohort_status.py`, `gate_check.py`, `apply_capabilities.py`, `coverage_check.py`,
`resume_enrollment.py`) checks the literal string `"pass"`, and `course-runner.md` itself
has always said `"pass"`/`"fail"`. A model that followed the content file literally and
wrote `"passed"` would silently strand the stage forever -- never counted as passed, the
course never completes, its cohort never converges, and any level gated behind it never
unlocks, with no error anywhere to surface it.

Verified the finding myself before acting on it rather than trusting the review's own
count: grepped the actual sentence patterns across all 1253 files. Confirmed exactly 3
patterns (445 broken, 696 + 112 already correct vocabulary) -- the review's own "445"
figure was exactly right.

**The deeper finding, which the review also named and which matters more than the typo
itself: no script had ever owned this write at all**, correct vocabulary or not. All
1253 files -- including the 808 that already said `pass`/`fail` correctly -- only ever
told the model to "record the pass" or similar prose, with zero code enforcing it. This
is the exact write-back-trust gap v1.10.0 closed for `confidence` and review-card fields,
except here it's the field that actually gates cohort convergence and the level ledger --
arguably the single most consequential unenforced write in the whole system.

**The fix, in the same shape as v1.10.0's `apply` subcommands:** new
`scripts/record_stage_result.py`, with one job: `apply(subjects_path, course_path,
stage_id, result)` sets `syllabus_status[stage_id]`, and on a genuine pass walks
`course.json`'s `stage_ladder` to find the next stage that isn't `withheld`, sets
`current_stage` to it, and resets `current_phase` to `"lesson"`. On fail, it only
records the result -- `current_stage` is untouched, since remediation happens within
the same stage. It never grades anything and never decides *whether* a test passed --
that judgment stays entirely with the model, same division of labour as every other
`apply` script.

**Migrated all 1253 `test.md` files mechanically**, not by hand: a one-time script
(`_staging/migrate_test_md.py`, not part of the shipped plugin) replaced each of the 3
known "record the result" sentences with a plain instruction to give a note, and
inserted a new `## Recording the result` block (calling `record_stage_result.py apply`
with that stage's own id) immediately before the `## If not passed` heading -- renamed
`## If fail` for vocabulary consistency -- which existed verbatim in all 1253 files, so
the insertion point needed no per-file judgment. Verified: 1253 changed, 0 unmatched,
0 missing the heading. `_template/stages/S1/test.md` updated the same way so every
future `/add-course` compile gets this by default. `validate_structure.py`: 0 problems
across all 62 courses after the migration.

`course-runner.md` updated to call `record_stage_result.py apply` instead of "record the
result into syllabus_status" left as an unenforced instruction, and the field-ownership
sentence now lists `syllabus_status`/`current_stage` alongside `confidence` and the other
script-owned fields.

**Tests.** New `tests/test_v1110.py`, 9 tests: pass advances to the next non-withheld
stage and resets phase; fail records the result without touching stage/phase; withheld
stages are correctly skipped, including when every remaining stage is withheld; an
unknown stage_id or an invalid result value (including the literal old bug value,
`"passed"`) is rejected rather than silently no-op'd; a re-pass after an earlier fail
still advances. Full suite: 295 tests, 0 failures (286 pre-existing + 9 new).

**What this doesn't fix, named plainly rather than left implicit:** exactly the same
residual as v1.10.0's own write-back fix -- nothing forces the model to actually call
`record_stage_result.py apply` instead of skipping it and just telling the learner they
passed. The write, once triggered, is now guaranteed correct; whether it gets triggered
at all stays a trust question, same as it does for every other `apply` script in this
plugin.

## 30 Sep 2026 — v1.12.0: disclose coverage exclusions even when status is "full"

A second review finding, independently re-verified: `gate_check.py`'s coverage block set
`disclose_to_learner = (effective_status != "full")`, so a course whose `computed_status`
was `"full"` never disclosed anything to the learner -- but `coverage_check.py` can mark a
course `"full"` purely because every uncovered item was declared out of scope with a
reason (e.g. an exam-board option the learner didn't select), not because every item is
actually taught. Checked against the real course library: `alevel_further_mathematics`
(174/298 items taught, 124 declared-excluded), `alevel_physics` (140/216), and
`alevel_sociology` (41/71) all show `coverage_status: "full"` for exactly this reason, and
under the old logic the learner was never told anything had been left out of scope at all.

Declared, reasoned exclusions are legitimate -- that's what makes "full" a meaningful
status for a course deliberately scoped to selected options, and `coverage_check.py`'s own
logic for counting them as "handled" isn't wrong. The bug was entirely in what
`disclose_to_learner` did with that information: it conflated "coverage_check.py found no
problem" with "the learner needs no disclosure," when those are different questions.

**Fix, in `gate_check.py._coverage_block`:** `disclose_to_learner` is now
`effective_status != "full" or items_excluded > 0`. When `effective_status` is `full` and
`items_excluded` is nonzero, `detail` is rewritten to say so explicitly ("declared coverage
of the SELECTED scope, not automatically the whole specification"), and the block now
always carries `items_excluded` and `excluded_items` (id -> reason) alongside the existing
`items_total`/`items_taught`/`uncovered_items`, so the caller can name exactly what and why
without a second lookup.

`course-runner.md`'s disclosure paragraph updated to a third line variant for this case
("this course covers the full specification for the selected scope -- N of M items are
taught; K items are explicitly out of scope"), and its "never say the whole specification
is covered" rule now requires `effective_status == "full"` **and** `items_excluded == 0`,
not `effective_status == "full"` alone.

**Tests.** `test_coverage.py` gained `test_full_with_declared_exclusions_still_discloses`
(full + exclusions still sets `disclose_to_learner`, `detail` mentions the exclusion, and
`excluded_items` carries the reason); the existing `test_full_and_full_means_no_disclosure`
now also asserts `items_excluded == 0` for that zero-exclusion case, so the two tests
together pin both sides of the fix. Full suite: 296 tests, 0 failures.

**What this doesn't fix:** whether `_declared_exclusions` themselves are honest is still
entirely a content-authoring question -- `coverage_check.py` only checks that an exclusion
names a real item and gives a non-empty reason, never that the reason is true or that the
item is genuinely out of the learner's selected scope. That's a `course-auditor` Tier 3
question (matching declared exclusions against the live specification), not something a
structural check can catch.

## 30 Sep 2026 — courses/ split to a private repo; Tier 1+2 audit run (no code changes)

Two follow-ups after the reviews' remaining open items were put to the repo owner directly rather
than decided unilaterally, per the earlier `DESIGN_NOTES.md` entries this same day.

**Repo split, agreed and done.** `courses/`/`_staging/`/`_historic/` moved out of the public
`edu-course-library` repo into a new private `edu-courses-private` repo, via `git filter-repo`:
extracted with history for the 7 commits that touched those paths, then stripped entirely from
`edu-course-library`'s history (not just its current HEAD) and force-pushed. Nothing on disk
changed -- the plugin still reads `courses/` etc. from the same local paths; only which repo
tracks them changed. This repo's own CI (`.github/workflows/plugin-tests.yml`) lost its
`validate-courses` job, since there's no `courses/` here to check anymore; the equivalent check now
runs in `edu-courses-private`'s CI, which checks this repo out read-only for the validators. Both
repos' CI verified green after the split. Full writeup: see the project roadmap doc's "Repos"
section.

**Audit, Tier 1+2 only, run and clean.** The second review's `/audit` recommendation (40 courses
missing `last_audited_plugin_version`, 22 stale, 21 never live-rechecked) was discussed rather than
run wholesale -- Tier 3 (live grounding re-verification, live syllabus diff) is a real per-course
cost and correctly stays parked until either synthetic users exist or a specific course's staleness
actually matters. What's cheap and mechanical (`validate_structure.py` structural checks, the two
Tier-1 checks CI doesn't cover -- orphaned enrollments, true duplicates -- and `migrate_schema.py`
across all 62 `course.json` files) was run for real: 0 problems, 0 duplicates, 0 orphans, 0 courses
needed migration. **`last_audited_plugin_version` was deliberately left untouched** -- writing
1.12.0 into it off a Tier-1+2-only pass would overclaim exactly the way this session's write-back
fixes have been about *not* doing; that field means "a full audit ran," and Tier 3 didn't. No code
changed, so no version bump and no test count change (still 296).

## 4 Oct 2026 — v1.13.0: atomic writes and per-file locking (tasks E-02, E-03, E-04)

First engine-hardening step of the redesign (`docs/PLAN.md`). Every script that persisted JSON did so with
`open(path, "w")`, which truncates before writing, and every read-modify-write was unguarded. Two concrete
failure modes followed: a crash mid-write left a partial file, and two overlapping calls on the same file lost
one update. The second was reproduced, not assumed: with locking removed, 12 parallel `error_log.py append`
calls retained 6-9 entries on every run.

New `scripts/tutorlib/` package (stdlib only; the bootstrap already deploys any subfolder containing
`__init__.py`): `atomic_io.write_json` (temp file in the same directory, fsync, `os.replace`; byte-identical
output to the writers it replaced; optional `.bak`) and `filelock` (sidecar `.lock` via `O_CREAT|O_EXCL`,
re-entrant in-process because scripts call each other on the same file, stale-lock breaking after 60 s, 10 s
timeout that raises rather than writing unlocked). All ten writers now use `atomic_io`; the eight
read-modify-write entry points (`confidence_update.apply`, `error_log.append/resolve`, `item_mastery.observe`,
`record_stage_result.apply`, `remediation_state.record/reset`, `resume_enrollment.resume`, `review_math.apply`,
`slot_advance.advance`) are wrapped with `@filelock.locked`. No CLI or output change. Not yet done:
`sqlite_store.py` (SQLite has its own locking), `apply_capabilities.py` CLI path (atomic but unlocked),
`bootstrap_scripts.py` manifest write, and the consent gate (E-05/E-06).

## 4 Oct 2026 — v1.14.0: consent enforced in code (tasks E-05, E-06)

`profile-kernel` defined `granted` / `limited` / `revoked`, but only `slot_advance.py` ever checked it; the other
eight writers and the SQLite history wrote regardless, so `revoked` depended entirely on the model remembering.
New `tutorlib/consent.py` classifies each write as **progress**, **scheduling** or **signal** and every writer
asks before writing. Decisions worth recording: remediation attempt counters count as *progress* (discarding them
would let a failed stage loop forever each session); `item_mastery` and all history rows are *signals* (derived
from graded work, and the history DB is the most complete record of a learner); review-card scheduling state is
*scheduling* even in the DB. Absent profile ⇒ granted (bare fixtures, course folders); unreadable profile or
unknown status ⇒ treated as `revoked` (fail closed). `migrate_schema.py` is deliberately exempt: it is the
explicit `/audit` maintenance path and changes shape, not content. A skipped write returns the computed result
plus `written: false` so in-session use ("used now, discarded") still works. `tests/test_consent.py` runs every
writer under every status and was checked to fail when the gate is disabled.

## 4 Oct 2026 — v1.15.0: /erase and /export become scripts; identifier and path guards (K-27, K-28, K-29, C-05, S-13, E-08)

Audit findings closed: `/export` omitted `tutor.sqlite3` (the fullest record of a learner) and `/erase` demanded a
"confirmation token" it never defined. Both were also model-executed file handling. `erase_profile.py` lists what
will be removed (`--dry-run`), then deletes only on the exact phrase `ERASE <user_id>`; `export_profile.py` writes
one zip (progress, decks, every history table as JSON, `manifest.json` with sha256) and refuses an output path
inside the profile root. Both validate the user id (`tutorlib.ids`: 1-64 chars, alphanumeric start, no separators,
no `..`, no Windows device names) and refuse symlinked learner folders / paths resolving outside the profile root
(`tutorlib.paths`). Exports are not consent-gated (read-only copy of the learner's own data); erase is
deliberately usable under any consent status. Id validation is wired into these two scripts only; applying it at
every script boundary is part of E-20.

## 4 Oct 2026 — v1.16.0: uniform CLI exit codes (tasks E-01, E-10 part, E-11)

Before touching any script's argument handling, `tests/test_golden_cli.py` snapshots every script's real CLI output
against a deterministic fixture (27 cases; a meta-test fails when a new script has no case). That baseline exposed an
inconsistency: three scripts reported failure as `{"error": ...}` with exit 0. `tutorlib/cli.py` `emit()` prints the
result and returns 1 when it carries an `error`; all script mains now `sys.exit(cli.emit(result))`. The only golden
diffs were those three `exit: 0 -> 1` lines. Deliberately not done yet: an argparse rewrite of the hand-parsed mains
(low value relative to risk while the goldens only just exist) and the full envelope; both remain open under E-09/E-10.

## 4 Oct 2026 — v1.16.1: single eligibility definition (task E-17)

Audit expectation was four divergent copies of the eligible/complete/suspended logic. Reading the code found
`is_complete` already shared (gate_check, prereq_check, roster_check, resume_enrollment import it from
`cohort_status`); what remained duplicated was the state tuples and the suspension literal, in three scripts
(the class of drift behind the v1.0.1 bug). They are now `cohort_status.LIVE_STATES`, `SLOT_STATES`,
`is_suspended()`. Behaviour-neutral: the 27 golden CLI snapshots and the full suite are unchanged.
`tests/test_eligibility.py` also scans the scripts so a re-derivation fails CI. `_load_json` helpers duplicated
across scripts are left for the `tutorlib` IO consolidation.

## 4 Oct 2026 — v1.17.0: schemas, validator, safe state loading (tasks S-05, S-06, S-07, S-09 part, E-20 part)

Schemas are authored from what the scripts actually write and what the skills define, then proven against both: they
accept every fixture and every file produced by running the real script flows, and reject the known historical
shapes (string `confidence`, `passed`, unknown roster state). They live in `tutorlib/schemas/` so the bootstrap
deploys them with the scripts; the validator (`tutorlib/schema.py`) implements only the JSON Schema subset used, with
no dependency. Schemas are deliberately permissive on additional properties (forward compatibility) and strict on
types, enums and ranges. `tutorlib/state.py` centralises JSON loading and adds the `schema_version`-newer-than-
supported refusal; `SUPPORTED` is asserted equal to `migrate_schema.py`'s constants in a test so the two cannot drift.
`cli.EXPECTED_ERRORS` gives the six writers one list of failures reported as JSON. Observation: the older
`tests/test_scripts.py` fixtures use `confidence: "medium"` and `error_patterns: ["x"]` — shapes the schema now
rejects; those tests exercise gating logic that ignores the fields, so they are left alone for now (cleanup under E-26).
Runtime enforcement of schemas at script boundaries (validate-before-write) is not enabled yet; it will follow once
real learner data has been run through `validate_schema.py` (E-20 remainder).

## 4 Oct 2026 — v1.18.0: root resolution, history-DB versioning, bootstrap repair (tasks E-07, E-15, E-22)

Three small robustness items. (1) `/EDU/` had always been a placeholder the model had to resolve per install; the
resolver is now code with an explicit precedence and a layout report that `/doctor` (P-13) will reuse. (2) The
history DB carries `PRAGMA user_version`; databases created before versioning (0) are stamped on first use with no
data change; a newer one is left byte-for-byte alone. WAL mode was considered and rejected for now: it adds sidecar
files that complicate backup/erase/export for no measured benefit at this write volume. (3) The bootstrap trusted the
version number alone, so a hand-edited or partially-deleted `.tutor-scripts/` stayed broken until the next release.
Same-version runs now diff the target against the bundle (sha256) and repair missing/modified files; extra files
inside a shipped package are tolerated; orphan removal is limited to what an earlier manifest recorded.

## 4 Oct 2026 — v1.19.0: session ledger and verifier (tasks V-01, V-02, V-03, V-05, V-06, V-08)

The v1.10.0 entry named the residual risk: scripts can own writes but cannot make the model call them. ADR 0001
established Cowork has no hooks, so detection lives in the scripts. Design choice: no transcript parsing and no
extra model-emitted "event lines" (V-04 dropped): the scripts themselves leave the trace. Each writer logs a ledger
line; the verifier derives what ELSE must have happened from what did (stage pass/fail -> confidence, cards,
remediation) instead of trusting the model to declare intent. A session is one `session_slot`; consent-skipped
writes are logged but not counted as writes. The verifier reports and never repairs. Limits, stated plainly: it
cannot detect a session where the model did nothing at all (no ledger lines), nor a wrong grade; it catches
incomplete or repeated bookkeeping. `invariants.py` complements it by checking state without a ledger. A test bug
worth recording: a first version of the linear-order check used `ladder[:last_pass]` with `last_pass = -1`, which
slices off only the last element and flagged every course with no passes; the fixture-is-clean test caught it.

## 4 Oct 2026 — v1.20.0: /doctor, /status, /help (tasks P-13, C-06, C-07, V-08 wiring)

The checks added in v1.13-1.19 (root layout, deployed-script repair, schemas, invariants, DB health, ledger
verification, consent) were each reachable only by running a script by hand. `doctor.py` composes them and speaks in
{status, detail, fix}; `status.py` gives the learner a one-screen answer to "where am I / what next". Both are
read-only; the skill forbids acting on a fix without the learner's say-so. `doctor.py` is exempt from the golden CLI
suite because its output embeds the interpreter version (covered by `tests/test_doctor_status.py` instead). The
next-action rule in `status.py` is deliberately simple (due reviews, then the live course with most stages left);
smarter selection waits for item-level mastery use (L-07).

## 4 Oct 2026 — v1.21.0: untrusted-content policy and scanner (tasks X-01, X-02, X-03)

The compiler and the live recheck turn web pages into course files that every later session loads as trusted
material; nothing stated that pages are data. Defence in depth: (1) policy in four skills and `docs/UNTRUSTED_CONTENT.md`
(extract facts with sources, never copy prose, never obey a directive, ignore instructions found in course files);
(2) a deterministic net: `scan_untrusted.py`, wired as a **blocking** check in `postcompile_gate.py` for the serious
classes. Rules were tuned against realistic teaching text first - "disregard unlawfully obtained evidence", "act as a
reasonable person", "send a letter before action" must pass - which is why `act as` is not a rule and the exfiltration
rule requires an object (learner/files/credentials...) AND a destination word. The scanner is heuristic and says so;
disguised injections need the skill rules and the planned injection evals (A-xx). Separate finding while reviewing how
learner words reach commands: the `error_log.py append` example put the free-text note inside shell double quotes, so
a quote or `$(...)` in it could execute. Notes now travel on stdin via a quoted heredoc; erasure pastes the script's
own phrase rather than the learner's message.

## 4 Oct 2026 — v1.22.0: backup and restore (tasks E-24, C-08)

`.gitignore` keeps learner data out of version control, so before this the only copy of a learner's history was the
live folder (the toolkit backup existed but defaulted to a path inside that folder). Design points: a backup is a
physical copy with a manifest of checksums; the history DB goes through SQLite's online-backup API so a concurrent
script write cannot produce a torn copy; restore verifies everything before touching disk, builds the result in a
sibling temp folder, and swaps by renaming the live folder aside rather than deleting it. Two bugs surfaced by the
tests, both fixed: a safety backup taken in the same second as the backup being restored got the same file name and
overwrote it (backups now never overwrite; a `-2`, `-3` suffix is added), and an early swap deleted the live folder
before the rename, so a failure mid-swap would have left nothing in place. `export_profile.py` remains the readable
logical export for the learner; backup/restore is for putting the system back exactly as it was. Not done: scheduled or
automatic backups (the plugin has no scheduler; the skill suggests backing up before `/audit` repairs and upgrades),
encryption (X-08), and copying a backup off the machine (left to the learner, and the skill says so).

## 4 Oct 2026 — v1.23.0: marketplace, build and release (tasks P-01, P-02, P-03, P-19, R-11, R-12)

Verified rather than assumed: `claude plugin validate --strict` (CLI 2.1.289) found one gap in the plugin manifest
(missing author) and none in 15 commands or 12 skills; marketplace add + install + uninstall + remove round-tripped
against this checkout. A packaging-time finding: skills and script docstrings cited `docs/*.md` paths that existed only
at the repo root, so an installed copy (source = `plugin/generic-tutor`) would have had dangling references; the three
referenced docs now live inside the plugin and skills use `${CLAUDE_PLUGIN_ROOT}`. The zip is built deterministically
so a release asset can be reproduced from the tag. The release workflow cannot be exercised before a tag exists; its
moving parts (version check, notes extraction, build) are covered by tests and run in the PR checks. Not done: running
the plugin inside Cowork itself, and a `/doctor` check that an installed copy matches the marketplace version.

## 4 Oct 2026 — v1.24.0: command context budget and command-specific skill splits (tasks P-15, K-05/K-09 first step)

Measured before changing anything: `/list-courses` loaded the entire 30 KB `course-runner` skill to print a status
table, and `/drop` loaded `journey-planner` plus `course-auditor` (39 KB) to flip one field. Those were the clear wins
because the moved text is needed by exactly one command; nothing on a teaching path was touched. Sections were moved
verbatim and checked line-for-line (0 lines lost; only pointer/heading lines added). Deliberately NOT done: splitting
`course-runner` and `course-compiler` internally (live recheck, convergence, remediation, diagnostics). Those
instructions are read in the middle of teaching, and on-demand reads of situational files would silently drop them if
the model skipped the read; there are no evals yet to measure that risk (Phase 3). They stay whole until a before/after
eval exists, which is why `/continue` (48.9 K chars, ~12 K tokens) remains the budget's biggest line. The ratchet means
the number can only go down on purpose. Character counts are an estimate (chars/4), good for comparison, not billing.

## 4 Oct 2026 — v1.25.0: skill contracts, description checks, argument validation (tasks K-00..K-04 rollout, K-33, C-01, C-02, C-15 part)

The Contract blocks were written from the scripts each skill actually calls and the fields each script owns (the
ownership table in `docs/ARCHITECTURE.md`), not from the skills' own prose, and the lint resolves every script named in
a Contract against `scripts/` so the block cannot drift into fiction. They cost context (every command that includes a
skill grows by about 0.6-1.1 K chars); the budget ratchet was raised once, on purpose, rather than weakening the check.
Descriptions matter because they are what routes a skill: capped at 400 characters, required to name a command or say
there is none. Argument handling used to be implicit in each command's last line; it is now explicit: missing id -> offer
the valid choices (never guess a "close match", which `profile-kernel` already forbade), invalid id -> state the rule.
Decision recorded in PLAN section 10 (item 3): the owner will not mark anything; evaluation references must come from
computable answers or openly licensed published schemes, and spot-checking is replaced by automated agreement checks.

## 5 Oct 2026 - evals: harness, five suites, sonnet baselines (tasks A-01, A-02 part, A-03 baseline, A-04, A-06, A-08, A-09, A-10, X-01 evals)

The owner will not mark anything, so every reference comes from construction, a deterministic oracle or openly licensed data
(GSM8K via the Hugging Face connector; the sandbox proxy blocks direct downloads). Suites run the real plugin text (tutor-core
plus the relevant course-runner paragraphs) as the system prompt through `claude -p` with no tools; each report carries a
hash of that text. Baseline (sonnet, 3 samples): grading 35/35 acceptable, 0 false passes, A1 vs oracle 100%; safety 12/12;
injection 8/8, 0 obeyed; gates 7/7 against real `gate_check.py` output; diagnostics 14/14 scored, 1 ambiguous.
What the numbers do and do not say: the grading and gate sets are easy and clean, so a perfect score shows the tutor does not
wave through wrong or unsupported answers and does stop at gates - not that grading is solved. Real learner text is messier.
Two process findings. (1) A first draft of the grading `slip` label said "fail"; the model answered "ask them to explain
first" - which the plugin's own rule (working does not support the answer -> diagnose before recording) supports. Labels now
carry an ACCEPTABLE SET and only outcomes outside it, plus a per-case CRITICAL outcome (false pass, advising on a real matter,
obeying an injection, teaching a blocked course), count as failures. (2) Two diagnostic scenarios were classified unanimously
differently from my label; both were genuinely ambiguous as written, so the scenarios were replaced with single-mechanism ones,
and the rule recorded in `diagnostics.py`: when samples agree against the label, suspect the label first, but never tune a
case toward the model's answer without that reason. A harness bug worth recording: a backend outage originally produced
"accuracy: None" (no data) instead of a failure; no usable reply is now an errored case that counts against accuracy.

## 5 Oct 2026 - v1.26.0: selection, interleaving and readiness (tasks L-03, L-04, L-05, L-07, L-10, C-13)

The tutor already measured per-item mastery, errors and review state but used them only as pacing hints. Three small,
deterministic scripts turn them into decisions, following docs/PEDAGOGY.md (spacing, retrieval and interleaving are the
better-evidenced mechanics; the gaps were that review was a flat list and practice ignored what the learner was weak on).
Choices worth recording: review ordering puts overdue before weak-first so the spacing schedule is respected, and weakness
is the tie-breaker within a day; round-robin across courses is what makes a mixed session, at the cost of a slightly
longer gap for a very overdue card in a minority course when `--limit` bites; `next_items` keeps >=1 prior item whenever
prior items exist and the set has 3+ items, because a ratio that rounds to zero would silently turn interleaving off. The
70/30 split and the weakness weights are design defaults, not fitted values (stated in the script docstring). Readiness is
deliberately a band, never a number or a grade: the evidence (a handful of BKT observations on synthetic-sized practice) does
not support a prediction, and `/readiness` says so every time via the caveats. Not done: exam simulation and past-paper
timing (needs a question-bank format, N-07), and evaluating whether these selections improve learning (needs real learner
data; the evals cover tutor behaviour, not outcomes).

## 5 Oct 2026 - v1.27.0: content contract, reusable content CI, min_engine_version (tasks N-01, N-02, N-03, S-12 part)

The engine and the (private) content library are developed apart, and the only interface was implicit in the scripts. The
contract is now written down and executable: one driver runs the same structure/coverage/schema/injection/version checks the
engine uses at runtime, and a reusable workflow lets the content repository run it without copying code (it checks out the
public engine at a pinned ref). `min_engine_version` lets content move ahead of an installed plugin safely; an unknown
engine version never blocks, because blocking on uncertainty would strand a working install. The driver deliberately does
not do live-web verification (grounding, coverage re-derivation): that needs judgement and network, and stays in `/audit`.
The earlier smoke test of the driver was replaced by one that seeds each fault class and asserts the course fails.
Not done: the content repository's own workflow file (it lives in that repository; the snippet is in the contract), and
schemas for `change.md` (S-11) and `exam/exam.md`.

## 5 Oct 2026 - evals: criteria suite (A-03 expansion)

Extended answers cannot be given a numeric oracle, so the reference is built in: each answer is assembled from sentence blocks
per criterion (the correct statement, a classic-error statement, or nothing) plus true padding, so which criteria it earns is
known by construction. The failure it hunts is the one a grading tutor is most prone to: crediting a point that is stated but
wrong. First run (sonnet, 3 samples): 16 scored, 2 ambiguous, 1 critical sample. The ambiguity traced to my construction -
the bookkeeping rubric had a "debits equal credits" criterion that contradicted the deliberately wrong "credit the inventory
account" block beside it, so a careful grader could reasonably deny it. Replacing it with an independent criterion gave
18/18, per-criterion accuracy 1.0, 0 critical samples. Recorded as a baseline; three samples per case is a small sample, and
the lone critical sample before the fix cannot be attributed with certainty to the construction flaw.

## 5 Oct 2026 - v1.28.0: opt-in deadline planning and retrieval warm-up (tasks L-12, K-20, L-02)

The planner's step 2 told the model to sum "course.json's per-stage estimate", a field nothing ever wrote; the arithmetic was
prose and the input did not exist. `plan_estimate.py` makes it a script with a stated default (3 slots per remaining stage:
lesson, practice, test; +10% review) that a course can override. Deadline support was an owner-delegated decision (PLAN
section 10, item 4): one optional date per course, never requested unprompted, only compared against the learner's own stated
rate; a past date is "expired" (reported, ignored) rather than silently acted on. The comparison bands (on_track >= 1.25x
needed, tight >= needed) are design defaults. Retrieval warm-up is a few lines in course-runner, deliberately outside the
test path: it reuses the existing review machinery, writes nothing to `syllabus_status`, and is skipped silently when nothing
is due. Not done: triage by marks-per-hour (there are no per-item mark weights in the data), and learner-facing display of the
target in `/status`.

## 5 Oct 2026 - v1.29.0: accessibility rules, exam simulation, dashboard, profile write path, migration backups (tasks K-04, L-18, L-08, K-31, N-07, U-03, C-09, C-11, E-12)

Accessibility is the first change measured BEFORE and AFTER with the eval harness. The first comparison used per-case majority
votes and said "no improvement" (0.67 vs 0.58, within noise on 12 cases); looking at violation classes per sample told a different
story (mode cases, 36 samples per arm: compliant 18 -> 25; italics 3 -> 0, no steps 3 -> 0, unexplained terms 8 -> 2, over-long
blocks 11 -> 10). Two metric bugs were found on the way: bold markers hid "Term** (explanation)" from the explained-at-first-use
check, and a required concept was lexical ("numerator") when a plain-language reply can legitimately say "top number". Lesson
recorded in the evals README: compare skill versions on sample_accuracy and violation classes over >=30 samples, never on
majority-vote accuracy alone. An explicit "count the sentences" instruction did not move the block-length violations (11 -> 10);
that rule is only partly followed and says so honestly here rather than in the skill.
Exam simulation follows the project's honesty rules: the paper carries no mark scheme, no grade boundaries are claimed (they are
per series and not held here), time cannot be enforced and the skill says so, and a mock never touches syllabus_status. No course
has a question bank yet (the compiler does not write one), so /mock is infrastructure until content exists; drafting banks is
deliberately not automated because marks and schemes must come from sourced material. profile_init/profile_set close the last
free-hand JSON write on learner data (profile edits were model-written); the whitelist excludes ids, ledgers and counters.

## 5 Oct 2026 - v1.30.0: session_state.py and the roster-reset bug (tasks K-32, V-09)

Writing the script owner for the remaining hand-written fields exposed a latent defect: nothing ever moved a course out of
test_pending_convergence after its stage passed. cohort_status derives test_ready from that state alone, so the next stage's
convergence check would have treated the course as already waiting. The reset now lives in record_stage_result.apply (the one
place that knows a pass happened), guarded by a shared TEST_PENDING constant because test_eligibility forbids state literals
outside cohort_status. The first version of the regression test used a standalone course as the "peer" and passed vacuously;
standalone courses are their own cohort, so the test now uses the dropped same-cohort fixture course made active.

## 5 Oct 2026 - v1.30.1: idempotency audit (E-13)

Calling every writer twice found one defect and several intentional non-idempotent events. The defect: apply(S2, pass) after
the learner had already moved on re-set current_stage to the stage after S2. The advance now only moves forward along the
ladder. The event-style writers (errors, confidence, mastery, remediation, review, mocks) stay non-idempotent on purpose; the
guarantee there is that the model calls them once per event, which verify_session already checks from the ledger.

## 5 Oct 2026 - v1.31.0: --help everywhere (E-09, partial)

The done-when of E-09 is "--help works on every script, legacy invocations still pass". Rewriting 45 hand-parsed CLIs onto
argparse would have changed error text pinned by the golden snapshots for no learner-visible gain, so --help is a shared
two-line hook that prints the docstring's Usage section. Argument parsing itself stays as it is; the full argparse migration
is deferred until E-10 (envelope) forces a touch of every script anyway.

## 5 Oct 2026 - v1.32.0: opt-in envelope and error codes (E-10, E-11)

Scripts print through many paths (emit, direct prints, sys.exit), so the envelope wraps the process rather than each call
site: --envelope swaps stdout for a buffer and writes the wrapped document at exit with the original status. This made every
script conform at once with no golden churn. Codes are inferred from message text, which is crude but covers the closed set
and is tested; scripts naming their own code, and making the envelope the default, wait until skills stop parsing legacy keys.

## 5 Oct 2026 - v1.33.0: history reports (E-16)

The SQLite history was written but never read. Role decided: append-only history for the auditor and for humans, never an input
to a teaching decision (JSON stays authoritative, so a corrupt or missing DB cannot change what a learner is taught). The three
reports are plain GROUP BY queries, opened read-only so a report can never create or alter the file; a missing DB is an error
that says when it appears. The auditor's cohort rollup still walks the JSON files; this is the per-learner view.

## 5 Oct 2026 - v1.34.0: deck_add.py (K-22, K-23, K-25)

stage-recap appended cards by editing the deck JSON, the last unowned write on scheduling data and the only place card quality
could not be checked. The limits are mechanical heuristics (length, one "?" per front, no "a) b)" lists, normalised-front
dedupe) chosen because they are decidable in code; whether a card is *good* stays with the model. Rejected cards are reported with a
reason so the model can rewrite once. Retiring cards and a cloze type (L-06) are not done: both need a schema change.

## 5 Oct 2026 - v1.35.0: audit_status.py (K-15)

The auditor's "version-check stub" was a sentence describing a comparison nobody ran, and (written before
the real library was checked; 22 of 62 courses do carry a stamp, from earlier releases) stamping stays the audit's job: passive
detection, active fixes. Patch releases are ignored on purpose: a patch never changes what an audit checks.
Golden snapshots now mask engine_version so a release bump does not churn them.

## 5 Oct 2026 - v1.35.1: first run over the real library

Until now the validator ran only on fixtures. The first run over the 62 real courses failed two (one scanner false positive that
blocks shipping, one schema too strict for a documented value) and produced 1,262 advisories from the engine's own template line.
Lesson: a blocking rule needs a precision check against real prose, not only a recall check against attack strings; the injection
tests now include teaching sentences that contain the trigger verbs as nouns. The scanner is still regex-based and will have
other false positives; it blocks only on four high-confidence rules and everything else stays advisory.
