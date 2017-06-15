import py_compile

class Compiler:

    def compile_file(self, content):
        """
        tries to compile file content
        :param content:
        :return:
            compilation success: 1
            compilation error: 0
        """
        try:
            py_compile.compile(content)
            return 1, "success"
        except Exception as e:
            return 0, e.args
