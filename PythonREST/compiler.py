import os
import py_compile


def compile_file(file_path):
    """
    :param file_path:
    :return:
        compilation success: 1
        compilation error: 0
    """
    if file_path and os.path.isfile(file_path):
        print("compiling...")
        try:
            py_compile.compile(file_path)
            print("compilation successful")
            return 1
        except Exception as e:
            print("this file can not be compiled:", e.args)
            return 0
    else:
        print("file doesn't exist or is not a file")
        return 0
