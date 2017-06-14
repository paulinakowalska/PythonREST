from PythonREST import server, client, reporter
import threading


# IP = "192.168.0.3"
IP = "10.129.4.227"
PORT = 8080

client = threading.Thread(target=client.run_client, name="client")
server = threading.Thread(target=server.run, args=(IP, PORT), name="server")

client.start()
server.start()

server.join()
client.join()
