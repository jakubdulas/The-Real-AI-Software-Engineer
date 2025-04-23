# example.py

This module contains a sample implementation of the `Coder` class, which represents a coding agent capable of creating projects based on specified requirements.

## Imports
- `SyncAgent` from `ai.base_agents.sync_agent.agent`: Base class for synchronous agents.
- `LinearAgent` from `ai.base_agents.linear_agent.agent`: Imported but not directly used in the code.
- `graph` from `ai.tot.v1.graph` and `ai.tot.v2.graph`: Used for managing different versions of the graph.
- `cot_graph` from `ai.cot.graph`: Represents the reasoning graph.
- `TypedDict`, `Annotated` from `typing`: For type hinting and defining type structures.
- `coder_system_prompt` from `.prompts`: System prompts for guiding the coding process.
- `tools` from `.tools`: Utility tools utilized by the Coder agent.
- `create_directory_tree` from `.utils`: Function to create a directory structure.

## Class: CoderAgentState

### Description
A `TypedDict` that defines the state structure for the `Coder` agent.

### Attributes
- `project_tree` (Annotated[dict]): Represents the current project directory tree structure.

## Class: Coder

### Description
A subclass of `SyncAgent` that implements a coding agent capable of generating and managing code based on input prompts.

### Methods

#### __init__(self, working_dir, llm="gpt-4o", reasoning_graph=cot_graph)
- **Parameters**:
  - `working_dir` (str): The directory where the project files will be created.
  - `llm` (str): Language model to be used, default is "gpt-4o".
  - `reasoning_graph`: The reasoning graph used by the agent.

#### invoke(self, *args, **kwargs)
- **Description**: Invokes the agent with the provided arguments and keyword arguments, initializing the project tree and working directory configuration.
- **Parameters**: Accepts any positional and keyword arguments.

### Main Execution Block
When this module is run directly, it creates an instance of the `Coder` class, invokes it with a prompt to create a Pacman game using Pygame, and prints the response message from the AI counterpart.