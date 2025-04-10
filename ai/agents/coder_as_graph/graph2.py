from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.prompts import PromptTemplate
from langgraph.graph import MessagesState, START, END
from langgraph.graph import StateGraph
from typing import Annotated, TypedDict, Literal
from pydantic import BaseModel, Field
from operator import add
from ai.utils import get_model
from ai.agents.coder.utils import create_directory_tree
from .cot import cot_graph
from pathlib import Path
import os, re


class CoderState(MessagesState):
    intermediate_steps: list[str]
    project_tree: list[dict]
    relevant_code: str


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


def get_code(output):
    match = re.search(r"```(?:python)?\n(.*?)\n```", output, re.DOTALL)

    if match:
        extracted_code = match.group(1)
        return extracted_code


def structure(state, config: RunnableConfig):
    model = config.get("configurable").get("llm")
    llm = get_model(model)

    class Path(BaseModel):
        path: str = Field(description="Path to code file")
        description: str

    class Schema(BaseModel):
        paths: list[Path]

    output = llm.with_structured_output(Schema).invoke(
        [
            (
                "system",
                "You are expirienced software developer. Your task is to design or update the project structure."
                "The project will be described by the user. You will be given project tree to avoid "
                "creating duplicated files. You need to return the paths to the files that either will be "
                "created or the code will be updated. To each path you need to shortly described what "
                "will be in the specific file. Return also the root directory."
                "",
            ),
            (
                "human",
                f"Project tree: {state.get("project_tree") or "Project is empty."}",
            ),
            *state.get("messages"),
        ]
    )
    return {"project_tree": output.model_dump()["paths"]}


def code(state, config: RunnableConfig):
    model = config.get("configurable").get("llm")
    llm = get_model(model)

    working_dir = config.get("configurable").get("working_dir")
    code_descriptions = []
    for path in state.get("project_tree"):
        full_path = os.path.join(working_dir, path["path"])
        create_structure(full_path)
        with open(full_path, "r") as f:
            code = f.read()

        output = llm.invoke(
            [
                (
                    "system",
                    "You are very expirienced software developer. "
                    "Your task is to create code based on the user requirements. You will be given project structure with "
                    "descriptions what the files should contain. You will be given a file to update. Return only code.",
                ),
                ("ai", f"This is what has been already done: {code_descriptions}"),
                (
                    "human",
                    f"Project paths: {state.get('project_tree')}.\n"
                    f"File that you must write code in: {path}.\n"
                    f"Current code in previous path: {code}\n"
                    "Code:",
                ),
            ]
        )
        print(output.content)
        new_code = get_code(output.content)

        with open(full_path, "w") as f:
            code = f.write(new_code)

        output = llm.invoke(
            [
                (
                    "system",
                    f"Documment the following code in markdown. Describte each class, method, funciton and contant which is in the file. Don't return the code. Structure: {state.get("project_tree")}. Document this part of the project which the code is in: {path}",
                ),
                ("human", f"Code: {code}"),
            ]
        )
        code_descriptions.append((path["path"], output.content))

    return state


graph_builder = StateGraph(CoderState)
graph_builder.add_node("structure", structure)
graph_builder.add_node("code", code)
graph_builder.set_entry_point("structure")
graph_builder.add_edge("structure", "code")
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
    #                 "what normal pacman game has.",
    #             )
    #         ]
    #     },
    #     config={"configurable": {"llm": "gpt-4o-mini", "working_dir": "./pacman"}},
    # )
