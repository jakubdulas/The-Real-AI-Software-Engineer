from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
import os


@tool
def create_file(filename: str):
    """Creates a file"""
    print("creating file...")

    with open(f"./codes/{filename}", "w+") as f:
        f.write("")
    return "created"


@tool
def create_code_and_save_to_file(filename: str, code: str):
    """Saves code to the file"""
    print("saving code...")

    with open(f"./codes/{filename}", "w+") as f:
        f.write(code)
    return "done"


@tool
def read_file(filename: str):
    """Read the code from given file"""
    print("reading code...")

    with open(f"./codes/{filename}", "r") as f:
        code = f.read()
    return code


@tool
def create_directory(directory: str):
    """Create directory. It creates relative directory"""
    os.makedirs(f"./codes/{directory}")
    return "done"


tools = [
    create_file,
    create_code_and_save_to_file,
    read_file,
    create_directory,
]
tool_node = ToolNode(tools)
