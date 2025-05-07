from typing import Literal
from typing_extensions import TypedDict

from langgraph.graph import MessagesState, END
from langgraph.types import Command
from langchain_core.runnables import RunnableConfig

from ai.base_agents.agent import Agent
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from ai.tot.v1.utils import get_model
from dotenv import load_dotenv
from ai.agents.project_manager.project_board import ProjectBoard

load_dotenv()


class MultiAgentSystem(Agent):
    SUPERVISOR_SYSTEM_PROMPT = (
        "You are a supervisor tasked with managing a conversation between the"
        " following workers: {members}. Given the following user request,"
        " respond with the worker to act next. Each worker will perform a"
        " task and respond with their results and status. When finished,"
        " respond with FINISH."
    )

    class State(MessagesState):
        next: str

    def __init__(self, project_board_dir):
        super().__init__(self.SUPERVISOR_SYSTEM_PROMPT, "gpt-4o-mini", None, None)
        self.members = []
        self.members_descriptions = {}
        self.names_node_state_schema = {}
        self.project_board_dir = project_board_dir

    def add_agent(self, name, graph, state_schema, agent_role):
        self.members.append(name)
        self.members_descriptions[name] = agent_role

        def node(state, config: RunnableConfig) -> Command[Literal["supervisor"]]:
            print(f"---- {name} ----")
            for msg in state.get("messages"):
                if isinstance(msg, HumanMessage):
                    print("Human:", msg.content)
                else:
                    print("AI:", msg.content)
            result = graph.invoke(state, config=config)
            return Command(
                update={
                    "messages": [
                        HumanMessage(content=result["messages"][-1].content, name=name),
                        HumanMessage(
                            content="Project board: "
                            + str(ProjectBoard(self.project_board_dir).project_board),
                            name=name,
                        ),
                    ]
                },
                goto="supervisor",
            )

        self.names_node_state_schema[name] = {
            "node": node,
            "state_schema": state_schema,
        }

    def build(self):
        options = self.members + ["FINISH"]

        def supervisor_node(
            state, config: RunnableConfig
        ) -> Command[Literal[*self.members, "__end__"]]:
            llm = get_model(config.get("configurable").get("llm"))
            system_prompt = config.get("configurable").get("system_prompt")
            system_prompt = self.SUPERVISOR_SYSTEM_PROMPT.format(
                members="\n".join(
                    f"{mem_name} - {task}"
                    for mem_name, task in self.members_descriptions.items()
                )
            )

            class Router(TypedDict):
                """Worker to route to next. If no workers needed, route to FINISH."""

                next: Literal[*options]

            messages = [("system", system_prompt)] + state["messages"]

            response = llm.with_structured_output(Router).invoke(messages)
            goto = response["next"]
            if goto == "FINISH":
                goto = END

            return Command(goto=goto, update={"next": goto})

        State = self.State
        for agent_obj in self.names_node_state_schema.values():
            State = self.merge_typed_dicts("State", State, agent_obj["state_schema"])

        self.state = State
        builder = StateGraph(State)
        builder.add_node("supervisor", supervisor_node)

        for agent_name, agent_obj in self.names_node_state_schema.items():
            builder.add_node(agent_name, agent_obj["node"])

        builder.add_edge(START, "supervisor")
        self.graph = builder.compile()


if __name__ == "__main__":
    system = MultiAgentSystem(
        "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/project_board.json"
    )
    from ai.agents.coder.agent import Coder
    from ai.agents.researcher.agent import Researcher
    from ai.agents.project_manager.agent import ProjectManager
    from ai.agents.documenter.agent import Documenter

    coder = Coder(
        "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/codes",
        "gpt-4o-mini",
    )
    system.add_agent("coder", coder, coder.state, "THis agent codes.")
    system.add_agent(
        "researcher",
        Researcher("gpt-4o-mini"),
        Researcher.ResearcherState,
        "This agent makes research.",
    )
    system.add_agent(
        "project_manager",
        ProjectManager(
            "gpt-4o-mini",
            "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/project_board.json",
            "coder, researcher, documenter",
        ),
        ProjectManager.ProjectManagerState,
        "This agent plans the work. It should be first agent to call because it coordinates the work.",
    )
    system.add_agent(
        "documenter",
        Documenter(
            "gpt-4o-mini",
            "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/codes",
            "/Users/jakubdulas/Documents/UPV/The-Real-AI-Software-Engineer/codes_docs",
        ),
        Documenter.DocumenterState,
        "This agent documents the code.",
    )
    system.build()
    # from langchain_core.runnables.graph import MermaidDrawMethod

    # with open("graph.png", "wb") as f:

    # f.write(
    #     system.graph.get_graph(xray=1).draw_mermaid_png(
    #         draw_method=MermaidDrawMethod.PYPPETEER,
    #     )
    # )
    system.invoke(
        {"messages": "Create pacman game in python"}, config={"recursion_limit": 100}
    )
