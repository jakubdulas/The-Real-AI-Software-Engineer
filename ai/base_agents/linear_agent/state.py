from langgraph.graph import MessagesState


class LinearAgentState(MessagesState):
    intermediate_steps: list[str]
