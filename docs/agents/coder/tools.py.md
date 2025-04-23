# tools.py

This module provides tools for managing code files within the project.

## Tools

### `update_code(file_path: str, old_code: str, new_code: str, config: RunnableConfig)`

Updates the code in a specified file by replacing old code with new code.

#### Parameters:
- `file_path` (str): Path to the code file.
- `old_code` (str): The old code to be replaced.
- `new_code` (str): The new code that will replace the old code.
- `config` (RunnableConfig): Configuration parameters for executing the tool.

### `remove_code(file_path: str, code_to_remove: str, config: RunnableConfig)`

Removes specific code from a designated file.

#### Parameters:
- `file_path` (str): Path to the code file.
- `code_to_remove` (str): The code that should be removed from the file.
- `config` (RunnableConfig): Configuration parameters for executing the tool.

### `create_file(file_path: str, tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig)`

Creates a new file for code.

#### Parameters:
- `file_path` (str): The path in which the new file will be created.
- `tool_call_id` (Annotated[str, InjectedToolCallId]): ID to track the tool invocation.
- `config` (RunnableConfig): Configuration parameters for executing the tool.

### `overwrite_code_in_file(file_path: str, code: str, tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig)`

Overwrites the content of a specified file with new code.

#### Parameters:
- `file_path` (str): Path to the code file.
- `code` (str): The new code to be written into the file.
- `tool_call_id` (Annotated[str, InjectedToolCallId]): ID to track the tool invocation.
- `config` (RunnableConfig): Configuration parameters for executing the tool.

### `read_file(file_path: str, config: RunnableConfig)`

Reads the content of a specified file and returns its code.

#### Parameters:
- `file_path` (str): Path to the code file.
- `config` (RunnableConfig): Configuration parameters for executing the tool.

### `create_directory(directory: str, tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig)`

Creates a relative directory to store code files.

#### Parameters:
- `directory` (str): Name of the directory to create.
- `tool_call_id` (Annotated[str, InjectedToolCallId]): ID to track the tool invocation.
- `config` (RunnableConfig): Configuration parameters for executing the tool.

### `run_code(file_path: str, config: RunnableConfig, state: Annotated[dict, InjectedState])`

Executes a Python file specified by the file path.

#### Parameters:
- `file_path` (str): The path to the Python file to be executed.
- `config` (RunnableConfig): Configuration parameters for executing the tool.
- `state` (Annotated[dict, InjectedState]): State information that may be needed during execution.

## Tools List

The module maintains a list of tools defined for ease of access: 
- `create_file`
- `overwrite_code_in_file`
- `read_file`
- `create_directory`
- `update_code`
- `remove_code`
- `run_code`

The tools list is used to create a `ToolNode` for execution.