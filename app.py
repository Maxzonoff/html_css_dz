from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/index.html":
            file_path = "index.html"
        elif self.path == "/contacts.html":
            file_path = "contacts.html"
        elif self.path == "/category.html":
            file_path = "category.html"
        elif self.path == "/catalog.html":
            file_path = "catalog.html"
        else:
            file_path = "contacts.html"

        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))


def run_server():
    server_adress = ("", 8000)
    httpd = HTTPServer(server_adress, SimpleHTTPRequestHandler)
    print("Сервер запущен на http://localhost:8000")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
