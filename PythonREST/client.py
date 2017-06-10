import http.client


server_ip = "192.168.0.3"
PORT = 8081


def load_file(file_path):
    """
    loads file content from given path"
    :param file_path:
    :return: file content
    """
    file = open(file_path)
    return file.read()


def send_file(content):
    """
    sends content to server defined in client module
    :param content:
    :return: server response
    """
    conn = http.client.HTTPConnection(server_ip, PORT)
    conn.request("PUT", "/", content)
    return conn.getresponse()

file_path = "D:\\Hello.py"
content = load_file(file_path)
response = send_file(content)

print(response.status, response.reason, response.read())
