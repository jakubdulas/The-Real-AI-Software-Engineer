from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import MessagesState
from operator import add
from langchain_core.messages import AIMessage
from dotenv import load_dotenv
from typing_extensions import Annotated
from .config import Configuration, _ensure_configurable
from ai.tot.v1.utils import get_model
from langchain_core.prompts.chat import MessagesPlaceholder
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


# def reason(state: CoderAgentState, config: Configuration) -> CoderAgentState:
def reason(state, config: Configuration):
    _ensure_configurable(config)
    configurable = config.get("configurable", {})
    reasoning_graph = configurable.get("reasoning_graph")
    steps = reasoning_graph.invoke(
        {"messages": state.get("messages")},
        config={"recursion_limit": 50, "configurable": configurable},
    ).get("intermediate_steps")

    formatted_steps = "\n".join([f"{n+1}. {step}" for n, step in enumerate(steps)])

    return {
        "messages": [
            AIMessage(
                content="My plan to achieve the goal that I must follow: "
                + formatted_steps
            )
        ],
        "intermediate_steps": steps,
    }


# def llm_node(state: CoderAgentState, config: Configuration) -> CoderAgentState:
def llm_node(state, config: Configuration):
    _ensure_configurable(config)
    tools = config.get("configurable").get("tools")
    llm = get_model(config.get("configurable").get("llm"))
    system_prompt = config.get("configurable").get("system_prompt")

    print(system_prompt)
    coder_template = ChatPromptTemplate(
        [
            ("system", system_prompt),
            # ("ai", "Current state: {state}"),
            MessagesPlaceholder("messages"),
        ]
    )

    runnable = coder_template | llm.bind_tools(tools)
    output = runnable.invoke({"messages": state.get("messages")})
    return {"messages": [output]}


# def should_continue(state: CoderAgentState):
def should_continue(state):
    if len(state.get("intermediate_steps")) == state.get("current_step"):
        return "__end__"

    tool_calls = state["messages"][-1].tool_calls
    if tool_calls:
        return "tools"

    return "__end__"
