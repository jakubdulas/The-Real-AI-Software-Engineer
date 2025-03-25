from langgraph.graph import MessagesState
from operator import add
from typing_extensions import Annotated


class CoderAgentState(MessagesState):
    current_dir: str
    intermediate_steps: list[str]
    current_step: Annotated[int, add]
