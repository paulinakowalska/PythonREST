from PythonREST import server, client, reporter
import threading


class main():

    # IP = "192.168.0.3"
    IP = "10.129.4.227"
    PORT = 8080
    k = client.Client
    s = server.Server

    # client = threading.Thread(target=client.run_client, args=self, name="client")
    # server = threading.Thread(target=server.run, args=(IP, PORT), name="server")

    def f(self):
        print("wywolanie f()")
        # client = threading.Thread(target=self.k.run_client, args=self, name="client")
        server = threading.Thread(target=self.s.run, args=(self, self.IP, self.PORT), name="server")

        # client.start()
        server.start()

        server.join()
        # client.join()
mojaklasa=main()
mojaklasa.f()
