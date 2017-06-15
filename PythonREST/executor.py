class Executor:

    def execute_program(self, content):
        """
        executes given content of program.
        :param content: content of program to execute
        :return: output of executed program
        """
        result = dict()
        print("executing file...")
        try:
            exec(content, dict(), result)
            print("file executed.")
            return 1, result["result"]
        except Exception as e:
            return 0, str(e.args)
