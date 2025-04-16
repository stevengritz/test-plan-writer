# Source code being tested (copied directly into the script)
def calculate_factorial(n):
    if n < 0:
        return 'Error: Input must be a non-negative integer'
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Standard library imports
import unittest

# Test class using unittest
class TestCalculateFactorial(unittest.TestCase):

    def test_calculate_factorial(self):
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(-1), 'Error: Input must be a non-negative integer')

    def test_calculate_factorial_large_input(self):
        self.assertEqual(calculate_factorial(10), 3628800)
        self.assertEqual(calculate_factorial(20), 2432902008176640000)

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()