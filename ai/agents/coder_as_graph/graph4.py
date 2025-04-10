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
import os, re
from operator import or_

# PROMPTS


PROMPT = """You are a professional Software Engineer AI agent. You create, edit, and manage files to deliver clean, maintainable, and production-ready software. You have access to tools that help you manage the filesystem and code generation process.
---

🛠 Tools
You can call only one tool at the time.

📂 create_directory_or_file(path_str: str)
- Creates a directory or file (along with parent directories).
- If the path has a file extension (like .py, .js, .ts), it creates a file.
- If it doesn't, it creates a directory.

📄 open_file(file_path: str)
- Opens and reads a file for editing.
- Sets this file as the active file for editing.
- Returns the file content.

✍️ EnterCodeEditor()
- Enters code editor mode.
- Your next output will be saved directly to the opened file.
- Output only valid file content (code, config, documentation, etc.).
- You should call this tool once at the time.

🛑 ExitCodeEditor()
- Exits code editor mode.
- Stops writing to the file and clears the active file context.
- You should call this tool once at the time.

✅ EndProcess()
- Use when all tasks are complete and the project is ready for delivery.

---

🧭 Workflow

1. Setup
   - Use create_directory_or_file() to prepare project structure.

2. Open File
   - Use open_file() to select a file to read and edit.

3. Enter Code Editor
   - Use EnterCodeEditor() to begin writing code to the opened file.
   - You will be told that you are in code editing mode.
   - When you are during editing code you must output only code (no explanations, no comments outside the file).
   - Use ExitCodeEditor() when done writing to return to normal planning or tool usage.

4. Repeat
   - Open and write to as many files as needed.
   - Repeat the cycle for each module or feature.

5. Finish
   - When everything is complete, call EndProcess().

---

✅ Code Best Practices

- Readable: Use meaningful names and clean formatting.
- Modular: Break logic into reusable functions and classes.
- Documented: Include docstrings and comments for complex logic.
- Secure & Efficient: Avoid dangerous patterns and unnecessary computations.
- Formatted: Follow style guides (e.g., PEP8 for Python).
- Testable: Include test cases or stubs where relevant.


Act like a real developer collaborating in a team. Be precise, efficient, and thoughtful.


Current project tree:
{project_tree}
"""


# STATE


class CoderState(MessagesState):
    intermediate_steps: list[str]
    opened_file: str
    code_editor: bool
    project_tree: dict


# UTILS


def get_path(text):
    match = re.search(r"<PATH>(.*?)</PATH>", text)
    if match:
        path = match.group(1)
        print(path)
        return path
    else:
        print("No path found.")


def get_code(output):
    match = re.search(r"```(?:python)?\n(.*?)\n```", output, re.DOTALL)

    if match:
        extracted_code = match.group(1)
        return extracted_code


# TOOLS


@tool
def create_directory_or_file(
    path_str: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Creates file and directories to this file.."""
    print(path_str)
    working_dir = config.get("configurable").get("working_dir")
    print(working_dir)
    print(os.path.join(working_dir, path_str))
    print("F")

    path = Path(os.path.join(working_dir, path_str))

    if path.suffix:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch(exist_ok=True)
        return Command(
            update={
                "messages": [
                    ToolMessage(
                        f"Created file",
                        tool_call_id=tool_call_id,
                    )
                ],
            }
        )
    else:
        path.mkdir(parents=True, exist_ok=True)
        return Command(
            update={
                "messages": [
                    ToolMessage(
                        f"Created directory: {path}",
                        tool_call_id=tool_call_id,
                    )
                ],
            }
        )


@tool
def open_file(
    file_path: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Opens and reads a file. This file you can edit. Returns file content."""
    print(file_path)
    working_dir = config.get("configurable").get("working_dir")
    print(working_dir)
    print(os.path.join(working_dir, file_path))
    print("O")
    with open(os.path.join(working_dir, file_path), "r") as f:
        code = f.read()

    return Command(
        update={
            "opened_file": file_path,
            "messages": [
                ToolMessage(
                    f"{file_path} has been opened. \nFile content: {code}",
                    tool_call_id=tool_call_id,
                )
            ],
        }
    )


class EndProcess(BaseModel):
    """Call this tool when you finish the project"""

    pass


@tool
def EnterCodeEditor(
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
):
    """Call this tool when you want to write the code to the opened file"""

    return Command(
        update={
            "code_editor": True,
            "messages": [
                ToolMessage(
                    f"Entered code editor. Now you are writing code ",
                    tool_call_id=tool_call_id,
                ),
                AIMessage(
                    content=f"You are in {state.get("opened_file")}. From now everything what you will return \
                          will be saved to the previosly mentioned file. You can exit it using ExitCodeEditor tool."
                ),
            ],
        }
    )


@tool
def ExitCodeEditor(
    tool_call_id: Annotated[str, InjectedToolCallId],
):
    """Exit code editing."""

    return Command(
        update={
            "code_editor": False,
            "opened_file": "",
            "messages": [
                ToolMessage(
                    f"Exited code editor",
                    tool_call_id=tool_call_id,
                )
            ],
        }
    )


tools = [
    create_directory_or_file,
    open_file,
    EnterCodeEditor,
    ExitCodeEditor,
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
                # + (
                #     "Now you are inside code editor. "
                #     if state.get("code_editor")
                #     else ""
                # ),
            ),
            *state.get("messages"),
        ]
    )
    print(output.content)
    if state.get("code_editor", False):
        if output.content:
            code = get_code(output.content)
            with open(os.path.join(working_dir, state.get("opened_file")), "w") as f:
                f.write(code)
    return {"messages": [output]}


def should_continue(state):
    tool_calls = state["messages"][-1].tool_calls

    if tool_calls:
        state["messages"][-1].tool_calls = state["messages"][-1].tool_calls[:1]
        print(state["messages"][-1].tool_calls)
        if tool_calls[0]["name"] == EndProcess.__name__:
            return "__end__"
        # if tool_calls[0]["name"] == EnterCodeEditor.__name__:
        #     return "coder"
        return "tools"
    return "llm_node"


# def coder(state, config: RunnableConfig):
#     model = config.get("configurable").get("llm")
#     llm = get_model(model)

#     output = llm.bind_tools(tools).invoke(
#         [
#             ("system", PROMPT),
#             *state.get("messages"),
#         ]
#     )
#     return {"messages": [output]}


graph_builder = StateGraph(CoderState)
graph_builder.add_node("init_state", init_state)
graph_builder.add_node("llm_node", llm_node)
# graph_builder.add_node("coder", coder)
graph_builder.add_node("tools", ToolNode(tools))
graph_builder.set_entry_point("init_state")
graph_builder.add_edge("init_state", "llm_node")
graph_builder.add_conditional_edges(
    "llm_node", should_continue, ["tools", "llm_node", "__end__"]
)
graph_builder.add_edge("tools", "llm_node")
graph = graph_builder.compile()

if __name__ == "__main__":
    from langchain_core.runnables.graph import MermaidDrawMethod

    # with open("graph.png", "wb") as f:

    #     f.write(
    #         graph.get_graph().draw_mermaid_png(
    #             draw_method=MermaidDrawMethod.API,
    #         )
    #     )
    graph.invoke(
        {
            "messages": [
                (
                    "human",
                    "create 2 functions, one taking any string and encoding like this: when a accours then it is b. If b then c. c id d. ans so on."
                    "Another function should return the value of y given formula y = 2x+5. ",
                )
            ]
        },
        config={
            "configurable": {"llm": "gpt-4o-mini", "working_dir": "test_dir"},
            "recursion_limit": 50,
        },
    )
