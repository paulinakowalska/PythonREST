from PythonREST import server, client, reporter
import threading


class Main:

    IP = "192.168.56.1"
    # IP = "10.129.4.227"
    PORT = 8080
    k = client.Client
    s = server.Server

    # client = threading.Thread(target=client.run_client, args=self, name="client")
    # server = threading.Thread(target=server.run, args=(IP, PORT), name="server")

    def start(self):
        print("starting program")
        client = threading.Thread(target=self.k.run_client, args=(self,), name="client")
        server = threading.Thread(target=self.s.run, args=(self, self.IP, self.PORT), name="server")

        client.start()
        server.start()

        server.join()
        client.join()

mk = Main()
mk.start()
