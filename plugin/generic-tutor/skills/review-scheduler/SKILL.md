---
name: review-scheduler
description: Runs due spaced-repetition flashcards, on demand via /review or automatically when a course is filling test_pending_convergence slots. Schedules by session slot, never by date. Does not author cards itself — stage-recap seeds the deck on every stage pass.
---

# Review Scheduler — slot-scheduled spaced repetition

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

## Scheduling (SM-2-lite; simple on purpose) — run the script, don't re-derive the arithmetic
- New card: `interval_sessions = 1`, `ease = 2.3`, `lapses = 0`, `due_at_slot` = the current slot + 1 (no script call needed for a brand-new card — there's nothing to compute yet).
- Every subsequent update (correct or incorrect recall), for a card that already has a recorded `interval_sessions`/`ease`/`lapses`:
  ```
  python3 /EDU/.tutor-scripts/review_math.py <old_interval_sessions> <old_ease> <old_lapses> <current_slot> <correct:true|false>
  ```
  Write its output straight back into the card's `interval_sessions`, `ease`, `lapses`, and `due_at_slot` — don't hand-compute the growth factor, the ease floor, or the reset-to-1-on-miss rule; this is exactly the kind of small recurring arithmetic that's easy to quietly reimplement inconsistently across sessions, and the script is the one place it's decided.
- A card is "due" whenever `session_slot` has reached or passed `due_at_slot`.
- The script guarantees a correct recall always lengthens the interval by at least one slot (a card can no longer get stuck at interval 1 after repeated lapses), and ease recovers slightly on each correct recall so a lapse is a setback, not a permanent penalty. Intervals are capped (30 sessions, `MAX_INTERVAL_SESSIONS` in the script) so a well-known card is still revisited within a term rather than drifting a year out.

## Running a review pass
1. Gather every due card, across every deck belonging to courses currently eligible for slots (per `journey-planner`).
2. Present them plainly, one at a time — right/wrong, brief explanation why, move on. This is retrieval practice, not a new teaching moment; don't re-lecture on a miss, just correct it and reschedule.
3. For each card just reviewed, call `review_math.py` (above) with its prior state and the recall outcome, and write the four returned fields back onto the card.
4. A review pass never writes to `syllabus_status` or `confidence` — it's a different kind of signal from a graded stage test, and conflating the two would undermine the honesty of what a "pass" actually means elsewhere in this system. A recurring miss on the same card is exactly what `error_patterns` (owned by `course-runner`) is for; surface a genuinely recurring one there instead.

## What this skill does not do
Does not author cards, does not grade a stage, does not touch `syllabus_status`, does not schedule by date. If a course has no deck yet (no stage has passed there), there's simply nothing to review for it — that's expected, not an error.
