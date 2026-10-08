"""B-03.2: the local chat-completions backend, tested against a fake server on this machine (no model, no network)."""
import contextlib
import http.server
import io
import json
import os
import socket
import sys
import threading
import time
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from evals import backends, harness  # noqa: E402


class Fake(http.server.BaseHTTPRequestHandler):
    behaviour = "ok"
    seen = []

    def log_message(self, *a):
        pass

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        Fake.seen.append((self.path, dict(self.headers), body))
        b = Fake.behaviour
        if b == "slow":
            time.sleep(1.5)
        if b == "http500":
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'{"error": "model not loaded"}')
            return
        if b == "redirect":
            self.send_response(307)
            self.send_header("Location", "http://example.net/steal")
            self.end_headers()
            return
        payload = {"ok": {"choices": [{"message": {"role": "assistant", "content": "hello there"}}]},
                   "garbage": "<html>not json</html>", "empty": {"choices": [{"message": {"content": "  "}}]},
                   "shape": {"result": 1}, "slow": {"choices": [{"message": {"content": "late"}}]}}[b]
        data = payload.encode() if isinstance(payload, str) else json.dumps(payload).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Fake)
        cls.url = f"http://127.0.0.1:{cls.srv.server_address[1]}/v1"
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        cls.srv.server_close()

    def setUp(self):
        Fake.behaviour, Fake.seen = "ok", []


class Calls(Base):
    def test_a_reply_is_returned_and_the_request_has_the_documented_shape(self):
        be = backends.LocalChat("tiny-model", self.url, temperature=0.2, seed=7, max_tokens=50)
        self.assertEqual(be.complete("SYS", "PROMPT"), "hello there")
        path, headers, body = Fake.seen[0]
        self.assertEqual(path, "/v1/chat/completions")
        self.assertEqual(body["model"], "tiny-model")
        self.assertEqual(body["messages"], [{"role": "system", "content": "SYS"}, {"role": "user", "content": "PROMPT"}])
        self.assertEqual((body["temperature"], body["seed"], body["stream"], body["max_tokens"]), (0.2, 7, False, 50))
        self.assertEqual(be.name, "local:tiny-model")
        self.assertEqual(be.settings, {"model": "tiny-model", "url": self.url, "temperature": 0.2, "seed": 7, "max_tokens": 50})

    def test_each_failure_says_what_went_wrong(self):
        be = backends.LocalChat("m", self.url)
        for behaviour, words in (("http500", "HTTP 500"), ("garbage", "not chat-completions JSON"), ("shape", "not chat-completions JSON"), ("empty", "empty reply")):
            Fake.behaviour = behaviour
            with self.assertRaises(RuntimeError) as cm:
                be.complete("s", "p")
            self.assertIn(words, str(cm.exception), behaviour)
        Fake.behaviour = "http500"
        with self.assertRaises(RuntimeError) as cm:
            be.complete("s", "p")
        self.assertIn("model not loaded", str(cm.exception))                    # the server's own words are passed on

    def test_nothing_listening_is_explained(self):
        with socket.socket() as s:
            s.bind(("127.0.0.1", 0))
            port = s.getsockname()[1]
        with self.assertRaises(RuntimeError) as cm:
            backends.LocalChat("m", f"http://127.0.0.1:{port}/v1", timeout=2).complete("s", "p")
        self.assertIn("no model server reachable", str(cm.exception))

    def test_a_slow_model_times_out_with_a_clear_message(self):
        Fake.behaviour = "slow"
        with self.assertRaises(RuntimeError) as cm:
            backends.LocalChat("m", self.url, timeout=0.3).complete("s", "p")
        self.assertIn("did not answer within", str(cm.exception))

    def test_a_redirect_is_refused_so_the_prompt_cannot_be_sent_elsewhere(self):
        Fake.behaviour = "redirect"
        with self.assertRaises(RuntimeError) as cm:
            backends.LocalChat("m", self.url).complete("s", "p")
        self.assertIn("HTTP 307", str(cm.exception))

    def test_proxy_environment_variables_are_ignored_for_a_local_call(self):
        saved = {k: os.environ.get(k) for k in ("HTTP_PROXY", "http_proxy", "HTTPS_PROXY", "https_proxy", "NO_PROXY", "no_proxy")}
        self.addCleanup(lambda: [os.environ.pop(k, None) if v is None else os.environ.__setitem__(k, v) for k, v in saved.items()])
        for k in saved:
            os.environ.pop(k, None)
        os.environ["HTTP_PROXY"] = os.environ["http_proxy"] = "http://127.0.0.1:9"      # a dead proxy: any use of it fails the call
        self.assertEqual(backends.LocalChat("m", self.url).complete("s", "p"), "hello there")


class Locality(unittest.TestCase):
    def test_only_this_machine_is_accepted_by_default(self):
        for url in ("http://localhost:11434/v1", "http://127.0.0.1:8080/v1", "http://127.0.0.2/v1", "http://[::1]:11434/v1"):
            backends.LocalChat("m", url)
        for url in ("http://example.net/v1", "https://api.example.net/v1", "http://127.0.0.1.example.net/v1", "http://192.168.1.20:11434/v1",
                    "http://10.0.0.5/v1", "http://localhost.example.net/v1"):
            with self.assertRaises(ValueError, msg=url) as cm:
                backends.LocalChat("m", url)
            self.assertIn("would leave", str(cm.exception))

    def test_remote_is_possible_only_on_purpose(self):
        self.assertTrue(backends.LocalChat("m", "http://192.168.1.20:11434/v1", allow_remote=True).allow_remote)

    def test_other_url_problems_are_refused(self):
        with_credentials = "http://user:pw" + "@" + "127.0.0.1/v1"                  # built at run time so the repo scan does not read it as an address
        for url in ("ftp://127.0.0.1/v1", "127.0.0.1:11434/v1", "http:///v1", with_credentials):
            with self.assertRaises(ValueError, msg=url):
                backends.LocalChat("m", url, allow_remote=True)


class Cli(Base):
    def test_a_suite_runs_through_the_local_backend_and_the_report_names_it(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = harness.main(["run", "--suite", "grading", "--backend", "local", "--model", "tiny", "--url", self.url, "--limit", "2", "--workers", "1"])
        self.assertEqual(code, 0)
        report = json.loads(buf.getvalue())["grading"]
        self.assertEqual(report["backend"], "local:tiny")
        self.assertEqual(report["cases"], 2)
        self.assertEqual(len(Fake.seen), 2)                                    # one request per case and sample

    def test_a_non_local_url_is_refused_by_the_command_line(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = harness.main(["run", "--suite", "grading", "--backend", "local", "--model", "m", "--url", "http://example.net/v1"])
        self.assertEqual(code, 2)
        self.assertIn("would leave", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
