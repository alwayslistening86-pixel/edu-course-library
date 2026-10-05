---
name: journey-planner
description: Computes and recomputes how a learner's weekly session capacity is allocated across their active, unlocked courses — in session slots, never calendar dates. Also owns /drop, and updates highest_level_cleared when a level's whole cohort completes.
---

# Journey Planner — slot-based allocation, no calendar

**Contract**
- **Owns:** the slot plan (advice only, nothing persisted), `/drop` (see `drop.md`), and raising `highest_level_cleared` when a whole level completes.
- **Reads:** `cohort_status.py` output (eligibility, bottleneck, `all_complete`, `level_ledger`), `roster_check.py`.
- **Calls:** `cohort_status.py`, `roster_check.py`, `roster_apply.py` (drop, advance), `plan_estimate.py`, `plan_target.py` (only when the learner gives a date).
- **Emits:** a sequence ("next N sessions: mostly X, review folded in") — never a calendar; approximate remaining time stated as an estimate.
- **Never:** stores a date unless the learner volunteers a real deadline (one optional `target`, via `plan_target.py`); schedules sessions on a calendar or reasons about weekdays; promises completion by a date; re-decides level-lock or convergence; sums eligibility by hand.
- **Failure modes:** no eligible courses → say what is blocking (dormant, suspended, nothing enrolled).

## Invocation
`/plan` runs once automatically as the final step of first-ever onboarding (after every initial course has been added), and again any time the learner explicitly re-runs it — after adding or dropping a course, or after a change to `availability.sessions_per_week`. It does not run silently mid-session; a re-plan is always visible and explicit, the same way every other state change in this system is.

## Why there are no dates anywhere in this file
Capacity is expressed purely as a rate — `sessions_per_week` — used only for rough arithmetic projection ("at this rate, roughly N weeks remaining"), never for placing anything on a calendar. Everything else this skill manages is a plain sequence of **session slots**: slot 1, slot 2, slot 3… A missed week doesn't make anything "late"; it just means the next slot happens whenever it happens. This keeps the framing honest about a fact that's true regardless of how carefully anyone plans: a learner could always move faster or slower than the plan assumes, and the system should never imply a false precision about *when* something happens — only *how much* is left and in *what order*.

## What determines eligibility to draw a slot at all
A course only receives slots if its `subjects/<course_id>.json.roster_state` is `active` or `test_pending_convergence` **and** its bound `course.json.grounding_status` is not `suspended_ungrounded`. `dormant` (level-locked), `dropped`, suspended, and **complete** courses draw nothing. Completeness (every stage `pass`, plus `exam_status: passed` if `course.json.exam.enabled`) is derived by `cohort_status.py`/`roster_check.py` on every call rather than stored as a `roster_state` value, so a finished course automatically stops occupying a roster slot and stops holding its cohort's convergence gate — there is no transition to forget to write. This means eligibility is entirely downstream of `course-compiler`'s level-lock and `course-runner`'s convergence gate — this skill doesn't re-decide either; it only allocates among whatever `cohort_status.py` (below) already reports as eligible. Don't compute this list by hand — the suspended-course exclusion specifically is the kind of check that's drifted out of a hand-derivation before (`DESIGN_NOTES.md` v1.0.1), so let the script be the one place it's decided.

## Allocation, per planning round
1. **List eligible courses and group them by cohort — run the script, don't re-derive it:**
   ```
   python3 /EDU/.tutor-scripts/cohort_status.py <the learner's profile subjects/ dir> <the /EDU/courses/ dir>
   ```
   Its output is already grouped by `cohort_id`, already restricted to eligible members (`active`/`test_pending_convergence`, not suspended), and already names each cohort's `bottleneck` (the eligible, not-yet-`test_pending_convergence` member with the most stages remaining) and whether it's `converged`. A learner can have more than one cohort active at once (e.g. a freshly-added low-level course running alongside the current lock-floor level); the script already keeps bottleneck identification **within each cohort separately** — never pool cohorts together when reading its output.
2. **Estimate remaining slots per course — run the script, don't sum by hand:**
   ```
   python3 /EDU/.tutor-scripts/plan_estimate.py <the learner's folder> <the /EDU/courses/ dir> --today <today's date, ISO>
   ```
   Per live course it gives stages remaining and an estimated slot count (3 per remaining stage unless the course sets `slot_estimates` / `slots_per_stage`, plus ~10% for review), the learner's `sessions_per_week`, and a rough `weeks_remaining_estimate`. These are labelled estimates; say so. `combined` is the total across courses for the step-5 split.
