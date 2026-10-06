# generic-tutor toolkit

A small, optional, read-only companion to the tutor, meant to run on your
own machine without opening a Claude session at all. It never teaches,
grades, or decides anything — it only shows what the tutor's own files
already say, and it works identically whether you ever open it or not.

## Where it comes from, and where it lives

This package ships as part of the `generic-tutor` plugin and is deployed
automatically to `<your EDU folder>/.tutor-scripts/toolkit/` the next time
you run `/run` in a Claude session (the same version-gated mechanism that
deploys every other script under `.tutor-scripts/` — see
`bootstrap_scripts.py`). You don't install it yourself.

## Using it

**GUI (recommended):** double-click `gui.pyw` inside
`.tutor-scripts/toolkit/`. On Windows, if `.pyw` files are associated with
`pythonw.exe` (the normal default for a python.org install), this opens one
small control-panel window with a handful of buttons — no console window,
no browser tab. Nothing else opens until you click a button; each button
opens exactly one small window for that one thing, and nothing refreshes on
its own — there's a Refresh button when you want fresh data. This is
deliberate: it's a status check that sits beside your Claude window, not a
second place to actually study.

**Command line:** from inside `.tutor-scripts/`, run
`python -m toolkit [--root <edu folder>] <command> <learner_id> [options]`. The folder is found from where the toolkit is deployed; `--root`, then the `EDU_TOOLKIT_ROOT` / `EDU_ROOT` environment variables, override that (same resolver as the plugin's scripts). Running a command with no arguments prints its usage.

<!-- toolkit-commands -->
| Command | What it does |
|---|---|
| `backup` | zip a learner's `profile/<id>/` folder |
| `health` | schema versions, deployed scripts version, suspended / attention courses |
| `progress` | roster state, stage, confidence, lowest-mastery items per course |
| `review-due` | cards due now (read-only) |
| `errors` | the error log grouped by cause and course |
| `export-anki` | write an `.apkg` from the review deck(s): tagged by course, stage, item and criterion; `{{c1::...}}` fronts become cloze cards; text only, no media |
<!-- /toolkit-commands -->

To restore a backup use `restore_profile.py` (dry run by default), not the toolkit.

## What it can do

- **Backup** — zips a learner's whole `profile/<id>/` folder to a
  timestamped file. This is the one genuinely important tool here: the
  plugin's own `.gitignore` deliberately excludes real learner data from
  version control, so this is currently the *only* backup path for a
  learner's history, mastery, and error patterns. Courses can always be
  recompiled; this can't be.
- **Health** — schema versions, which scripts version is actually deployed
  on this machine, and which courses are suspended or need attention.
- **Progress** — roster state, current stage, confidence, and a summary of
  per-item mastery (lowest items first) for each enrolled course.
- **Review due** — what the spaced-repetition deck says is due right now,
  relative to the current session slot. Never marks a card reviewed or
  changes its scheduling — that only happens through `/review` in a real
  session.
- **Errors** — the error log, grouped by cause and by course. Never
  re-diagnoses anything; only aggregates what's already been classified.
- **Export to Anki** — writes a real `.apkg` file from your review deck(s),
  one Anki sub-deck per course, importable straight into the actual Anki
  app (desktop or mobile), so you can review on your phone with Anki's own
  scheduler if you want to. This is content portability, not a scheduling
  sync: Anki gets its own copy of the cards and schedules them itself from
  scratch, independent of this system's own spaced-repetition state, which
  is untouched either way. Needs `genanki` installed once
  (`pip install genanki`) — every other tool on this page works with no
  install at all; this is the one exception, and it fails with a plain
  install instruction rather than breaking anything else if it's missing.

## What it will never do

No pedagogy, no re-grading, no "what to study next" that overrides the
tutor. It never calls `item_mastery.observe()`, never edits `roster_state`,
`confidence`, `syllabus_status`, or a review card's scheduling fields — see
`core.py`'s docstring for the full list of design rules this package holds
itself to. The one thing it *can* write is its own side-log under
`profile/<id>/toolkit_log/` (currently just a record of backups taken),
which the tutor never reads for any gate, mastery, or grading decision.

## If you want a real compiled `.exe` instead of a `.pyw`

`gui.pyw` uses only the Python standard library (`tkinter`), so it's
already in the right shape for `pyinstaller --onefile --windowed gui.pyw`
— but that has to be run on Windows itself (PyInstaller can't cross-build a
Windows binary from another OS), so it's a step you'd run yourself, once,
in a real Windows terminal, against this file.
