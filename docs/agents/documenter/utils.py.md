# utils.py

This module contains utility functions that facilitate various file and directory operations used by the `Documenter` class.

## Functions

### `create_directory_tree(directory)`

Generates a hierarchical representation of the directory structure starting from the specified directory.

#### Parameters:
- `directory` (str): The directory path from which the tree structure is created.

#### Returns:
- `dict`: A nested dictionary representing the directory tree where keys are directory and file names, and values are `None`.

### `find_file_in_tree(tree, filename, current_path="")`

Searches through a directory tree to find the specified filename and returns its relative path if found.

#### Parameters:
- `tree` (dict): The directory tree structure created using `create_directory_tree`.
- `filename` (str): The name of the file to search for in the tree.
- `current_path` (str, optional): The current path from which to look; defaults to an empty string.

#### Returns:
- `str`: The relative path of the found file or `None` if the file is not found in the tree.

### `run_shell_command(command: str) -> str`

Executes a shell command and returns its output, handling errors and timeouts effectively.

#### Parameters:
- `command` (str): The shell command to execute.

#### Returns:
- `str`: The output from the executed command or an error message if the command fails.