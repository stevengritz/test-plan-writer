# Source code being tested (copied directly into the script)
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Standard library imports
import unittest

# Test class using unittest
class TestCountVowels(unittest.TestCase):

    def test_count_vowels_empty(self):
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_single_char(self):
        self.assertEqual(count_vowels("a"), 1)

    def test_count_vowels_multiple_chars(self):
        self.assertEqual(count_vowels("hello"), 2)

    def test_count_vowels_special_chars(self):
        self.assertEqual(count_vowels("!@#$%"), 0)

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()