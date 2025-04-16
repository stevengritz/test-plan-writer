
# Source code being tested (copied directly into the script)
def calculate_factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('Input must be a non-negative integer')
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Standard library imports
import unittest

# Test class using unittest
class TestCalculateFactorial(unittest.TestCase):

    def test_calculate_factorial_normal_cases(self):
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(5), 120)

    def test_calculate_factorial_edge_cases(self):
        with self.assertRaises(ValueError) as cm:
            calculate_factorial(-1)
        self.assertEqual(str(cm.exception), 'Input must be a non-negative integer')

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()