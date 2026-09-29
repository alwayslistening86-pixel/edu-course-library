---
name: course-runner
description: Resumes and teaches an existing course via /continue, and lists course status via /list-courses. Enforces the level-lock and phase-convergence gates, runs the once-per-calendar-day live source recheck, and hands off to stage-recap and review-scheduler at the right moments.
---

# Course Runner — v8 (grounding-gated, prerequisite-gated, cohort-convergent, bottleneck-aware, coverage-honest, notice- and practical-aware, diagnostic)

## Invocation
This skill runs via `/continue <course_id>` (to teach) or `/list-courses` (to see status across all courses — including each course's `coverage_status`: `full`, `partial` with items-taught-of-items-itemised, or `unverified`, so a learner can see at a glance which courses are known to cover their specification and which are not). From v1.3.0 `/list-courses` also shows, per course: **standalone** (instead of a level) or the level with its `level_basis` — a `declared` level is always labelled "declared", never shown as if it came from a framework; its prerequisites (`requires_complete`, any-of entries as "one of …") and, for the active learner, whether each is met; any practical stages and the capability they need; and, for the learner's own enrolments, **theory-only** where practical stages are withheld (a complete theory-only course is shown as "complete (theory-only)"). Courses in `/EDU/_historic/` are not courses for learning and are not listed. A natural-language "let's carry on with Contract Law" should get redirected to `/continue ou_contract_law` rather than triggering this skill on inferred intent.

## Gate order — all of these run, in this order, before any teaching happens
**Run the gate check for real, don't re-derive it by reading files yourself:**
```
python3 /EDU/.tutor-scripts/gate_check.py <course.json path> <subjects.json path, or the literal string NONE if it doesn't exist yet> <the learner's profile subjects/ dir> <the /EDU/courses/ dir> <today's date, ISO format>
```
Treat its JSON output as authoritative — `can_proceed` and `first_blocking_gate` tell you whether to stop, and exactly where. Do not independently re-check `folder_access`, `grounding_status`, or `roster_state` by reading the files yourself once the script has answered; a hand-rederivation of the same gate is exactly the kind of prose-drift that let `cohort_id` go unused for a full release (see `DESIGN_NOTES.md`'s v1.0.1 entry). The gates, for reference (what the script is actually checking, so you can explain a block plainly to the learner):
1. **Folder access** — `course.json.folder_access.status` must be confirmed. If blocked, ask the same confirmation question the compiler would have asked.
2. **Grounding** — `course.json.grounding_status` must not be `suspended_ungrounded`. If blocked, say plainly that this course's rubric source could no longer be verified, that progress is frozen exactly as it stands, and that the learner may either leave it held (no cost, revisited automatically whenever `course-auditor` runs) or drop it with no trace at all (see `course-auditor` for exactly what "no trace" means — this is different from an ordinary `/drop`). Do not run the live recheck or anything else on a suspended course; that's `course-auditor`'s job, not this skill's.
3. **Enrollment state** — the learner's own `roster_state` for this course must be `active` or `test_pending_convergence` (an enrollment file that doesn't exist yet is the defensive-create case and passes), and the course must not be complete. `dormant`: say so plainly, name what it's waiting on (see `course-compiler`'s level-lock section), and stop — don't teach a dormant course under any circumstance. **Prerequisites (v1.3.0):** the same gate also blocks when the script reports `prerequisites.met: false` (detail names the unmet entries). Say which courses must be finished first ("one of …" for an any-of entry), and stop. This normally can't happen, because `/add-course` refuses an unmet prerequisite, but it can if a prerequisite course was reopened (e.g. by a capability declaration) after this one was added. `dropped`: progress is preserved but the course is paused — tell the learner to resume it via `/add-course` (which re-checks the roster cap); never teach it directly, since that would sidestep the cap. Complete (every stage passed, exam passed if enabled): congratulate and stop; a complete course is derived from data, not a stored state, and no longer counts toward the roster cap or holds up its cohort.
4. **Live recheck gating** — the script only reports `needs_recheck: true/false`; see below for what to actually do when it's true. This is not a stop gate.
5. **Phase-convergence** — the script's gate-5 output tells you whether this course's cohort has converged and, if not, who the bottleneck is; see below for what that governs.

