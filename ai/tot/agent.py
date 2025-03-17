from langgraph.graph import MessagesState
from langchain_core.runnables import RunnableConfig
from typing import Literal
from typing_extensions import Annotated
from pydantic import BaseModel
from operator import add

from .config import Configuration, _ensure_configurable
from .schemas import ThoughtSchema
from .tree import ThoughtTree
from ai.prompts import thinker_prompt
from ai.abstract_agent import Agent


def create_goal(state: ToTState) -> ToTState:
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


def reasoning_node(state: ToTState) -> ToTState:
    if "tree" in state and state["tree"]:
        propositions = []
        for path in state["tree"].get_not_finished_paths():
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

        return {"propositions": propositions, "depth": 1}
    else:
        formatted_prompt = thinker_prompt.format(system_prompt=system_prompt)
        prompts = [
            [("system", formatted_prompt), state["messages"][-1]] for _ in range(5)
        ]

        thoughts = llm.with_structured_output(ThoughtSchema).batch(prompts)
        thoughts = [t.model_dump() for t in thoughts]

        return {"propositions": [thoughts], "depth": 0}


def build_tree(state: ToTState) -> ToTState:
    propositions = state.get("propositions", [[]])
    tree = state.get("tree", ThoughtTree(state["goal"]))
    for leaf, propositions_for_leaf in zip(tree.get_leaf_nodes(), propositions):
        for prop in propositions_for_leaf:
            tree.add_thought(leaf["thought"], prop["thought"], prop["finish"])
    return {"tree": tree, "depth": 0}


def score_and_prune(state: ToTState, config: RunnableConfig) -> ToTState:
    class Scores(BaseModel):
        score: int
        reason: str

    tree = state["tree"]
    config = _ensure_configurable(config)
    system_prompt = (
        "Your task is to critisize the plan for achieving given goal."
        "Assign points from 1 to 10."
    )
    prompts = []
    paths = tree.get_not_finished_paths()

    for path in paths:
        steps = "\n".join(
            [f"{n+1}. {thought['thought']}" for n, thought in enumerate(path)]
        )
        prompts.append(
            [
                ("system", system_prompt),
                (
                    "user",
                    "Goal: "
                    "{goal} \n"
                    "Plan:"
                    "{plan}".format(goal=state["goal"], plan=steps),
                ),
            ]
        )
    scores = llm.with_structured_output(Scores).batch(prompts)
    scores = [s.model_dump()["score"] for s in scores]

    paths_scores = list(zip(paths, scores))
    paths_scores_sorted = list(sorted(paths_scores, key=lambda x: x[-1], reverse=True))

    for path, score in paths_scores_sorted[: config.get("max_candidates")]:
        tree.set_score(path[-1]["thought"], score)

    for path, _ in paths_scores_sorted[config.get("max_candidates") :]:
        tree.remove_node(path[-1]["thought"])

    return {"tree": tree, "depth": 0}


def should_continue(
    state: ToTState, config: Configuration
) -> Literal["format_response", "reasoning_node"]:
    config = _ensure_configurable(config)
    if state["tree"].are_all_paths_finished() or state["depth"] >= config.get(
        "max_depth"
    ):
        return "format_response"
    return "reasoning_node"


def format_response(state: ToTState):
    return {
        "intermediate_steps": [
            t["thought"] for t in state["tree"].get_highest_scoring_path()[0]
        ]
    }


class ToTAgent(Agent):
    def __init__(self, llm, system_prompt, tools):
        super().__init__(llm, system_prompt, tools)

    class ToTState(MessagesState):
        tree: ThoughtTree
        propositions: list[ThoughtSchema]
        goal: str
        depth: Annotated[int, add]
        intermediate_steps: list[str]
