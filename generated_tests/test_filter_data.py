# Source code being tested (copied directly into the script)
def filter_data(data, condition):
    return [item for item in data if condition(item)]

# Standard library imports
import unittest

# Test class using unittest
class TestFilterData(unittest.TestCase):
    def test_filter_data(self):
        self.assertEqual(filter_data([1, 2, 3, 4, 5], lambda x: x > 3), [4, 5])
        self.assertEqual(filter_data([], lambda x: x > 0), [])
        self.assertEqual(filter_data([1, 2, 3], lambda x: x < 0), [])

    def test_filter_data_complex_condition(self):
        self.assertEqual(filter_data([1, 2, 3, 4, 5], lambda x: x % 2 == 0), [2, 4])

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()