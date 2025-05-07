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
def update_documentation(
    file_path: str,
    old_documentation: str,
    new_documentation: str,
    config: RunnableConfig,
):
    """Updates documentation. Specify the file path, old documentation that must be replaced and the new documentation.
    If old documentation will not be found in file, you will be informed.
    """
    print("Updating documentation...")
    documentation_dir = config.get("configurable").get("documentation_dir")

    documentation = ""
    with open(f"{documentation_dir}/{file_path}", "r") as f:
        documentation = f.read()

    if old_documentation not in documentation:
        return f"Old documentation not in given file. Read the file: {file_path}, understand and call this tool again"

    new_documentation = documentation.replace(
        old_documentation, new_documentation, count=1
    )

    with open(f"{documentation_dir}/{file_path}", "w+") as f:
        f.write(new_documentation)

    with open(f"{documentation_dir}/{file_path}", "r") as f:
        documentation = f.read()

    return f"Updated documentation:\n {documentation}"


@tool
def remove_documentation(
    file_path: str, documentation_to_remove: str, config: RunnableConfig
):
    """Removes documentation. Read the file in file_path and removes provided documentation."""
    print("Removing documentation...")
    documentation_dir = config.get("configurable").get("documentation_dir")

    documentation = ""
    with open(f"{documentation_dir}/{file_path}", "r") as f:
        documentation = f.read()

    if documentation_to_remove not in documentation:
        return f"documentation to remove not in given file. Read the file: {file_path}, understand and call this tool again"

    new_documentation = documentation.replace(documentation_to_remove, "", count=1)

    with open(f"{documentation_dir}/{file_path}", "w+") as f:
        f.write(new_documentation)

    with open(f"{documentation_dir}/{file_path}", "r") as f:
        documentation = f.read()

    return f"Updated documentation:\n {documentation}"


@tool
def create_file(
    file_path: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Creates a file"""
    print("creating file....")
    documentation_dir = config.get("configurable").get("documentation_dir")
    print(file_path)
    with open(f"{documentation_dir}/{file_path}", "w+") as f:
        f.write("")
    return Command(
        update={
            "project_tree": create_directory_tree(documentation_dir),
            "messages": [ToolMessage("Success", tool_call_id=tool_call_id)],
        }
    )


@tool
def overwrite_documentation_in_file(
    file_path: str,
    documentation: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Overwrites documentation to the new file. Use this tool when a new file was created and you want to write the documentation."""
    print(f"Saving documentation to: {file_path}")

    documentation_dir = config.get("configurable").get("documentation_dir")

    with open(f"{documentation_dir}/{file_path}", "w+") as f:
        f.write(documentation)
    return Command(
        update={
            "project_tree": create_directory_tree(documentation_dir),
            "messages": [ToolMessage("Success", tool_call_id=tool_call_id)],
        }
    )


@tool
def read_file(file_path: str, config: RunnableConfig):
    """Read the documentation from given file"""
    print(f"Reading documentation: {file_path}")
    documentation_dir = config.get("configurable").get("documentation_dir")

    with open(f"{documentation_dir}/{file_path}", "r") as f:
        documentation = f.read()

    print(documentation)
    return documentation


@tool
def create_directory(
    directory: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Create directory. It creates relative directory"""
    documentation_dir = config.get("configurable").get("documentation_dir")

    print(f"Creating directory: {directory}")
    os.makedirs(f"{documentation_dir}/{directory}")
    return Command(
        update={
            "project_tree": create_directory_tree(documentation_dir),
            "messages": [ToolMessage("Success", tool_call_id=tool_call_id)],
        }
    )


@tool
def read_code(file_path: str, config: RunnableConfig):
    """Read the code from given file"""
    print(f"Reading code: {file_path}")
    working_dir = config.get("configurable").get("working_dir")

    with open(f"{working_dir}/{file_path}", "r") as f:
        code = f.read()

    return code


tools = [
    create_file,
    overwrite_documentation_in_file,
    read_file,
    create_directory,
    update_documentation,
    remove_documentation,
    read_code,
    # get_project_board,
]
tool_node = ToolNode(tools)
