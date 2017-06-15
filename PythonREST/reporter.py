import os
from builtins import staticmethod
import filecmp


class Reporter:

    path = "/server/programs/"

    def save_program(self, content):
        """
        creates new file with a given content at server's path containing programs
        :param content: program's code
        :return: name of saved file
        """
        self.create_file_directory_if_not_exists(self, self.path)

        files = len(os.listdir(self.path))
        name = "program".__add__(str(files+1).__add__(".py"))
        file = open(self.path.__add__(name), 'w')
        file.write(content.decode())
        file.close()
        return name

    def compare(self, name):
        """
        compares content of file with given name from built-in directory to another file contents in this directory
        :param name: name of file to compare
        :return: list of file names with same content
        """
        result = []
        for i in (os.listdir(self.path)):
            if i != name:
                comparison = filecmp.cmp(self.path.__add__(i), self.path.__add__(name), shallow=False)
                if comparison:
                    result.append(i)
        return result

    @staticmethod
    def get_file_path(self):
        return self.path

    @staticmethod
    def create_file_directory_if_not_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def does_directory_exist(self, path):
        return os.path.exists(path)
