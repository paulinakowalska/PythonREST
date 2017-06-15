import os
from builtins import staticmethod


class Reporter:

    path = "/server/programs"

    def save_program(self, content):
        """
        creates new file with a given content at server's path containing programs
        :param content: programs code
        :return: None
        """
        self.create_file_directory_if_not_exists(self.path)

        files = len(os.listdir(self.path))
        file = open(self.path.__add__("/program".__add__(str(files+1)).__add__(".py")), 'w')
        file.write(content.decode())

    @staticmethod
    def get_file_path(self):
        return self.path

    @staticmethod
    def create_file_directory_if_not_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def does_directory_exist(self, path):
        return os.path.exists(path)
