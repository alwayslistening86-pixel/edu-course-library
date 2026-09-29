---
name: stage-recap
description: Fires automatically the moment a stage test genuinely passes — never on fail, never on any other trigger. Generates flashcards that seed review-scheduler's deck, and a standalone take-home worksheet with an answer key. Has no command of its own; course-runner invokes it.
---

# Stage Recap — fires on pass, produces one tracked output and one untracked one

## Invocation
No command of its own. `course-runner` invokes this skill at exactly one moment: immediately after a stage's `test.md` is graded and the result recorded as `syllabus_status: "pass"` for that stage. A fail routes to remediation instead (see `course-runner`) — recap and remediation are a clean split by outcome, and neither should try to do the other's job.

## Two outputs, deliberately asymmetric

### 1. Flashcards — tracked, feeds `review-scheduler`
Draft a small set of cards from the just-passed stage's `rubric.json` criteria and the key facts/steps the stage actually taught — enough to exercise recall of the criteria that were graded, not an exhaustive re-teaching of the stage. Tag each with `stage_id` and hand them to `review-scheduler` to append to that course's deck (`due_at_slot` starting at the next slot, per that skill's scheduling rule). This is the concrete answer to what fills a course's slots while it's waiting at `test_pending_convergence` later in its journey — those review sessions are drawing directly on cards generated here, at each of a course's own prior passes.

**If this stage's `error_patterns` has entries** (check `subjects/<course_id>.json` — a genuine pass doesn't erase the history of what it took to get there), add one extra card per distinct diagnosed cause, phrased against the actual misconception or slip rather than as a generic restatement of the rubric criterion. Where an entry's `misconception_id` matches an entry in `stages/<stage_id>/misconceptions.json`, phrase the card directly against that documented pattern and its correction — this is what keeps a documented misconception from resurfacing untested just because the stage was ultimately passed. This is additive, not a replacement for the rubric-derived cards above.

### 2. Take-home worksheet — untracked, handed off, forgotten
A short set of extra practice items in the same spirit as the stage's `practice.md`, using reserved seed material where the compiler set any aside for this purpose, or freshly constructed in the same spirit otherwise. **Always include a full answer key** — since nothing about this is discussed back with the system, an unanswered worksheet is close to useless for a learner checking their own work alone.

Generate it as a small document via the environment's document-creation tooling and hand it to the learner as a file (not an artifact, not a persistent object) — this is a one-off courtesy, not a system feature with a lifecycle.

**This output is never tracked, anywhere, by design.** It does not touch `syllabus_status`, `error_patterns`, `confidence`, or any review deck. The system does not know, and never asks, whether the learner opens it, attempts it, or ignores it entirely. This is the one deliberate exception to the rule that everything else in this plugin eventually feeds back into some piece of state — homework is explicitly not expected to ever be done; it exists purely as an extra opportunity, and adding any tracking to it would misrepresent what it's for.

## What this skill does not do
Does not fire on a failed test. Does not grade anything, ever — the worksheet's answer key is for the learner's own use, not for the system to check against. Does not persist any record of whether the worksheet was generated more than once for the same stage-pass (regenerating it on request is harmless, since nothing depends on it existing exactly once). Does not write to any file outside `review-scheduler`'s deck for the flashcard half of its output.
