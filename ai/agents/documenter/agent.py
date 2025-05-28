from typing import Annotated

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

from typing import Literal
from typing_extensions import TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState, END
from langgraph.types import Command
from langchain_core.runnables import RunnableConfig

from ai.base_agents.agent import Agent
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import create_react_agent

from ai.tot.v1.utils import get_model
from dotenv import load_dotenv
from .tools import tools
from .utils import create_directory_tree


# TODO: Add project
class Documenter:
    SYSTEM_PROMPT = """You are a code documenter. Your task is to generate documentation for a codebase. The documentation for each file should be saved in a separate text file named using the following pattern: name_of_file.code_extension.md.
You have access to tools that allow you to:
Read source code files
Read existing documentation files
Create and update documentation files
Please follow these guidelines:
Output all documentation in Markdown format.
Start by documenting files that are imported by other files, as understanding these is essential for documenting the rest of the codebase.
When documenting a file, ensure you fully understand all the classes and functions it imports from other modules.
After documenting a file, proceed to the files that depend on it.
If documentation already exists for a file, evaluate its quality and improve it if necessary.
Your goal is to produce accurate, comprehensive, and well-structured documentation for the entire codebase.
Keep the project strucure.
Call max 3 tools per step. 
Write very detailed documentation to each file.
Document the code step by step, read -> understand -> document. Take another file and read -> understand. If necessery create file structure
and others. But if you can see imports from different files go to these files but also one by one. So read -> read parent -> (do it as you go to the main file) -> document.
Then go to the childs. If you can see import that is in the project structure and it is not documented, then go to this file first then document the rest.
Remember to save all of the documentation to the files.

Project structure (code):
{structure}

Documentation structure:
{doc_structure}
"""

    class DocumenterState(MessagesState):
        remaining_steps: 1000

    def __init__(self, llm, code_dir, documentation_dir, skip_dirs=[]):
        load_dotenv()
        print(create_directory_tree(code_dir, skip_dirs))
        self.graph = create_react_agent(
            get_model(llm),
            tools=tools,
            prompt=self.SYSTEM_PROMPT.format(
                structure=create_directory_tree(code_dir),
                doc_structure=create_directory_tree(documentation_dir),
            ),
            state_schema=self.DocumenterState,
        )

    def invoke(self, *args, **kwargs):
        return self.graph.invoke(*args, **kwargs)


if __name__ == "__main__":
    documenter = Documenter(
        "gpt-4o",
        "/Users/jakubdulas/Documents/NextProcure/offers-analyzer-demo/src/ai_processor",
        # "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/ai",
        "/Users/jakubdulas/Documents/NextProcure/offers-analyzer-demo/docs/ai_processor",
        skip_dirs=["kuba"],
    )
    state = documenter.invoke(
        {
            "messages": [
                (
                    "human",
                    """Document the whole code given in the directories. Be detailed and descirbe the workflow and describe the algorithms. Make some diagrams when applicable.""",
                )
            ]
        },
        config={
            "recursion_limit": 1000,
            "configurable": {
                "working_dir": "/Users/jakubdulas/Documents/NextProcure/offers-analyzer-demo/src/ai_processor",
                # "working_dir": "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/ai",
                "documentation_dir": "/Users/jakubdulas/Documents/NextProcure/offers-analyzer-demo/docs/ai_processor",
            },
        },
    )
    print(state["messages"][-1])
