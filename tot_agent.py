from langchain_core.runnables import Runnable
from typing import TypedDict
from pydantic import BaseModel
from abstract_agent import Agent
from langchain_core.prompts import PromptTemplate
from langgraph.graph import MessagesState


class ThoughtsScores(BaseModel):
    thought: str
    score: int


class ThoughtsState(MessagesState):
    thoughts: list[str]


class ToTAgentState(MessagesState):
    thoughts: dict


class ReasoningAgentState(MessagesState):
    thought_list: list[str]


thinker_template = """
{{ system_prompt }}.

Before executing the task, think deeply about the next step to solve the task given by the user. Give a few ideas.
{% if steps %}
Already taken steps: 
{{ steps }}
{% endif %}
"""

thinker_prompt = PromptTemplate(
    template=thinker_template,
    input_variables=["system_prompt", "steps"],
    template_format="jinja2",
)


def reasoning_node(state: ThoughtsState):
    system_prompt = "Your system prompt here"
    formatted_prompt = thinker_prompt.format(system_prompt=system_prompt)


class ToTAgent(Agent):
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
