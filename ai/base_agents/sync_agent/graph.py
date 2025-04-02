from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage
from dotenv import load_dotenv
from .config import Configuration, _ensure_configurable
from ai.utils import get_model
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


def next_step(state, config: Configuration):
    if "current_step" not in state:
        current_step = 0
    else:
        current_step = state.get("current_step") + 1
    return {
        "current_step": current_step,
        "messages": [
            AIMessage(
                content=f"Focus on this step: {state.get('intermediate_steps')[current_step]}"
            )
        ],
    }


def llm_node(state, config: Configuration):
    _ensure_configurable(config)
    tools = config.get("configurable").get("tools")
    agent_state_variables = config.get("configurable").get("agent_state_variables")
    llm = get_model(config.get("configurable").get("llm"))
    system_prompt = config.get("configurable").get("system_prompt")
    template = ChatPromptTemplate(
        [
            ("system", system_prompt),
            MessagesPlaceholder("messages"),
        ]
    )

    prompt_state = str({k: v for k, v in state.items() if k in agent_state_variables})

    runnable = template | llm.bind_tools(tools)
    output = runnable.invoke(
        {
            "messages": state.get("messages"),
            "state": prompt_state,
        }
    )
    return {"messages": [output]}


def zero_state(state):
    return {"intermediate_steps": [], "current_step": 0}


def should_continue(state):
    tool_calls = state["messages"][-1].tool_calls
    if tool_calls:
        return "tools"

    if len(state.get("intermediate_steps")) - 1 == state.get("current_step"):
        return "zero_state"
    return "next_step"
