"""
Temperature Converter
---------------------
A clean, modular, and testable console-based program for converting temperatures 
between Celsius, Fahrenheit, and Kelvin. 

Features:
- User input for numeric value and temperature unit
- Conversion between all three units
- Input validation and graceful error handling
- Clean formatted output

Functions:
- convert: Reusable, for all temperature unit conversions
- prompt_temperature_input: Handles user entry, validation
- display_conversion_results: Formats output for readability
- main: Main program loop
"""
from typing import Tuple, Dict, Union

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert temperature between Celsius, Fahrenheit, and Kelvin.

    Args:
        value (float): The temperature value to convert.
        from_unit (str): Source unit ('C', 'F', 'K').
        to_unit (str): Target unit ('C', 'F', 'K').

    Returns:
        float: Converted temperature value.
    """
    # Normalize units (case-insensitive, allow full names/abbreviations)
    unit_map = {
        'celsius': 'C', 'c': 'C',
        'fahrenheit': 'F', 'f': 'F',
        'kelvin': 'K', 'k': 'K',
    }
    try:
        from_u = unit_map[from_unit.strip().lower()]
        to_u = unit_map[to_unit.strip().lower()]
    except (KeyError, AttributeError):
        raise ValueError(f"Unsupported temperature unit(s): '{from_unit}' or '{to_unit}'")

    if from_u == to_u:
        return float(value)

    # Step 1: Convert to Celsius
    if from_u == 'C':
        celsius = value
    elif from_u == 'F':
        celsius = (value - 32) * 5 / 9
    elif from_u == 'K':
        celsius = value - 273.15
    else:
        raise ValueError(f"Unsupported temperature unit: {from_unit}")

    # Step 2: Check absolute zero
    kelvin_equivalent = celsius + 273.15
    if kelvin_equivalent < 0:
        raise ValueError("Temperature below absolute zero (0 K)")

    # Step 3: Convert from Celsius to target
    if to_u == 'C':
        return celsius
    elif to_u == 'F':
        return celsius * 9 / 5 + 32
    elif to_u == 'K':
        return kelvin_equivalent
    else:
        raise ValueError(f"Unsupported temperature unit: {to_unit}")

def prompt_temperature_input() -> Tuple[float, str]:
    """
    Prompt the user for a numeric value and unit. Validates input and returns both.
    Returns:
        (float, str): Tuple of value and normalized unit ('C', 'F', 'K').
    """
    unit_map = {
        'celsius': 'C', 'c': 'C',
        'fahrenheit': 'F', 'f': 'F',
        'kelvin': 'K', 'k': 'K',
    }
    while True:
        raw_value = input("Enter the temperature value: ").strip()
        try:
            value = float(raw_value)
        except ValueError:
            print(f"Invalid numeric value: '{raw_value}'. Try again (e.g. 23.5 or -10).")
            continue
        raw_unit = input("Enter the temperature unit (Celsius, Fahrenheit, Kelvin): ").strip().lower()
        unit = unit_map.get(raw_unit)
        if unit is None:
            print(f"Invalid unit: '{raw_unit}'. Use Celsius, Fahrenheit, or Kelvin (e.g. 'C', 'F', 'K').")
            continue
        return value, unit

def display_conversion_results(base_value: float, base_unit: str, conversions: Dict[str, Union[float, str]]) -> None:
    """
    Print temperature conversions for all units, clearly formatted.
    Args:
        base_value (float): Original temperature value.
        base_unit (str): Unit of base_value ('C', 'F', 'K').
        conversions (dict): Mapping 'C'/'F'/'K' to float (success) or str (error).
    """
    symbols = {'C': '°C', 'F': '°F', 'K': 'K'}
    print("\nConverted temperatures:")
    for unit in ['C', 'F', 'K']:
        val = conversions[unit]
        if isinstance(val, float):
            print(f"  {val:.2f} {symbols[unit]}")
        else:
            print(f"  Error for {symbols[unit]}: {val}")

def main():
    print("\n==== Temperature Converter ====")
    try:
        value, unit = prompt_temperature_input()
    except EOFError:
        print("\nInput was closed. Exiting.")
        return

    units = ['C', 'F', 'K']
    results = {}
    for target_unit in units:
        try:
            results[target_unit] = convert(value, unit, target_unit)
        except ValueError as e:
            results[target_unit] = str(e)
    display_conversion_results(value, unit, results)

if __name__ == "__main__":
    main()
