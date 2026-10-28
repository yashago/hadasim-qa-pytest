import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

CARS = [
    {"licenseId": "ABC123", "manufacturer": "Toyota", "modelYear": 2020},
    {"licenseId": "XYZ789", "manufacturer": "Honda", "modelYear": 2018},
    {"licenseId": "LMN456", "manufacturer": "Tesla", "modelYear": 2023},
]

_servers = {}


class CarHandler(BaseHTTPRequestHandler):
    # GET /cars             -> all cars
    # GET /cars/<licenseId> -> single car or 404
    def do_GET(self):
        parts = self.path.strip("/").split("/")
        if parts == ["cars"]:
            self._send(200, CARS)
        elif len(parts) == 2 and parts[0] == "cars":
            car = next((c for c in CARS if c["licenseId"] == parts[1]), None)
            if car:
                self._send(200, car)
            else:
                self._send(404, {"error": f"Car {parts[1]} not found"})
        else:
            self._send(404, {"error": "Not found"})

    def _send(self, status, body):
        payload = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format, *args):
        pass  # keep pytest output quiet


def create_api_server(port=0):
    # port=0 lets the OS pick a free port
    server = ThreadingHTTPServer(("127.0.0.1", port), CarHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    server_url = f"http://127.0.0.1:{server.server_address[1]}"
    _servers[server_url] = server
    return server_url


def remove_api_server(server_url):
    server = _servers.pop(server_url)
    server.shutdown()
    server.server_close()
