"""
Engine version and compatibility (N-02).

A course may declare `min_engine_version` in course.json when it relies on a field or behaviour added in a given plugin
release. The running version is read from the deployed manifest (`<scripts>/.manifest.json`) or, when running from the plugin
source tree, from `.claude-plugin/plugin.json`. If the version cannot be determined, nothing is blocked (we cannot judge).
"""
import json
import os

_SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse(v):
    try:
        parts = tuple(int(p) for p in str(v).strip().split("."))
        return parts if len(parts) == 3 else None
    except (TypeError, ValueError):
        return None


def engine_version(scripts_dir=None):
    base = scripts_dir or _SCRIPTS
    for rel, key in ((".manifest.json", "plugin_version"), (os.path.join("..", ".claude-plugin", "plugin.json"), "version")):
        try:
            with open(os.path.join(base, rel), encoding="utf-8") as f:
                v = parse(json.load(f).get(key))
            if v:
                return v
        except (OSError, ValueError):
            continue
    return None


def check_min(required, scripts_dir=None):
    """(ok, running_version_str_or_None). ok is True when no requirement is declared, the version is unknown, or it suffices."""
    need = parse(required) if required else None
    if need is None:
        return True, None
    have = engine_version(scripts_dir)
    if have is None:
        return True, None
    return have >= need, ".".join(map(str, have))
