from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.prompts import PromptTemplate
from langgraph.graph import MessagesState, START, END
from langgraph.graph import StateGraph
from typing import Annotated, TypedDict, Literal
from pydantic import BaseModel
from operator import add
from ai.utils import get_model


class Configuration(TypedDict, total=False):
    max_depth: int
    max_candidates: int


def _ensure_configurable(config: RunnableConfig) -> Configuration:
    """Get params that configure the search algorithm."""
    configurable = config.get("configurable", {})
    return {
        **configurable,
        "max_depth": configurable.get("max_depth", 5),
        "max_candidates": configurable.get("max_candidates", 2),
    }


class CoTState(MessagesState):
    intermediate_steps: Annotated[list[str], add]
    last_step: bool


class ThoughtSchema(BaseModel):
    thought: str
    finish: bool


thinker_template = """
{{ system_prompt }}.

Before executing the task, think deeply about the next step to solve the task given by the user.
The tought you will give is the step of how to complete given by the user task.
The purpose of the thoughts is to break the problem into smaller steps.
Already taken steps: 
{% if steps %}{{ steps }}{% else %}This is your first step to solve this problem.{% endif %}

What is the next step to solve this problem? Is it the last step thast must be taken to complete the task?
Return only the next step in one sentence.
"""

thinker_prompt = PromptTemplate(
    template=thinker_template,
    input_variables=["system_prompt", "intermediate_steps"],
    template_format="jinja2",
)


def reasoning_node(state: CoTState, config: Configuration) -> CoTState:
    llm = get_model(config.get("configurable").get("llm"))
    system_prompt = config.get("configurable").get("system_prompt")

    if "intermediate_steps" in state and state["intermediate_steps"]:
        formatted_prompt = thinker_prompt.format(
            system_prompt=system_prompt,
            steps="\n".join(
                [f"{n+1}. {step}" for n, step in enumerate(state["intermediate_steps"])]
            ),
        )
    else:
        formatted_prompt = thinker_prompt.format(system_prompt=system_prompt)

    thought = (
        llm.with_structured_output(ThoughtSchema)
        .invoke([("system", formatted_prompt), state["messages"][-1]])
        .model_dump()
    )

    return {
        "intermediate_steps": [thought["thought"]],
        "last_step": thought["finish"],
    }


def should_continue(
    state: CoTState, config: RunnableConfig
) -> Literal["reasoning_node", "__end__"]:
    max_depth = _ensure_configurable(config).get("max_depth")
    if state["last_step"] or len(state["intermediate_steps"]) >= max_depth:
        return "__end__"
    return "reasoning_node"


graph_builder = StateGraph(CoTState, config_schema=Configuration)

graph_builder.add_node("reasoning_node", reasoning_node)

graph_builder.add_edge(START, "reasoning_node")
graph_builder.add_conditional_edges(
    "reasoning_node", should_continue, ["reasoning_node", "__end__"]
)
cot_graph = graph_builder.compile()


if __name__ == "__main__":

    with open("./cot_graph.png", "wb") as f:
        f.write(cot_graph.get_graph(xray=True).draw_mermaid_png())

    # cot_state = cot_graph.invoke(
    #     {"messages": [("user", "How to create pacman in python")]},
    #     config={
    #         "max_depth": 10,
    #         "configurable": {
    #             "llm": "gpt-4o-mini",
    #             "system_prompt": "You are code assistant.",
    #         },
    #     },
    # )
    # print(cot_state["intermediate_steps"])
