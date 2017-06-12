def execute_program(content):
    """
    executes given content of program.
    :param content: content of program to execute
    :return: output of executed program
    """
    result = dict()
    print("executing file...")
    exec(content, dict(), result)
    print("file executed.")
    return result["result"]