3. **Within each cohort, use the script's `bottleneck`** to weight the majority of that cohort's share of this round's `sessions_per_week` toward it.
4. **Everything else in `test_pending_convergence`** (in any cohort) gets only enough slots to keep its `review-scheduler` cadence alive (see `course-runner`'s phase-convergence section) — not a full share, since it has no new content to advance right now.
5. **Split `sessions_per_week` across cohorts** in rough proportion to each cohort's remaining estimated slots (step 2) before applying steps 3–4 within each — a learner with one small low-level course and one large current-floor course shouldn't have the small one starved just because it happens to share the plan with a bigger one in a different cohort.
6. **Within a session that must carry new material for more than one course**, prefer pairing a lesson (heavier, novel) against a review block (lighter, retrieval-only) over two dense lesson blocks back to back, once `review-scheduler` has material to draw on. Where two lesson blocks must share a session regardless, a contrasting pair (e.g. quantitative + humanities) is a reasonable anti-fatigue default — worth being honest that this specific pairing heuristic is a sensible design choice, not a strongly evidenced one, unlike the spacing benefit itself.
7. **Report the plan as a sequence, not a schedule**: "next N sessions: mostly Chemistry (bottleneck), a Contract Law review block folded in every other session" — never "Tuesday: Chemistry."

## Feasibility, stated plainly
**Deadline-aware planning is opt-in.** If — and only if — the learner mentions a real external date for a course (an exam, a resit), offer to record it: `python3 /EDU/.tutor-scripts/plan_target.py set <subjects.json> <YYYY-MM-DD> <today>` (and `clear` when they drop it). That one stored date is the only calendar date in the system and is not a schedule; nothing is placed on a calendar. Never ask for a date unprompted, and never infer one.

With a target set, `plan_estimate.py … --today <today>` adds a `target` block to the course: `days_left`, `slots_available` at the learner's stated rate, and `feasibility` — `on_track`, `tight`, `short` (with `shortfall_slots`) or `expired` (a date well in the past: ignored; offer to clear it) or `unknown` (no rate on file). Report it plainly and approximately ("at two sessions a week you have room for about 12 sessions before then; this course needs about 7 more"), never as a promise. When `short`, lay out the `options` it returns (more sessions, accept that later stages won't be reached before the date, move the date) and let the learner choose; do not quietly re-plan around the shortfall or trim a course's content. Without a target there is no deadline maths: only the rate-based "roughly N weeks" estimate.

## `/drop <course_id>`
Dropping a course (ordinary and suspended-course cases, waking what a drop unblocked) is described in `drop.md` in this folder; `/drop` loads it. Read it before dropping anything.

## Standalone courses and theory-only stages (v1.3.0)
- **Standalone courses** (`course.json.standalone: true`) draw slots exactly like any other eligible course. The script puts each one in its own cohort (`cohort_id` `"standalone:<course_id>"`), so it's its own bottleneck and tests as soon as it alone is ready. In step 5, treat each standalone cohort as one more cohort in the split. A standalone course never enters the level ledger. When one completes, there is no `highest_level_cleared` update to make: `level_walk` ignores non-numeric cohorts. Say plainly that finishing it frees a roster slot, and that its completion now satisfies any course that lists it as a prerequisite.
- **`withheld` stages** (a practical stage the learner hasn't unlocked) cost no slots. They count as done, and the script's `remaining_stage_count` already leaves them out.

## Updating `highest_level_cleared`
After any stage-test pass or exam pass changes a course's status to `complete`, ask `cohort_status.py` — don't re-derive completeness in prose, and don't re-list the profile's `subjects/` directory by hand:
```
python3 /EDU/.tutor-scripts/cohort_status.py <the learner's profile subjects/ dir> <the /EDU/courses/ dir>
```
Read the entry for the finished course's `cohort_id`. **`all_complete` is the one place this is decided**: it is `true` when at least one member is complete and nothing is blocking, where "complete" means every `syllabus_status` entry is `pass` and, if `course.json.exam.enabled`, `exam_status` is `passed`. `blocking_members` names anything still unfinished that counts (`active`, `test_pending_convergence`, `dormant`). **`excluded_members`** names unfinished courses that deliberately do *not* block a level from clearing: a **dropped** course (the learner set it down — `/drop` is a pause, and `roster_check.py` already ignores dropped courses when computing the lock floor, so counting them here would let an abandoned course hold every higher-level course dormant forever with no way out short of erasing the profile) and a **grounding-suspended** course (its source vanished under the learner; that is not their fault — see `course-auditor`). Exclusion is never silent: when a level clears with anything in `excluded_members`, tell the learner plainly which courses were left out and why ("Level 4 cleared. Contract Law was dropped unfinished, so it didn't count toward this — resuming it later via `/add-course` will reopen this level and lock the higher courses again until it is finished"), so the ledger stays honest about what was actually studied here.

**Then walk the ledger up rather than setting it to this one cohort's level.** The same output carries `level_ledger` — `stored`, `suggested_highest_level_cleared`, `cleared_cohorts` (the cohorts, in order, that were clear above the stored value) and `stopped_at` (the first cohort that isn't, with its `blocking`). The walk exists because the ledger can be deliberately lowered by a resume (`resume_enrollment.py --reopen-*`): if levels 1–3 were cleared, a level-2 course is resumed (ledger → 1) and later finishes, this course's own level is 2, but level 3 is still fully complete and must clear again in the same step — writing only `max(current, 2)` would leave it stranded until some other level-3 course happened to finish. It never lowers the ledger and stops at the first cohort that isn't `all_complete`; a level with no cohort at all, or whose only members are `excluded_members` (nothing complete, nothing blocking — for example a level whose sole course was dropped), is stepped over as vacuously clear rather than stopped at. Such levels are listed in `skipped_cohorts`; tell the learner about them the same way as any other excluded course ("Level 2 held only Contract Law, which was dropped, so the ledger passed over it"). Stopping there would strand every finished higher level behind a course the learner has set down.

Don't write the ledger yourself: run `python3 /EDU/.tutor-scripts/roster_apply.py advance <the learner's profile dir> <the /EDU/courses/ dir>`. It walks the ledger up as far as `level_walk` allows (never down), writes `highest_level_cleared`, and wakes the dormant courses that unlocks (`woke`). Tell the learner every level in `cleared_cohorts` and which courses woke, and let them re-enter allocation from the next planning round. If `written` is false, say which `blocking` members remain (`stopped_at`).

## What this skill does not do
Does not store or reason about calendar dates, days of the week, or reminders. Does not decide level-lock or convergence state itself — it only allocates among what those two gates have already made eligible. Does not promise completion by a specific date, only a rate-based estimate stated as one.
