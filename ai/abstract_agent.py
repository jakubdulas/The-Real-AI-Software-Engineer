from langchain_core.runnables import Runnable
from abc import ABC, abstractmethod


class Agent(ABC):
    def __init__(self, llm: Runnable, system_prompt: str, tools: list):
        self.llm = llm
        self.system_prompt = system_prompt
        self.tools = tools

    @abstractmethod
    def invoke(
        self,
    ):
        pass
