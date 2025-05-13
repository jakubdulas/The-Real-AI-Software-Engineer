from typing import TypedDict, Literal


class NewTicket(TypedDict):
    task_name: str
    task_description: str
    assignee: Literal["Coder", "Documenter", "Researcher"]


class Ticket(NewTicket):
    id: int
    done: bool


class Sprint(TypedDict):
    goal: str
    tasks: list[Ticket]


class Metadata(TypedDict):
    num_tasks: int = 0
    ...


class ProjectBoardType(TypedDict):
    sprints: dict[str, Sprint]
    backlog: list[Ticket]
    metadata: Metadata


if __name__ == "__main__":
    board = ProjectBoardType(
        sprints=[Ticket(task_description="ABCX", task_name="avx", assignee="I")]
    )
    print(board)
