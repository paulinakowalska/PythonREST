from PythonREST import server, client
import threading


IP = "192.168.0.3"
PORT = 8080

client = threading.Thread(target=client.run_client, name="client")
server = threading.Thread(target=server.run, args=(IP, PORT), name="server")

client.start()
server.start()

server.join()
client.join()

