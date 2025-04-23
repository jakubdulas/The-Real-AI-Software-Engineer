# utils.py

This module contains utility functions for handling file and directory operations in the project.

## Functions

### `create_directory_tree(directory)`

Generates a hierarchical representation of the directory structure within the specified directory.

#### Parameters:
- `directory` (str): The root directory from which the tree structure will be created.

#### Returns:
- `dict`: A nested dictionary representing the directory tree structure, with directory names as keys and subdirectories/files as values.

### `find_file_in_tree(tree, filename, current_path="")`

Searches for a given filename in the directory tree and returns its path if found.

#### Parameters:
- `tree` (dict): A directory tree structure created by `create_directory_tree`.
- `filename` (str): The name of the file to find.
- `current_path` (str, optional): The current directory path in recursive search, default is an empty string.

#### Returns:
- `str`: The relative path to the specified file if found, otherwise `None`.

### `run_shell_command(command: str) -> str`

Executes a shell command and returns its output while handling errors and timeouts.

#### Parameters:
- `command` (str): The shell command to execute.

#### Returns:
- `str`: The output of the command if executed successfully, or an error message if the command fails.