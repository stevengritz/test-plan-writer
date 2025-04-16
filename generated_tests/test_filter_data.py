# Source code being tested (copied directly into the script)
def filter_data(data):
    return [x for x in data if x % 2 == 0]

# Standard library imports
import unittest

# Test class using unittest
class TestFilterData(unittest.TestCase):

    def test_filter_data(self):
        self.assertEqual(filter_data([1, 2, 3, 4, 5]), [2, 4])
        self.assertEqual(filter_data([]), [])
        self.assertEqual(filter_data([10, 20, 30, 40]), [20, 40])

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()