import socketserver

from PythonREST import executor
import http.server


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("got your message. thank you!".encode())

    def do_PUT(self):
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self._set_headers()
        self.wfile.write("file successfully received".encode())
        print(content)

IP = "192.168.0.3"
PORT = 8081

Handler = MyHandler

with socketserver.TCPServer((IP, PORT), Handler) as httpd:
    print("server started.")
    httpd.serve_forever()

# TODO fix unreachable code below
file_path = "D:\\Hello.py"
executor.execute_file(file_path)

