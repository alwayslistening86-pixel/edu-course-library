# B-02.1: Local interface design

Micro-task B-02.1 of `docs/WAVE7.md`. Design only; nothing is built. It uses the owner's accepted defaults for D3 (a page served only to this computer, standard library, no framework, no internet) and D4 (a stage test is passed without a model only where its items are script-markable).

## What this is, and what it is not
A page a child can open without a chat window, over the scripts that already exist. In its first version **no model is involved at all**: every bookkeeping step is a script call, and every piece of text on the page is either static interface text or text that is already in the course files. A teaching voice (Claude or a local model) is added later through one defined seam (section 6) and gains no write access by doing so.

It is **not** a replacement for the chat path. The chat path keeps working unchanged; with no interface running, behaviour is exactly as today.

## 1. Constraints (from the rules the repo already keeps)
- Standard-library Python only, Python 3.10 floor; no web framework, no front-end build step, no third-party script or font loaded from anywhere.
- Scripts own every write. The interface calls scripts; it never edits a progress file itself, and a test (B-02.2) fails if it does.
- No network except the loopback address. No outbound requests. Nothing is sent anywhere.
- Accessibility modes (`dyslexia_mode`, `plain_language_mode`, `screen_reader_mode`) and the learner's locale apply to the page. Static text is written once in plain language and the spelling follows `identity.locale`.
- Learner data never enters this repository; the page reads the learner's own profile folder at run time.

## 2. Screens
Each row names the scripts it calls (read-only unless marked **writes**) and what the page shows when something goes wrong. Script names are the real ones in `plugin/generic-tutor/scripts/`.

| Screen | Purpose | Scripts | Failure states shown |
|---|---|---|---|
| **Start** | Check the profile is usable, pick a learner | `resolve_root.py`, then (after B-01.3) `profile_check.py`; lists learner folders | No data root; profile fails its check (plain reason, nothing else loads); newer-than-engine profile |
| **Today** | Where they are and what to do next | `status.py` (`next_action`), `session_plan.py` | No eligible course; everything dormant or suspended (said plainly, as `status.py` does) |
| **Study** | Show the lesson text for the current stage | none (reads `lesson.md` as written, shown as text) | Missing lesson file; course gate suspended (`grounding_status`) |
| **Practice** | One item at a time, script-marked | `next_items.py`, `practice_pick.py` (**writes** which item was met), the marking script (B-02.3), `item_mastery.py` (**writes**), `confidence_update.py` (**writes**) | Course not itemised (falls back to the stage's practice file); no script-markable item left (says so; the stage then needs a model or an adult) |
| **Review** | Due cards, one at a time | `review_select.py`, `review_math.py apply` (**writes**) | Nothing due; consent for scheduling is limited or revoked (the script writes nothing and says so) |
| **Result** | What was recorded, honestly | `recent_activity.py` | The script reported `written: false` (shown, never hidden) |
| **Summary** (adult) | Printable progress for a parent or tutor | `dashboard_html.py --summary-for` | Consent revoked; refused as the script does |

Screens the interface will not have in its first version, and why:
- **Stage test.** A rubric-graded test needs an examiner (the model today). Where a stage's test items are all script-markable (B-02.3) the interface can run it and call `record_grading.py` then `record_stage_result.py`; otherwise it says "this test needs an adult or the chat tutor" and stops. This is the D4 decision made concrete.
- **Cause-of-error diagnosis** (`error_log.py` needs a `cause`, which is a judgment). The first version records mastery and confidence from a marked answer and does not write an error cause. Who may make that judgment when no capable model is present is the B-04 question; until it is answered, the interface leaves it unrecorded rather than guessing.
- **Onboarding, adding a course, drop, erase, backup, restore, audit.** These are staff or adult actions and stay in the chat path or the command line.

## 3. A session, end to end
1. The adult starts the interface with a command that names the profile root. The page opens on the same computer only.
2. **Start**: the learner is chosen; the profile check runs; a failure stops here with a plain message.
3. **Today**: `status.py` says what is next; one large button follows its `next_action`.
4. **Practice** or **Review**, a screen at a time. After each marked answer the page shows right or wrong, the stored explanation from the item (not generated), and moves on.
5. **Result**: what was written. If a write was refused (consent) or skipped, that is shown.
6. A **Stop** button is always visible and always safe: scripts write atomically, so stopping between items loses at most the item in progress (see ADR 0011 for the unplug case).

## 4. The command layer
One module of plain functions, one per screen action, each wrapping the scripts' own functions (the scripts are importable, and have `main()` for the command line). It adds **no logic of its own**: no marking rules, no scheduling arithmetic, no consent decisions. Its outputs are described by schemas so the page and the tests agree on shape. B-02.2 builds it and proves, with a recording stand-in for the scripts, that every write the layer causes is a script call.

## 5. Safety stance (the full threat model is B-02.5)
The server listens on `127.0.0.1` only and refuses any other `Host` header (a guard against another website steering a browser into it), requires a token generated per launch for every request, refuses cross-site requests, sets a strict content-security policy with no inline script from outside, limits request size, and never follows a path outside the learner's folder. It makes no outbound request. A page opened by a child must not be able to read another learner's folder, and B-01.9 already tests that no script can. These are listed here so B-02.5 starts from them; they are not yet tested.

## 6. The teaching-voice seam (designed now, built last)
A single interface, `voice(context) -> text`, whose default returns the static lesson text. A later voice receives the **context it is handed** (the current stage's text, the item, the learner's accessibility flags) and returns text to display. It receives no script handle, no file path and no way to write; the layer calls the scripts, never the voice. This keeps the rule "the model talks, scripts decide and write" true on this surface by construction, and it is the property B-05 relies on when it enforces roles here. B-02.8 writes this down properly.

## 7. How it will be measured
- **Correctness:** a headless client completes a deterministic practice and review loop on a fixture course, and the history database shows the same rows the chat path would write (B-02.7).
- **Safety:** one test per attack in section 5 (B-02.5).
- **Accessibility:** a browser smoke test on the pre-installed Chromium for each mode, plus a manual checklist (keyboard-only use, screen-reader order, no colour-only meaning, text can be enlarged).
- **Use:** an adult sits with one real learner and writes down what confuses them (B-02.10). This is the measure that matters and the only one this environment cannot run.

## 8. What would stop this
- If the server cannot be made safe against another website on the same computer, it ships as a terminal tool or not at all (B-02.5).
- If the pilot shows the chat path already meets the need, B-02 pauses and the effort goes to content.

## Open points for later micro-tasks
- Whether the page should be one file served from memory or a small set of static files (decide in B-02.5 with the content-security policy).
- How the first-run text is written for a child versus the adult who installs it (B-02.9).
- Which of the item types in B-02.3 the compiler can write from real board material without inventing keys (a content question for the enrichment run, not for this surface).
