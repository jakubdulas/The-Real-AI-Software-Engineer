from ai.agents.coder.agent import Coder
from ai.agents.documenter.agent import Documenter
from ai.agents.project_manager.agent import ProjectManager
from ai.agents.researcher.agent import Researcher
from operator import add
from typing import TypedDict, Annotated


# coder = -

pm = ProjectManager(
    "gpt-4o-mini", "./project_board.json", "Coder, Researcher, Documenter"
)


class SystemState(TypedDict):
    pm_messages = Annotated[list, add]
    coder_messages = Annotated[list, add]
    documenter_messages = Annotated[list, add]
    researcher_messages = Annotated[list, add]


# def plan_project(state):