**Notices (v1.3.0) are reported alongside the gates, not as one.** The script's `notices.due` lists the course's `learner_notices` that apply to the learner's current stage (or the whole course) and that this learner hasn't yet acknowledged. At the start of the session, before teaching, read each one to the learner plainly and in full (it's usually time-limited, e.g. set texts that change for later exam years, with a possible re-sit). Then append `{"id": <notice id>, "on": <today>}` to the enrolment's `notices_acknowledged`, so it isn't repeated. Never skip or summarise away a due notice.

**Practical stages (v1.3.0)** come in the script's `practical` block. If `withheld_stages` is non-empty, the learner is studying this course **theory-only**. Say so in the same opening line as any coverage disclosure, name the withheld stages, and name the `items_withheld_for_learner` if they ask. Never teach or test a `withheld` stage; move straight past it in the ladder. If the learner declares the capability mid-course (via `/profile`), `profile-kernel` runs `apply_capabilities.py`, which unlocks those stages. When `current_stage_is_practical` is true, the stage is open to this learner. Tell them at the start that its test is marked from the work they share (images), against the board's own criteria, and is practice, not certified coursework. Run `apply_capabilities.py` defensively once per session for a course with practical stages; it's idempotent. If it would reopen a completed course, don't write it, and ask the learner first.

**Standalone courses (v1.3.0)** pass the same gates. The script's `standalone: true` means the course has no level: it's never dormant for level reasons, its cohort is itself alone, so it tests as soon as it's ready, and finishing it never changes `highest_level_cleared`. Never describe a standalone course as being "at level N".

**Coverage is reported alongside the gates but is not one of them.** The script's `coverage` block (`effective_status`, `disclose_to_learner`, `detail`, and — once itemised — `items_total`, `items_taught`, `uncovered_items`) never changes `can_proceed`: a course whose syllabus has not been fully itemised and mapped is still teachable, but it must never be presented as the whole specification. When `disclose_to_learner` is `true`, say so in **one plain line at the start of the session** (not repeated mid-session): *"this course is [unverified — never checked against the full specification | partial — N of M specification items are taught]; it does not yet cover everything the exam board's syllabus lists."* Name the uncovered items if the learner asks. Never say or imply that finishing the stage ladder means the specification has been covered unless `effective_status` is `full`, and even then only as *declared* coverage (see below). The value is computed from the files each time (`coverage_check.py`); a stale stored `full` cannot silence it.

The script stops at the first blocking gate (1–3) and won't report gates past it — that mirrors "don't run anything else on a suspended course" exactly, so there's nothing further to check once it returns a block. Only when `can_proceed` is `true` does teaching, review, or grading proceed.

## Live recheck gating
Gate 4's `needs_recheck` (from `gate_check.py`, above) already applied the deterministic part of this rule — `currency == "historical"` skips permanently, and a `last_live_recheck` of today's date skips for today — so don't re-derive that decision by reading `course.json` again. If `needs_recheck` is `false`, go straight to the next gate. If `true`, run the recheck below — this part is genuinely a research task (real web search and comparison), not something the script can do, so it stays entirely your job.

**Live recheck procedure:**
1. Read `rubric.json` and `curriculum_map.json` for the bound source.
2. Search for that source's current, live specification and mark scheme.
3. Compare: does the current stage's grading criteria/threshold still match `rubric.json`? Does `covers_syllabus_refs` still correspond to a real, current syllabus item? If the course is itemised (`_syllabus_items`), does the live specification's version/issue still match `_items_source.version`? A mismatch is logged in `change.md` and `/audit` is recommended — the runner does not re-itemise; that is `course-auditor`'s coverage pass.
4. **Nothing changed** → proceed silently, no write needed.
5. **Something changed** → append a dated entry to `change.md` (create if needed) with old value, new value, affected stage(s), and source reference. Tell the learner plainly what changed and what it means for their current stage. If a stage already marked `pass` in `syllabus_status` is invalidated by the actual graded criterion changing (not just wording), flag it — don't leave a stale pass on record.
6. If web search isn't available in this context, skip the recheck and say so plainly rather than proceeding as if it happened.
7. **If the source no longer resolves at all** (not drifted — genuinely gone), don't guess or wait for the next scheduled recheck: set `grounding_status: suspended_ungrounded` immediately, with a `suspension` block recording why and when, and stop — this is now Gate 2's job on every future `/continue` until `course-auditor` revives it.
8. **Whether or not it actually ran** (steps 4–7 above, but not the `needs_recheck: false` skip), write `last_live_recheck` = today's date to `course.json` — this is the one write in this section that isn't conditional on outcome, and it's why the next `/continue` this calendar day will get `needs_recheck: false` from the script without re-running any of this.

## Phase-convergence — the cohort testing gate
A **cohort is every course sharing the same `subjects/<course_id>.json.cohort_id`** — not every active course in the roster globally. `cohort_id` is nothing more than a per-learner cached copy of that course's own `academic_level`, read from `course.json` and written once when the enrollment file is created (see `course-compiler`); it's stored on the subjects file, rather than looked up fresh each time, purely so this gate can group cohorts from the learner's own `subjects/*.json` files without opening every course's `course.json` to do it. It never changes afterward for a given enrollment. This matters because a learner can legitimately have courses at two different levels active at once — e.g. a fresh level-2 course added after `highest_level_cleared` reached 3, running alongside a level-4 course that's the current lock floor — and those two have no business waiting on each other's test-readiness; they aren't part of the same "term." Scoping by level is what the school-term analogy in this section actually intends, and is the reason the schema carries a `cohort_id` field at all.

**The actual grouping and convergence check is computed by `gate_check.py` (via `cohort_status.py`) in the gate check above — don't re-derive it by reading every `subjects/*.json` yourself.** Its gate-5 output already applied the correct restriction (only `roster_state: active` or `test_pending_convergence`, excluding anything whose bound `course.json.grounding_status` is `suspended_ungrounded`) and already scopes strictly by `cohort_id`, never globally — this is precisely the rule that a hand-rederivation got wrong once before (`DESIGN_NOTES.md` v1.0.1: cohort_id existed in the schema but the convergence check pooled every course together instead). Trust `converged`, `waiting_on`, and `bottleneck` from its output.

**No course enters `current_phase: test` until every course in its cohort is simultaneously ready to test.** A course that finishes its current stage's lesson and practice does not proceed to test — it moves to `roster_state: test_pending_convergence` and waits there. The moment the script reports `converged: true` for that cohort, a testing round fires for all its eligible members at once. Nobody tests while anybody else in the *same-level* cohort is still mid-lesson or mid-practice — this is a whole-cohort rule, not a pairwise one, but it is scoped to one `cohort_id`, never global across levels.

**What fills a waiting course's slots**: a course sitting in `test_pending_convergence` doesn't idle and doesn't sneak ahead into new content. Its allocated session time defaults to spaced review of its own already-covered material via `review-scheduler` — this is exactly what the flashcards `stage-recap` generated at its own prior stage-passes are for. `journey-planner` should weight the cohort's shared capacity toward whichever course is the actual bottleneck (the one still furthest from test-ready), diverting just enough of the waiting course's slots to keep its review cadence alive rather than a full share.

**A failed test at convergence uses the identical mechanism as a structural wait.** If one course in the round fails its test while others pass, the failed course doesn't block the others from starting their next stage — it simply becomes the next round's bottleneck. Its content for the interim switches to remediation (see below) instead of new lesson material; the passed courses' slots get weighted down and diverted to their own review while they wait on this one course, exactly as if it were still catching up structurally. One mechanism, two triggers (behind vs. failed) — no separate logic needed for each.

## Remediation after a failed stage test
A failed test records `syllabus_status: "fail"` for that stage and does **not** advance `current_stage`. Log the failure the same way as any other diagnosed error (`error_log.py append`, `source_phase test`) — this is what "informed by `error_patterns`" concretely means; don't remediate from a vague sense of what went wrong when the structured record exists to say exactly. Also update confidence for the fail (see "Confidence" below).

**Record the attempt and get the action, rather than deciding it yourself:**
```
python3 /EDU/.tutor-scripts/remediation_state.py record <subjects.json> <stage_id> <cause> <current_slot>
```
- `same_framework_reexplain` (attempt 1) — re-explain within the current framework, targeted at the classified cause. Then attempt the stage's test again once the learner and the session both indicate readiness.
- `different_approach_and_check_earlier_stage` (attempt 2) — the same cause recurred, so switch to a genuinely different worked example or analogy. If `cause` is `missing_prerequisite` (or the pattern otherwise looks like one), this is also the moment to check whether the honest fix is revisiting an earlier stage or an earlier course, not re-explaining the current one again — say so plainly to the learner rather than pushing on regardless.
- `escalate` (past attempt 2) — **do not run a third system-driven remediation loop.** The stage stays `test_pending_convergence`. Tell the learner plainly, and honestly, that this one is taking longer than expected — this is not a judgment on them; it's logged for `course-auditor`'s cohort-wide rollup as a signal the *lesson* might need work, not just the learner. The learner may keep working the stage informally (it just stops counting as a system-driven attempt).

Only a genuine re-pass updates `syllabus_status` to `"pass"` — never fold "the learner has attempted this enough times" into a soft pass. On a genuine re-pass, call `remediation_state.py reset` (see above) and use `confidence_update.py`'s `pass_remediated` event, not `pass_clean` — real progress, credited less than a pass with no remediation needed.

## Confidence
`confidence` (in `subjects/<course_id>.json`, default `0.5` — genuinely unknown, not "struggling") is no longer a field nothing computes. On every graded stage-test outcome, call:
```
python3 /EDU/.tutor-scripts/confidence_update.py <old_confidence> <pass_clean|pass_remediated|fail> [--misconception]
```
Use `pass_clean` for a pass with no remediation this stage, `pass_remediated` for a pass that needed remediation, `fail` for a fail. Add `--misconception` when this event also produced (or confirmed) an `error_patterns` entry tagged `cause: misconception` — the costliest cause to leave uncorrected, penalised beyond an ordinary fail. Write the returned `new_confidence` back to `subjects/<course_id>.json`. `tutor-core`'s pacing rules ("doing well → move faster," "struggling → slow down") read this number — don't let it go stale by skipping the update on a routine pass.

## Folder shape this skill expects
```
/EDU/courses/<course_id>/
  course.json
  rubric.json                 ← REQUIRED, every entry sourced
  curriculum_map.json         ← REQUIRED: index of each stage's syllabus area(s); from 1.2.0 also the itemised syllabus (_syllabus_items) and each stage's covers_items
  connectors.md                ← records which suggested connectors are actually connected
  change.md                   ← created on first detected change; absent if none yet
  stages/
    <stage_id>/
      lesson.md
      practice.md
      test.md
      misconceptions.json       ← OPTIONAL, non-blocking: 2-4 sourced entries per stage (see "misconceptions.json" note above)
  exam/
    exam.md                   ← only if course.json.exam.enabled
```
Before running any stage content that mentions a connector, check `connectors.md` — only treat a connector as usable if marked `connected` there.

Progress lives outside this folder, at `/EDU/profile/<active_user_id>/subjects/<course_id>.json` (see `profile-kernel`). `course-compiler` creates this file at enrollment time (both the dedupe-match and fresh-build paths). If it's somehow still missing on `/continue` for a course that genuinely exists under `/EDU/courses/`, create it defensively with the same defaults `course-compiler` would have used, then run `apply_capabilities.py` if the course has practical stages, rather than failing. The defaults are `roster_state: "active"`, `cohort_id` = the course's `academic_level` (or `"standalone:<course_id>"` for a standalone course), `syllabus_status` all-`unsat`, `current_stage` the ladder's first entry, and `notices_acknowledged: []`. `/continue` cannot run without an active profile; if none is active, tell the learner to `/run <user_id>` first.

## Running a stage (after all gates clear)
**Gate check** — prerequisites (`requires_complete`, a list since v1.3.0) are already checked by `gate_check.py` Gate 3. Don't re-derive them by reading other courses' files.

**Lesson** → `stages/<stage>/lesson.md`, no framework imposed, check understanding conversationally. **If the course is itemised, the stage's `covers_items` — resolved to their titles in `_syllabus_items` — is the checklist of what this lesson must teach, and `lesson.md` is the plan and floor, not the ceiling.** Work through every listed item before moving to practice; where `lesson.md` is silent or thin on an item, teach it from the source specification (`_items_source.url`) rather than skipping it, and say honestly if you are not certain of a detail. Do not teach an item that belongs to a later stage's `covers_items`. An unitemised (`unverified`) course is taught from `lesson.md` alone, with the disclosure above. **Nothing here tracks per-item progress** — a stage's pass is still decided by its `test.md` against `rubric.json`, which samples the stage rather than testing every item, so never tell a learner that a stage pass proves every item in it was mastered.

**Practice** → `stages/<stage>/practice.md`, framework introduced and exercised, low stakes, no grading. **This is also the diagnostic branch's home** — see "Diagnosing during practice, not just after a failed test" below. Struggle here is the cheap place to catch and correct a misconception; don't wait for a graded test to notice it.

**Test** → only reached via the convergence gate above. `stages/<stage>/test.md`, graded strictly against `rubric.json`. Record the result into `syllabus_status`. Only advance `current_stage` on a genuine pass, then to the next ladder stage that isn't `withheld`. **Grade the method, not just the final answer, wherever `rubric.json` gives you M/A/B (method/accuracy/communication) tags or an equivalent structured breakdown** — a right answer reached by a coincidentally-cancelling wrong method, or the right option picked for the wrong reason, is not a genuine pass even though the output matches. For anything short of a full worked long-answer this is easy to skip under time pressure; don't. If the learner's shown or stated working doesn't actually support the answer, that's a `diagnostic_gate.py` trigger-d case (reasoning_mismatch) — run the diagnostic exchange below before recording the grade, not after.

**On a genuine pass** → hand off to `stage-recap` immediately (flashcards seeded into `review-scheduler`'s deck, plus the untracked take-home worksheet) before moving on. **Also update confidence** (see "Confidence" below) and, if this stage had any `remediation` entry, clear it: `python3 /EDU/.tutor-scripts/remediation_state.py reset <subjects.json> <stage_id>`.

## Diagnosing during practice, not just after a failed test
Before this version, the only adaptive response in this skill was remediation after a hard test fail — a learner could visibly flounder through `practice.md`, still attempt the test, fail, and only then get any response tailored to what actually went wrong. This section is the missing branch.

**Run the gate, don't guess whether a moment is worth stopping for:**
```
python3 /EDU/.tutor-scripts/diagnostic_gate.py <subjects.json> <stage_id> <item_id> <explicit_confusion:true|false> <reasoning_mismatch:true|false>
```
Pass `explicit_confusion: true` when the learner has said, in any words, that they're confused or stuck. Pass `reasoning_mismatch: true` whenever the exchange surfaces a right answer with wrong or absent reasoning — a learner explaining their thinking unprompted, or asked to explain it, and that explanation not actually supporting the answer they gave. The script also checks two conditions from `error_log.py`'s own data (two unresolved misses on the same item; a recurring `cause` tag within this stage), so you don't need to track those by hand across a session. If `fire` is `false`, keep teaching normally — this branch is deliberately narrow; it should not fire on every wrong answer (see "What this costs" below).

**When it fires:** always **elicit before explaining** — ask what the learner did or thought, don't just tell them what's wrong. Their answer is what lets you classify `cause` against the script's `taxonomy` (one of `slip`, `missing_prerequisite`, `misconception`, `misapplied_procedure`, `comprehension` — the script returns the full table, including the right response and the wrong one to avoid, for each). This classification is a real judgment call; the script only decided the moment was worth stopping for, it never guesses the cause for you.

**Log what you found:**
```
python3 /EDU/.tutor-scripts/error_log.py append <subjects.json> <stage_id> <item_id> <practice|test> <cause> <misconception_id|NONE> "<free-text note>" <current_slot>
```
Match `misconception_id` to `stages/<stage_id>/misconceptions.json` when the diagnosed cause matches a known entry there (see "misconceptions.json" below); `NONE` when it's novel. Respond according to the taxonomy's `right_response` for the classified cause — never a generic re-explanation regardless of cause, that's exactly the failure mode this branch exists to avoid.

**When a later attempt on the same item is correct and confident**, resolve it rather than leaving a permanent black mark:
```
python3 /EDU/.tutor-scripts/error_log.py resolve <subjects.json> <item_id> <current_slot>
```
Without this, pacing would keep treating a learner as weak on something they've since mastered.

## What this costs, honestly
A diagnostic exchange is more turns and more tokens per stage than replaying `lesson.md` slower — that is the actual mechanism by which this gets closer to what a teacher does, not a free upgrade. It should not fire on every wrong answer; `diagnostic_gate.py`'s trigger conditions are deliberately narrow (recurrence, explicit confusion, or a caught false-positive) so the cost lands only where it's earned. This also isn't infallible — classifying a cause from what the learner says stays a judgment call the scripts bound and remember, never remove.

## Exam
Once every stage in `syllabus_status` shows `pass` (or `withheld`, for a practical stage the learner hasn't unlocked), and `course.json.exam.enabled` is true, mark `exam_status: "available"`. For a theory-only learner the exam covers the taught stages only; say so, and don't set exam questions on withheld stages. Grade against `rubric.json`'s `exam_rubric`. Record `exam_status: "passed"` only on a genuine pass. A course whose exam passes (or whose stage ladder completes with no exam) reaches `status: complete` — see `journey-planner` for how this feeds `highest_level_cleared`.

## Every write goes to the active learner's micro-profile (never another course's, never another learner's), except `last_live_recheck` and `grounding_status`
`current_stage`, `current_phase`, `syllabus_status`, `roster_state`, `exam_status`, `confidence`, `error_patterns`, `remediation`, `last_session_summary`, `notices_acknowledged` — all live in `/EDU/profile/<active_user_id>/subjects/<course_id>.json`. `error_patterns` is owned by `error_log.py`, `remediation` by `remediation_state.py`, `confidence` by `confidence_update.py` — write only through those scripts, never by hand-editing the field, for the same reason `review-scheduler` never hand-computes an interval. `last_live_recheck`, `grounding_status`, and `change.md` live on the shared course itself, since they're facts about the content, not about any one learner. `stages/<stage_id>/misconceptions.json` (2–4 sourced entries per stage, authored by `course-compiler`) also lives on the shared course — content, not learner state — and is read-only from this skill's side; a genuinely recurring novel misconception is a `course-auditor` proposal, never written here.

## What this still avoids
No hash chains, no refusal codes beyond plain honest explanations, no cross-course writes, no subject knowledge in this file, no testing outside a convergence round, no silent patching of a rubric or level that can no longer be verified (that's a suspension, handled by `course-auditor`, never smoothed over here).
