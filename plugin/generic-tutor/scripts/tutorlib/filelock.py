"""
Advisory file lock for read-modify-write sequences (E-04).

Two overlapping `error_log.py append` calls would each load the same file,
add their own entry and save, silently dropping one. `locked("param")`
serialises such calls per target file.

Mechanism: a sidecar `<file>.lock` created with O_CREAT|O_EXCL (atomic on
every platform, no fcntl/msvcrt needed). Re-entrant within a process, because
scripts call each other (error_log.append -> item_mastery.observe on the same
subjects file). A lock older than STALE_SECONDS is assumed to belong to a
crashed process and is broken. If the lock cannot be acquired within TIMEOUT
seconds a LockTimeout is raised -- callers surface it as an error rather than
writing unlocked.

Slow media: the wait is TIMEOUT seconds by default and can be raised with the environment variable EDU_LOCK_TIMEOUT (whole
seconds, 1 to 600). Many writers queueing on a slow disk (a removable stick, a loaded runner with a virus scanner) can
legitimately wait longer than the default; the stale-lock age follows it (twice the wait, never less than STALE_SECONDS).

Windows: a lock file that another process is deleting (or that an indexer or
antivirus scanner briefly holds open) reports PermissionError, not
FileExistsError, when we try to create it, and the same can make our own
unlink fail once. Both are contention, not a real permission problem, so on
Windows they are retried; elsewhere a PermissionError still surfaces at once.
"""
import functools
import inspect
import os
import threading
import time

TIMEOUT_SECONDS = 10.0
STALE_SECONDS = 60.0
TIMEOUT_ENV = "EDU_LOCK_TIMEOUT"
MAX_TIMEOUT_SECONDS = 600
POLL_SECONDS = 0.02
UNLINK_ATTEMPTS = 8
PERMISSION_IS_CONTENTION = os.name == "nt"

_held = threading.local()


class LockTimeout(RuntimeError):
    pass


def _held_set():
    if not hasattr(_held, "paths"):
        _held.paths = {}
    return _held.paths


def default_timeout(env=None):
    """TIMEOUT_SECONDS unless EDU_LOCK_TIMEOUT holds a whole number of seconds from 1 to MAX_TIMEOUT_SECONDS (anything else is ignored)."""
    raw = (os.environ if env is None else env).get(TIMEOUT_ENV, "")
    if raw.isdigit() and 1 <= int(raw) <= MAX_TIMEOUT_SECONDS:
        return float(int(raw))
    return TIMEOUT_SECONDS


def _holder(lock_path):
    """Who holds a lock, from its own contents: 'pid N for S s' (best effort; empty when unreadable)."""
    try:
        with open(lock_path, encoding="utf-8") as f:
            pid, started = f.read().split()[:2]
        return f"; held by process {int(pid)} for {max(0.0, time.time() - float(started)):.1f}s"
    except (OSError, ValueError):
        return ""


class file_lock:
    def __init__(self, path, timeout=None, stale=None):
        self.target = os.path.abspath(path)
        self.lock_path = self.target + ".lock"
        self.timeout = default_timeout() if timeout is None else timeout
        self.stale = max(STALE_SECONDS, 2 * self.timeout) if stale is None else stale

    def __enter__(self):
        held = _held_set()
        if held.get(self.lock_path, 0) > 0:
            held[self.lock_path] += 1
            return self
        deadline = time.monotonic() + self.timeout
        while True:
            try:
                fd = os.open(self.lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                os.write(fd, f"{os.getpid()} {time.time()}\n".encode())
                os.close(fd)
                break
            except (FileExistsError, PermissionError) as e:
                if isinstance(e, PermissionError) and not PERMISSION_IS_CONTENTION:
                    raise
                self._break_if_stale()
                if time.monotonic() >= deadline:
                    raise LockTimeout(f"could not lock {self.target} within {self.timeout}s ({type(e).__name__}: {e}){_holder(self.lock_path)}") from None
                time.sleep(POLL_SECONDS)
        held[self.lock_path] = 1
        return self

    def _break_if_stale(self):
        try:
            if time.time() - os.path.getmtime(self.lock_path) > self.stale:
                os.unlink(self.lock_path)
        except OSError:
            pass

    def __exit__(self, *exc):
        held = _held_set()
        held[self.lock_path] -= 1
        if held[self.lock_path] == 0:
            del held[self.lock_path]
            self._unlink_lock()
        return False

    def _unlink_lock(self):
        """Remove the lock file; a brief PermissionError (Windows) is retried, any other failure leaves it to the stale-lock rule."""
        for attempt in range(UNLINK_ATTEMPTS):
            try:
                os.unlink(self.lock_path)
                return
            except PermissionError:
                if attempt == UNLINK_ATTEMPTS - 1:
                    return
                time.sleep(POLL_SECONDS * (attempt + 1))
            except OSError:
                return


def locked(param):
    """Decorator: hold file_lock(<value of argument named `param`>) for the call."""
    def deco(fn):
        sig = inspect.signature(fn)

        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            path = sig.bind(*args, **kwargs).arguments[param]
            with file_lock(path):
                return fn(*args, **kwargs)
        return wrapper
    return deco
