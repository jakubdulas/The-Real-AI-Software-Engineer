from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.prompts import PromptTemplate
from langgraph.graph import MessagesState, START, END
from langgraph.graph import StateGraph
from typing import Annotated, TypedDict, Literal
from pydantic import BaseModel, Field
from operator import add
from ai.utils import get_model
from .tools import create_directory, create_file, read_file
from .cot import cot_graph


BRAIN_PROMPT = """You are coder's brain. Your task is to think about the tasks in order to 
accomplish given task. You will be given a list what has been done. Think about what to do next."""
# You will get the plan of achieving the task."""

CODE_PROMPT = """You are expirienced programmer. You will be given code. 
Use tools to create directories, files and read files. 
Return only code."""


class CoderState(MessagesState):
    intermediate_steps: list[str]
    project_tree: dict
    relevant_code: str


class CodeSchema(BaseModel):
    code: str
    dir: str


class Codes(BaseModel):
    codes: list[CodeSchema]


class Dir(BaseModel):
    path: str
    description: str = Field(description="Description what should be there")


class DirsSchema(BaseModel):
    directories: list[Dir] = Field(description="List of directories")


def llm_node(state: CoderState, config: RunnableConfig):
    model_name = config.get("configurable").get("llm")
    # llm = get_model(model_name)
    intermediate_steps = cot_graph.invoke(
        {"messages": state.get("messages")},
        config={"configurable": {"llm": model_name}},
    ).get("intermediate_steps")

    # output = llm.invoke(
    #     [
    #         ("system", BRAIN_PROMPT),
    #         ("ai", "Nothing has been done. You begin."),
    #         *state.get("messages"),
    #     ]
    # )
    return {"intermediate_steps": intermediate_steps}


import os
from pathlib import Path


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


import re


def get_code(output):
    match = re.search(r"```(?:python)?\n(.*?)\n```", output, re.DOTALL)

    if match:
        extracted_code = match.group(1)
        return extracted_code


def code(state: CoderState, config: RunnableConfig):
    model_name = config.get("configurable").get("llm")
    llm = get_model(model_name)
    # .bind_tools([create_directory, create_file, read_file])
    print(state.get("intermediate_steps")[0])

    directories = llm.with_structured_output(DirsSchema).invoke(
        [
            (
                "system",
                "Based on the provided by the user prompts and the current step, return the files that must be created with directories",
            ),
            *state.get("messages"),
            # ("ai", "Focus on: " + state.get("intermediate_steps")[0]),
        ]
    )

    print("directories", directories.directories)

    for dir_ in directories.directories:
        create_structure(dir_.path)

    directories = list(filter(lambda x: "." in x.path, directories.directories))

    for directory in directories:
        output = llm.invoke(
            [
                (
                    "system",
                    f"You are intelligent Software engineer. Here you have the project structure. {directories}. Now focus on Writing code to the file {directory.model_dump()} based on the user requirements. Return only code.",
                ),
                *state.get("messages"),
                # ("ai", "Focus on: " + state.get("intermediate_steps")[0]),
            ]
        )
        print("#" * 50 + " CODE " + "#" * 50)
        print(output.content)

        file_path = Path(directory.path)
        file_path.write_text(get_code(output.content))

        output = llm.invoke(
            [
                (
                    "system",
                    f"Documment the following code in markdown. Describte each class, method, funciton and contant which is in the file. Don't return the code. Structure: {directories}. Document this part of the project which the code is in: {directory.model_dump()}",
                ),
                ("human", f"Code: {output.content}"),
            ]
        )
        print("#" * 50 + " DOCUMENTATION " + "#" * 50)
        print(output.content)

    return state


def debug(state: CoderState, config: RunnableConfig):
    model_name = config.get("configurable").get("model")


graph = StateGraph(CoderState)


graph.add_node("llm_node", llm_node)
graph.add_node("code", code)

graph.add_edge(START, "llm_node")
graph.add_edge("llm_node", "code")
graph.add_edge("code", END)

graph = graph.compile()
if __name__ == "__main__":
    from langchain_core.runnables.graph import MermaidDrawMethod

    with open("graph.png", "wb") as f:

        f.write(
            graph.get_graph().draw_mermaid_png(
                draw_method=MermaidDrawMethod.API,
            )
        )

    # graph.invoke(
    #     {"messages": [("human", "create pacman game in python")]},
    #     config={"configurable": {"llm": "gpt-4o-mini"}},
    # )
