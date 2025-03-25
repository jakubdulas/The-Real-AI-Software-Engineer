from langgraph.graph import MessagesState, START, END, StateGraph
from langchain_core.runnables import RunnableConfig
from typing import Literal
from typing_extensions import Annotated
from pydantic import BaseModel
from operator import add

from .prompts import thinker_prompt
from ai.utils import get_model

from .config import Configuration, _ensure_configurable
from .schemas import ThoughtSchema
from .tree import ThoughtTree


class ToTState(MessagesState):
    tree: dict
    propositions: list[ThoughtSchema]
    goal: str
    depth: Annotated[int, add]
    intermediate_steps: list[str]
    enhanced: bool


def create_goal(state: ToTState, config: Configuration) -> ToTState:
    llm = get_model(config.get("configurable", {}).get("llm"))
    output = llm.invoke(
        [
            (
                "system",
                "State the goal of the user. In one short sentece. Tell what is the user intention.",
            ),
            state["messages"][-1],
        ]
    ).content
    return {"goal": output}


def reasoning_node(state: ToTState, config: Configuration) -> ToTState:
    llm = get_model(config.get("configurable", {}).get("llm"))
    system_prompt = config.get("configurable", {}).get("system_prompt")

    if "tree" in state and state["tree"]:
        propositions = []
        for path in ThoughtTree.from_dict(state.get("tree")).get_not_finished_paths():
            formatted_prompt = thinker_prompt.format(
                system_prompt=system_prompt,
                steps="\n".join(
                    [f"{n+1}. {thought['thought']}" for n, thought in enumerate(path)]
                ),
            )
            prompts = [
                [("system", formatted_prompt), state["messages"][-1]] for _ in range(5)
            ]
            thoughts = llm.with_structured_output(ThoughtSchema).batch(prompts)
            thoughts = [t.model_dump() for t in thoughts]
            propositions.append(thoughts)

        return {"propositions": propositions, "depth": 1, "enhanced": False}
    else:
        formatted_prompt = thinker_prompt.format(system_prompt=system_prompt)
        prompts = [
            [("system", formatted_prompt), state["messages"][-1]] for _ in range(5)
        ]

        thoughts = llm.with_structured_output(ThoughtSchema).batch(prompts)
        thoughts = [t.model_dump() for t in thoughts]

        return {"propositions": [thoughts], "depth": 0, "enhanced": False}


def build_tree(state: ToTState) -> ToTState:
    propositions = state.get("propositions", [[]])
    if "tree" in state:
        tree = ThoughtTree.from_dict(state.get("tree"))
    else:
        tree = ThoughtTree(state["goal"])

    for leaf, propositions_for_leaf in zip(tree.get_leaf_nodes(), propositions):
        for prop in propositions_for_leaf:
            tree.add_thought(leaf["thought"], prop["thought"], prop["finish"])
    return {"tree": tree.to_dict(), "depth": 0}


def score_and_prune(state: ToTState, config: RunnableConfig) -> ToTState:
    llm = get_model(config.get("configurable", {}).get("llm"))

    class Scores(BaseModel):
        score: int
        reason: str

    tree = ThoughtTree.from_dict(state.get("tree"))
    config = _ensure_configurable(config)
    system_prompt = (
        "You will be given part of a plan of how to achieve given goal."
        "Your task is to critisize the most recent step."
        "It might be also the first step."
        "Assign points from 1 to 10 to the last step taking into account whole plane."
    )
    prompts = []
    paths = tree.get_not_finished_paths()

    for path in paths:
        steps = "\n".join(
            [f"{n+1}. {thought['thought']}" for n, thought in enumerate(path[1:])]
        )
        prompts.append(
            [
                ("system", system_prompt),
                (
                    "user",
                    "Goal: "
                    "{goal} \n"
                    "Plan:\n"
                    "{plan}".format(goal=state["goal"], plan=steps),
                ),
            ]
        )
    scores = llm.with_structured_output(Scores).batch(prompts)
    scores = [s.model_dump() for s in scores]

    paths_scores = list(zip(paths, scores))
    paths_scores_sorted = list(
        sorted(paths_scores, key=lambda x: x[-1]["score"], reverse=True)
    )

    for path, score_reason in paths_scores_sorted[: config.get("max_candidates")]:
        tree.set_score(path[-1]["thought"], score_reason["score"])
        tree.set_score_reason(path[-1]["thought"], score_reason["reason"])

    for path, _ in paths_scores_sorted[config.get("max_candidates") :]:
        tree.remove_node(path[-1]["thought"])

    return {
        "tree": tree.to_dict(),
        "depth": 0,
        "enhanced": state.get("enhanced", False),
    }


