import json
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


RESULTS_FILE = Path(__file__).with_name("quiz-results.json")


def read_results():
    try:
        results = json.loads(RESULTS_FILE.read_text(encoding="utf-8"))
        return results if isinstance(results, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_results(results):
    RESULTS_FILE.write_text(json.dumps(results), encoding="utf-8")


class QuizRequestHandler(SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        if self.path != "/api/results":
            self.send_error(404)
            return
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/results":
            self.send_json(read_results())
            return
        super().do_GET()

    def do_POST(self):
        if self.path != "/api/results":
            self.send_error(404)
            return
        try:
            length = int(self.headers.get("Content-Length", 0))
            result = json.loads(self.rfile.read(length))
            name = str(result.get("name", "")).strip()
            score = max(0, int(result.get("score", 0)))
        except (ValueError, TypeError, json.JSONDecodeError):
            self.send_error(400, "Invalid result")
            return
        results = read_results()
        results.append({"name": name, "score": score})
        results.sort(key=lambda item: int(item.get("score", 0)), reverse=True)
        write_results(results[:10])
        self.send_json({"ok": True})

    def do_DELETE(self):
        if self.path != "/api/results":
            self.send_error(404)
            return
        write_results([])
        self.send_json({"ok": True})

    def send_json(self, value):
        payload = json.dumps(value).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    ThreadingHTTPServer(("0.0.0.0", port), QuizRequestHandler).serve_forever()