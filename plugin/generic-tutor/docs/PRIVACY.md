# Privacy and data handling (X-04, X-09)

## What is personal data here
| Data | Where | Sensitivity |
|---|---|---|
| Profile: name, education level, learning difficulties, accessibility needs, goals, availability | `profile/<id>/student_profile.json` | **High** (may reveal health/support needs) |
| Progress, confidence, error history with free-text notes, session summaries | `profile/<id>/subjects/*.json` | Medium–High |
| Review decks | `profile/<id>/subjects/*_review_deck.json` | Low–Medium |
| Append-only history (errors, mastery trend, review log, confidence events, per-criterion marks; no answer text) | `profile/<id>/tutor.sqlite3` | Medium–High |
| Backups / exports the plugin produces | wherever the learner saves them | same as the source data |

Nothing in this repo is personal data; `profile/*/` is git-ignored. Course content is shared, not personal.

## Controls
- **Isolation:** each learner has their own folder; a session reads and writes only the active learner's folder (guard in code: task E-08; hook: P-06).
- **Consent:** `granted` (everything persists), `limited` (only progress and scheduling persist), `revoked` (nothing persists). Enforced in code by every state-writing script (`tutorlib/consent.py`, v1.14.0); an unreadable consent block fails closed.
- **Export:** `/export` bundles the learner's data (history DB currently missing — K-28).
- **Erasure:** `/erase` deletes the whole learner folder after an explicit confirmation phrase (K-27, C-05). Backups and exports the learner saved elsewhere are theirs to delete.
- **Backup / restore:** `/backup` writes a checksummed zip *outside* the learner folder (default `<root>/backups/`) so `/erase` does not remove it and a backup never contains a backup; `/restore` verifies every checksum before changing anything and takes a safety backup before replacing an existing learner. Backups are full copies of personal data — store them accordingly; erasing a learner does not delete backups made earlier.
- **No telemetry:** the plugin sends nothing anywhere. Web access happens only inside the live source recheck and course compiler, to fetch public specifications.

## Third parties
Claude (the model host) processes the conversation, including anything the learner types and the profile fields read into context. Suggested MCP connectors (`uk-legal`, `govuk`) are opt-in, third-party and see only the queries sent to them (X-06).

## Minors
Learners may be school-age. This is a single-household tool: whoever installs it controls the data folder. Guardian-oversight features (accounts, automatic reports to parents) are deliberately out of scope; what exists instead is a printable progress summary (`/dashboard summary for <who>`, U-06) made only when the learner (or the adult running the install) asks, naming its recipient, leaving out weak items, mistake causes and mock detail, refused if consent is revoked, and never sent anywhere; if a child uses it, the adult who runs the install is responsible for the data folder, backups and consent choices.

**When a learner says something worrying.** The tutor is told to stop the lesson, say it is a study helper and not the right help, point to a trusted adult (and the local emergency number if danger is immediate), never promise secrecy, and never write the disclosure into notes, summaries or the learner's record (rule and detail in `skills/tutor-core`; checked by the `wellbeing` eval suite with invented cases). The tutor cannot contact anyone, so for a child an adult should be present in the early sessions; this is a study tool's guard, not a safeguarding service.
