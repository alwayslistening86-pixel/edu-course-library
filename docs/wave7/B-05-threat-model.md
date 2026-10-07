# B-05.1: what a role can and cannot stop

Micro-task B-05.1 of `docs/WAVE7.md`. A design note, nothing is built. It answers one question before any role code is written (B-05.3, B-05.4): where can a role be **enforced**, and where is it only **advice**? It uses the three roles of `docs/wave7/B-05-script-roles.md` (tutor voice, examiner, staff) and the rule of ADR 0012 (a voice that is not the examiner records nothing in the examiner-only class).

## The one fact everything else follows from
A role is only a lock against a party that cannot change its own role. The party we worry about is the model, so the question for each surface is: **can the model run arbitrary commands there?**

- If it **cannot** (it can only call a fixed list of actions that the surrounding program chooses), the program can enforce a role, because the model never holds the means to act as another role.
- If it **can** (a shell, or a script interpreter), any control that lives in the model's reach is advice: an environment variable it can set, a file it can write, a flag it can pass.

## Surface by surface

| Surface | Can the model run arbitrary commands? | Can a role be enforced? | What stops it |
|---|---|---|---|
| **The local interface** (B-02; the engine serves pages, a model only fills in replies) | No: the model returns text; the program decides which script to call and as which role | **Yes**, by the program | The interface never exposes a staff or examiner action to the tutor-voice model; the role is held by the program's own code, not read from anything the model controls |
| **A chat session with a shell** (Claude Code, Cowork with a terminal, any agent with a bash tool) | Yes | **No. Advice only** | Nothing in the model's reach is a lock. The optional hook guard (`scripts/hook_guard.py`) is a speed bump, see below |
| **A chat session without a shell** (a tool list with no command execution) | No | **Yes**, if the tool list is fixed by the host | Whatever the host allows; the engine cannot check what the host did |
| **A shared machine with separate operating-system accounts** | Yes, but only as its own account | **Yes**, by the operating system | Staff-only files owned by another account and not readable by the learner's account; the engine cannot set this up, a person must |

## Evidence for "advice only" in a shell session (checked 8 Oct 2026)
The hook guard's shell check is a text match (`BASH_WRITE` in `hook_guard.py`: redirections, `tee`, `sed -i`, `rm`, `mv`, `cp`, `truncate`, `dd`, `sqlite3`, `ln`). Run against a learner folder it:
- **denies** `echo x > profile/ann/student_profile.json`;
- **allows** `python3 -c "open('profile/ann/student_profile.json','w').write('x')"` (no listed word appears);
- **allows** `EDU_ROLE=staff python3 .tutor-scripts/erase_profile.py profile/ann` (an environment variable set in the same command is just text to the guard);
- **allows** a path built from a shell variable.

`tests/test_hook_guard_limits.py` pins these four results, so this table cannot drift from the code unnoticed. If the guard is ever made stronger, that test fails and this note must be updated in the same change. The guard still has value (it stops the common slip and makes a deliberate bypass visible in the ledger), and nothing here argues for removing it. It must not be described to a school as a lock.

## What follows for the design
1. **Say it plainly in the product.** Where the role is advice, the session plan and the docs say "this setup relies on the model following its instructions", not "protected".
2. **Enforce in the program, not in the model's reach.** Role checks (`tutorlib.roles.require(script, role)`, B-05.3) take the role from a source the model cannot write in the surface being used: the local interface's own process, or a launcher that starts the script as a separate process with the role in a file the learner's account cannot read. They never trust an environment variable or a flag as a proof of role; those are accepted only as a *request* to behave more restrictively, never less.
3. **Fail towards restriction.** No role configured means today's behaviour (nothing changes for any current install). A role configured but unreadable means the most restricted role, with the reason stated.
4. **Examiner-only work waits.** In a surface where roles are only advice, ADR 0012's rule still holds as an instruction, and the record of what was left unrecorded is the only defence. The honest statement for a school is that real separation needs the local interface or separate operating-system accounts.
5. **What this does not solve.** A model with a shell can also read the answer keys, the mark schemes and the hold-back material. Keeping these from a learner who is *also* using that shell is a different problem (the learner is not the model); the roles here are about the model's writes, not about concealing course material from someone at the keyboard.

## Test for B-05.3 and B-05.4
Each enforced surface gets a test that tries to act as another role *through that surface's real entry point* and is refused; each advice-only surface gets a test or a documented example showing the limit (as `test_hook_guard_limits.py` does for the guard). B-05.7 repeats this adversarially by hand.

## Not decided
- Whether to ship a launcher for the operating-system-accounts option, or only document it (a school adviser's call; see B-06.4).
- Whether the hook guard should grow a stricter mode that refuses any shell command touching a learner folder except the engine's own scripts. It would still be bypassable by a determined model; the cost is false refusals. Recommendation: not now.
