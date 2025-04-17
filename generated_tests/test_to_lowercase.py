# Source code being tested (copied directly into the script)
def to_lowercase(s):
    return s.lower()

# Standard library imports
import unittest

# Test class using unittest
class TestToLowercase(unittest.TestCase):

    def test_to_lowercase_empty(self):
        self.assertEqual(to_lowercase(""), "")

    def test_to_lowercase_single_char(self):
        self.assertEqual(to_lowercase("A"), "a")

    def test_to_lowercase_multiple_chars(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")

    def test_to_lowercase_special_chars(self):
        self.assertEqual(to_lowercase("!@#$%"), "!@#$%")

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()