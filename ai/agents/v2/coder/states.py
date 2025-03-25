from langgraph.graph import MessagesState


class CoderAgentState(MessagesState):
    current_dir: str
    intermediate_steps: list[str]
    current_step: int
