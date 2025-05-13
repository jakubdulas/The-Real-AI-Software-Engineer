from .types import ProjectBoardType, Ticket, NewTicket
import json
import os


class ProjectBoard:
    def __init__(
        self, project_board_dir: str, project_board: ProjectBoardType | None = None
    ):
        self.project_board_dir = project_board_dir
        self.project_board: ProjectBoardType = project_board
        if not self.project_board:
            if not os.path.exists(project_board_dir):
                self.init_project_board()
            else:
                self.read_project_board()

    def init_project_board(self) -> ProjectBoardType:
        project_board = {"sprints": {}, "backlog": [], "metadata": {"num_tasks": 0}}
        # self.save_project_board(project_board)
        self.project_board = project_board

    def read_project_board(self) -> ProjectBoardType:
        print("READ")
        with open(self.project_board_dir, "r") as f:
            self.project_board = json.load(f)
        return self.project_board

    def save_project_board(self, board=None) -> ProjectBoardType:
        if board:
            self.project_board = board
        with open(self.project_board_dir, "w+") as f:
            f.write(json.dumps(self.project_board, indent=2))
        return self.project_board

    def add_ticket(self, ticket_data: NewTicket, sprint_name: str | None = None):
        if sprint_name not in self.project_board["sprints"] and sprint_name is not None:
            raise Exception("Sprint with given name does not exist")

        self.project_board["metadata"]["num_tasks"] += 1
        ticket_id = self.project_board["metadata"]["num_tasks"]
        ticket = Ticket(**ticket_data, id=ticket_id, done=False)

        if sprint_name is None:
            self.project_board["backlog"].append(ticket)
        else:
            self.project_board["sprints"][sprint_name]["tasks"].append(ticket)
        # self.save_project_board()
        return ticket_id

    def add_sprint(self, sprint_goal: str):
        sprint_name = f"Sprint {len(self.project_board['sprints'])+1}"
        self.project_board["sprints"][sprint_name] = {"goal": sprint_goal, "tasks": []}
        return sprint_name
        # self.save_project_board()

    def edit_ticket(self, ticket_id: int, updated_data: NewTicket):
        def update_ticket(ticket: Ticket) -> Ticket:
            ticket.update(updated_data)
            return ticket

        for i, ticket in enumerate(self.project_board["backlog"]):
            if ticket["id"] == ticket_id:
                self.project_board["backlog"][i] = update_ticket(ticket)
                # self.save_project_board()
                return

        for sprint in self.project_board["sprints"].values():
            for i, ticket in enumerate(sprint["tasks"]):
                if ticket["id"] == ticket_id:
                    sprint["tasks"][i] = update_ticket(ticket)
                    # self.save_project_board()
                    return

        raise Exception("Ticket not found")

    def remove_ticket(self, ticket_id: int):
        self.project_board["backlog"] = [
            t for t in self.project_board["backlog"] if t["id"] != ticket_id
        ]

        for sprint in self.project_board["sprints"].values():
            sprint["tasks"] = [t for t in sprint["tasks"] if t["id"] != ticket_id]

        # self.save_project_board()

    def remove_sprint(self, sprint_name: str):
        if sprint_name not in self.project_board["sprints"]:
            raise Exception("Sprint not found")

        del self.project_board["sprints"][sprint_name]
        # self.save_project_board()

    def edit_sprint(self, sprint_name: str, new_goal: str):
        if sprint_name not in self.project_board["sprints"]:
            raise Exception("Sprint not found")

        self.project_board["sprints"][sprint_name]["goal"] = new_goal
        # self.save_project_board()

    def move_ticket_to_backlog(self, ticket_id: int):
        for sprint in self.project_board["sprints"].values():
            for i, ticket in enumerate(sprint["tasks"]):
                if ticket["id"] == ticket_id:
                    self.project_board["backlog"].append(ticket)
                    del sprint["tasks"][i]
                    # self.save_project_board()
                    return
        raise Exception("Ticket not found in any sprint")

    def move_ticket_to_sprint(self, ticket_id: int, sprint_name: str):
        if sprint_name not in self.project_board["sprints"]:
            raise Exception("Sprint not found")

        for i, ticket in enumerate(self.project_board["backlog"]):
            if ticket["id"] == ticket_id:
                self.project_board["sprints"][sprint_name]["tasks"].append(ticket)
                del self.project_board["backlog"][i]
                # self.save_project_board()
                return

        for sprint in self.project_board["sprints"].values():
            for i, ticket in enumerate(sprint["tasks"]):
                if ticket["id"] == ticket_id:
                    self.project_board["sprints"][sprint_name]["tasks"].append(ticket)
                    del sprint["tasks"][i]
                    # self.save_project_board()
                    return

        raise Exception("Ticket not found in backlog or sprints")

    def mark_ticket_as_done(self, ticket_id: int):
        for ticket in self.project_board["backlog"]:
            if ticket["id"] == ticket_id:
                ticket["done"] = True
                # self.save_project_board()
                return

        for sprint in self.project_board["sprints"].values():
            for ticket in sprint["tasks"]:
                if ticket["id"] == ticket_id:
                    ticket["done"] = True
                    # self.save_project_board()
                    return

        raise Exception("Ticket not found")


if __name__ == "__main__":
    pb = ProjectBoard(
        "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/project_board.json"
    )
    ticket_id1 = pb.add_ticket(
        {"assignee": "test", "task_description": "sth", "task_name": "SRG"}
    )
    pb.add_sprint("Super cool")
    ticket_id2 = pb.add_ticket(
        {"assignee": "test 2", "task_description": "sth 2", "task_name": "SRG 2"},
        "Sprint 1",
    )
    pb.edit_sprint("Sprint 1", "Super cool goal")
    pb.edit_ticket(ticket_id1, {"assignee": "New assignee"})
    pb.move_ticket_to_sprint(ticket_id1, "Sprint 1")
    pb.move_ticket_to_backlog(ticket_id2)
    pb.mark_ticket_as_done(ticket_id1)
