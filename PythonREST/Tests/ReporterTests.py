# import unittest, reporter
import unittest
from PythonREST import reporter


class Test_ReporterTests(unittest.TestCase):

    def test_file_path_equals(self):
        r = reporter.Reporter()
        path = r.get_file_path(r)

        self.assertEqual(path, "/server/programs")

    def test_directory_exists(self):
        r = reporter.Reporter()
        fakePath = "/server/fake"
        isDirectoryExists = r.does_directory_exist(fakePath)

        self.assertNotEqual(isDirectoryExists, True)

    def test_create_file_directory_if_not_exists(self):

        #add here remove directory

        r = reporter.Reporter();
        path = "/server/tests"

        r.create_file_directory_if_not_exists(r, path)
        does_directory_exist = r.does_directory_exist(path)

        self.assertEqual(does_directory_exist, True)


if __name__ == '__main__':
    unittest.main()
