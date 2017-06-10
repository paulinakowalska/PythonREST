import socketserver

import PythonREST.executor
import http.server


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("got your message. thank you!".encode())

IP = "192.168.0.3"
PORT = 8081

Handler = MyHandler

with socketserver.TCPServer((IP, PORT), Handler) as httpd:
    print("server started.")
    httpd.serve_forever()

# TODO fix unreachable code below
file_path = "D:\\Hello.py"
PythonREST.executor.execute_file(file_path)

