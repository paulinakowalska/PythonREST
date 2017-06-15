from PythonREST import server, client, config
import threading


class Main:

    IP = config.IP
    PORT = config.PORT
    k = client.Client
    s = server.Server

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
