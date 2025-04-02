from langgraph.graph import MessagesState


class SyncAgentState(MessagesState):
    intermediate_steps: list[str]
    current_step: int
