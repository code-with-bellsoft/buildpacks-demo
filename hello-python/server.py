import http.server
import os
import socketserver

PORT = int(os.environ.get("PORT", "8080"))

web_dir = os.path.join(os.path.dirname(__file__), "web")
os.chdir(web_dir)

handler = http.server.SimpleHTTPRequestHandler

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

with ReusableTCPServer(("", PORT), handler) as httpd:
    print(f"Listening on http://localhost:{PORT}")
    httpd.serve_forever()
