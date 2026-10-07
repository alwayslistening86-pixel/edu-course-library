# Intake questions

Loaded by `/add-profile` and on the first-ever load when no learner exists.

## Intake questions (asked once per new profile, conversationally, not as a rigid form)
1. General education level / context.
2. Brief vs. detailed explanation preference.
3. Any known learning difficulty or support need (working memory, reading load, attention, spatial reasoning).
4. Any accessibility needs (dyslexia-friendly formatting, plain-language support, screen-reader-friendly plain text, session-length sensitivity).
5. **Study availability**, for the journey planner: a *rate*, not a schedule — `sessions_per_week` and `session_minutes`. No days of the week, no calendar dates are ever collected here; the whole planning model is slot-based, not date-based (see journey-planner).
6. **Roster capacity**: how many courses the learner wants to be able to hold *incomplete* at once. State plainly that this is a real commitment — adding a course beyond this cap later requires completing or dropping one first — so the answer should reflect genuine bandwidth, not enthusiasm.
7. **Sharing work (optional):** can they share images of their own work (drawings, CAD screenshots, photos of something they made) when a course asks for it? Record the answer under `capabilities.share_images` with today's date. If they're unsure, leave it unset: courses with practical stages then run theory-only until they declare it.
8. What are they hoping to study — this drives the `/add-course` prompts that follow immediately after, now that a real `roster.max_incomplete_courses` exists for `course-compiler`'s Step -1 to gate against. **This question is asked last, deliberately** — it's the one that triggers building, and building shouldn't start before the cap it must be checked against is known.

## What each answer is stored as
Collect the answers, then make **one** call: `python3 /EDU/.tutor-scripts/profile_init.py <the /EDU/profile/ dir> <user_id> <today> <<'EOF' {…} EOF` with a flat JSON object on stdin (learner words never go on a command line). Unknown keys, invalid values and an existing id are refused with a reason; ask again for just that answer.

| Question | Key | Valid values |
|---|---|---|
| 1 level / context | `identity.education_level`, `identity.display_name`, `identity.locale`, `identity.home_language` (optional) | text, at most 80 / 80 / 20 / 40 characters |
| 2 explanation preference | `preferences.style` | `brief` or `detailed` |
| 3 support needs | `learning_signals.working_memory_support_needed`, `…verbal_load_sensitivity`, `…spatial_support_needed`, `…pace` | `none`/`some`/`significant`; pace `fast`/`standard`/`slow`; free notes in `learning_signals.notes` (500 characters) |
| 4 accessibility | `preferences.accessibility.dyslexia_mode`, `…plain_language_mode`, `…screen_reader_mode` | true or false |
| 5 availability | `availability.sessions_per_week`, `availability.session_minutes` | 1–21; 5–240 |
| 6 roster capacity | `roster.max_incomplete_courses` | 1–20 |
| 7 sharing work | `capabilities.share_images` | true or false |
| 8 what to study | `goals` | up to 10 short strings; then go to `/add-course` |

A returning learner changes any answer later with `/profile`, which calls `profile_set.py <profile> <key> <value> <today>` with the same keys and rules. Nothing else is stored from intake.

Fill in what you get; leave the rest unset rather than guessing.
