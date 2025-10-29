from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from Routes.TodoRoutes import Router

router = Router()

class Server(BaseHTTPRequestHandler):
    def _send(self, response):
        status = response.get("status", 200)
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_GET(self):
        res = router.handle("GET", self.path)
        self._send(res)

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        data = json.loads(body) if body else {}
        res = router.handle("POST", self.path, data)
        self._send(res)

    def do_PATCH(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        data = json.loads(body) if body else {}
        res = router.handle("PATCH", self.path, data)
        self._send(res)

    def do_DELETE(self):
        res = router.handle("DELETE", self.path)
        self._send(res)

if __name__ == "__main__":
    server = HTTPServer(("localhost", 5000), Server)
    print("🚀 Serveur lancé sur http://localhost:5000")
    server.serve_forever()
