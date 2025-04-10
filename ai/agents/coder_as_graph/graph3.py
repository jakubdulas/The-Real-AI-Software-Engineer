from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.prompts import PromptTemplate
from langgraph.graph import MessagesState, START, END
from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.types import Command
from langchain_core.messages import ToolMessage

from typing import Annotated, TypedDict, Literal
from pydantic import BaseModel, Field
from operator import add
from ai.utils import get_model
from ai.agents.coder.utils import create_directory_tree
from .cot import cot_graph
from pathlib import Path
from ai.agents.coder.tools import create_file, create_directory, read_file
import os, re


class CoderState(MessagesState):
    intermediate_steps: list[str]
    selected_file_path: str


def create_structure(path_str):
    try:
        path = Path(path_str)

        if path.suffix:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)
        else:
            path.mkdir(parents=True, exist_ok=True)
            print(f"Created directory: {path}")
    except Exception as e:
        print(e)


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


@tool
def select_file_path(
    file_path: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
):
    """Selects a file to be overwritten."""
    return Command(
        update={
            "selected_file_path": file_path,
            "messages": [
                ToolMessage(
                    f"{file_path} has been selected.", tool_call_id=tool_call_id
                )
            ],
        }
    )


tools = [create_file, create_directory, read_file, select_file_path]


def coder(state, config: RunnableConfig):
    working_dir = config.get("configurable").get("working_dir")
    model = config.get("configurable").get("llm")
    llm = get_model(model)

    output = llm.bind_tools(tools).invoke(
        [
            (
                "system",
                "You are very expirienced software developer. "
                "Your task is to create code based on the user requirements. You will be given project structure with "
                "descriptions what the files should contain. You will be given a file to update."
                "Use tools that will help you to create project structure or if you need to read some file."
                "If you don't need to use tools any more then return the code."
                "remember that before giving the code you must select the file using appropriate tool."
                "Then the selected file will be overwritten with the code that you provide. "
                "Generate code for each file until the project is finished."
                "You can use selected_file_path only one time at the time."
                "If the project is finished THEN return text: <STOP>",
            ),
            *state.get("messages"),
        ]
    )
    print(output.content)
    code = get_code(output.content)
    if code:
        with open(os.path.join(working_dir, state.get("selected_file_path")), "w") as f:
            f.write(code)

    # output = llm.invoke(
    #     [
    #         (
    #             "system",
    #             f"Documment the following code in markdown. Describte each class, method, funciton and contant which is in the file. Don't return the code. Structure: {state.get("project_tree")}. Document this part of the project which the code is in: {path}",
    #         ),
    #         ("human", f"Code: {code}"),
    #     ]
    # )
    # code_descriptions.append((path["path"], output.content))

    return {"messages": [output], "code_generated": bool(code)}


def should_continue(state):
    tool_calls = state["messages"][-1].tool_calls
    if tool_calls:
        return "tools"

    if "<STOP>" in state["messages"][-1].content:
        return "__end__"
    return "coder"


graph_builder = StateGraph(CoderState)
graph_builder.add_node("coder", coder)
graph_builder.add_node("tools", ToolNode(tools))
graph_builder.set_entry_point("coder")
graph_builder.add_conditional_edges(
    "coder", should_continue, ["tools", "coder", "__end__"]
)
graph_builder.add_edge("tools", "coder")
graph = graph_builder.compile()

if __name__ == "__main__":
    from langchain_core.runnables.graph import MermaidDrawMethod

    with open("graph.png", "wb") as f:

        f.write(
            graph.get_graph().draw_mermaid_png(
                draw_method=MermaidDrawMethod.API,
            )
        )
    # graph.invoke(
    #     {
    #         "messages": [
    #             (
    #                 "human",
    #                 "create pacman game in python. It should be console game with only ascii characters. "
    #                 "No sound, no images. Just code and console. It should detect collisions, count points and everything "
    #                 "what normal pacman game has. Mark pacman as P and ghosts as G.",
    #             )
    #         ]
    #     },
    #     config={"configurable": {"llm": "gpt-4o-mini", "working_dir": "./pacman"}},
    # )
