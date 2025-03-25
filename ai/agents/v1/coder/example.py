from ai.agents.v1.linear_agent import LinearAgent
from .prompts import coder_system_prompt
from .states import CoderAgentState
from .tools import tools
from ai.tot.v1.graph import graph

coder = LinearAgent(CoderAgentState, "gpt-4o-mini", coder_system_prompt, tools, graph)

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
