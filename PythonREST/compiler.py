import py_compile


def compile_file(content):
    """
    :param content:
    :return:
        compilation success: 1
        compilation error: 0
    """
    try:
        py_compile.compile(content)
        return 1
    except Exception:
        return 0
