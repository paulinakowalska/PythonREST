from PythonREST import server, client, config
import threading


class Main:
    k = client.Client
    s = server.Server

    def start(self):
        print("starting program")
        client = threading.Thread(target=self.k.run_client, args=(self, 1), name="client")
        server = threading.Thread(target=self.s.run, args=(self, config.IP, config.PORT), name="server")
        client2 = threading.Thread(target=self.k.run_client, args=(self, 2), name="client2")

        client.start()
        server.start()
        client2.start()

        server.join()
        client.join()
        client2.join()

    def test_all_programs_locally(self):
        print("testing client-server based application:"
              "\n1. creating server: IP={}, PORT={}"
              "\n2. creating 5 client threads - each sending different program to server after few seconds delay:"
              "\n3. printing communication output"
              "\n\nstarting application...".format(config.IP, config.PORT))

        s1 = threading.Thread(target=self.s.run, args=(self, config.IP, config.PORT), name="server")
        c1 = threading.Thread(target=self.k.run_client, args=(self, 1), name="c1")
        c2 = threading.Thread(target=self.k.run_client, args=(self, 2), name="c2")
        c3 = threading.Thread(target=self.k.run_client, args=(self, 3), name="c3")
        c4 = threading.Thread(target=self.k.run_client, args=(self, 4), name="c4")
        c5 = threading.Thread(target=self.k.run_client, args=(self, 5), name="c5")

        s1.start()
        c1.start()
        c2.start()
        c3.start()
        c4.start()
        c5.start()

        s1.join()
        c1.join()
        c2.join()
        c3.join()
        c4.join()
        c5.join()

mk = Main()
# mk.start()
mk.test_all_programs_locally()
