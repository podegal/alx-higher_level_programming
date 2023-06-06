#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the function
       max_integer
    """

    def test_max_int(self):
        """list of integers test
        """
        self.assertEqual(max_integer([4, 1, 5, 3]), 5)

    def test_repeat_int(self):
        """list with repeated number
        """
        self.assertEqual(max_integer([90, 90, 30, 30]), 90)

    def test_single_list(self):
        """List with only one element
        """
        self.assertEqual(max_integer([3]), 3)

    def test_empty_list(self):
        """Empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_max_start(self):
        """max at the beginning of the list
        """
        self.assertEqual(max_integer([60, 30, 20, 10]), 60)

    def test_sorted_list(self):
        """sorted list
        """
        self.assertEqual(max_integer([-2, 3, 13, 400]), 400)

    def test_neg_int(self):
        """list with negative integer
        """
        self.assertEqual(max_integer([-1, -2, -100, -50, -9]), -1)

    def test_float_number(self):
        """list containing float
        """
        self.assertEqual(max_integer([20, 90, -3, 29.6, -110.99]), 90)

    def test_zero_list(self):
        """list with only zero
        """
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_list_comp(self):
        """Comprehension list
        """
        self.assertEqual(max_integer([i * i for i in range(11)]), 100)

    def test_big_list(self):
        """big list
        """
        self.assertEqual(max_integer([
            10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
            110, 120, 130, 140, 150, 160, 170, 180,
            907, 308, 909, 910, 2000, 511, 912, 913,
            714, 515, 416, 917, 618, 319, 920, 999,
            908, 98, 99, 937, 97, 896, 96, 495, 95]), 2000)

    def test_string_list(self):
        """list containing a string
        """
        with self.assertRaises(TypeError):
            max_integer([1, '3', 4, '5'])

    def test_tuple(self):
        """tuple as list
        """
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)

    def test_tuple_list(self):
        """list containing a tuple
        """
        with self.assertRaises(TypeError):
            max_integer([1, (3, 9,) 4])

    def test_list_list(self):
        """list containing a list
        """
        with self.assertRaises(TypeError):
            max_integer([1, [4, 6], 2])

    def test_number(self):
        """passes a number as argument
        """
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_dict(self):
        """passes dict as argument
        """
        with self.assertRaises(KeyError):
            max_integer({'b': 2, 'c': 3})
