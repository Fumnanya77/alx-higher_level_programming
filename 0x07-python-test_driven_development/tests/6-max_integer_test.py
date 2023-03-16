#!/usr/bin/python3
"""Test Cases on the maxium integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing the `max_integer` function"""
    def test_max_integer(self):
        self.assertEqual(max_integer([]), None)
		self.assertEqual(max_integer(list) == 1, list[0])


if __name__=__main__:
    unittest.main()
