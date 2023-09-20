#!/usr/bin/python3
"""unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):

    def test_positive_max(self):
        self.assertEqual(max_integer([4, 30, 14]), 30)

    def test_negative_max(self):
        self.assertEqual(max_integer([-4, -30, -14]), -4)

    def test_middle_max(self):
        self.assertEqual(max_integer([4, 30, 14]), 30)

    def test_end_max(self):
        test_max = max_integer([14, 30, 4])
        self.assertEqual(test_max, 30, "should return max if element at end")

    def test_one_element(self):
        self.assertEqual(max_integer([6]), 6)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_list_nothing(self):
        self.assertEqual(max_integer(), None)
