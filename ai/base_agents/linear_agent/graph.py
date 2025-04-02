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


def llm_node(state, config: Configuration):
    _ensure_configurable(config)
    tools = config.get("configurable").get("tools")
    agent_state_variables = config.get("configurable").get("agent_state_variables")
    llm = get_model(config.get("configurable").get("llm"))
    system_prompt = config.get("configurable").get("system_prompt")
    prompt_state = str({k: v for k, v in state.items() if k in agent_state_variables})

    print(system_prompt)
    coder_template = ChatPromptTemplate(
        [
            ("system", system_prompt),
            MessagesPlaceholder("messages"),
        ]
    )

    runnable = coder_template | llm.bind_tools(tools)
    output = runnable.invoke({"messages": state.get("messages"), "state": prompt_state})
    return {"messages": [output]}


def should_continue(state):
    tool_calls = state["messages"][-1].tool_calls
    if tool_calls:
        return "tools"

    return "__end__"
