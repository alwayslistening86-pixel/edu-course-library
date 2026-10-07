# Security

This repo contains the tutor **engine only**. No learner data and no course content (exam-board derived) is stored here; both live outside the repo (`profile/<id>/` is git-ignored, courses are in the private `edu-courses-private`).

Report a problem privately to the repository owner (GitHub: *Security → Report a vulnerability*) rather than opening a public issue. In scope: path traversal or unintended writes outside a learner's folder, consent bypass, prompt-injection paths from fetched web content into stored state, and anything that could expose learner data. See [`docs/PRIVACY.md`](docs/PRIVACY.md).
