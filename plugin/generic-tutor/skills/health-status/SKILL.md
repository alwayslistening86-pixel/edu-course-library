---
name: health-status
description: Runs /status (where the active learner stands and what to do next), /dashboard (a private one-page HTML progress report), /readiness (an honest, bounded answer to "am I ready?") and /doctor (a read-only health check). Reports and suggests; never repairs anything itself.
---

# Health & Status

**Contract**
- **Owns:** nothing — both commands are read-only.
- **Reads:** via `status.py` and `doctor.py` only.
- **Calls:** `status.py`, `doctor.py`, `readiness.py`, `dashboard_html.py`.
- **Emits:** a short plain-language summary; for `/doctor`, failures first, each with its suggested fix.
- **Never:** edits a learner file, deletes a lock, redeploys scripts or "fixes" anything on its own; reads or shows another learner's data in `/status`.
- **Failure modes:** a script `error` (no profile, no data root) is shown verbatim with the one next step it implies (`/run <id>`, `/add-profile`, connect the folder).

## `/status`
Requires an active learner (`/run <user_id>` first). Run:
```
python3 /EDU/.tutor-scripts/status.py <the active learner's folder> <the /EDU/courses/ dir>
```
Present, in this order, in a few lines (not a data dump):
1. **Where you are** — session number (`session_slot`), roster `occupancy` of `max`.
2. **Each course** — name, stages passed of total, current stage and phase, roster state. A `dormant` course is "waiting for a lower level", a `dropped` one is paused. Mention `theory_only` completions as such. If `coverage_status` is not `full`, say the course does not yet cover the whole specification (same honesty rule as `course-runner`).
3. **Confidence** — only as a rough word ("building", "steady", "wobbly"), from the number; never present it as an exam-readiness or grade prediction.
4. **Reviews due** — `due_reviews_total`, and `unresolved_errors` only if non-zero.
5. **Next step** — `next_action.command` and its reason, as a suggestion.
If `consent` is `limited` or `revoked`, add one line saying what is not being remembered.

## `/doctor`
Does not need an active learner. Run:
```
python3 /EDU/.tutor-scripts/doctor.py [--learner <user_id>]
```
(If `.tutor-scripts` is not deployed yet, run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/doctor.py --root <data root>` instead.) Present `fail` checks first, then `warn`, then one line for how many passed. For each non-ok check give `detail` and the `fix`. Offer to help with a fix, but only act on the learner's say-so and never delete or overwrite learner data as part of a "fix" without an explicit yes. A `last-session` warning means the previous session's bookkeeping is incomplete — explain it exactly as `profile-kernel` does after `/run`.

## `/readiness <course_id>`
Requires an active learner. Run `python3 /EDU/.tutor-scripts/readiness.py <the active learner's folder> <the /EDU/courses/ dir> <course_id>` and answer from it only. It is **not a grade prediction**: say the `band` in words (not enough evidence yet / early / building / solid), how much evidence stands behind it (`strength`, and how many of the taught items have actually been observed), the weakest items by name, any `recent_mocks` as percentages on those papers (never as grades), and then state the caveats it returns — in particular that session practice is not exam conditions and, if coverage is not full, which part of the specification is untaught. Never convert a band into a grade, mark or percentage, never reassure beyond the evidence, and if the band is `not_enough_evidence` say plainly that more practice is needed before anyone can say.

## `/dashboard`
Requires an active learner. Choose an output path **outside** the learner's folder (default `<the /EDU/ root>/exports/<user_id>-progress.html`) and run `python3 /EDU/.tutor-scripts/dashboard_html.py <the active learner's folder> <the /EDU/courses/ dir> <output.html> --today <today, ISO>`. Hand the file to the learner as a normal file. It is one self-contained page (no scripts, no network) with per-course progress, reviews due, readiness bands with caveats, weakest items, unresolved mistakes by cause and recent mock percentages. Tell the learner it contains personal data, that it is a snapshot (run it again for fresh numbers), and that `/erase` does not delete exports they have saved.
