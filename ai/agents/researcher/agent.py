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


class Researcher:
    SYSTEM_PROMPT = "You are researcher. Your task is to collect all necesary data to achieve given goal. Always return very broad answer with all necessary details. The more you return the better."

    class ResearcherState(MessagesState):
        remaining_steps: list[str]

    def __init__(self, llm):
        load_dotenv()
        tavily_tool = TavilySearchResults(max_results=5)
        self.graph = create_react_agent(
            get_model(llm),
            tools=[tavily_tool],
            prompt=self.SYSTEM_PROMPT,
            state_schema=Researcher.ResearcherState,
        )

    def invoke(self, *args, **kwargs):
        return self.graph.invoke(*args, **kwargs)


if __name__ == "__main__":
    researcher = Researcher("gpt-4o-mini")
    state = researcher.invoke(
        {"messages": [("human", "How to make human in the loop in langgraph")]}
    )
    print(state["messages"][-1])
