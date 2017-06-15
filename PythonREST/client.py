import http.client
import os
import time
from PythonREST import config


class Client:
    path = os.getcwd().__add__("\Programs\\")
    file1_path = "{}{}".format(path, "anotherLongTimeProgram.py")
    file2_path = "{}{}".format(path, "example.py")
    file3_path = "{}{}".format(path, "fail.py")
    file4_path = "{}{}".format(path, "longTimeProgram.py")
    file5_path = "{}{}".format(path, "sum.py")

    @staticmethod
    def load_file(self, file_path):
        """
        loads file content from given path"
        :param file_path: filepath to file
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
        1. loads file from built-in filepath based on received id
        2. sends content of loaded file to server defined by IP and PORT variables set in configuration
        :return: None - prints received responses
        """
        time.sleep(2)
        print("client {} started.".format(id))
        print("client {} loading file...".format(id))
        if id == 1:
            content = Client.load_file(self, file_path=Client.file1_path)
        elif id == 2:
            content = Client.load_file(self, file_path=Client.file2_path)
        elif id == 3:
            content = Client.load_file(self, file_path=Client.file3_path)
        elif id == 4:
            content = Client.load_file(self, file_path=Client.file4_path)
        else:
            content = Client.load_file(self, file_path=Client.file5_path)
        print("file loaded. sending file number {}...".format(id))
        response = Client.send_file(self, str(id), content, config.IP, config.PORT)
        print(response.status, response.reason, response.read().decode())
