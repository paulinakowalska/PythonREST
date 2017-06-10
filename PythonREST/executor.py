import os
import PythonREST.compiler


def execute_file(file_path):
    """
    executes file from given path.
    :param file_path
    :return:
        file executed: 1
        error occurred: 0
    """
    if file_path and os.path.isfile(file_path):
        if PythonREST.compiler.compile_file(file_path):
            file = open(file_path)
            result = dict()
            print("executing file...")
            exec(file.read(), dict(), result)
            print("file executed. output:", result["result"])
            send_result(result["result"])
            file.close()
            return 1
        else:
            print("couldn't compile file")
            return 0
    else:
        print("file doesn't exist or is unable to open")
        return 0


def send_result(result):
    """
    :param result:
    Sends result back to client.
    """
    # TODO implement this method
