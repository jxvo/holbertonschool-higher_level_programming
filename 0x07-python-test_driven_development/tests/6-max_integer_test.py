#!/usr/bin/python3
import unittest


class TestMaxInteger(unittest.TestCase):
    """test mthods for max_integer function"""
    def setUp(self):
        """ensures function is run properly before testing"""
        self.max_integer = __import__('6-max_integer').max_integer

    def test_max_in_the_middle(self):
        """tests standard operation"""
        test_list = [1, 2, 99, 3, 4]
        self.assertEqual(self.max_integer(test_list), 99)

    def test_max_at_the_end(self):
        """standard operation: max is at the end"""
        test_list = [1, 2, 3, 4, 99]
        self.assertEqual(self.max_integer(test_list), 99)

    def test_max_at_the_beginning(self):
        """standard operation: max is at the beginning"""
        test_list = [99, 1, 2, 3, 4]
        self.assertEqual(self.max_integer(test_list), 99)

    def test_max_one_negative(self):
        """standard operation: list containing one negative value"""
        test_list = [-99, 1, 2, 3, 4]
        self.assertEqual(self.max_integer(test_list), 4)

    def test_max_all_negative(self):
        """standard operation: list containing all negative values"""
        test_list = [-99, -1, -2, -3, -4]
        self.assertEqual(self.max_integer(test_list), -1)

    def test_max_one_element(self):
        """standard operation: list containing only one element"""
        test_list = [99]
        self.assertEqual(self.max_integer(test_list), 99)

    def test_arg_empty_list(self):
        """tests empty list argument"""
        self.assertIs(self.max_integer([]), None)

    def test_arg_noargs(self):
        """test no arguments"""
        self.assertIs(self.max_integer(), None)
