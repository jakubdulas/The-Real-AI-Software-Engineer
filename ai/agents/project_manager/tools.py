from langchain_core.tools import tool, InjectedToolCallId
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableConfig
from langgraph.prebuilt import ToolNode
from typing import Annotated, Optional, Literal
from langgraph.types import Command
import os
from langgraph.prebuilt import InjectedState
from .project_board import ProjectBoard


@tool
def create_ticket(
    task_name: str,
    task_description: str,
    assignee: Literal["Coder", "Documenter", "Researcher"],
    config: RunnableConfig,
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
    # sprint_name: Optional[str] = None,
    sprint_name: str,
):
    "Creates ticket for task. Once created you will get ticket id. If sprint_name is not provided, then the task will be added to the backlog."
    project_board_dir = config.get("configurable").get("project_board_dir")
    pb = state.get("project_board")
    pb = ProjectBoard(project_board_dir, pb)
    ticket_id = pb.add_ticket(
        {
            "assignee": assignee,
            "task_description": task_description,
            "task_name": task_name,
        },
        sprint_name,
    )
    return Command(
        update={
            "project_board": pb.project_board,
            "messages": [
                ToolMessage(f"Done. Ticker id: {ticket_id}", tool_call_id=tool_call_id)
            ],
        }
    )


@tool
def create_sprint(
    sprint_goal: str,
    config: RunnableConfig,
    tool_call_id: Annotated[str, InjectedToolCallId],
    state: Annotated[dict, InjectedState],
):
    "Creates sprint"
    project_board_dir = config.get("configurable").get("project_board_dir")
    pb = state.get("project_board")
    pb = ProjectBoard(project_board_dir, pb)

    sprint_name = pb.add_sprint(sprint_goal)
    return Command(
        update={
            "project_board": pb.project_board,
            "messages": [
                ToolMessage(
                    f"Done. Created sprint with name: {sprint_name}",
                    tool_call_id=tool_call_id,
                )
            ],
        }
    )


@tool
def edit_sprint(
    sprint_name: str,
    sprint_goal: str,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
    state: Annotated[dict, InjectedState],
):
    "Edits sprint"
    project_board_dir = config.get("configurable").get("project_board_dir")
    pb = state.get("project_board")
    pb = ProjectBoard(project_board_dir, pb)

    pb.edit_sprint(sprint_name, sprint_goal)
    return Command(
        update={
            "project_board": pb.project_board,
            "messages": [ToolMessage("Done", tool_call_id=tool_call_id)],
        }
    )


@tool
def edit_ticket(
    ticket_id: int,
    tool_call_id: Annotated[str, InjectedToolCallId],
    config: RunnableConfig,
    state: Annotated[dict, InjectedState],
    task_name: Optional[str] = None,
    task_description: Optional[str] = None,
    assignee: Optional[Literal["Coder", "Documenter", "Researcher"]] = None,
):
    "Edits ticket"
    project_board_dir = config.get("configurable").get("project_board_dir")
    pb = state.get("project_board")
    pb = ProjectBoard(project_board_dir, pb)

    if assignee:
        pb.edit_ticket(ticket_id, {"assignee": assignee})
    if task_name:
        pb.edit_ticket(ticket_id, {"task_name": task_name})
    if task_description:
        pb.edit_ticket(ticket_id, {"task_description": task_description})
    return Command(
        update={
            "project_board": pb.project_board,
            "messages": [ToolMessage("Done", tool_call_id=tool_call_id)],
        }
    )


@tool
def remove_sprint(
    sprint_name: str,
    config: RunnableConfig,
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
):
    "Removes sprint"
    project_board_dir = config.get("configurable").get("project_board_dir")
    pb = state.get("project_board")
    pb = ProjectBoard(project_board_dir, pb)

    pb.remove_sprint(sprint_name)
    return Command(
        update={
            "project_board": pb.project_board,
            "messages": [ToolMessage("Done", tool_call_id=tool_call_id)],
        }
    )


@tool
def remove_ticket(
    ticket_id: int,
    config: RunnableConfig,
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
):
    "Removes ticket"

    project_board_dir = config.get("configurable").get("project_board_dir")
    pb = state.get("project_board")
    pb = ProjectBoard(project_board_dir, pb)

    pb.remove_ticket(ticket_id)
    return Command(
        update={
            "project_board": pb.project_board,
            "messages": [ToolMessage("Done", tool_call_id=tool_call_id)],
        }
    )


@tool
def move_ticket_to_backlog(
    ticket_id: int,
    config: RunnableConfig,
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
):
    "Moves ticket to the backlog"
    project_board_dir = config.get("configurable").get("project_board_dir")
    pb = state.get("project_board")
    pb = ProjectBoard(project_board_dir, pb)

    pb.move_ticket_to_backlog(ticket_id)
    return Command(
        update={
            "project_board": pb.project_board,
            "messages": [ToolMessage("Done", tool_call_id=tool_call_id)],
        }
    )


@tool
def move_ticket_to_sprint(
    ticket_id: int,
    sprint_name: str,
    config: RunnableConfig,
    state: Annotated[dict, InjectedState],
    tool_call_id: Annotated[str, InjectedToolCallId],
):
    "Moves ticket to the sprint"
    project_board_dir = config.get("configurable").get("project_board_dir")
    pb = state.get("project_board")
    pb = ProjectBoard(project_board_dir)

    pb.move_ticket_to_sprint(ticket_id, sprint_name)
    return Command(
        update={
            "project_board": pb.project_board,
            "messages": [ToolMessage("Done", tool_call_id=tool_call_id)],
        }
    )


# @tool
# def ask_about_project_progress(
#     config: RunnableConfig,
# ):
#     'Asks "Hows the project guys"'
#     pass


tools = [
    create_sprint,
    create_ticket,
    edit_sprint,
    edit_ticket,
    remove_ticket,
    remove_sprint,
    # move_ticket_to_backlog,
    # move_ticket_to_sprint,
]
