# graph.py

This module implements a state graph for a code generation process, integrating large language model (LLM) capabilities to create a project structure based on user prompts.

## Constants

### `BRAIN_PROMPT`

A prompt instructing the LLM to think strategically about how to achieve a given coding task, taking into account previous steps in the project.

### `CODE_PROMPT`

A prompt for the LLM, indicating that it has to work with code and utilize the tools available to create directories, files, and read files.

## Classes

### `CoderState`

Inherits from `MessagesState` and holds the following attributes:
- `intermediate_steps` (list[str]): A list of intermediate steps taken to accomplish the task.
- `project_tree` (dict): A representation of the project structure.
- `relevant_code` (str): Code relevant to the ongoing task.

### `CodeSchema`

A Pydantic model representing a single code entity with the attributes:
- `code` (str): The code itself.
- `dir` (str): The directory where the code is located.

### `Codes`

A Pydantic model that encompasses a list of `CodeSchema` objects.

### `Dir`

A Pydantic model to represent directories with fields:
- `path` (str): The path to the directory.
- `description` (str): A description of what should be contained in this directory.

### `DirsSchema`

A Pydantic model holding a list of `Dir` objects.

## Functions

### `llm_node(state: CoderState, config: RunnableConfig)`

Processes the LLM to obtain intermediate steps based on the current state of messages. It retrieves the list of intermediate steps for further actions.

#### Parameters:
- `state` (CoderState): The current state containing messages and previous instructions.
- `config` (RunnableConfig): Configuration parameters for executing the tool.

#### Returns:
- `dict`: A dictionary containing `intermediate_steps` based on the LLM's analysis.

### `create_structure(path_str)`

Creates the directory structure specified by the `path_str`. It handles both files and directories and ensures parent directories exist.

#### Parameters:
- `path_str` (str): The path for the directory or file to be created.

### `get_code(output)`

Extracts code wrapped in triple backticks from the provided output string.

#### Parameters:
- `output` (str): The string output containing the code.

#### Returns:
- `str`: The extracted code if found; otherwise, returns `None`.

### `code(state: CoderState, config: RunnableConfig)`

Main function responsible for creating file and directory structures based on LLM analysis. It invokes LLM to generate directories and write the corresponding code to the files.

#### Parameters:
- `state` (CoderState): The current state containing messages and project status.
- `config` (RunnableConfig): Configuration parameters for executing the tool.

#### Returns:
- `CoderState`: The updated state after processing the code generation and file operations.

### `debug(state: CoderState, config: RunnableConfig)`

Function intended for debugging processes within the coder state, focusing on the LLM model.

#### Parameters:
- `state` (CoderState): The state to debug.
- `config` (RunnableConfig): Configuration parameters for debugging.