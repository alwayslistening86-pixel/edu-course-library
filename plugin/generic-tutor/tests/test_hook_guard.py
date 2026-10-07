"""P-05..P-08: the optional Claude Code hooks, driven through the real stdin/stdout interface with a hook simulator."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCRIPT = os.path.join(ROOT, "scripts", "hook_guard.py")


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = os.path.realpath(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.root = os.path.join(self.tmp, "EDU")
        for lid, consent in (("ann", "granted"), ("bob", "granted"), ("cy", "revoked")):
            d = os.path.join(self.root, "profile", lid, "subjects")
            os.makedirs(d)
            with open(os.path.join(self.root, "profile", lid, "student_profile.json"), "w") as f:
                json.dump({"consent": {"status": consent}, "session_slot": 3}, f)
        os.makedirs(os.path.join(self.root, "courses", "c1", "stages"))
        self.sid = "sess-" + os.path.basename(self.tmp)
        self.env = {**os.environ, "EDU_ROOT": self.root, "TMPDIR": self.tmp}
        self.env.pop("EDU_TOOLKIT_ROOT", None)

    def fire(self, event, **kw):
        ev = {"hook_event_name": event, "session_id": self.sid, "cwd": self.root, **kw}
        p = subprocess.run([sys.executable, SCRIPT], input=json.dumps(ev), capture_output=True, text=True, env=self.env)
        self.assertEqual(p.returncode, 0, p.stderr)
        return json.loads(p.stdout) if p.stdout.strip() else {}

    def tool(self, name, **inp):
        out = self.fire("PreToolUse", tool_name=name, tool_input=inp)
        h = out.get("hookSpecificOutput", {})
        return h.get("permissionDecision", "allow"), h.get("permissionDecisionReason", "")

    def p(self, *parts):
        return os.path.join(self.root, *parts)


class Guard(Base):
    def test_script_owned_files_cannot_be_edited_by_hand(self):
        for f in (("profile", "ann", "student_profile.json"), ("profile", "ann", "subjects", "c1.json"),
                  ("profile", "ann", "subjects", "c1_review_deck.json"), ("profile", "ann", "tutor.sqlite3"),
                  ("profile", "ann", ".session_ledger.jsonl"), ("profile", "access.json")):
            d, why = self.tool("Write", file_path=self.p(*f), content="x")
            self.assertEqual(d, "deny", f)
            self.assertIn("script", why)
        self.assertEqual(self.tool("Write", file_path=self.p("profile", "ann", "worksheet.md"), content="x")[0], "allow")
        self.assertEqual(self.tool("Edit", file_path=self.p("profile", "ann", "worksheet.md"))[0], "allow")

    def test_revoked_consent_blocks_every_write_but_not_reads(self):
        self.assertEqual(self.tool("Write", file_path=self.p("profile", "cy", "notes.md"), content="x")[0], "deny")
        self.assertEqual(self.tool("Bash", command="echo hi > profile/cy/n.txt")[0], "deny")
        self.assertEqual(self.tool("Bash", command="echo hi > profile\\cy\\n.txt")[0], "deny")                    # a backslash path is the same path
        self.assertEqual(self.tool("Read", file_path=self.p("profile", "cy", "notes.md"))[0], "allow")

    def test_another_learners_folder_is_off_limits_once_a_learner_is_pinned(self):
        self.assertEqual(self.tool("Read", file_path=self.p("profile", "ann", "x.md"))[0], "allow")   # pins ann
        d, why = self.tool("Read", file_path=self.p("profile", "bob", "x.md"))
        self.assertEqual(d, "deny")
        self.assertIn("another learner", why)
        self.assertEqual(self.tool("Bash", command="cat profile/bob/student_profile.json")[0], "deny")
        self.assertEqual(self.tool("Bash", command="python3 .tutor-scripts/status.py profile/bob")[0], "deny")
        self.assertEqual(self.tool("Bash", command="python3 .tutor-scripts/status.py profile/ann")[0], "allow")

    def test_scripts_are_always_allowed_to_write(self):
        self.assertEqual(self.tool("Bash", command="python3 .tutor-scripts/roster_apply.py drop profile/ann courses c1 > /dev/null")[0], "allow")

    def test_shell_writes_to_owned_files_are_denied(self):
        for cmd in ("echo '{}' > profile/ann/student_profile.json", "sed -i s/a/b/ profile/ann/subjects/c1.json", "rm profile/ann/tutor.sqlite3"):
            self.assertEqual(self.tool("Bash", command=cmd)[0], "deny", cmd)
        self.assertEqual(self.tool("Bash", command="ls profile/ann && cat profile/ann/student_profile.json")[0], "allow")

    def test_courses_are_read_only_while_a_teaching_command_runs(self):
        target = self.p("courses", "c1", "stages", "S1", "lesson.md")
        self.assertEqual(self.tool("Write", file_path=target, content="x")[0], "allow")        # no command yet
        self.fire("UserPromptSubmit", prompt="/generic-tutor:continue c1")
        d, why = self.tool("Write", file_path=target, content="x")
        self.assertEqual(d, "deny")
        self.assertIn("teaching command", why)
        self.assertEqual(self.tool("Bash", command="echo x >> courses/c1/change.md")[0], "deny")
        self.assertEqual(self.tool("Read", file_path=target)[0], "allow")
        self.fire("UserPromptSubmit", prompt="/audit")
        self.assertEqual(self.tool("Write", file_path=target, content="x")[0], "allow")

    def test_paths_outside_the_root_and_other_tools_are_allowed(self):
        self.assertEqual(self.tool("Write", file_path=os.path.join(self.tmp, "elsewhere.md"), content="x")[0], "allow")
        self.assertEqual(self.tool("WebFetch", url="https://example.org")[0], "allow")

    def test_a_symlink_into_a_learner_folder_is_seen_through(self):
        link = os.path.join(self.tmp, "sneaky")
        os.symlink(self.p("profile", "ann"), link)
        self.assertEqual(self.tool("Write", file_path=os.path.join(link, "student_profile.json"), content="x")[0], "deny")

    def test_bad_input_never_blocks(self):
        p = subprocess.run([sys.executable, SCRIPT], input="not json", capture_output=True, text=True, env=self.env)
        self.assertEqual((p.returncode, p.stdout.strip()), (0, ""))


class Lifecycle(Base):
    def test_session_start_deploys_scripts_and_names_the_learners(self):
        out = self.fire("SessionStart")
        ctx = out["hookSpecificOutput"]["additionalContext"]
        self.assertIn("ann, bob, cy", ctx)
        self.assertIn("/run", ctx)
        self.assertTrue(os.path.isfile(self.p(".tutor-scripts", "hook_guard.py")))
        self.assertTrue(os.path.isfile(self.p(".tutor-scripts", ".manifest.json")))

    def test_session_start_without_a_root_says_so(self):
        env = {**self.env, "EDU_ROOT": ""}
        ev = {"hook_event_name": "SessionStart", "session_id": "x", "cwd": self.tmp}
        out = json.loads(subprocess.run([sys.executable, SCRIPT], input=json.dumps(ev), capture_output=True, text=True, env=env).stdout)
        self.assertIn("no data folder", out["hookSpecificOutput"]["additionalContext"])

    def test_stop_reports_missing_writes_without_blocking(self):
        self.tool("Read", file_path=self.p("profile", "ann", "x.md"))           # pins ann
        sys.path.insert(0, os.path.join(ROOT, "scripts"))
        from tutorlib import ledger
        ledger.record(self.p("profile", "ann", "student_profile.json"), "record_stage_result.py", "apply", "c1",
                      detail={"stage_id": "S1", "result": "pass"})
        out = self.fire("Stop")
        self.assertIn("missing state writes", out["systemMessage"])
        self.assertIn("S1", out["systemMessage"])
        self.assertNotIn("decision", out)                                  # shown, never blocking

    def test_stop_with_no_learner_is_silent(self):
        self.assertEqual(self.fire("Stop"), {})


class Config(unittest.TestCase):
    def test_hooks_json_wires_every_event_to_the_script(self):
        with open(os.path.join(ROOT, "hooks", "hooks.json"), encoding="utf-8") as f:
            h = json.load(f)["hooks"]
        self.assertEqual(sorted(h), ["PreToolUse", "SessionStart", "Stop", "UserPromptSubmit"])
        for ev, groups in h.items():
            for g in groups:
                for cmd in g["hooks"]:
                    self.assertIn("scripts/hook_guard.py", cmd["command"], ev)
        self.assertIn("Bash", h["PreToolUse"][0]["matcher"])


if __name__ == "__main__":
    unittest.main()
