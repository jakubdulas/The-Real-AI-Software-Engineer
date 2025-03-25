from langchain_core.runnables import Runnable


class Agent:
    def __init__(
        self,
        graph: Runnable,
        llm: str,
        system_prompt: str,
        tools: list | None = None,
        reasoning_graph: Runnable | None = None,
    ):
        self.graph = graph
        self.llm = llm
        self.system_prompt = system_prompt
        self.tools = tools
        self.reasoning_graph = reasoning_graph

    def invoke(self, *args, **kwargs):
        config = kwargs.pop("config", {})
        configurable = config.pop("configurable", {})
        configurable.update(
            {
                "system_prompt": self.system_prompt,
                "llm": self.llm,
                "tools": self.tools,
                "reasoning_graph": self.reasoning_graph,
            }
        )

        return self.graph.invoke(
            *args,
            **kwargs,
            config={"configurable": configurable, **config},
        )
