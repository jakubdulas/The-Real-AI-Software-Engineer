# tools.py

This module provides various tools for managing documentation within the project. These tools can create, read, update, and delete documentation files.

## Tools

### `update_documentation(file_path: str, old_documentation: str, new_documentation: str, config: RunnableConfig)`

Updates the documentation in a specified file. It replaces old documentation with new documentation.

#### Parameters:
- `file_path` (str): The path to the documentation file.
- `old_documentation` (str): The documentation text that needs to be replaced.
- `new_documentation` (str): The new documentation text that will replace the old text.
- `config` (RunnableConfig): Configuration parameters for running the tool.

### `remove_documentation(file_path: str, documentation_to_remove: str, config: RunnableConfig)`

Removes specific documentation from a file.

#### Parameters:
- `file_path` (str): The path to the documentation file.
- `documentation_to_remove` (str): The documentation text to be removed.
- `config` (RunnableConfig): Configuration parameters for running the tool.

### `create_file(file_path: str, tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig)`

Creates a new file for documentation.

#### Parameters:
- `file_path` (str): The path where the new file will be created.
- `tool_call_id` (Annotated[str, InjectedToolCallId]): The ID for tracking the tool call.
- `config` (RunnableConfig): Configuration parameters for running the tool.

### `overwrite_documentation_in_file(file_path: str, documentation: str, tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig)`

Overwrites any existing documentation in the specified file with new documentation.

#### Parameters:
- `file_path` (str): The path to the documentation file.
- `documentation` (str): The new documentation text to be written into the file.
- `tool_call_id` (Annotated[str, InjectedToolCallId]): The ID for tracking the tool call.
- `config` (RunnableConfig): Configuration parameters for running the tool.

### `read_file(file_path: str, config: RunnableConfig)`

Reads the documentation from a specified file.

#### Parameters:
- `file_path` (str): The path to the documentation file.
- `config` (RunnableConfig): Configuration parameters for running the tool.

### `create_directory(directory: str, tool_call_id: Annotated[str, InjectedToolCallId], config: RunnableConfig)`

Creates a directory for documentation files.

#### Parameters:
- `directory` (str): The name of the directory to create.
- `tool_call_id` (Annotated[str, InjectedToolCallId]): The ID for tracking the tool call.
- `config` (RunnableConfig): Configuration parameters for running the tool.

### `read_code(file_path: str, config: RunnableConfig)`

Reads the code from a specified file.

#### Parameters:
- `file_path` (str): The path to the code file.
- `config` (RunnableConfig): Configuration parameters for running the tool.

## Tools List

The module also maintains a list of all tools defined for ease of access: 
- `create_file`
- `overwrite_documentation_in_file`
- `read_file`
- `create_directory`
- `update_documentation`
- `remove_documentation`
- `read_code`

The tools list is used to create a `ToolNode` for execution.