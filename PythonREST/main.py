from PythonREST import server, client, reporter
import threading


class Main:

    # IP = "192.168.43.92"
    # IP = "10.129.4.227"
    IP = "192.168.0.3"

    PORT = 8080
    k = client.Client
    s = server.Server

    # client = threading.Thread(target=client.run_client, args=self, name="client")
    # server = threading.Thread(target=server.run, args=(IP, PORT), name="server")

    def start(self):
        print("starting program")
        client = threading.Thread(target=self.k.run_client, args=(self, 1), name="client")
        server = threading.Thread(target=self.s.run, args=(self, self.IP, self.PORT), name="server")
        client2 = threading.Thread(target=self.k.run_client, args=(self, 2), name="client2")

        client.start()
        server.start()
        client2.start()

        server.join()
        client.join()
        client2.join()

mk = Main()
mk.start()
