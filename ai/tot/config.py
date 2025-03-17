from langchain_core.runnables import RunnableConfig
from typing import TypedDict


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
