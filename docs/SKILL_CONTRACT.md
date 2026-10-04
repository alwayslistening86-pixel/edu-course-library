# Skill contract template (K-00)

Every skill should begin, directly after its frontmatter and title, with this block. It is what lets docs-lint and reviewers check a skill against the code.

```markdown
**Contract**
- **Owns:** state this skill is responsible for (and which script writes it).
- **Reads:** files/fields it consults.
- **Calls:** scripts it runs (names must exist under `scripts/`).
- **Emits:** what the learner sees / files handed over.
- **Never:** hard prohibitions (writes outside the active learner, hand-computing script-owned values, …).
- **Failure modes:** what to do when a script errors, a file is missing, or consent blocks a write.
```

Rules:
1. Procedures call scripts for anything deterministic; never restate arithmetic or schemas — link to `docs/DATA_MODEL.md` / `schemas/`.
2. Describe *current* behaviour only; release history belongs in `CHANGELOG.md`.
3. No private version numbers in headings.
4. Frontmatter `name` equals the folder; `description` is trigger-precise (what it does, when it fires, what it never does).
5. A skill with no command says so in `description` and is included by the commands that use it.

Rollout is incremental (K-01…K-32); `tools/lint_docs.py` will start requiring the block once most skills have it.
