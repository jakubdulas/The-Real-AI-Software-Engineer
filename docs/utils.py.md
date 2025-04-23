# utils.py

This module provides utility functions for the project.

## Functions

### `get_model(model: str, temperature=1)`

This function returns an instance of the `ChatOpenAI` model based on the specified model name.

#### Parameters:
- `model` (str): The name of the model to be instantiated. It is expected to contain the substring "gpt".
- `temperature` (int, optional): A parameter that influences the randomness of the model's outputs. Default value is 1.

#### Returns:
- `ChatOpenAI`: An instance of the `ChatOpenAI` class if the model is a valid GPT model.

#### Raises:
- `ValueError`: If the specified model name does not contain "gpt".