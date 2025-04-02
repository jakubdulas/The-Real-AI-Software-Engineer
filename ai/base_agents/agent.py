from langchain_core.runnables import Runnable
from typing import TypedDict, Type


class Agent:
    PROMPT = """{system_prompt}\n\nCurrent state: {{state}}"""

    def __init__(
        self,
        system_prompt: str,
        llm: str,
        graph: Runnable,
        tools: list | None = None,
        reasoning_graph: Runnable | None = None,
        state: dict | None = TypedDict,
        parent_state: dict | None = TypedDict,
    ):
        self.graph = graph
        self.llm = llm
        self.system_prompt = system_prompt
        self.tools = tools
        self.reasoning_graph = reasoning_graph
        self.state = state
        self.parent_state = parent_state

    def invoke(self, *args, **kwargs):
        config = kwargs.pop("config", {})
        configurable = config.pop("configurable", {})
        agent_state_variables = self.state.__annotations__.keys()

        configurable.update(
            {
                "system_prompt": self.PROMPT.format(system_prompt=self.system_prompt),
                "llm": self.llm,
                "tools": self.tools,
                "reasoning_graph": self.reasoning_graph,
                "agent_state_variables": agent_state_variables,
            }
        )

        return self.graph.invoke(
            *args, **kwargs, config={"configurable": configurable, **config}
        )

    def merge_typed_dicts(self, name: str, *dicts: dict) -> dict:
        merged_annotations = {}
        for d in dicts:
            merged_annotations.update(d.__annotations__)
        return TypedDict(name, merged_annotations)
