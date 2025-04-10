import os, contextlib


@contextlib.contextmanager
def change_directory(path):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(original_path)


def run_code_in_directory(
    code_str: str,
    directory: str = "./",
    globals_dict=None,
    locals_dict=None,
):
    """
    Executes a string of Python code within the context of a specified directory.

    This function temporarily switches the working directory to the provided one
    and executes the given code string using Python's `exec()` function.

    Args:
        code_str (str): The Python code to execute, provided as a string.
        directory (str, optional): The path of the directory to execute the code in.
        globals_dict (dict, optional): A dictionary for global variables used during execution.
                                       If None, a new empty dict is created.
        locals_dict (dict, optional): A dictionary for local variables used during execution.
                                      If None, a new empty dict is created.

    Returns:
        tuple: A tuple containing the globals and locals dictionaries after execution.

    Example:
        code = '''
        with open("log.txt", "w") as f:
            f.write("Logging from within code string.")
        '''
        run_code_in_directory(code, "/tmp/scripts")
    """
    if globals_dict is None:
        globals_dict = {}
    if locals_dict is None:
        locals_dict = {}

    with change_directory(directory):
        exec(code_str, globals_dict, locals_dict)


if __name__ == "__main__":
    print(
        run_code_in_directory(
            "from encoder import custom_encoder\n\nprint(custom_encoder('abc'))",
            "./pacman/utils",
        )
    )
