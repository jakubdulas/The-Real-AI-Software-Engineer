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

from ai.base_agents.agent import Agent
from ai.tot.v1.utils import get_model
from dotenv import load_dotenv
from .tools import tools
from .project_board import ProjectBoard
from .types import ProjectBoardType
import json


# TODO: Story points that will define how employees are overloaded with work. It will indicate if new spint is required.
# TODO: Subtasks
# TODO: Add to ticket -> "depends_on": ticker_id or None
# TODO: Form e.g. add questions about project scope etc.


def merge_dicts_recursive(d1, d2):
    if not isinstance(d1, dict) or not isinstance(d2, dict):
        return d2

    result = dict(d1)
    for key, value in d2.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = merge_dicts_recursive(result[key], value)
            elif isinstance(result[key], list) and isinstance(value, list):
                # Combine unique elements while preserving order
                result[key] = result[key] + [v for v in value if v not in result[key]]
            else:
                result[key] = value  # Overwrite with new value
        else:
            result[key] = value
    return result


class ProjectManager(Agent):
    SYSTEM_PROMPT = """
You are the best project manager. You will be given by the user what they want to achieve. Your task is to plan the project in the way that tasks are distributed well, 
they are well defined, detailed, not too general. remember to split big problem into small components. Plan the work into at least 2 sptints. You will get set of tools that will 
help you to organize the work. Create sprint by sprint. When You finish the sprint then you can go further. Don't stop until the whole project is not planned.
Use one tool at a time.
You must plan the work in sprints. Don't add tasks to backlog only.
Plan all tasks that must be completed to accomplush entire project.

Your team: {team}

Current Project Board:
{project_board}
"""

    class ProjectManagerState(MessagesState):
        remaining_steps: 1000
        project_board: Annotated[ProjectBoardType, merge_dicts_recursive]

    def __init__(self, llm, project_board_dir, team):
        load_dotenv()
        self.project_board_dir = project_board_dir
        self.pb = ProjectBoard(project_board_dir)
        self.graph = create_react_agent(
            get_model(llm),
            tools=tools,
            prompt=self.SYSTEM_PROMPT.format(
                project_board=json.dumps(self.pb.project_board), team=team
            ),
            state_schema=self.ProjectManagerState,
        )

    def invoke(self, *args, **kwargs):
        if "config" in kwargs:
            if "configurable" in kwargs["config"]:
                kwargs["config"]["configurable"][
                    "project_board_dir"
                ] = self.project_board_dir
            else:
                kwargs["config"]["configurable"] = {
                    "project_board_dir": self.project_board_dir
                }
        else:
            kwargs["config"] = {
                "configurable": {"project_board_dir": self.project_board_dir}
            }
        print(args[0])
        args[0]["project_board"] = self.pb.project_board
        output = self.graph.invoke(*args, **kwargs)
        pb = ProjectBoard(self.project_board_dir, output["project_board"])
        print("---->", pb.project_board)
        pb.save_project_board()
        return output


if __name__ == "__main__":
    project_manager = ProjectManager(
        "gpt-4o-mini",
        "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/project_board.json",
        "Coder, documenter, researcher.",
    )
    state = project_manager.invoke(
        {
            "messages": [
                (
                    "human",
                    "Create Pacman game in python.",
                )
            ]
        },
        config={
            "recursion_limit": 1000,
            "configurable": {
                "project_board_dir": "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/project_board.json"
            },
        },
    )
