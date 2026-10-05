---
name: review-scheduler
description: Runs due spaced-repetition flashcards, on demand via /review or automatically when a course is filling test_pending_convergence slots. Schedules by session slot, never by date. Does not author cards itself — stage-recap seeds the deck on every stage pass.
---

# Review Scheduler — slot-scheduled spaced repetition

**Contract**
- **Owns:** presenting due cards and rescheduling them (`review_math.py apply` writes the scheduling fields).
- **Reads:** `<course>_review_deck.json`, `student_profile.json.session_slot`.
- **Calls:** `review_select.py` (which cards, in what order), `review_math.py` (rescheduling).
- **Emits:** one card at a time, a brief correction on a miss, nothing else.
- **Never:** authors cards (`stage-recap` does); touches `syllabus_status` or `confidence`; schedules by date; re-teaches on a miss.
- **Failure modes:** no deck yet → nothing to review, not an error; `written: false` → the review still happened, it just will not be remembered.

## Invocation
`/review` runs a due-card session on demand for the active learner, across all their active courses. It also runs automatically, without a separate command, whenever `course-runner` needs to fill a course's slots while that course sits in `roster_state: test_pending_convergence` — see the phase-convergence section of `course-runner`.

## This skill does not create content
Cards are authored entirely by `stage-recap`, at the moment a stage's test genuinely passes, from that stage's rubric criteria and key facts. This skill only stores, schedules, and presents them — keeping the "who writes graded/teaching content" boundary consistent with the rest of the plugin (this file is scheduling logic, not subject knowledge, the same separation `tutor-core` already draws for itself).

## Deck file (`/EDU/profile/<active_user_id>/subjects/<course_id>_review_deck.json`)
Lives alongside the course's own micro-profile, under the same learner-isolation rules as everything else in `/EDU/profile/`.
```json
{
  "schema_version": 1,
  "course_id": "aqa_gcse_maths_8300",
  "cards": [
    {
      "id": "string",
      "stage_id": "S3",
      "item_id": "RM6" or null,
      "criterion": "M2" or null,
      "front": "string",
      "back": "string",
      "interval_sessions": 4,
      "due_at_slot": 18,
      "ease": 2.3,
      "lapses": 0
    }
  ]
}
```
`due_at_slot` is a session-slot count, not a date — consistent with `journey-planner` having no calendar concept anywhere in the system. **The current slot is `student_profile.json.session_slot`** (advanced once per session by `slot_advance.py` at `/run`; `gate_check.py` also echoes it as `current_slot`). Read it from disk — never estimate it from conversation history.

`item_id`/`criterion` (added alongside the pre-existing `stage_id`) name the specific syllabus item and rubric criterion a card exercises, when `stage-recap` can derive one cleanly at authoring time — the same taxonomy `error_log.py` tags entries with, so a card and the error that motivated it can be traced to the same item/criterion pair. Both are optional and independently nullable: a card built straight from a rubric criterion that doesn't map to one clean item, or a generic stage-level card, is still valid with one or both left `null` — `stage_id` remains the floor every card always carries. This skill does not derive or validate these fields itself; it stores whatever `stage-recap` hands it, unchanged, the same relationship it already has with `stage_id`.

## Scheduling (SM-2-lite; simple on purpose) — run the script, don't re-derive the arithmetic
- New card: `interval_sessions = 1`, `ease = 2.3`, `lapses = 0`, `due_at_slot` = the current slot + 1 (no script call needed for a brand-new card — there's nothing to compute yet).
- Every subsequent update (correct or incorrect recall), for a card that already has a recorded `interval_sessions`/`ease`/`lapses`:
  ```
  python3 /EDU/.tutor-scripts/review_math.py apply <deck.json> <card_id> <current_slot> <correct:true|false>
  ```
  **`apply` writes the four fields (`interval_sessions`, `ease`, `lapses`, `due_at_slot`) straight onto the card in the deck file itself** — this script owns the write, the same way `error_log.py`/`item_mastery.py` always have, so there's nothing left to hand-copy back. Don't hand-compute the growth factor, the ease floor, or the reset-to-1-on-miss rule; this is exactly the kind of small recurring arithmetic that's easy to quietly reimplement inconsistently across sessions, and the script is the one place it's decided. (The old positional `<old_interval> <old_ease> <old_lapses> <current_slot> <correct>` form still exists, pure arithmetic only, no file touched — for testing, not for live sessions.)
- A card is "due" whenever `session_slot` has reached or passed `due_at_slot`.
- The script guarantees a correct recall always lengthens the interval by at least one slot (a card can no longer get stuck at interval 1 after repeated lapses), and ease recovers slightly on each correct recall so a lapse is a setback, not a permanent penalty. Intervals are capped (30 sessions, `MAX_INTERVAL_SESSIONS` in the script) so a well-known card is still revisited within a term rather than drifting a year out.

## Running a review pass
1. **Select the cards with the script, don't gather them by hand:**
   ```
   python3 /EDU/.tutor-scripts/review_select.py <the learner's folder> <the /EDU/courses/ dir> [--course <id>] [--stage <id>] [--item <id>] [--limit N]
   ```
   It returns the due cards (front and back included) already ordered — most overdue first, then the items the learner knows least, then lowest ease — and dealt round-robin across courses so one subject cannot take the whole session, capped at `--limit` (default 20) with `remaining_due` telling you how many are left for next time. Pass `--course` / `--stage` / `--item` when the learner asks to review one topic (`/review <course>`). It only includes courses eligible for slots (per `journey-planner`).
2. Present them plainly, one at a time — right/wrong, brief explanation why, move on. This is retrieval practice, not a new teaching moment; don't re-lecture on a miss, just correct it and reschedule.
3. For each card just reviewed, call `review_math.py apply` (above) with its card_id and the recall outcome — it writes the four updated fields onto the card itself.
4. A review pass never writes to `syllabus_status` or `confidence` — it's a different kind of signal from a graded stage test, and conflating the two would undermine the honesty of what a "pass" actually means elsewhere in this system. A recurring miss on the same card is exactly what `error_patterns` (owned by `course-runner`) is for; surface a genuinely recurring one there instead.

## What this skill does not do
Does not author cards, does not grade a stage, does not touch `syllabus_status`, does not schedule by date. If a course has no deck yet (no stage has passed there), there's simply nothing to review for it — that's expected, not an error.
