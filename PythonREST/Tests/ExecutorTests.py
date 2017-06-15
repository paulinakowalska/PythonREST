import unittest, executor

class Test_ExecutorTests(unittest.TestCase):
    def test_execute_program(self):

        exec = executor.Executor();

        file_path = "D:\\longTimeProgram1.py"

        file = open(file_path)
        content = file.read()

        test, result = exec.execute_program(content)

        self.assertEqual(test, 1)

if __name__ == '__main__':
    unittest.main()
