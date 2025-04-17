# Source code being tested (copied directly into the script)
def remove_whitespace(s):
    return ''.join(s.split())

# Standard library imports
import unittest

# Test class using unittest
class TestRemoveWhitespace(unittest.TestCase):

    def test_remove_whitespace_empty(self):
        self.assertEqual(remove_whitespace(""), "")

    def test_remove_whitespace_single_char(self):
        self.assertEqual(remove_whitespace("a"), "a")

    def test_remove_whitespace_multiple_chars(self):
        self.assertEqual(remove_whitespace("hello world"), "helloworld")

    def test_remove_whitespace_special_chars(self):
        self.assertEqual(remove_whitespace("!@#$% "), "!@#$%")

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()