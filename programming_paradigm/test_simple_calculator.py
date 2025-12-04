import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract(self):
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = self.calc.multiply(7, 6)
        self.assertEqual(result, 42)

    def test_division(self):
        result = self.calc.divide(12, 2)
        self.assertEqual(result, 6)

    def test_division_by_zero(self):
        result = self.calc.divide(5, 0)
        self.assertEqual(result, "Error: Cannot divide by zero.")

if __name__ == "__main__":
    unittest.main()
