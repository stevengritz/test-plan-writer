# Source code being tested (copied directly into the script)
def is_palindrome(s):
    return s == s[::-1]

# Standard library imports
import unittest

# Test class using unittest
class TestIsPalindrome(unittest.TestCase):

    def test_is_palindrome_empty(self):
        self.assertTrue(is_palindrome(""))

    def test_is_palindrome_single_char(self):
        self.assertTrue(is_palindrome("a"))

    def test_is_palindrome_multiple_chars(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_is_palindrome_special_chars(self):
        self.assertFalse(is_palindrome("!@#$%"))

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()