import http.client
import time

IP = "192.168.0.3"
PORT = 8080
file_path = "D:\\Hello.py"


def load_file(file_path):
    """
    loads file content from given path"
    :param file_path:
    :return: file content
    """
    file = open(file_path)
    return file.read()


def send_file(name, content, server_ip, PORT):
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


def run_client():
    """
    fakes client behavior with following steps:
    1. loads file from built-in filepath
    2. sends content of loaded file to server defined by built-in IP and PORT variables
    :return: None - prints received responses
    """
    time.sleep(2)
    print("loading file...")
    content = load_file(file_path)
    print("file loaded. sending file...")
    response = send_file("program1", content, IP, PORT)
    print(response.status, response.reason, response.read().decode())
