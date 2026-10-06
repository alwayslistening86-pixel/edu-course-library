# Architecture decision records

One short file per decision: context/why, decision, consequences. New decisions get the next number. `docs/history/DESIGN_NOTES.md` is the frozen long-form history up to v1.61.0.

- [0002](0002-slot-based-scheduling.md) — Time is counted in session slots, never dates
- [0003](0003-sm2-lite-over-fsrs.md) — Keep SM-2-lite for review; do not adopt FSRS
- [0004](0004-json-source-of-truth-sqlite-history.md) — JSON is authoritative; SQLite is append-only history
- [0005](0005-scripts-own-writes.md) — Deterministic logic and state writes live in scripts, not prose
- [0006](0006-courses-in-private-repo.md) — Course content lives in a private companion repo
- [0007](0007-no-placement-no-attestation.md) — No placement diagnostic and no attestation of prior credit
- [0008](0008-no-hash-chained-audit.md) — No hash-chained audit log
- [0001](0001-hooks-and-platform-support.md) — Hooks, platform support and plugin validation
- [0009](0009-optional-target-date.md) — An optional, learner-stated target date (amends 0002)
