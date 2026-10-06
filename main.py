import os
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def _respond(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"status":"ok","agent":"hello"}')

    def do_GET(self):
        self._respond()

    def do_POST(self):
        self._respond()

    def log_message(self, fmt, *args):
        print(fmt % args, flush=True)


port = int(os.environ.get("PORT", 8080))
print(f"listening on {port}", flush=True)
HTTPServer(("0.0.0.0", port), Handler).serve_forever()