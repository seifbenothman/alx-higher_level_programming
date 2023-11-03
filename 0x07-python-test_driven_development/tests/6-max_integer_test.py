#!/usr/bin/python3
"""
Unittest
"""

import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max int empty list"""
    def test_max_integer_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_max_integer_single_element_list(self):
        """Test single elem"""
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_max_integer_positive_values(self):
        """Test positive V"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_max_integer_mixed_values(self):
        """Test mixed V"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_max_integer_negative_values(self):
        """Test Negative V"""
        result = max_integer([-1, -3, -4, -2])
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
