# Source code being tested (copied directly into the script)
def to_uppercase(s):
    return s.upper()

# Standard library imports
import unittest

# Test class using unittest
class TestToUppercase(unittest.TestCase):

    def test_to_uppercase_empty(self):
        self.assertEqual(to_uppercase(""), "")

    def test_to_uppercase_single_char(self):
        self.assertEqual(to_uppercase("a"), "A")

    def test_to_uppercase_multiple_chars(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")

    def test_to_uppercase_special_chars(self):
        self.assertEqual(to_uppercase("!@#$%"), "!@#$%")

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()