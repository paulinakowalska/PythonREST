# import unittest, client
import unittest
from PythonREST import client


class Test_ClientTests(unittest.TestCase):

    def test_load_file(self):

        file_path = "D:\\Hello.py"
        file = open(file_path)

        result = ''

        if file:
            result = True
        else:
            result = False

        self.assertEqual(result, True)

    def test_send_file(self):

        # to run test running server is required
        cli = client.Client();

        PORT = cli.getServerPort()
        IP = cli.getServerIP()
        filePath = cli.getFilePath()

        content = cli.load_file(filePath)

        resp = cli.send_file("program1", content, IP, PORT)

        result = ''

        if resp:
            result = True
        else:
            result = False

        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
