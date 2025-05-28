import unittest
from converter import convert

class TestTemperatureConverter(unittest.TestCase):
    # Test case for input validation
    def test_invalid_numeric_input(self):
        with self.assertRaises(ValueError):
            convert(float('invalid'), 'Celsius', 'Fahrenheit')

    def test_invalid_unit_input(self):
        with self.assertRaises(ValueError):
            convert(32, 'InvalidUnit', 'Celsius')

    # Test case for conversion accuracy
    def test_conversion_at_absolute_zero_kelvin(self):
        self.assertAlmostEqual(convert(0, 'Kelvin', 'Celsius'), -273.15, places=2)
        self.assertAlmostEqual(convert(0, 'Kelvin', 'Fahrenheit'), -459.67, places=2)

    def test_conversion_freezing_point_water(self):
        self.assertAlmostEqual(convert(0, 'Celsius', 'Fahrenheit'), 32, places=2)
        self.assertAlmostEqual(convert(0, 'Celsius', 'Kelvin'), 273.15, places=2)

    def test_very_high_temperature(self):
        self.assertAlmostEqual(convert(5778, 'Kelvin', 'Celsius'), 5504.85, places=2)

    def test_same_unit_conversion(self):
        self.assertEqual(convert(100, 'Celsius', 'Celsius'), 100)

    # Test handling large and small values
    def test_large_float_value(self):
        self.assertIsNotNone(convert(1.7e+308, 'Celsius', 'Fahrenheit'))

    def test_negative_near_zero(self):
        self.assertIsNotNone(convert(-1e-10, 'Fahrenheit', 'Kelvin'))

if __name__ == '__main__':
    unittest.main()