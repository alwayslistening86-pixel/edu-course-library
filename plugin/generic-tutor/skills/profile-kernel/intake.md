# Intake questions

Loaded by `/add-profile` and on the first-ever load when no learner exists. Moved verbatim from `SKILL.md`.

## Intake questions (asked once per new profile, conversationally, not as a rigid form)
1. General education level / context.
2. Brief vs. detailed explanation preference.
3. Any known learning difficulty or support need (working memory, reading load, attention, spatial reasoning).
4. Any accessibility needs (dyslexia-friendly formatting, plain-language support, session-length sensitivity).
5. **Study availability**, for the journey planner: a *rate*, not a schedule — `sessions_per_week` and `session_minutes`. No days of the week, no calendar dates are ever collected here; the whole planning model is slot-based, not date-based (see journey-planner).
6. **Roster capacity**: how many courses the learner wants to be able to hold *incomplete* at once. State plainly that this is a real commitment — adding a course beyond this cap later requires completing or dropping one first — so the answer should reflect genuine bandwidth, not enthusiasm.
7. **Sharing work (optional):** can they share images of their own work (drawings, CAD screenshots, photos of something they made) when a course asks for it? Record the answer under `capabilities.share_images` with today's date. If they're unsure, leave it unset: courses with practical stages then run theory-only until they declare it.
8. What are they hoping to study — this drives the `/add-course` prompts that follow immediately after, now that a real `roster.max_incomplete_courses` exists for `course-compiler`'s Step -1 to gate against. **This question is asked last, deliberately** — it's the one that triggers building, and building shouldn't start before the cap it must be checked against is known.

Fill in what you get; leave the rest unset rather than guessing.
