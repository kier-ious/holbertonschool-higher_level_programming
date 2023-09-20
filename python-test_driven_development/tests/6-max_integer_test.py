#!/usr/bin/python3
"""unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestStringMethods(unittest.TestCase):

    def test(self):
        self.assertTrue(max_integer)

    def positive_max(self):
        self.assertEqual(max_integer([4, 30, 14]), 60)

    def negative_max(self):
        self.assertEqual(max_integer([-4, -30, -14]), -60)

    def middle_max(self):
        self.assertEqual(max_integer([4, 30, 14]), 60)

    def end_max(self):
        test_max = max_integer([14, 30, 4])
        self.assertEqual(test_max, 30, "should return max if element at end")

    def one_element(self):
        self.assertEqual(max_integer([6]), 6)

    def list_empty(self):
        self.assertEqual(max_integer([]), None)

    def list_nothing(self):
        self.assertEqual(max_integer(), None)
