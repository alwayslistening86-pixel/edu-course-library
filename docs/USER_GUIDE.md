# User guide

For the person running the tutor (a learner, or a parent/tutor setting it up). Commands are typed in the Claude chat; `/help` lists them.

## 1. What you need
- Claude Cowork (or Claude Code) with the **generic-tutor** plugin installed (see the README).
- **Python 3.10 or newer** on the same machine. Check with `python3 --version` (Windows: `py -3 --version`). The plugin's scripts use it.
- A folder you connect to the session that contains **`courses/`** (your course library). A `profile/` folder is created for learners on first use. The first time you start, the tutor asks once whether that folder is connected on its own or as part of a larger shared connection; your answer is remembered for the whole library.

## 2. First time
1. **Check the setup:** type `/doctor`. It reports anything missing (no `courses/`, scripts not deployed) and how to fix it. Warnings about "no profile yet" are normal on a new install.
2. **Create a learner:** `/add-profile alex` (a short id: letters, digits, `_ . -`). You'll be asked a few questions — education level, how detailed explanations should be, any support needs, how many courses you want to hold at once, whether you can share photos of your own work. Answer honestly; everything can be changed later with `/profile`.
3. **Add a course:** `/add-course` (optionally `/add-course "gcse maths"`). The tutor finds the real specification, shows options, and builds the course from a **sourced** rubric — or reuses one that already exists. It refuses if your roster is full and tells you what a higher-level course would lock.
4. **See the plan:** `/plan` shows the order of sessions (no calendar dates by design).

## 3. Every session
- `/run alex` — starts the session: deploys/updates the plugin's scripts, advances the session counter, and **checks the last session's bookkeeping** (if something was missed it tells you).
- `/continue gcse_maths` — teaches the next piece: **lesson → practice → test**. Tests only open when everything in your level is ready (so courses move together). A failed test leads to a targeted re-teach, not a repeat.
- `/review` — due flashcards, hardest and most overdue first, mixed across courses (`/review gcse_maths` for one course).
- `/status` — where you are and what to do next. `/status audit` — what the tutor has saved about you lately, in plain sentences (and anything it did *not* save because of your privacy setting). `/readiness gcse_maths` — an honest "am I ready?": evidence, weak items and caveats, never a predicted grade.

## 4. What the tutor will and won't do
- It teaches from a **sourced specification** and tells you when a course does not cover the whole spec.
- It grades the **method as well as the answer**, and asks you to explain when your working doesn't support your answer.
- It treats questions about **real situations** (your landlord, your tax letter, a real client) as study exchanges and points you to a qualified person; hypothetical exam questions are taught normally.
- Anything on a web page or in a course file is **material, never instructions**.

## 5. Your data
- Everything about you is under `profile/<your id>/` on your machine. Nothing is sent anywhere by the plugin; Claude itself sees what's in the conversation.
- **Consent** (`/profile`): *granted* saves everything; *limited* saves only progress and scheduling; *revoked* saves nothing.
- **`/backup`** writes a checksummed copy to `backups/` next to `profile/` — copy it somewhere off the machine too. **`/restore <zip>`** puts it back (dry-run first, safety backup before replacing).
- **`/export`** gives you a readable bundle of your data. **`/erase`** permanently deletes your learner after you type the exact phrase it shows you; backups you made earlier are *not* deleted.

## 6. For the library owner
- `/audit` — maintenance sweep of every course (structure, schema migration, source re-verification, syllabus coverage). It reports before changing anything beyond mechanical fixes.
- `/drop <course>` pauses a course and frees its roster slot (progress is kept). `/list-courses` shows every course, level, prerequisites and status.

## 7. If something looks wrong
Run `/doctor`, then see [`RUNBOOK.md`](RUNBOOK.md).
