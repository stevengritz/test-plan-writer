# Source code being tested (copied directly into the script)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Standard library imports
import unittest

# Test class using unittest
class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(5, 5), 0)

    # Edge case: Test with zero
    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()