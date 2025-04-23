# tools.py

This module consists of various tools used for manipulating code files within the code generation framework. These tools allow for creating, updating, removing, and executing code files.

## Tools

### `update_code(file_path: str, old_code: str, new_code: str, config: RunnableConfig)`

Updates a specified code file by replacing occurrences of old code with new code.

#### Parameters:
- `file_path` (str): The path to the code file being updated.
- `old_code` (str): The existing code that needs to be replaced.
- `new_code` (str): The new code that will replace the old code.
- `config` (RunnableConfig): Configuration parameters guiding the execution of the tool.

### `remove_code(file_path: str, code_to_remove: str, config: RunnableConfig)`

Removes specified code from a designated file.

#### Parameters:
- `file_path` (str): The path to the code file from which code will be removed.
- `code_to_remove` (str): The code that needs to be removed.
- `config` (RunnableConfig): Configuration parameters guiding the execution of the tool.

### `create_file(file_path: str, tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig)`

Creates a new file at the specified path for code storage.

#### Parameters:
- `file_path` (str): The path where the new file will be created.
- `tool_call_id` (Annotated[str, InjectedToolCallId]): Identifier for tracking tool calls.
- `config` (RunnableConfig): Configuration parameters guiding the execution of the tool.

### `overwrite_code_in_file(file_path: str, code: str, tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig)`

Overwrites the content of a file with new code. This is used after creating a new file.

#### Parameters:
- `file_path` (str): The path to the file being overwritten.
- `code` (str): The new code that will replace the existing content.
- `tool_call_id` (Annotated[str, InjectedToolCallId]): Identifier for tracking tool calls.
- `config` (RunnableConfig): Configuration parameters guiding the execution of the tool.

### `read_file(file_path: str, config: RunnableConfig)`

Reads the contents of a specified code file and returns its code.

#### Parameters:
- `file_path` (str): The path to the code file.
- `config` (RunnableConfig): Configuration parameters guiding the execution of the tool.

### `create_directory(directory: str, tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig)`

Creates a directory for organizing code files.

#### Parameters:
- `directory` (str): The name of the directory to be created.
- `tool_call_id` (Annotated[str, InjectedToolCallId]): Identifier for tracking tool calls.
- `config` (RunnableConfig): Configuration parameters guiding the execution of the tool.

### `run_code(file_path: str, config: RunnableConfig, state: Annotated[dict, InjectedState])`

Executes a Python file located at the specified path.

#### Parameters:
- `file_path` (str): The path to the Python file to be executed.
- `config` (RunnableConfig): Configuration parameters guiding the execution of the tool.
- `state` (Annotated[dict, InjectedState]): State information relevant to the execution.