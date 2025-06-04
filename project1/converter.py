# Temperature Converter: Unit Constants, Validation, Conversion Logic, and Console UI

# Supported unit constants
CELSIUS = 'Celsius'
FAHRENHEIT = 'Fahrenheit'
KELVIN = 'Kelvin'

ALLOWED_UNITS = {CELSIUS, FAHRENHEIT, KELVIN}

def is_valid_unit(unit: str) -> bool:
    """
    Check if the given unit is among the supported temperature units.
    Args:
        unit (str): Unit string to validate.
    Returns:
        bool: True if unit is supported; False otherwise.
    """
    return unit.capitalize() in ALLOWED_UNITS

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a temperature value from one unit to another.
    Args:
        value (float): The temperature value to convert.
        from_unit (str): The current unit of value.
        to_unit (str): The desired target unit.
    Returns:
        float: The converted value in the target unit.
    Raises:
        ValueError: If from_unit or to_unit is invalid.
    """
    u_from = from_unit.capitalize()
    u_to = to_unit.capitalize()
    if u_from not in ALLOWED_UNITS or u_to not in ALLOWED_UNITS:
        raise ValueError(f"Unsupported temperature units: {from_unit}, {to_unit}")
    if u_from == u_to:
        return value
    # Convert input to Celsius first
    if u_from == CELSIUS:
        temp_c = value
    elif u_from == FAHRENHEIT:
        temp_c = (value - 32) * 5 / 9
    elif u_from == KELVIN:
        temp_c = value - 273.15
    else:
        raise ValueError(f"Unsupported input unit: {from_unit}")
    # Now Celsius to target
    if u_to == CELSIUS:
        return temp_c
    elif u_to == FAHRENHEIT:
        return temp_c * 9 / 5 + 32
    elif u_to == KELVIN:
        return temp_c + 273.15
    else:
        raise ValueError(f"Unsupported target unit: {to_unit}")


def get_user_input():
    """
    Prompt user to enter a numeric temperature value and a supported unit.
    Validates numeric input and unit selection.
    Returns:
        Tuple (value: float, unit: str)
    """
    while True:
        raw_value = input(f"Enter the temperature value: ").strip()
        try:
            value = float(raw_value)
        except ValueError:
            print("Error: Please enter a valid numeric value.")
            continue
        unit = input(f"Enter the unit ({'/'.join(ALLOWED_UNITS)}): ").strip()
        if not is_valid_unit(unit):
            print(f"Error: Unit must be one of: {', '.join(ALLOWED_UNITS)}.")
            continue
        return value, unit.capitalize()

def display_converted_temperatures(value: float, from_unit: str):
    """
    Given a starting value and its unit, convert to the other two units and display all three
    values clearly labeled.
    """
    units = [CELSIUS, FAHRENHEIT, KELVIN]
    results = {}
    for unit in units:
        results[unit] = convert(value, from_unit, unit)
    print("\n--- Temperature Conversion Results ---")
    for unit in units:
        print(f"{unit:>10}: {results[unit]:.2f}")
    print()

def main():
    print("Temperature Converter (Celsius, Fahrenheit, Kelvin)")
    value, from_unit = get_user_input()
    display_converted_temperatures(value, from_unit)

if __name__ == "__main__":
    main()
