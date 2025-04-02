from langchain_core.tools import tool, InjectedToolCallId
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import ToolNode
from typing import Annotated
from langgraph.types import Command
from .utils import create_directory_tree, run_shell_command, find_file_in_tree
import os
from langgraph.prebuilt import InjectedState


@tool
def update_code(file_path: str, old_code: str, new_code: str, config: RunnableConfig):
    """Updates code. Specify the file path, old code that must be replaced and the new code.
    If old code will not be found in file, you will be informed.
    """
    print("Updating code...")
    working_dir = config.get("configurable").get("working_dir")

    code = ""
    with open(f"{working_dir}/{file_path}", "r") as f:
        code = f.read()

    if old_code not in code:
        return f"Old code not in given file. Read the file: {file_path}, understand and call this tool again"

    new_code = code.replace(old_code, new_code)

    with open(f"{working_dir}/{file_path}", "w+") as f:
        f.write(new_code)

    with open(f"{working_dir}/{file_path}", "r") as f:
        code = f.read()

    return f"Updated code:\n {code}"


@tool
def remove_code(file_path: str, code_to_remove: str, config: RunnableConfig):
    """Removes code. Read the file in file_path and removes provided code."""
    print("Removing code...")
    working_dir = config.get("configurable").get("working_dir")

    code = ""
    with open(f"{working_dir}/{file_path}", "r") as f:
        code = f.read()

    if code_to_remove not in code:
        return f"Code to remove not in given file. Read the file: {file_path}, understand and call this tool again"

    new_code = code.replace(code_to_remove, "")

    with open(f"{working_dir}/{file_path}", "w+") as f:
        f.write(new_code)

    with open(f"{working_dir}/{file_path}", "r") as f:
        code = f.read()

    return f"Updated code:\n {code}"


@tool
def create_file(
    file_path: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Creates a file"""
    print("creating file....")
    working_dir = config.get("configurable").get("working_dir")

    with open(f"{working_dir}/{file_path}", "w+") as f:
        f.write("")
    return Command(
        update={
            "project_tree": create_directory_tree(working_dir),
            "messages": [ToolMessage("Success", tool_call_id=tool_call_id)],
        }
    )


@tool
def overwrite_code_in_file(
    file_path: str,
    code: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Overwrites code to the new file. Use this tool when a new file was created and you want to write the code."""
    print(f"Saving code to: {file_path}")

    working_dir = config.get("configurable").get("working_dir")

    with open(f"{working_dir}/{file_path}", "w+") as f:
        f.write(code)
    return Command(
        update={
            "project_tree": create_directory_tree(working_dir),
            "messages": [ToolMessage("Success", tool_call_id=tool_call_id)],
        }
    )


@tool
def read_file(file_path: str, config: RunnableConfig):
    """Read the code from given file"""
    print(f"Reading code: {file_path}")
    working_dir = config.get("configurable").get("working_dir")

    with open(f"{working_dir}/{file_path}", "r") as f:
        code = f.read()

    print(code)
    return code


@tool
def create_directory(
    directory: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Create directory. It creates relative directory"""
    working_dir = config.get("configurable").get("working_dir")

    print(f"Creating directory: {directory}")
    os.makedirs(f"{working_dir}/{directory}")
    return Command(
        update={
            "project_tree": create_directory_tree(working_dir),
            "messages": [ToolMessage("Success", tool_call_id=tool_call_id)],
        }
    )


@tool
def run_code(
    file_path: str, config: RunnableConfig, state: Annotated[dict, InjectedState]
):
    "Runs python file"
    # " so that the paths will be passed using format."
    # "I will change the command in this way: command.format(working_dir=working_dir, path=path)"
    # "If no string is returned it means that the code works. If not then please fix your mistakes"
    working_dir = config.get("configurable").get("working_dir")
    # # command = command.format(working_dir=working_dir, path=path)

    # if "{working_dir}" not in command:
    #     return "Please fix your mistake. There is no {working_dir} in command."
    # if "{path}" not in command:
    #     return "Please fix your mistake. There is no {path} in command."
    # print(command, path)
    # print("Running code using:", command)

    return run_shell_command(f"python3.12 {working_dir}/{file_path}")


tools = [
    create_file,
    overwrite_code_in_file,
    read_file,
    create_directory,
    update_code,
    remove_code,
    run_code,
]
tool_node = ToolNode(tools)
