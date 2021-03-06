from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import ThreadingMixIn

from PythonREST import executor, compiler, reporter
# import executor, compiler, reporter


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
        """sets headers"""
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

    def do_PUT(self):
        """
        handles PUT requests. reads received file, tries to compile it and gives response to client about compilation.
        if compilation was successful executes received program and sends response to client with received output.
        :return: None - sends responds to client
        """
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self._set_headers()
        self.wfile.write("file successfully received\n".encode())

        try:
            c = compiler.Compiler()

            c.compile_file(content)
            self.wfile.write("compilation successful\n".encode())
        except Exception as e:
            self.wfile.write("compilation failed. Reason:".__add__(e.args).encode())

        exec = executor.Executor()
        test, result = exec.execute_program(content)

        if test:
            self.wfile.write("program has been executed successfully and returned: ".__add__(str(result)).encode())
        else:
            self.wfile.write("program execution failed ".__add__(result).encode())

        r = reporter.Reporter()
        name = r.save_program(content)
        result = r.compare(name)
        self.wfile.write("\nfiles with same content actually saved on server:\n".__add__("\n".join(result)).encode())
        if not result:
            self.wfile.write("None".encode())
