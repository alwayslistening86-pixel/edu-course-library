# Change log - alevel_politics

## 2026-09-27 - built

Built against Edexcel 9PL0 Issue 4 (May 2026). Non-core idea: Feminism. Comparative option: 3A, the USA. No GCSE prerequisite (Politics is not a GCSE subject).

## 2026-09-29 — mark-scheme arithmetic remediation

**Found by:** `.tutor-scripts/mark_scheme_check.py`, run for the first time across the whole library.

**Fixed:** a systematic pattern across 14 practice items, all "give two X [4 marks]" style questions where the answer key listed several valid candidate answers under a single `B1` or `B2` tag rather than crediting each candidate its own tag. Affected: S01_Democracy_and_Participation, S02_Political_Parties, S04_Voting_Behaviour_and_Media, S05_Conservatism, S07_Socialism, S08_The_Constitution, S09_Parliament, S10_PM_and_Executive, S12_Feminism, S13_US_Constitution_and_Federalism, S14_US_Congress, S15_US_Presidency, S17_US_Democracy_and_Participation, S18_Comparative_Theories_Constitutions_and_Legislatures. Each rewritten with one `B2` tag per candidate answer (`B1` for S18's exactly-three-required item, which needed no "any N" framing) and, where more candidates are listed than required, an explicit "-- any N for full marks" note -- matching the flexible-credit convention already used elsewhere in this library.

**Revalidated:** `validate_structure.py` clean, `coverage_check.py` full (71/83 taught, 12 pre-existing declared-out-of-scope items unchanged), `mark_scheme_check.py` 0 mismatches.
