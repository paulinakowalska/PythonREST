import os
import PythonREST.compiler


result = dict()


def execute_file(file_path):
    """
    executes file from given path and saves output.
    use get_result() to receive program output
    :param file_path
    :return:
        file executed: 1
        error occurred: 0
    """
    if file_path and os.path.isfile(file_path):
        if PythonREST.compiler.compile_file(file_path):
            file = open(file_path)
            print("executing file...")
            exec(file.read(), dict(), result)
            print("file executed. use get_result() to get program output")
            file.close()
            return 1
        else:
            print("couldn't compile file")
            return 0
    else:
        print("file doesn't exist or is unable to open")
        return 0


def get_result():
    """
    gets output from executed file
    :return: program output
    """
    return result["result"]
