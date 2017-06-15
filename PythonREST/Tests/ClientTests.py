import unittest, client, config
#import unittest
#from PythonREST import client


class Test_ClientTests(unittest.TestCase):

    def test_load_file(self):

        file_path = "D:\\Hello.py"

        cli = client.Client();
        file = cli.load_file(self, file_path)

        result = ''

        if file:
            result = True
        else:
            result = False

        self.assertEqual(result, True)

    def test_send_file(self):

        # to run test running server is required
        cli = client.Client();

        PORT = config.PORT
        IP = config.IP
        filePath = "D:\\Hello.py"

        content = cli.load_file(self, filePath)

        resp = cli.send_file(self, "program1", content, IP, PORT)

        result = ''

        if resp:
            result = True
        else:
            result = False

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
