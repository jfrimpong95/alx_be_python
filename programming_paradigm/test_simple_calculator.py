import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(7, 6), 42)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(12, 2), 6)

    def test_division_by_zero(self):
        """Test division by zero."""
        self.assertEqual(self.calc.divide(5, 0), "Error: Cannot divide by zero.")

if __name__ == "__main__":
    unittest.main()
