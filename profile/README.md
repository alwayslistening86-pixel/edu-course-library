# profile/

Per-learner state for the generic-tutor plugin: progress, spaced-review
decks, error history, confidence tracking — created automatically the first
time a learner runs `/run <learner_id>` or `/add-profile`, never by hand.

Real learner subfolders here are git-ignored (see the repository root
`.gitignore`) and are never committed — this is personal data, kept local
even though the rest of this repository is public. `access.json` (a bare
folder-access confirmation flag, not learner data) is the only thing
tracked from this directory.
