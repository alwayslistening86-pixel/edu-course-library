"""Model backends for the eval harness. A backend turns (system_text, prompt) into response text."""
import ipaddress
import json
import os
import socket
import subprocess
import tempfile
import urllib.error
import urllib.parse
import urllib.request


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


DEFAULT_LOCAL_URL = "http://127.0.0.1:11434/v1"      # Ollama's default; llama.cpp's server is usually http://127.0.0.1:8080/v1


def _is_local_host(host):
    """True for `localhost` and literal loopback addresses. A name that merely resolves to loopback is not trusted (no DNS lookup is made)."""
    if host == "localhost":
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None                                   # a redirect could carry the prompt to another host


class LocalChat(Backend):
    """A model served on this machine through the common chat-completions format (Ollama, llama.cpp server, and others), standard library only
    (B-03.2, owner decision D5). The prompt never leaves the machine unless `allow_remote` is set on purpose:
      * the host must be `localhost` or a literal loopback address, else ValueError at construction;
      * proxy environment variables are ignored and redirects are refused, so a local call cannot be quietly routed elsewhere;
      * no credentials in the URL, and only http(s).
    `settings` records what shaped the answers, for B-03.3 to store with each result. A failure raises RuntimeError saying what went wrong
    (nothing listening, a timeout, an HTTP error with the server's own words, a reply that is not chat-completions JSON, an empty reply)."""

    def __init__(self, model, url=DEFAULT_LOCAL_URL, timeout=180, temperature=0.0, seed=0, max_tokens=None, allow_remote=False):
        parts = urllib.parse.urlsplit(url)
        if parts.scheme not in ("http", "https") or not parts.hostname:
            raise ValueError(f"url must be http(s)://host[:port]/path, got {url!r}")
        if parts.username or parts.password:
            raise ValueError("put no credentials in the url")
        if not allow_remote and not _is_local_host(parts.hostname):
            raise ValueError(f"{parts.hostname!r} is not this machine: the eval prompts would leave it. Use localhost or 127.0.0.1, or pass allow_remote=True on purpose")
        self.model, self.url, self.timeout = model, url.rstrip("/"), timeout
        self.temperature, self.seed, self.max_tokens, self.allow_remote = temperature, seed, max_tokens, allow_remote
        self.name = f"local:{model}"
        handlers = [_NoRedirect]
        if not allow_remote:
            handlers.append(urllib.request.ProxyHandler({}))
        self._opener = urllib.request.build_opener(*handlers)

    @property
    def settings(self):
        return {"model": self.model, "url": self.url, "temperature": self.temperature, "seed": self.seed, "max_tokens": self.max_tokens}

    def complete(self, system, prompt):
        body = {"model": self.model, "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
                "temperature": self.temperature, "seed": self.seed, "stream": False}
        if self.max_tokens:
            body["max_tokens"] = self.max_tokens
        req = urllib.request.Request(self.url + "/chat/completions", data=json.dumps(body).encode("utf-8"),
                                     headers={"Content-Type": "application/json"}, method="POST")
        try:
            with self._opener.open(req, timeout=self.timeout) as resp:
                raw = resp.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace").strip()[:300] if hasattr(e, "read") else ""
            raise RuntimeError(f"the model server answered HTTP {e.code} at {self.url}: {detail or e.reason}") from None
        except (socket.timeout, TimeoutError):
            raise RuntimeError(f"the model server at {self.url} did not answer within {self.timeout}s") from None
        except urllib.error.URLError as e:
            if isinstance(e.reason, (socket.timeout, TimeoutError)):
                raise RuntimeError(f"the model server at {self.url} did not answer within {self.timeout}s") from None
            raise RuntimeError(f"no model server reachable at {self.url} ({e.reason}); start one (for example `ollama serve`) or pass --url") from None
        try:
            text = json.loads(raw)["choices"][0]["message"]["content"]
        except (ValueError, KeyError, IndexError, TypeError):
            raise RuntimeError(f"the reply from {self.url} is not chat-completions JSON: {raw[:200]!r}") from None
        if not isinstance(text, str) or not text.strip():
            raise RuntimeError(f"the model at {self.url} returned an empty reply")
        return text