def enhance_thoughts(state: ToTState, config: RunnableConfig):
    llm = get_model(config.get("configurable", {}).get("llm"))
    tree = ThoughtTree.from_dict(state.get("tree"))

    system_prompt = (
        "You will be given part of a plan of how to achieve given goal."
        "Your task is to improve the last step based on the feedback."
    )
    prompts = []
    paths = tree.get_not_finished_paths()

    class ImprovedThought(BaseModel):
        improved_thought: str

    for path in paths:
        steps = "\n".join(
            [f"{n+1}. {thought['thought']}" for n, thought in enumerate(path[1:])]
        )
        prompts.append(
            [
                ("system", system_prompt),
                (
                    "user",
                    "Goal: "
                    "{goal} \n"
                    "Plan: "
                    "{plan}\n"
                    "Feedback: "
                    "{feedback}".format(
                        goal=state["goal"],
                        plan=steps,
                        feedback=path[-1]["score_reason"],
                    ),
                ),
            ]
        )

    improved_thoughts = llm.with_structured_output(ImprovedThought).batch(prompts)
    for path, improved_thought in zip(paths, improved_thoughts):
        tree.change_thought(path[-1]["thought"], improved_thought.improved_thought)

    return {"tree": tree.to_dict(), "enhanced": True}


def format_response(state: ToTState):
    return {
        "intermediate_steps": [
            t["thought"]
            for t in ThoughtTree.from_dict(state["tree"]).get_highest_scoring_path()[0]
        ][1:]
    }


def should_continue(
    state: ToTState, config: Configuration
) -> Literal["format_response", "reasoning_node", "enhance_thoughts"]:
    config = _ensure_configurable(config)
    enhanced = state.get("enhanced", False)

    if not enhanced:
        return "enhance_thoughts"

    if ThoughtTree.from_dict(state["tree"]).are_all_paths_finished() or state[
        "depth"
    ] >= config.get("max_depth"):
        return "format_response"
    return "reasoning_node"


graph_builder = StateGraph(ToTState, config_schema=Configuration)

graph_builder.add_node("create_goal", create_goal)
graph_builder.add_node("reasoning_node", reasoning_node)
graph_builder.add_node("build_tree", build_tree)
graph_builder.add_node("score_and_prune", score_and_prune)
graph_builder.add_node("enhance_thoughts", enhance_thoughts)
graph_builder.add_node("format_response", format_response)

graph_builder.add_edge(START, "create_goal")
graph_builder.add_edge("create_goal", "reasoning_node")
graph_builder.add_edge("reasoning_node", "build_tree")
graph_builder.add_edge("build_tree", "score_and_prune")
graph_builder.add_conditional_edges(
    "score_and_prune",
    should_continue,
    ["format_response", "reasoning_node", "enhance_thoughts"],
)
graph_builder.add_edge("enhance_thoughts", "score_and_prune")
graph_builder.add_edge("format_response", END)

graph = graph_builder.compile()


if __name__ == "__main__":
    graph.invoke(
        {"messages": [("human", "Create pacman game")]},
        config={"configurable": {"llm": "gpt-4o-mini"}},
    )

    # with open("output.png", "wb") as f:
    #     f.write(graph.get_graph().draw_mermaid_png())
