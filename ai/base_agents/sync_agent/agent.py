from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver
from ..agent import Agent
from .graph import llm_node, reason, should_continue, next_step, zero_state
from .state import SyncAgentState


class SyncAgent(Agent):
    def __init__(self, state, llm, system_prompt, tools, reasoning_graph=None):
        graph_builder = StateGraph(
            self.merge_typed_dicts(state.__name__, state, SyncAgentState)
        )
        graph_builder.add_node("llm_node", llm_node)
        graph_builder.add_node("reason", reason)
        graph_builder.add_node("next_step", next_step)
        graph_builder.add_node("zero_state", zero_state)
        graph_builder.add_node("tools", ToolNode(tools))

        graph_builder.add_edge(START, "reason")
        graph_builder.add_edge("reason", "next_step")
        graph_builder.add_edge("next_step", "llm_node")
        graph_builder.add_conditional_edges(
            "llm_node", should_continue, ["tools", "next_step", "zero_state"]
        )
        graph_builder.add_edge("tools", "llm_node")
        graph_builder.add_edge("zero_state", "__end__")

        # checkpointer = MemorySaver()

        self.graph = graph_builder.compile()
        super().__init__(
            system_prompt,
            llm,
            self.graph,
            tools,
            reasoning_graph,
            state=state,
            parent_state=SyncAgentState,
        )
