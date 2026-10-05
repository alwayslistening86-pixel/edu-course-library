---
description: List the commands and the usual order to use them in
---

Explain the tutor's commands briefly, adapting to where the learner is (no profile yet → start with `/add-profile`).

**Usual flow:** `/add-profile <name>` once → `/add-course` for each subject → `/plan` → each session `/run <name>`, then `/continue <course>` (and `/review` when cards are due).

| Command | What it does |
|---|---|
| `/add-profile <name>` | create a new learner profile |
| `/run <name>` | start a session as that learner (also deploys scripts and checks the last session) |
| `/profile` | view or change your profile, roster size, accessibility, consent |
| `/add-course` | find and build a course (or reuse an existing one) |
| `/list-courses` | every course with its status, level and prerequisites |
| `/plan` | how your sessions are shared across courses (no dates) |
| `/continue <course>` | learn: lesson, practice, test |
| `/review [course] [stage]` | run due flashcards (interleaved across courses, weakest first) |
| `/readiness <course>` | an honest "am I ready?" — evidence and caveats, never a grade |
| `/status` | where you are and what to do next |
| `/drop <course>` | pause a course and free its roster slot |
| `/audit` | maintenance check of every course |
| `/doctor` | health check of the install and your data |
| `/backup` | full checksummed backup of your progress, kept outside your learner folder |
| `/restore <zip>` | put a learner back from a backup (verified first; asks before replacing) |
| `/export` | save all your data to one zip |
| `/erase` | permanently delete your data (asks you to type a confirmation phrase) |
| `/help` | this list |
