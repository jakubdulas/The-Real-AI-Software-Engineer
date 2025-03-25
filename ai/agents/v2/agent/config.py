from langchain_core.runnables import RunnableConfig, Runnable
from typing import TypedDict


class Configuration(TypedDict, total=False):
    system_prompt: str
    llm: str
    tools: list
    reasoning_graph: Runnable | None


def _ensure_configurable(config: RunnableConfig) -> Configuration:
    """Get params that configure the search algorithm."""
    configurable = config.get("configurable", {})
    return {
        **configurable,
        "llm": configurable.get("llm", "gpt-4o-mini"),
    }
