#!/usr/bin/env python3
"""
bootstrap_scripts.py — deterministic install/update of the tutor's shared
scripts directory (/EDU/.tutor-scripts/) from whatever's bundled inside the
currently-running plugin, on every landing (profile-kernel's landing logic).

Why this needs to be real code, not a "compare the version numbers" prose
instruction: semver comparison is exactly the kind of thing that LOOKS
trivial but has a genuinely correct answer that a naive approach gets
wrong — e.g. a plain string/lexicographic compare puts "1.9.0" ABOVE
"1.10.0". This script does a real tuple comparison instead.

Design, and the two failure modes it exists to avoid:
  1. "Always overwrite" would silently clobber a script a prior session
     already deployed, every single time the plugin updates for an
     unrelated reason (a wording fix in some SKILL.md, say) — destroying
     the "scripts survive a plugin update the way course.json does"
     guarantee this whole design rests on.
  2. "Never overwrite once deployed" (the previous version of this design)
     protects that guarantee but means a genuine bug fix to a script's own
     logic never reaches an install that already has an older copy —
     exactly the gap this script exists to close.
The fix used here: version-gated update, not a blanket rule either way.
  - No manifest at the target yet -> fresh deploy of everything, at the
    plugin's current version.
  - Target's recorded version is OLDER than the running plugin's version
    -> this is a genuine update; overwrite every shipped script and record
       the new version. Reported, never silent (see main()'s output).
  - Versions match -> no-op.
  - Target's recorded version is NEWER than the running plugin's (should
    not happen in normal use - the only way scripts land on a machine is
    via this same script, always sourced from the currently-running
    plugin) -> don't touch anything; flag it rather than guessing which
    direction is "right".

/EDU/ itself is never hardcoded here or anywhere else in this plugin - the
caller resolves wherever this install's real EDU folder lives (the
existing connected-folder convention every other path in this plugin
already relies on) and passes that resolved path in as target_dir.

**(v1.6.0) Script PACKAGES, not just flat files.** The toolkit (a separate,
optional, read-only client-side tool — see scripts/toolkit/README.md) ships
as a real Python package (toolkit/__init__.py, toolkit/core.py, ...) rather
than flat top-level scripts, so it needs its own directory tree deployed as
a unit, not individual .py files. Any immediate subdirectory of source_dir
that contains an __init__.py is treated as a package and deployed wholesale
(shutil.copytree, replacing whatever's at the target on a genuine update -
same version-gating as everything else here, never a partial/stale merge of
old and new package files). A subdirectory without __init__.py is not a
package and is ignored, same as any other non-.py entry in source_dir.

Usage:
    python3 bootstrap_scripts.py <source scripts dir> <plugin.json path> <target .tutor-scripts dir>

<source scripts dir> is the plugin's own bundled scripts/ folder
(${CLAUDE_PLUGIN_ROOT}/scripts). <plugin.json path> is read only for its
"version" field. <target .tutor-scripts dir> is created if it doesn't
exist. Output: JSON to stdout.
"""
import json
import os
import shutil
import sys

MANIFEST_NAME = ".manifest.json"


def _parse_version(v):
    """'1.10.0' -> (1, 10, 0). Never a lexicographic string compare."""
    try:
        return tuple(int(p) for p in str(v).strip().split("."))
    except (ValueError, AttributeError):
        return None


def _load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def bootstrap(source_dir, plugin_json_path, target_dir):
    plugin_manifest = _load_json(plugin_json_path)
    if not plugin_manifest or "version" not in plugin_manifest:
        return {"error": f"could not read a 'version' field from {plugin_json_path}"}
    running_version_str = plugin_manifest["version"]
    running_version = _parse_version(running_version_str)
    if running_version is None:
        return {"error": f"plugin.json version {running_version_str!r} is not parseable as X.Y.Z"}

    if not os.path.isdir(source_dir):
        return {"error": f"bundled scripts dir not found: {source_dir}"}
    shipped_files = sorted(f for f in os.listdir(source_dir) if f.endswith(".py"))
    shipped_packages = sorted(
        d for d in os.listdir(source_dir)
        if os.path.isdir(os.path.join(source_dir, d)) and os.path.isfile(os.path.join(source_dir, d, "__init__.py"))
    )
    if not shipped_files and not shipped_packages:
        return {"error": f"no .py files or packages found in bundled scripts dir: {source_dir}"}

    os.makedirs(target_dir, exist_ok=True)
    target_manifest_path = os.path.join(target_dir, MANIFEST_NAME)
    deployed = _load_json(target_manifest_path)
    deployed_version_str = deployed.get("plugin_version") if deployed else None
    deployed_version = _parse_version(deployed_version_str) if deployed_version_str else None

    def _write_all():
        written = []
        for fn in shipped_files:
            shutil.copy2(os.path.join(source_dir, fn), os.path.join(target_dir, fn))
            written.append(fn)
        for pkg in shipped_packages:
            dest = os.path.join(target_dir, pkg)
            if os.path.isdir(dest):
                shutil.rmtree(dest)
            shutil.copytree(os.path.join(source_dir, pkg), dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            written.append(pkg + "/")
        with open(target_manifest_path, "w", encoding="utf-8") as f:
            json.dump({"plugin_version": running_version_str, "files": shipped_files, "packages": shipped_packages}, f, indent=2)
            f.write("\n")
        return written

    if deployed_version is None:
        written = _write_all()
        return {
            "action": "deployed_fresh",
            "from_version": None,
            "to_version": running_version_str,
            "files_written": written,
        }

    if deployed_version < running_version:
        written = _write_all()
        return {
            "action": "updated",
            "from_version": deployed_version_str,
            "to_version": running_version_str,
            "files_written": written,
        }

    if deployed_version == running_version:
        return {
            "action": "up_to_date",
            "version": running_version_str,
            "files_written": [],
        }

    # deployed_version > running_version - should not happen normally.
    return {
        "action": "warning_target_newer_than_bundle",
        "deployed_version": deployed_version_str,
        "running_plugin_version": running_version_str,
        "files_written": [],
        "note": "target's recorded version is newer than the currently-running plugin's "
                "version - left untouched rather than guessing which is right; if this "
                "wasn't expected, check which plugin version is actually installed.",
    }


def main():
    if len(sys.argv) != 4:
        print(json.dumps({"error": "usage: bootstrap_scripts.py <source scripts dir> <plugin.json path> <target .tutor-scripts dir>"}))
        sys.exit(2)
    print(json.dumps(bootstrap(sys.argv[1], sys.argv[2], sys.argv[3]), indent=2))


if __name__ == "__main__":
    main()
