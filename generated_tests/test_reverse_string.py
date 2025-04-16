
# Source code being tested (copied directly into the script)
def reverse_string(s):
    if not isinstance(s, str):
        raise ValueError('Input must be a string')
    return s[::-1]

# Standard library imports
import unittest

# Test class using unittest
class TestReverseString(unittest.TestCase):

    def test_reverse_string_normal_cases(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string(''), '')
        self.assertEqual(reverse_string('12345'), '54321')

    def test_reverse_string_edge_cases(self):
        with self.assertRaises(ValueError) as cm:
            reverse_string(None)
        self.assertEqual(str(cm.exception), 'Input must be a string')

        with self.assertRaises(ValueError) as cm:
            reverse_string(123)
        self.assertEqual(str(cm.exception), 'Input must be a string')

# Boilerplate to run tests
if __name__ == '__main__':
    unittest.main()