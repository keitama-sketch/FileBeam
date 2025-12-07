import http.server

server = http.server.HTTPServer(
    ('0.0.0.0', 8000),
    http.server.SimpleHTTPRequestHandler
)

print("HTTP server running on http://127.0.0.1:8000/")
server.serve_forever()
