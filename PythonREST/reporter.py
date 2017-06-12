import os

class Reporter:

    def save_program(self, content):
        """
        creates new file with a given content at server's path containing programs
        :param content: programs code
        :return: None
        """

        path = "/server/programs"
        
        self.create_file_directory_if_not_exists(path)

        files = len(os.listdir(path))
        file = open(path.__add__("/program".__add__(str(files+1)).__add__(".py")), 'w')
        file.write(content.decode())

    def get_file_path(content):

        path = "/server/programs"

        return path

    def create_file_directory_if_not_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def is_directory_exists(self, path):

        return os.path.exists(path)



