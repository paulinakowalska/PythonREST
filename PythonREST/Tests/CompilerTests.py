import unittest, client, compiler

class Test_CompilerTests(unittest.TestCase):

    def test_compile_file(self):

        file_path = "D:\\longTimeProgram1.py"

        file = open(file_path)
        content = file.read()

        comp = compiler.Compiler()
        result = comp.compile_file(content)

        self.assertEqual(1, result)

if __name__ == '__main__':
    unittest.main()
