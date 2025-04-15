
# Source code being tested (copied directly into the script)
def add(a, b):
    return a + b

# Standard library imports
import unittest

# Test class using unittest
class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -2), -3)

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()