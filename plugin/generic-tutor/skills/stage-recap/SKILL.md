---
name: stage-recap
description: Fires automatically the moment a stage test genuinely passes — never on fail, never on any other trigger. Generates flashcards that seed review-scheduler's deck, and a standalone take-home worksheet with an answer key. Has no command of its own; course-runner invokes it.
---

# Stage Recap — fires on pass, produces one tracked output and one untracked one

**Contract**
- **Owns:** seeding review cards for a just-passed stage (appended to the course's deck) and handing over an untracked take-home worksheet.
- **Reads:** the stage's `rubric.json` criteria, the learner's `error_patterns` for that stage, `misconceptions.json`.
- **Calls:** no scripts; new cards use the deck's scheduling defaults (interval 1, ease 2.3, due next slot) and `review-scheduler` takes over.
- **Emits:** flashcards in the deck and a worksheet file with a full answer key.
- **Never:** fires on a failed test; tracks or grades the worksheet; reproduces test items in the worksheet; writes outside the deck.
- **Failure modes:** deck file missing → create it with the standard shape; card tags it cannot derive → `null`, never forced.

## Invocation
No command of its own. `course-runner` invokes this skill at exactly one moment: immediately after a stage's `test.md` is graded and the result recorded as `syllabus_status: "pass"` for that stage. A fail routes to remediation instead (see `course-runner`) — recap and remediation are a clean split by outcome, and neither should try to do the other's job.

## Two outputs, deliberately asymmetric

### 1. Flashcards — tracked, feeds `review-scheduler`
Draft a small set of cards from the just-passed stage's `rubric.json` criteria and the key facts/steps the stage actually taught — enough to exercise recall of the criteria that were graded, not an exhaustive re-teaching of the stage. Tag each with `stage_id` and hand them to `review-scheduler` to append to that course's deck (`due_at_slot` starting at the next slot, per that skill's scheduling rule). This is the concrete answer to what fills a course's slots while it's waiting at `test_pending_convergence` later in its journey — those review sessions are drawing directly on cards generated here, at each of a course's own prior passes.

**Also tag each card with `item_id` and `criterion` when derivable.** A card built directly from one `rubric.json` criterion carries that criterion's key as `criterion`; when that criterion maps to a single syllabus item in `curriculum_map.json`, carry that item's id as `item_id` too. When a card doesn't tie cleanly to one criterion or one item — a broader stage-level recall card, say — leave the corresponding field `null` rather than forcing a fit; `stage_id` is the floor every card gets regardless. This is what lets a review card, a graded error, and a mastery estimate all be traced back to the same taxonomy instead of three separate ad-hoc labels.

**If this stage's `error_patterns` has entries** (check `subjects/<course_id>.json` — a genuine pass doesn't erase the history of what it took to get there), add one extra card per distinct diagnosed cause, phrased against the actual misconception or slip rather than as a generic restatement of the rubric criterion. Carry that entry's own `item_id` and `rubric_criterion` (if set) onto the card — the error already recorded exactly which item/criterion it was, so reuse it rather than re-deriving it. Where an entry's `misconception_id` matches an entry in `stages/<stage_id>/misconceptions.json`, phrase the card directly against that documented pattern and its correction — this is what keeps a documented misconception from resurfacing untested just because the stage was ultimately passed. This is additive, not a replacement for the rubric-derived cards above.

### 2. Take-home worksheet — untracked, handed off, forgotten
A short set of extra practice items in the same spirit as the stage's `practice.md`, using reserved seed material where the compiler set any aside for this purpose, or freshly constructed in the same spirit otherwise. **Always include a full answer key** — since nothing about this is discussed back with the system, an unanswered worksheet is close to useless for a learner checking their own work alone.

Generate it as a small document via the environment's document-creation tooling and hand it to the learner as a file (not an artifact, not a persistent object) — this is a one-off courtesy, not a system feature with a lifecycle.

**This output is never tracked, anywhere, by design.** It does not touch `syllabus_status`, `error_patterns`, `confidence`, or any review deck. The system does not know, and never asks, whether the learner opens it, attempts it, or ignores it entirely. This is the one deliberate exception to the rule that everything else in this plugin eventually feeds back into some piece of state — homework is explicitly not expected to ever be done; it exists purely as an extra opportunity, and adding any tracking to it would misrepresent what it's for.

## What this skill does not do
Does not fire on a failed test. Does not grade anything, ever — the worksheet's answer key is for the learner's own use, not for the system to check against. Does not persist any record of whether the worksheet was generated more than once for the same stage-pass (regenerating it on request is harmless, since nothing depends on it existing exactly once). Does not write to any file outside `review-scheduler`'s deck for the flashcard half of its output.
