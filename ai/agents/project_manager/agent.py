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
from .project_board import ProjectBoard
from .types import ProjectBoardType
import json


class ProjectManagerState(MessagesState):
    remaining_steps: 1000
    project_board: ProjectBoardType


# TODO: Story points that will define how employees are overloaded with work. It will indicate if new spint is required.


class ProjectManager:
    SYSTEM_PROMPT = """
You are the best project manager. You will be given by the user what they want to achieve. Your task is to plan the project in the way that tasks are distributed well, 
they are well defined, detailed, not too general. remember to split big problem into small components. Plan the work into sptints. You will get set of tools that will 
help you to organize the work. Create sprint by sprint. When You finish the sprint then you can go further. Don't stop until the whole project is not planned.
Use one tool at a time.

Your team: {team}

Current Project Board:
{project_board}
"""

    def __init__(self, llm, project_board_dir, team):
        load_dotenv()
        self.pb = ProjectBoard(project_board_dir)
        print(self.pb.project_board)
        self.graph = create_react_agent(
            get_model(llm),
            tools=tools,
            prompt=self.SYSTEM_PROMPT.format(
                project_board=json.dumps(self.pb.project_board), team=team
            ),
            state_schema=ProjectManagerState,
        )

    def invoke(self, *args, **kwargs):
        args[0]["project_board"] = self.pb.project_board
        return self.graph.invoke(*args, **kwargs)


if __name__ == "__main__":
    project_manager = ProjectManager(
        "gpt-4o-mini",
        "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/project_board.json",
        "Software engineer, software architect, researcher, Tester.",
    )
    state = project_manager.invoke(
        {
            "messages": [
                (
                    "human",
                    "Create AI marketing platform in which I can generate marketing copy, generate images and publish all stuff to social media.",
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
    print(state["messages"][-1])
