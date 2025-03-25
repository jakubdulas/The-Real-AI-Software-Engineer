from langchain_core.runnables import Runnable
from .graph import llm_node, reason, should_continue
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from ai.agents.v1.agent import Agent


class LinearAgent(Agent):
    def __init__(self, state_schema, llm, system_prompt, tools, reasoning_graph=None):
        coder_builder = StateGraph(state_schema)

        coder_builder.add_node("llm_node", llm_node)
        coder_builder.add_node("reason", reason)
        coder_builder.add_node("tools", ToolNode(tools))

        coder_builder.add_edge(START, "reason")
        coder_builder.add_edge("reason", "llm_node")
        coder_builder.add_conditional_edges(
            "llm_node", should_continue, ["tools", "__end__"]
        )
        coder_builder.add_edge("tools", "llm_node")

        checkpointer = MemorySaver()

        coder = coder_builder.compile(checkpointer=checkpointer)
        super().__init__(coder, llm, system_prompt, tools, reasoning_graph)
