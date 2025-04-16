# Source code being tested (copied directly into the script)
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Standard library imports
import unittest

# Test class using unittest
class TestCalculateFactorial(unittest.TestCase):
    def test_calculate_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)

    def test_calculate_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-5)

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()