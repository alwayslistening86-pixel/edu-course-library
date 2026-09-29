---
name: data-erasure
description: Permanently deletes the active learner's data on request, giving real effect to consent.status "revoked" rather than leaving it as a flag nothing acts on. Requires explicit confirmation — this is irreversible.
---

# Data Erasure

## Invocation
`/erase`, for the currently active learner only, and only with an explicit confirmation token supplied in the same or a following message — this is a genuinely irreversible action and should be treated with the same weight as any other permanent-deletion request: confirm plainly what will be removed before doing it, and do not proceed on an ambiguous or one-word request alone.

## What gets removed
The learner's entire `/EDU/profile/<user_id>/` folder — `student_profile.json`, every `subjects/<course_id>.json`, every review deck. This is a different and stronger action than `consent.status: "revoked"` alone (which, per `profile-kernel`, only stops *future* writes) — erasure removes what's already stored.

## What doesn't get removed
Shared course content under `/EDU/courses/` is untouched — it belongs to no single learner and other learners may still be enrolled in it. If this was the only learner enrolled in a given course, that course simply becomes unenrolled, not deleted; `course-auditor` will surface it as having no active enrollments on its next pass, but does not delete course content on that basis alone.

## After erasure
Confirm plainly what was removed. If the learner wants to start again later, that's a fresh `/add-profile` — nothing about this system treats a prior, erased profile as recoverable, by design.
