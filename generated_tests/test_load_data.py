
# Source code being tested (copied directly into the script)
def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return 'Data loaded successfully'
    except FileNotFoundError:
        return 'File not found'

# Standard library imports
import unittest

# Test class using unittest
class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        self.assertEqual(load_data('data.csv'), 'Data loaded successfully')

    def test_load_data_non_existent(self):
        self.assertEqual(load_data('non_existent.csv'), 'File not found')

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()