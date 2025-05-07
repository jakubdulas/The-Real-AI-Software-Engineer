from ai.base_agents.sync_agent.agent import SyncAgent
from ai.base_agents.linear_agent.agent import LinearAgent
from ai.tot.v1.graph import graph as tot_graph_v1
from ai.tot.v2.graph import graph as tot_graph_v2
from ai.cot.graph import cot_graph
from typing import TypedDict, Annotated
from .prompts import coder_system_prompt
from .tools import tools
from operator import or_
from .utils import create_directory_tree


class CoderAgentState(TypedDict):
    project_tree: Annotated[dict, or_]


class Coder(SyncAgent):
    def __init__(self, working_dir, llm="gpt-4o", reasoning_graph=cot_graph):
        print("RESONING GRAPH", reasoning_graph)
        super().__init__(
            CoderAgentState, llm, coder_system_prompt, tools, reasoning_graph
        )
        self.working_dir = working_dir

    def invoke(self, *args, **kwargs):
        args[0]["project_tree"] = create_directory_tree(self.working_dir)
        if "config" in kwargs:
            if "configurable" in kwargs["config"]:
                kwargs["config"]["configurable"]["working_dir"] = self.working_dir
        return super().invoke(*args, **kwargs)


if __name__ == "__main__":
    out = Coder(
        "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/codes"
    ).invoke(
        {
            "messages": [
                (
                    "human",
                    "Create simple gogin server. I want to use graphql.",
                )
            ]
        },
        config={"configurable": {"thread_id": 3}, "recursion_limit": 100},
    )
    print(out["messages"][-1].content)

    # coder

    # with open("./output.png", "wb") as f:
    #     f.write(coder.graph.get_graph(xray=True).draw_mermaid_png())
