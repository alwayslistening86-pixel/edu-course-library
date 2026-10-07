#!/usr/bin/env python3
"""
verify_sources.py -- are a course's cited sources still there, and have they changed? (N-04) Network, read-only unless --write.

    python3 verify_sources.py <course_dir> [--today YYYY-MM-DD] [--write] [--allow-local]

Collects every URL the course cites (rubric `source_urls`, each stage's `source.urls`, the curriculum map's `_items_source.url`) and fetches each once.
For each it reports `status`: ok (HTTP 2xx), dead (404/410 or the host does not exist), blocked (403/407/429 or a network that refuses us: unknown, not dead),
or error; plus the HTTP code, size and a SHA-256 of the body. **Only that metadata is kept or shown: the page text is hashed and discarded,** so nothing a
page says can reach the model (UNTRUSTED_CONTENT.md) and no board material is copied.

With `--write` the result is stored in `<course_dir>/source_snapshots.json`; the previous hash is kept, and `changed` is true when the hash differs from it.
A changed hash means "look again", not "the specification changed": pages move, add banners and re-render. `/audit` and the live recheck decide what a
change means. Only http(s) URLs are fetched; addresses on this machine or a private network are refused unless `--allow-local` (used by tests).
Bodies over 8 MB are hashed up to that size and flagged `truncated`. One slow host cannot stall the run (10 s per request).
"""
import datetime
import hashlib
import ipaddress
import json
import os
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request

from tutorlib import atomic_io, cli

MAX_BYTES = 8 * 1024 * 1024
TIMEOUT = 10
UA = "generic-tutor-source-check/1 (metadata only)"
SNAP = "source_snapshots.json"


def collect_urls(course_dir):
    urls = []

    def add(u):
        if isinstance(u, str) and u.strip() and u.strip() not in urls:
            urls.append(u.strip())
    try:
        with open(os.path.join(course_dir, "rubric.json"), encoding="utf-8") as f:
            rub = json.load(f)
    except (OSError, ValueError):
        rub = {}
    if not isinstance(rub, dict):
        rub = {}
    for u in rub.get("source_urls") if isinstance(rub.get("source_urls"), list) else []:
        add(u)
    stages = rub.get("stage_rubrics") if isinstance(rub.get("stage_rubrics"), dict) else {}
    for entry in list(stages.values()) + [rub.get("exam_rubric")]:
        src = entry.get("source") if isinstance(entry, dict) else None
        for u in src.get("urls") if isinstance(src, dict) and isinstance(src.get("urls"), list) else []:
            add(u)
    try:
        with open(os.path.join(course_dir, "curriculum_map.json"), encoding="utf-8") as f:
            cmap = json.load(f)
        src = cmap.get("_items_source") if isinstance(cmap, dict) else None
        add(src.get("url") if isinstance(src, dict) else None)
    except (OSError, ValueError):
        pass
    return urls


def is_http_url(u):
    p = urllib.parse.urlparse(u)
    return p.scheme in ("http", "https") and bool(p.hostname)


def _refused(host, allow_local):
    if allow_local:
        return None
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return None                                    # fetch will report it as dead
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_loopback or ip.is_private or ip.is_link_local or ip.is_reserved:
            return f"{host} resolves to a local or private address"
    return None


