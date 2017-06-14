import http.client
import time


class Client:

    # IP = "192.168.43.92"
    IP = "192.168.0.3"
    # IP = "192.168.56.1"

    PORT = 8080
    # file_path = "D:\\Hello.py"
    file_path = "D:\\longTimeProgram1.py"
    file_path2 = "D:\\longTimeProgram2.py"

    @staticmethod
    def load_file(self, file_path):
        """
        loads file content from given path"
        :param file_path:
        :return: file content
        """
        file = open(file_path)
        return file.read()

    @staticmethod
    def send_file(self, name, content, server_ip, PORT):
        """
        sends content to server defined in client module
        :param:
        name: name of file to send
        content: content of file to send
        server_ip: ip of server where content should be sent
        PORT: port where server is listening for requests
        :return: server response
        """
        conn = http.client.HTTPConnection(server_ip, PORT)
        conn.request("PUT", "/".__add__(name), content)
        return conn.getresponse()

    def run_client(self, id):
        """
        fakes client behavior with following steps:
        1. loads file from built-in filepath
        2. sends content of loaded file to server defined by built-in IP and PORT variables
        :return: None - prints received responses
        """
        time.sleep(2)
        print("client started.")
        print("loading file...")
        if id == 1:
            content = Client.load_file(self, file_path=Client.file_path)
        else:
            content = Client.load_file(self, file_path=Client.file_path2)
        print("file loaded. sending file...")
        response = Client.send_file(self, "program1", content, Client.IP, Client.PORT)
        print(response.status, response.reason, response.read().decode())
