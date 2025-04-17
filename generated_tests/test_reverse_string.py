# Source code being tested (copied directly into the script)
def reverse_string(s):
    return s[::-1]

# Standard library imports
import unittest

# Test class using unittest
class TestReverseString(unittest.TestCase):

    def test_reverse_string_empty(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_single_char(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_string_multiple_chars(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_string_special_chars(self):
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()