def fetch(url, allow_local=False):
    """(status, http, sha256, bytes, truncated). Never raises; never returns the body."""
    p = urllib.parse.urlparse(url)
    if p.scheme not in ("http", "https") or not p.hostname:
        return {"status": "error", "http": None, "note": "not an http(s) URL"}
    why = _refused(p.hostname, allow_local)
    if why:
        return {"status": "error", "http": None, "note": why}
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:                       # noqa: S310 - scheme checked above
            h, n, truncated = hashlib.sha256(), 0, False
            while True:
                chunk = r.read(65536)
                if not chunk:
                    break
                n += len(chunk)
                if n > MAX_BYTES:
                    truncated = True
                    break
                h.update(chunk)
            return {"status": "ok", "http": r.status, "sha256": h.hexdigest(), "bytes": min(n, MAX_BYTES), "truncated": truncated}
    except urllib.error.HTTPError as e:
        kind = "dead" if e.code in (404, 410) else "blocked" if e.code in (401, 403, 407, 429, 451) else "error"
        return {"status": kind, "http": e.code}
    except urllib.error.URLError as e:
        reason = e.reason
        if isinstance(reason, socket.gaierror):
            return {"status": "dead", "http": None, "note": "host not found"}
        return {"status": "blocked" if "tunnel" in str(reason).lower() or "403" in str(reason) else "error", "http": None, "note": str(reason)[:80]}
    except (TimeoutError, OSError) as e:
        return {"status": "error", "http": None, "note": f"{type(e).__name__}: {str(e)[:60]}"}


def load_snapshots(course_dir):
    try:
        with open(os.path.join(course_dir, SNAP), encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) and isinstance(d.get("snapshots"), dict) else {"schema_version": 1, "snapshots": {}}
    except (OSError, ValueError):
        return {"schema_version": 1, "snapshots": {}}


def verify(course_dir, today=None, write=False, allow_local=False, fetcher=None):
    if not os.path.isfile(os.path.join(course_dir, "course.json")):
        return {"error": f"FileNotFoundError: no course.json in {course_dir}"}
    fetcher = fetcher or fetch
    today = today or datetime.date.today().isoformat()
    old = load_snapshots(course_dir)
    new = {"schema_version": 1, "snapshots": {}}
    rows = []
    for url in collect_urls(course_dir):
        got = fetcher(url, allow_local) if fetcher is fetch else fetcher(url)
        prev = old["snapshots"].get(url, {})
        snap = {k: v for k, v in got.items() if v is not None}
        snap["checked_on"] = today
        prev_hash = prev.get("sha256")
        snap["changed"] = bool(prev_hash and snap.get("sha256") and prev_hash != snap["sha256"])
        if snap.get("sha256"):
            snap["previous_sha256"] = prev_hash if snap["changed"] else prev.get("previous_sha256")
            snap["changed_on"] = today if snap["changed"] else prev.get("changed_on")
        elif prev:
            snap.update({k: prev[k] for k in ("sha256", "bytes", "previous_sha256", "changed_on") if k in prev})   # keep the last good hash through an outage
        snap = {k: v for k, v in snap.items() if v is not None}
        new["snapshots"][url] = snap
        rows.append({"url": url, "status": snap["status"], "http": snap.get("http"), "changed": snap["changed"], "first_seen": not prev})
    summary = {"urls": len(rows), "ok": sum(r["status"] == "ok" for r in rows), "dead": sum(r["status"] == "dead" for r in rows),
               "blocked": sum(r["status"] == "blocked" for r in rows), "error": sum(r["status"] == "error" for r in rows),
               "changed": sum(r["changed"] for r in rows)}
    if write and rows:
        atomic_io.write_json(os.path.join(course_dir, SNAP), new)
    return {"course_dir": course_dir, "checked_on": today, "summary": summary, "sources": rows, "written": bool(write and rows)}


def main(argv):
    args = list(argv)
    write, local, today = "--write" in args, "--allow-local" in args, None
    args = [a for a in args if a not in ("--write", "--allow-local")]
    if "--today" in args:
        i = args.index("--today")
        if i + 1 >= len(args):
            print(json.dumps({"error": "--today needs a date"}))
            return 2
        today = args[i + 1]
        del args[i:i + 2]
    if len(args) != 1:
        print(json.dumps({"error": "usage: verify_sources.py <course_dir> [--today YYYY-MM-DD] [--write] [--allow-local]"}))
        return 2
    return cli.emit(verify(args[0], today, write, local))


if __name__ == "__main__":
    cli.handle_help(__doc__)
    sys.exit(main(sys.argv[1:]))
