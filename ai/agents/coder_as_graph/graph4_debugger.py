from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.prompts import PromptTemplate
from langgraph.graph import MessagesState, START, END
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.types import Command
from langchain_core.messages import ToolMessage, AIMessage
from langgraph.prebuilt import InjectedState

from typing import Annotated, TypedDict, Literal
from pydantic import BaseModel, Field
from operator import add
from ai.utils import get_model
from ai.agents.coder.utils import create_directory_tree
from .cot import cot_graph
from pathlib import Path
from ai.agents.coder.tools import read_file
from ai.agents.coder.utils import run_shell_command
import os, contextlib
from operator import add

# PROMPTS


PROMPT = """
You are a helpful AI debugger agent responsible for identifying and resolving issues in Python code. You have access to the following tools:

Tools Available:

read_file(file_path)
Use this to open and read the contents of a file from the user's working directory.

run_code(file_path)
Use this to execute the provided Python file. Observe any output or errors to assist in debugging.

add_feedback_message(feedback_message)
Use this to provide direct, constructive feedback to the user about their code. This can include suggestions for improvements, warnings, or explanations of bugs.

EndProcess()
Use this only when the debugging process is complete and no further issues remain. This signals that the session can be safely concluded.

Your Goals:

Understand the problem by reading the code using read_file.

Diagnose bugs or runtime issues by executing the code using run_code.

Communicate clearly with the user by adding helpful messages with add_feedback_message.

Guide the user toward fixing the bug, optimizing the code, or resolving unexpected behavior.

Conclude the session by calling EndProcess when the problem is fully resolved.

Best Practices:

Always explain why an issue occurs, not just what to change.

Suggest improvements even if the code runs correctly.

Keep messages short, informative, and beginner-friendly if possible.

Use tools efficiently: avoid reading or running files repeatedly unless needed.

You're now ready to begin debugging. Be methodical, kind, and helpful.

Current project tree:
{project_tree}
"""


# STATE


class DebuggerState(MessagesState):
    intermediate_steps: list[str]
    project_tree: dict
    feedback: Annotated[list[str], add]


# TOOLS


@contextlib.contextmanager
def change_directory(path):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(original_path)


@tool
def run_code_in_directory(
    config: RunnableConfig,
    code_str: str,
    directory: str = "",
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
    working_dir = config.get("configurable").get("working_dir")
    if globals_dict is None:
        globals_dict = {}
    if locals_dict is None:
        locals_dict = {}

    with change_directory(os.path.join(working_dir, directory)):
        exec(code_str, globals_dict, locals_dict)


@tool
def read_file(
    file_path: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Opens and reads a file. This file you can edit. Returns file content."""
    working_dir = config.get("configurable").get("working_dir")
    with open(os.path.join(working_dir, file_path), "r") as f:
        code = f.read()

    return Command(
        update={
            "messages": [
                ToolMessage(
                    f"File content:\n {code}",
                    tool_call_id=tool_call_id,
                )
            ],
        }
    )


@tool
def add_feedback_message(
    feedback_message: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
):
    """Adds feedback message."""
    return Command(
        update={
            "feedback": [feedback_message],
            "messages": [
                ToolMessage(
                    f"Added feedback:\n {feedback_message}",
                    tool_call_id=tool_call_id,
                )
            ],
        }
    )


class EndProcess(BaseModel):
    """Call this tool when you finish debugging"""

    pass


@tool
def run_code(
    file_path: str, config: RunnableConfig, state: Annotated[dict, InjectedState]
):
    "Runs python file"
    working_dir = config.get("configurable").get("working_dir")

    return run_shell_command(f"python3.12 {os.path.join(working_dir, file_path)}")


tools = [
    read_file,
    run_code,
    add_feedback_message,
    run_code_in_directory,
    EndProcess,
]


def init_state(state, config: RunnableConfig):
    working_dir = config.get("configurable").get("working_dir")
    return {"project_tree": create_directory_tree(working_dir)}


def llm_node(state, config: RunnableConfig):
    working_dir = config.get("configurable").get("working_dir")
    model = config.get("configurable").get("llm")
    llm = get_model(model).bind_tools(tools)
    project_tree = create_directory_tree(working_dir)
    output = llm.invoke(
        [
            (
                "system",
                PROMPT.format(project_tree=project_tree),
            ),
            *state.get("messages"),
        ]
    )
    return {"messages": [output]}


def should_continue(state):
    tool_calls = state["messages"][-1].tool_calls
    if tool_calls:
        if tool_calls[0]["name"] == EndProcess.__name__:
            return "__end__"
        return "tools"
    return "llm_node"


graph_builder = StateGraph(DebuggerState)
graph_builder.add_node("init_state", init_state)
graph_builder.add_node("llm_node", llm_node)
graph_builder.add_node("tools", ToolNode(tools))
graph_builder.set_entry_point("init_state")
graph_builder.add_edge("init_state", "llm_node")
graph_builder.add_conditional_edges(
    "llm_node", should_continue, ["tools", "llm_node", "__end__"]
)
graph_builder.add_edge("tools", "llm_node")
graph = graph_builder.compile()

if __name__ == "__main__":
    output = graph.invoke(
        {
            "messages": [
                (
                    "ai",
                    "Debug the code given in projet tree.",
                )
            ]
        },
        config={"configurable": {"llm": "gpt-4o-mini", "working_dir": "test2"}},
    )
    print(output["feedback"])
