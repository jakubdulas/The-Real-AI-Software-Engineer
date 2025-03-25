from ai.agents.v2.sync_agent.agent import SyncAgent
from ai.tot.v2.graph import graph
from .prompts import coder_system_prompt
from .states import CoderAgentState
from .tools import tools

coder = SyncAgent(CoderAgentState, "gpt-4o-mini", coder_system_prompt, tools, graph)

if __name__ == "__main__":
    out = coder.invoke(
        {
            "messages": [
                (
                    "human",
                    "Create pacman game in Python using pygame. Use squares as characters.",
                )
            ]
        },
        config={"configurable": {"thread_id": 3, "recursion_limit": 50}},
    )
    print(out["messages"][-1].content)

    # with open("./output.png", "wb") as f:
    #     f.write(coder.graph.get_graph().draw_mermaid_png())
