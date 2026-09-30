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
- **Guardian-oversight** — this is a private, non-distributed plugin; that concern
  doesn't apply here and was cut rather than built speculatively.
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
