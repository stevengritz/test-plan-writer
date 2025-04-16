# Source code being tested (copied directly into the script)
def reverse_string(s):
    return s[::-1]

# Standard library imports
import unittest

# Test class using unittest
class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string(''), '')
        self.assertEqual(reverse_string('12345'), '54321')

    def test_reverse_string_long(self):
        long_string = 'a' * 1000000
        self.assertEqual(reverse_string(long_string), long_string[::-1])

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()