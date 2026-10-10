from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("<h1>Meu primeiro Pod no Kubernetes!</h1><p>Projeto de Nayara e Lucas</p>".encode("utf-8"))

HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()