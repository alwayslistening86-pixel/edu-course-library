"""Model backends for the eval harness. A backend turns (system_text, prompt) into response text."""
import os
import subprocess
import tempfile


class Backend:
    name = "base"

    def complete(self, system, prompt):  # pragma: no cover - interface
        raise NotImplementedError


class ClaudeCli(Backend):
    """Runs `claude -p` headlessly: no tools, no slash commands, no MCP, no session saved, in an empty
    temp directory (so the repo's CLAUDE.md and settings do not leak into the run)."""

    def __init__(self, model="sonnet", timeout=180, retries=2):
        self.model, self.timeout, self.retries = model, timeout, retries
        self.name = f"claude-cli:{model}"

    def complete(self, system, prompt):
        cmd = ["claude", "-p", "--model", self.model, "--tools", "", "--disable-slash-commands", "--strict-mcp-config",
               "--no-session-persistence", "--system-prompt", system, "--output-format", "text"]
        last = None
        for _ in range(self.retries + 1):
            with tempfile.TemporaryDirectory() as td:
                try:
                    p = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=self.timeout, cwd=td,
                                       env={**os.environ, "CLAUDE_CODE_DISABLE_AUTO_MEMORY": "1"})
                except subprocess.TimeoutExpired:
                    last = "timeout"
                    continue
            if p.returncode == 0 and p.stdout.strip():
                return p.stdout
            last = (p.stderr or p.stdout or f"exit {p.returncode}").strip()[:300]
        raise RuntimeError(f"claude CLI failed: {last}")


class Scripted(Backend):
    """Deterministic stand-in for tests: `fn(system, prompt) -> str`."""

    def __init__(self, fn, name="scripted"):
        self.fn, self.name = fn, name

    def complete(self, system, prompt):
        return self.fn(system, prompt)
