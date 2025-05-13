# from langgraph.prebuilt import create_react_agent
# from ai.utils import get_model

# from typing import Annotated

# from langchain_community.tools.tavily_search import TavilySearchResults
# from langchain_core.tools import tool

# from typing import Literal
# from typing_extensions import TypedDict

# from langchain_openai import ChatOpenAI
# from langgraph.graph import MessagesState, END
# from langgraph.types import Command
# from langchain_core.runnables import RunnableConfig

# from ai.base_agents.agent import Agent
# from langchain_core.messages import HumanMessage
# from langgraph.graph import StateGraph, START, END

# from ai.base_agents.agent import Agent
# from ai.tot.v1.utils import get_model
# from dotenv import load_dotenv
# from .tools import tools
# from .project_board import ProjectBoard
# from .types import ProjectBoardType
# from .graph import pm_graph as graph
# import json


# class ProjectManagerState(MessagesState):
#     remaining_steps: 1000
#     project_board: Annotated[ProjectBoardType, merge_dicts_recursive]


# pm_graph = create_react_agent(
#     get_model(llm),
#     tools=tools,
#     prompt=SYSTEM_PROMPT.format(project_board=json.dumps(pb.project_board), team=team),
#     state_schema=self.ProjectManagerState,
# )
