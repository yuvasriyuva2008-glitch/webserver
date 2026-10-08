from http.server import HTTPServer, SimpleHTTPRequestHandler
server=HTTPServer(('',8000), SimpleHTTPRequestHandler)
print("Server running on http://localhost:8000")
server.serve_forever()