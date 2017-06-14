from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

from PythonREST import executor, compiler
# import executor, compiler
# import threading


class Server(ThreadingMixIn, HTTPServer):

    def run(self, IP, PORT):
        """
        starts server at given host and port
        :param IP: host's IP to start server
        :param PORT: server's port to listen requests
        :return: None
        """
        server = Server((IP, PORT), MyHandler)
        print("server started.")
        server.serve_forever()


class MyHandler(SimpleHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

    def do_PUT(self):
        """
        handles PUT requests. reads received file. tries to compile it and gives response to client about compilation.
        if compilation was successful executes received program and sends response to client with received output.
        :return: None - sends responds to client
        """
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self._set_headers()
        self.wfile.write("file successfully received\n".encode())
        # if compiler.compile_file(content):
        if 1 == 1:
            self.wfile.write("compilation successful\n".encode())
            result = executor.execute_program(content)
            self.wfile.write("program has been executed successfully and returned: ".__add__(str(result)).encode())
        else:
            self.wfile.write("file couldn't be compiled".encode())
