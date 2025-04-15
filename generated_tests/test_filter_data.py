
# Source code being tested (copied directly into the script)
def filter_data(data, condition):
    return [item for item in data if condition(item)]

# Standard library imports
import unittest

# Test class using unittest
class TestFilterData(unittest.TestCase):
    def test_filter_data(self):
        data = [{'value': 10}, {'value': 20}, {'value': 30}]
        condition = lambda x: x['value'] > 15
        self.assertEqual(filter_data(data, condition), [{'value': 20}, {'value': 30}])

    def test_filter_data_empty(self):
        data = []
        condition = lambda x: x['value'] > 15
        self.assertEqual(filter_data(data, condition), [])

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()