from ai.agents.coder.agent import Coder
from ai.agents.documenter.agent import Documenter
from ai.agents.project_manager.agent import ProjectManager
from ai.agents.researcher.agent import Researcher
from operator import add
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver


def create_system(code_dir, model="gpt-4o-mini"):
    team = """
    Coder - able to create files, write files with code and run it. This agent can only write code. It can't create images. Only Code. Python Code.
    Reseracher - able to use internet to make research. Can only browse internet and return search results.
    Documenter - able to create code documentation. It can create files and write docs based on the code that has been written. Should be used only at the and of the project to document the code."""

    project_board_dir = code_dir + "/.project/project_board.json"
    docs_dir = code_dir + "/.project/docs"

    pm = ProjectManager(model, project_board_dir, team)
    coder = Coder(code_dir, model)
    documenter = Documenter(model, code_dir, docs_dir)
    researcher = Researcher(model)

    class InputSystemState(TypedDict):
        project_scope: str

    class SystemState(InputSystemState):
        pm_messages: Annotated[list, add]
        coder_messages: Annotated[list, add]
        documenter_messages: Annotated[list, add]
        researcher_messages: Annotated[list, add]

        project_board: dict
        current_sprint: int

    def plan_project(state):
        output = pm.invoke(
            {"messages": ("human", state.get("project_scope"))},
        )
        return {
            "pm_messages": [
                ("human", state.get("project_scope")),
                output["messages"][-1],
            ],
            "project_board": output["project_board"],
        }

    def start_sprint(state):
        current_sprint = state.get("current_sprint", -1) + 1
        return {"current_sprint": current_sprint}

    def should_start_sprint(state):
        sprints = state.get("project_board").get("sprints")
        current_sprint = state.get("current_sprint", -1) + 1

        if len(sprints) <= current_sprint:
            return "__end__"
        return "start_sprint"

    def complete_tasks(state):
        print(state.get("current_sprint"))
        current_sprint_data = list(state.get("project_board")["sprints"].values())[
            state.get("current_sprint")
        ]

        coder_msgs = state.get("coder_messages", [])
        new_coder_msgs = []
        documenter_msgs = state.get("documenter_messages", [])
        new_documenter_msgs = []
        researcher_msgs = state.get("researcher_messages", [])
        new_researcher_msgs = []
        researches = []

        print(f"complete_tasks - tasks: {current_sprint_data["tasks"]}")

        for task in current_sprint_data["tasks"]:
            task_messages = [
                (
                    "human",
                    state["project_scope"],
                ),
                (
                    "human",
                    f"You are working on sprint which goal is: {current_sprint_data['goal']}",
                ),
                (
                    "human",
                    f"Complete the given task and only this task: {task['task_name']} - {task['task_description']}",
                ),
            ]

            print(task["assignee"], "-", task["task_name"])
            if task["assignee"] == "Coder":
                new_coder_msgs.extend(task_messages)
                print(coder_msgs)
                output = coder.invoke(
                    {"messages": coder_msgs + new_coder_msgs},
                    config={"configurable": {"working_dir": code_dir}},
                )
                new_coder_msgs.append(output["messages"][-1])

            elif task["assignee"] == "Documenter":
                new_documenter_msgs.extend(task_messages)
                output = documenter.invoke(
                    {"messages": documenter_msgs + new_documenter_msgs},
                    config={
                        "configurable": {
                            "working_dir": code_dir,
                            "documentation_dir": docs_dir,
                        }
                    },
                )
                new_documenter_msgs.append(output["messages"][-1])

            elif task["assignee"] == "Researcher":
                new_researcher_msgs.extend(task_messages)
                output = researcher.invoke(
                    {"messages": researcher_msgs + new_researcher_msgs}
                )
                new_researcher_msgs.append(output["messages"][-1])
                new_coder_msgs.append(
                    ("ai", f"Research results: {output["messages"][-1].content}")
                )
                new_documenter_msgs.append(
                    ("ai", f"Research results: {output["messages"][-1].content}")
                )

            else:
                raise ValueError(f"there is no agent called: {task["assignee"]}")

        return {
            "coder_messages": new_coder_msgs,
            "documenter_messages": new_documenter_msgs,
            "researcher_messages": new_documenter_msgs,
        }

    graph_builder = StateGraph(SystemState, input=InputSystemState)
    graph_builder.add_node("plan_project", plan_project)
    graph_builder.add_node("start_sprint", start_sprint)
    graph_builder.add_node("complete_tasks", complete_tasks)

    graph_builder.add_edge(START, "plan_project")
    graph_builder.add_conditional_edges(
        "plan_project", should_start_sprint, ["start_sprint", "__end__"]
    )
    graph_builder.add_edge("start_sprint", "complete_tasks")
    graph_builder.add_conditional_edges(
        "complete_tasks", should_start_sprint, ["start_sprint", "__end__"]
    )

    return graph_builder.compile()


if __name__ == "__main__":
    # with open("./system_graph.png", "wb") as f:
    #     f.write(system.get_graph().draw_mermaid_png())

    output = create_system().invoke(
        {
            "project_scope": "Create django project for web app. THis app is about todo list connected with tracking the workouts and managing time."
        },
        config={"recursion_limit": 300, "configurable": {"thread_id": 3}},
    )
