from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from ai.agents.v2.agent import Agent
from .graph import llm_node, reason, should_continue, next_step


class SyncAgent(Agent):
    def __init__(self, state_schema, llm, system_prompt, tools, reasoning_graph=None):
        graph_builder = StateGraph(state_schema)

        graph_builder.add_node("llm_node", llm_node)
        graph_builder.add_node("reason", reason)
        graph_builder.add_node("next_step", next_step)
        graph_builder.add_node("tools", ToolNode(tools))

        graph_builder.add_edge(START, "reason")
        graph_builder.add_edge("reason", "next_step")
        graph_builder.add_edge("next_step", "llm_node")
        graph_builder.add_conditional_edges(
            "llm_node", should_continue, ["tools", "next_step", "__end__"]
        )
        graph_builder.add_edge("tools", "llm_node")

        checkpointer = MemorySaver()

        graph = graph_builder.compile(checkpointer=checkpointer)
        super().__init__(graph, llm, system_prompt, tools, reasoning_graph)
