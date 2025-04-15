# Source code being tested (copied directly into the script)
def add(a, b):
    return a + b

# Standard library imports
import unittest

# Test class using unittest
class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

    def test_addition_negative(self):
        self.assertEqual(add(-2, -3), -5)

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()