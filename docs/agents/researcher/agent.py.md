# agent.py

This module defines the `Researcher` class, which is designed to collect necessary data and provide detailed answers to various goals. The `Researcher` utilizes a language model to generate responses and gather information relevant to user queries.

## Classes

### `Researcher`

This class is responsible for data collection and research based on provided user goals.

#### Constants:
- `SYSTEM_PROMPT`: A string that instructs the language model about its role as a researcher, emphasizing the need for comprehensive answers with all necessary details.

#### Initialization:

The constructor method initializes the `Researcher` class with the following parameters:
- `llm`: The language model identifier (e.g., "gpt-4o-mini").

#### Methods:

- `invoke(*args, **kwargs)`:
  Calls the underlying language model to generate responses based on provided messages and configurations. It returns the state of the research process.

## Example:

The `Researcher` class can be executed directly, as indicated in the main block. It creates an instance of `Researcher` and invokes the research process based on a user query.