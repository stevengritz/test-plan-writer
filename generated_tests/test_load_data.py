# Source code being tested (copied directly into the script)
import pandas as pd

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return 'Data loaded successfully'
    except FileNotFoundError:
        return 'File not found'

# Standard library imports
import unittest
import os

# Test class using unittest
class TestLoadData(unittest.TestCase):
    def test_load_data(self):
        # Create a test file
        with open('data.csv', 'w') as f:
            f.write('col1,col2\n1,2')
        self.assertEqual(load_data('data.csv'), 'Data loaded successfully')
        os.remove('data.csv')

    def test_load_data_non_existent(self):
        self.assertEqual(load_data('non_existent_file.csv'), 'File not found')

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()