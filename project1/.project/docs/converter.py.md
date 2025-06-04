# Temperature Converter Documentation

## Overview

This file implements a simple and interactive console-based temperature converter supporting three units: **Celsius**, **Fahrenheit**, and **Kelvin**. The user can input a numeric temperature value and specify its unit, after which the program converts the value to the other two units and displays all three results. The code is organized for readability, validation, and ease of testing, with clear function separation for core responsibilities.

The main components are:
- **Unit constants and supported units declaration**
- **Validation helper for temperature unit**
- **Conversion logic packaged in a reusable function `convert`**
- **Console user input collection with validation**
- **Display formatting for conversion results**
- **Main application flow**

All functions are cleanly separated and include detailed docstrings—making logic, parameters, and intended use clear.

---

## Constants & Unit Declarations

- `CELSIUS`, `FAHRENHEIT`, `KELVIN`: String constants for supported temperature units.
- `ALLOWED_UNITS`: A set of supported units, used for unit validation.

---

## Functions

### `is_valid_unit(unit: str) -> bool`

Checks if the provided unit string is among the supported units (Celsius, Fahrenheit, Kelvin).

**Parameters:**
- `unit` (str): The unit string entered by the user.

**Returns:**
- `bool`: True if the unit is supported; False otherwise.

**Usage:** Helps validate user input.

---

### `convert(value: float, from_unit: str, to_unit: str) -> float`

Performs conversion between any two supported temperature units.

**Parameters:**
- `value` (float): The numeric temperature value to convert.
- `from_unit` (str): The unit of the input temperature (case-insensitive).
- `to_unit` (str): The desired output unit (case-insensitive).

**Returns:**
- `float`: The converted temperature value in the target unit.

**Raises:**
- `ValueError`: If either unit is unsupported.

**Implementation Details:**
- All conversions are internally routed via Celsius for centralization.
- No-op if units match.

---

### `get_user_input() -> Tuple[float, str]`

Handles interactive retrieval and validation of user input (both value and unit).

**Returns:**
- Tuple (`value`: float, `unit`: str): The validated input value and normalized unit string (title-cased).

**User Experience:**
- Prompts for numeric value and unit string from console input.
- Provides clear error messages for invalid input or unsupported units.

---

### `display_converted_temperatures(value: float, from_unit: str)`

Displays clear conversion results for all three units, given an input value and source unit.

**Parameters:**
- `value` (float): The value to convert.
- `from_unit` (str): The original unit of the value.

**Behavior:**
- Converts the source value to all three possible units using `convert`.
- Prints each unit/value clearly and formatted to two decimal places, labeled and lined up.

---

### `main()`

The central routine that ties program execution together.

- Prints a header.
- Prompts the user for input using `get_user_input()`.
- Runs `display_converted_temperatures()` to present results.

---

## Example Usage

```
Temperature Converter (Celsius, Fahrenheit, Kelvin)
Enter the temperature value: 100
Enter the unit (Celsius/Fahrenheit/Kelvin): Celsius

--- Temperature Conversion Results ---
   Celsius: 100.00
Fahrenheit: 212.00
    Kelvin: 373.15
```

---

## Testing & Extensibility
- The `convert` function is fully reusable and testable—import and call it directly with various inputs for unit tests.
- Input validation is cleanly separated for clarity and maintenance.

---

## Entry Point

Running the script directly as a Python file (`python converter.py`) launches the interactive UI. All execution is under the `if __name__ == "__main__":` guard, making imports and testing safe.