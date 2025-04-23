# agent.py

This module defines the `Documenter` class, which serves as a code documentation generator. It utilizes a large language model (LLM) to create documentation for a given codebase by analyzing source files and generating documentation in Markdown format.

## Classes

### `DocumenterState`

A custom state class that extends `MessagesState` to track the documentation progress with a single attribute:
- `remaining_steps` (int): A counter representing the number of remaining steps in the documentation process.

### `Documenter`

This class is designed to automate the documentation process for a codebase.

#### Constants:
- `SYSTEM_PROMPT`: A string that contains the instructions for the LLM to guide its documentation tasks, detailing how it should operate and the structure of the output.

#### Initialization:

The constructor method initializes the `Documenter` class with the following parameters:
- `llm`: The language model identifier (e.g., "gpt-4o-mini").
- `code_dir`: The directory where the codebase to document is located.
- `documentation_dir`: The directory where the generated documentation files will be saved.

#### Methods:

- `invoke(*args, **kwargs)`:
  Calls the underlying LLM to generate documentation based on provided messages and configurations. It returns the state of the documentation process.

#### Usage:

The `Documenter` class is designed to be instantiated with the necessary configuration and invoked to start the documentation process. The system prompt, formatted with project structure and documentation structure, guides the LLM in generating the required documentation.

## Example:

The `Documenter` class can be executed directly, as indicated in the main block. It creates an instance of `Documenter` and invokes the documentation generation process for the entire project.