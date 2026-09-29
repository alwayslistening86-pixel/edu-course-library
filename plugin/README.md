# plugin/generic-tutor

Source of truth for the `generic-tutor` Cowork plugin, tracked here so it gets
real version control and backup instead of living only in an ephemeral cloud
session's plugin cache.

This is the **source**, not what's necessarily installed right now — after
any change here, package it (`zip -r generic-tutor.plugin . -x '*.DS_Store'`
from inside `plugin/generic-tutor/`) and install/update it through Cowork's
plugin UI in the normal way. `.claude-plugin/plugin.json`'s `version` field is
the single source of truth for which release is checked in here; bump it on
every change, and add a dated entry to `DESIGN_NOTES.md` inside the plugin
folder the same way every prior version has been documented.
