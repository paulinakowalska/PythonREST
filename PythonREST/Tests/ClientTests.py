import unittest, client

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

    #def test_send_file(self):

    #    IP = "192.168.0.3"
    #    PORT = 8080
    #    file_path = "D:\\Hello.py"

    #    cli = client.Client();

    #    content = cli.load_file(file_path)

    #    resp = cli.send_file("program1", content, IP, PORT)

    #    result = ''

    #    if resp:
    #        result = True
    #    else:
    #        result = False

    #    self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
