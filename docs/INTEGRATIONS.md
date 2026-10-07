# Third-party integrations (MCP servers)

The plugin ships a `.mcp.json` that **declares** two community MCP servers. Nothing is connected automatically: each client asks you to approve a server before it is used, and a course only treats a connector as usable when its own `connectors.md` marks it `connected` (see `course-runner`).

| Server | Declared URL | Source | Used for | Suggested by |
|---|---|---|---|---|
| `uk-legal` | `https://uk-legal-mcp.fly.dev/mcp` | `paulieb89/uk-legal-mcp` (MIT) | case law, legislation, Hansard, OSCOLA citation checks | the four law and legal-practice courses |
| `govuk` | `https://govuk-mcp.fly.dev/mcp` | `paulieb89/govuk-mcp` (MIT) | GOV.UK content, SRA/BSB regulatory guidance | the same courses |

## What you should know before approving one
- **Who runs it.** Both URLs are hosted instances run by the servers' author, not by this project or by Anthropic. This project has not verified the operator's identity, uptime or retention beyond a 30 Sep 2026 read of the open-source code (read-only tools, no red flags; recorded in `plugin/generic-tutor/DESIGN_NOTES.md`). The hosted instance can differ from the published code.
- **What is sent.** Only what the model puts in a tool call: a case name, a citation, a statute section, a search phrase. The plugin never passes your profile, progress files or backups to a connector. A search phrase you typed may still end up in a query, so do not paste personal details into a law question.
- **Authentication.** None configured. Nothing you own is accessed.
- **If you would rather not.** Leave it unapproved. The courses run unchanged: legal authorities are then cited from the model's own knowledge with the usual caveat that they were not checked against the live record. You can instead run the server yourself (`uvx uk-legal-mcp`, per its README) and point your client at the local address.
- **If it is down or slow.** The tutor treats an unavailable connector as not connected and says so; no stage depends on one.

## Adding another
A new server needs: its source repository and licence, who operates the hosted instance, what each tool sends, whether it needs credentials, and a line in the course's `connectors.md` with status `suggested`. Never ship one marked `connected`, and never add a server that requires a learner's credentials to the plugin's `.mcp.json`.
