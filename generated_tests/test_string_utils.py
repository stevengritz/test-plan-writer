# Source code being tested (copied directly into the script)
def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

# Standard library imports
import unittest

# Test class using unittest
class TestStringUtils(unittest.TestCase):
    def test_to_uppercase(self):
        self.assertEqual(to_uppercase('hello'), 'HELLO')
        self.assertEqual(to_uppercase('WORLD'), 'WORLD')

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase('HELLO'), 'hello')
        self.assertEqual(to_lowercase('WORLD'), 'world')

    # Edge case: Test with empty string
    def test_to_uppercase_empty_string(self):
        self.assertEqual(to_uppercase(''), '')

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()