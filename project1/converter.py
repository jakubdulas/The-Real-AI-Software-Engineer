def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert temperature between Celsius, Fahrenheit, and Kelvin.
    Args:
        value (float): The numeric temperature value to convert.
        from_unit (str): The unit to convert from ("Celsius", "Fahrenheit", "Kelvin").
        to_unit (str): The unit to convert to ("Celsius", "Fahrenheit", "Kelvin").
    Returns:
        float: The converted temperature value.
    Raises:
        ValueError: If an unknown unit is provided.
    """
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    # Convert input value to Celsius first
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {from_unit}")

    # Now convert from Celsius to target unit
    if to_unit == "celsius":
        return celsius
    elif to_unit == "fahrenheit":
        return celsius * 9 / 5 + 32
    elif to_unit == "kelvin":
        return celsius + 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {to_unit}")


def get_numeric_input(prompt: str) -> float:
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input)
            return value
        except ValueError:
            print("Invalid number. Please enter a valid numeric value.")


def get_unit_input(prompt: str) -> str:
    valid_units = {
        "celsius": ["c", "celsius"],
        "fahrenheit": ["f", "fahrenheit"],
        "kelvin": ["k", "kelvin"]
    }
    units_flat = [u for aliases in valid_units.values() for u in aliases]
    while True:
        user_input = input(prompt).strip().lower()
        for normal, aliases in valid_units.items():
            if user_input in aliases:
                return normal.capitalize()
        print(f"Invalid unit. Please select from: {', '.join([u.capitalize() for u in valid_units.keys()])} (or C/F/K)")

def main():
    print("--- Temperature Converter ---")
    value = get_numeric_input("Enter the temperature value: ")
    unit = get_unit_input("Enter the unit (Celsius, Fahrenheit, Kelvin or C/F/K): ")
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    print(f"\nInput: {value} {unit}")
    print("Converted values:")
    for target_unit in units:
        if target_unit != unit:
            converted = convert(value, unit, target_unit)
            print(f"  {converted:.2f} {target_unit}")

if __name__ == "__main__":
    main()
