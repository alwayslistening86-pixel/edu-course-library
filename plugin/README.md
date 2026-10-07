# plugin/generic-tutor

The source of the `generic-tutor` plugin for Claude (Cowork and Claude Code): `skills/`, `commands/`, `scripts/`, `hooks/`, `tests/`, `evals/` and shipped `docs/`.

Install it from the repository root (`claude plugin marketplace add ...`, see the main README and `docs/INSTALL.md`), or build the zip with `python3 tools/build_plugin.py`. `.claude-plugin/plugin.json`'s `version` is the single source of truth for the release; change it only with `python3 tools/bump_version.py` (it edits every version carrier, refreshes the deployed script copy and adds the changelog heading). History is in `CHANGELOG.md` at the repository root, and older history in `docs/history/`. How to work on it: `CONTRIBUTING.md`, `docs/CONTRIBUTING-DEV.md`.
