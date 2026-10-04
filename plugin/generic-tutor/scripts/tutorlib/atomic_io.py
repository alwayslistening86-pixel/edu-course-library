"""
Crash-safe JSON persistence (E-03).

A learner's progress lives in plain JSON files. Opening a file with "w"
truncates it first, so a crash or kill mid-write leaves a partial, unparseable
file. write_json() instead writes a temp file in the SAME directory, flushes
and fsyncs it, then os.replace()s it over the target -- atomic on POSIX and on
Windows (same volume), so readers only ever see the old or the new content.

Output format is byte-identical to the writers it replaced:
json.dump(indent=2, ensure_ascii=False) followed by a single "\\n".
"""
import json
import os
import tempfile


def write_json(path, data, *, backup=False):
    """Atomically write `data` as JSON to `path`. With backup=True the previous
    file (if any) is first copied to `<path>.bak`. Raises on failure; the old
    file is left untouched in that case."""
    directory = os.path.dirname(os.path.abspath(path))
    if backup and os.path.isfile(path):
        _copy_atomic(path, path + ".bak")
    fd, tmp = tempfile.mkstemp(prefix=os.path.basename(path) + ".", suffix=".tmp", dir=directory)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _copy_atomic(src, dst):
    directory = os.path.dirname(os.path.abspath(dst))
    fd, tmp = tempfile.mkstemp(prefix=os.path.basename(dst) + ".", suffix=".tmp", dir=directory)
    try:
        with os.fdopen(fd, "wb") as out, open(src, "rb") as inp:
            out.write(inp.read())
            out.flush()
            os.fsync(out.fileno())
        os.replace(tmp, dst)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
