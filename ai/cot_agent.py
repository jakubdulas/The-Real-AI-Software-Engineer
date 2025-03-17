from langchain_core.runnables import Runnable
from typing import TypedDict
from pydantic import BaseModel
from ai.abstract_agent import Agent
from langchain_core.prompts import PromptTemplate
from langgraph.graph import MessagesState


class CoTAgent(Agent):
    def __init__(self, llm: Runnable, system_prompt: str):
        self.llm = llm
        self.system_prompt = system_prompt

    def invoke(self):
        # self.llm.invoke([
        #     ("system", "")
        # ])
        pass


if __name__ == "__main__":
    system_prompt = "Your system prompt here"
    steps = "Step 1: Analyze the requirements.\nStep 2: Design the solution."

    formatted_prompt = thinker_prompt.format(system_prompt=system_prompt)
    print(formatted_prompt)
