from .graph import llm_node, reason, should_continue
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from ..agent import Agent
from .state import LinearAgentState


class LinearAgent(Agent):
    def __init__(self, state, llm, system_prompt, tools, reasoning_graph=None):
        graph_builder = StateGraph(
            self.merge_typed_dicts(state.__name__, state, LinearAgentState)
        )
        graph_builder.add_node("llm_node", llm_node)
        graph_builder.add_node("reason", reason)
        graph_builder.add_node("tools", ToolNode(tools))

        graph_builder.add_edge(START, "reason")
        graph_builder.add_edge("reason", "llm_node")
        graph_builder.add_conditional_edges(
            "llm_node", should_continue, ["tools", "__end__"]
        )
        graph_builder.add_edge("tools", "llm_node")

        checkpointer = MemorySaver()

        graph = graph_builder.compile(checkpointer=checkpointer)
        super().__init__(
            system_prompt,
            llm,
            graph,
            tools,
            reasoning_graph,
            state=state,
            parent_state=LinearAgentState,
        )
