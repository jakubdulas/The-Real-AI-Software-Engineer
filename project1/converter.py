def convert(value, from_unit, to_unit):
    """
    Convert temperature from one unit to another.

    Parameters:
        value (float): The numerical value of the temperature.
        from_unit (str): The unit of the temperature to convert from ('Celsius', 'Fahrenheit', 'Kelvin').
        to_unit (str): The unit of the temperature to convert to ('Celsius', 'Fahrenheit', 'Kelvin').

    Returns:
        float: Converted temperature value.
    """
    # Conversion formulas
    def celsius_to_fahrenheit(value):
        return (value * 9/5) + 32

    def celsius_to_kelvin(value):
        return value + 273.15

    def fahrenheit_to_celsius(value):
        return (value - 32) * 5/9

    def fahrenheit_to_kelvin(value):
        return (value - 32) * 5/9 + 273.15

    def kelvin_to_celsius(value):
        return value - 273.15

    def kelvin_to_fahrenheit(value):
        return (value - 273.15) * 9/5 + 32

    # Conversion logic
    if from_unit == to_unit:
        return value
    elif from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return celsius_to_fahrenheit(value)
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return celsius_to_kelvin(value)
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return fahrenheit_to_celsius(value)
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return fahrenheit_to_kelvin(value)
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return kelvin_to_celsius(value)
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return kelvin_to_fahrenheit(value)
    else:
        raise ValueError('Invalid units for conversion')

def main():
    while True:
        value, unit = get_user_input()

        # Convert to other units
        if unit == 'Celsius':
            fahrenheit = convert(value, unit, 'Fahrenheit')
            kelvin = convert(value, unit, 'Kelvin')
            print(f"{value}°C = {fahrenheit}°F = {kelvin}K")
        elif unit == 'Fahrenheit':
            celsius = convert(value, unit, 'Celsius')
            kelvin = convert(value, unit, 'Kelvin')
            print(f"{value}°F = {celsius}°C = {kelvin}K")
        elif unit == 'Kelvin':
            celsius = convert(value, unit, 'Celsius')
            fahrenheit = convert(value, unit, 'Fahrenheit')
            print(f"{value}K = {celsius}°C = {fahrenheit}°F")
        
        # Ask if the user wants to do more conversions
        more = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if more != 'yes':
            print("Goodbye!")
            break


def get_user_input():
    while True:
        try:
            value = float(input("Enter the temperature value: "))
            unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ").strip()
            if unit not in ['Celsius', 'Fahrenheit', 'Kelvin']:
                raise ValueError('Invalid unit')
            return value, unit
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

        print('Temperature Converter - Enter the temperature value and unit')
        break # Temporary break to prevent infinite loop

if __name__ == '__main__':
    main()

