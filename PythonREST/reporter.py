import os


def save_program(content):
    """
    creates new file with a given content at server's path containing programs
    :param content: programs code
    :return: None
    """
    path = "/server/programs"
    if not os.path.exists(path):
        os.makedirs(path)
    files = len(os.listdir(path))
    file = open(path.__add__("/program".__add__(str(files+1)).__add__(".py")), 'w')
    file.write(content.decode())
