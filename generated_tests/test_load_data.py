# Source code being tested (copied directly into the script)
import os

def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return 'Loaded data successfully'
    except FileNotFoundError:
        return 'File not found'

# Standard library imports
import unittest

# Test class using unittest
class TestLoadData(unittest.TestCase):
    def setUp(self):
        with open('temp_data.csv', 'w') as f:
            f.write('test data')

    def tearDown(self):
        os.remove('temp_data.csv')

    def test_load_data(self):
        self.assertEqual(load_data('temp_data.csv'), 'Loaded data successfully')

    def test_load_data_non_existent(self):
        self.assertEqual(load_data('non_existent.csv'), 'File not found')

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()