# Source code being tested (copied directly into the script)
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Standard library imports
import unittest

# Test class using unittest
class TestCalculateFactorial(unittest.TestCase):
    def test_calculate_factorial(self):
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(5), 120)

    def test_calculate_factorial_large(self):
        self.assertEqual(calculate_factorial(20), 2432902008176640000)

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()