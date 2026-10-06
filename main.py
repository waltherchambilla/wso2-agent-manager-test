import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/chat":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else b"{}"
        try:
            msg = json.loads(body).get("message", "")
        except Exception:
            msg = ""

        payload = json.dumps({"response": f"hola, dijiste: {msg}"}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status":"ok"}')

    def log_message(self, fmt, *args):
        print(fmt % args, flush=True)


port = int(os.environ.get("PORT", 8000))
print(f"listening on {port}", flush=True)
HTTPServer(("0.0.0.0", port), Handler).serve_forever()