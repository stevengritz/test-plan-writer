import unittest
from utils.string_utils import reverse_string, count_vowels, is_palindrome

class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels(""), 0)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("")) # Empty string is considered a palindrome
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

if __name__ == '__main__':
    unittest.main()
