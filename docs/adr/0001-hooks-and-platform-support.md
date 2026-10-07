# ADR 0001 — Hooks, platform support and plugin validation (P-04)

Status: accepted (provisional until the "to verify" items are confirmed on a real Cowork install)
Date: 2026-10-04

## Context
The redesign wants enforcement at tool-call time (consent/path guard, auto-bootstrap) and a session-end write verifier (PLAN §4, V-xx). Whether that is possible depends on which surfaces support plugin hooks.

## Findings
Source: a documentation lookup done by a research subagent against the official Claude Code docs (hooks, plugin manifest/marketplace/CLI references). **Not independently verified by us** — see "To verify".

- **Events:** SessionStart, UserPromptSubmit, PreToolUse (can block, rewrite input, inject context), PostToolUse (can alter output, cannot block), Stop (can prevent stopping), SessionEnd (cleanup), PermissionRequest, StopFailure. Handler types: command, http, mcp_tool, prompt, agent.
- **Plugins can ship hooks:** `hooks/hooks.json` (wrapped in a top-level `"hooks"` key) or `hooks` in `plugin.json` (file path, inline event map, or array). `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, `${CLAUDE_PROJECT_DIR}` resolve in commands.
- **Hook input:** JSON on stdin (`session_id`, `transcript_path`, `cwd`, `hook_event_name`, `tool_name`, `tool_input`, …). **Exit 0** = continue; **exit 2** = block (stderr shown); other codes = non-blocking error. JSON on stdout can return `permissionDecision` (deny/allow/ask/defer), `additionalContext`, `updatedInput`.
- **Platform support:** hooks are **Claude Code CLI/IDE only**. **Claude Cowork (desktop) does not support hooks**; claude.ai has mods only.
- **Distribution:** `marketplace.json` with `plugins[].source` (relative path or `{source: github, repo, ref, sha}`); install via `claude plugin marketplace add owner/repo`.
- **Validation:** `claude plugin validate <path> [--strict]` (exit 0 pass / 1 fail / 2 error) checks manifest, paths, hook config, skill/command frontmatter, MCP config, unknown fields.

## Decision
1. **Cowork is the primary target and has no hooks**, so enforcement cannot depend on them. The **write verifier (V-03) with a session ledger (V-01) is the primary safety mechanism**: scripts record every state write; the next `/run` reconciles expected vs actual writes and reports gaps. Consent and path checks move **into the scripts** (E-05, E-06, E-08) — which works on every surface.
2. **Hooks become an optional hardening layer for Claude Code users** (P-05…P-08): auto-bootstrap on SessionStart, PreToolUse path/consent guard, Stop-time verifier. They add safety but nothing may *require* them; every behaviour must be correct without them.
3. **Packaging:** add a repo-root `marketplace.json` (P-02) and run `claude plugin validate --strict` in CI where the CLI is available (new task P-19). Hook files ship in the plugin but are inert on Cowork.
4. **Context injection fallback for Cowork:** since SessionStart cannot run, `/run` (profile-kernel) remains the bootstrap entry point, as today.

## Consequences
- Phase 1 (engine hardening) is *more* important than originally framed: it is the only enforcement layer present on every surface.
- Phase 2 splits into 2a (portable: ledger, verifier, `/doctor`, new commands) and 2b (Claude-Code-only hooks).
- Anything the guard hooks would block must also be detectable after the fact by the verifier/invariants checker (V-08).

## To verify (before Phase 2b)
- Hooks absent on Cowork: confirm on an actual install and against https://claude.com/docs/plugins/platform-support.
- Exact `hooks.json` schema accepted by `claude plugin validate` for the version in use.
- Whether Cowork exposes any equivalent (scheduled tasks, connectors) usable for reconciliation.

## Update, v1.66.0
Hooks are implemented (`hooks/hooks.json`, `scripts/hook_guard.py`) and were exercised in a live Claude Code session: SessionStart deployed the scripts, PreToolUse denied a `Write` to `student_profile.json` and a shell redirect into `subjects/`. `claude plugin validate --strict` accepts the config. Still unverified: Cowork's behaviour (assumed to ignore the file) and Windows paths in the guard.

