#!/usr/bin/python3
"""Test module for rectangle model"""

import unittest
import io
import contextlib
import importlib
import models
from models.base import Base
from models.rectangle import Rectangle



class TestRectangle(unittest.TestCase):
    """contains methods designed to test our Rectangle class"""

    def setUp(self):
        """reset all of our class modules"""
        importlib.reload(models.base)
        importlib.reload(models.rectangle)

    def tearDown(self):
        """resets global obj count so correct ID is output everytime"""
        Base._Base__nb_objects = 0
        self.assertEqual(Base._Base__nb_objects, 0)

    def test_init(self):
        """test instantiation with id attritbute"""
        r_wh = Rectangle(1, 2)
        r_std = Rectangle(2, 4, 0, 0)
        r_all = Rectangle(3, 6, 2, 2, 99)
        with self.assertRaises(TypeError):
            r_str = Rectangle("two", "three", 0, 0, "99")
            r_neg = Rectangle(-1, -2, 0, 0, -99)
            r_none = Rectangle(None)
            r_empty = Rectangle()

        self.assertEqual(r_wh.id, 1)
        self.assertEqual(r_std.id, 2)
        self.assertEqual(r_all.id, 99)

    def test_str(self):
        """test rectangle's __str__ method"""

        tstr_std = Rectangle(1, 2)
        tstr_all = Rectangle(3, 6, 2, 2, 99)

        self.assertEqual(tstr_std.__str__(), '[Rectangle] (1) 0/0 - 1/2')
        self.assertEqual(tstr_all.__str__(), '[Rectangle] (99) 2/2 - 3/6')

    def test_area(self):
        """test area"""
        ta_std = Rectangle(2, 3)
        ta_all = Rectangle(4, 6, 0, 0, 99)

        self.assertEqual(ta_std.area(), 6)
        self.assertEqual(ta_all.area(), 24)

    def test_display(self):
        """test display"""

        output = io.StringIO()

        td_std = Rectangle(3, 5)
        td_all = Rectangle(3, 5, 0, 1, 99)

        std_expected = "###\n###\n###\n###\n###\n"
        all_expected = "\n###\n###\n###\n###\n###\n"

        with self.subTest():
            with contextlib.redirect_stdout(output):
                td_std.display()
            self.assertEqual(output.getvalue(), std_expected)

        output.truncate(0)
        output.seek(0)

        with self.subTest():
            with contextlib.redirect_stdout(output):
                td_all.display()
            self.assertEqual(output.getvalue(), all_expected)

    def test_update(self):
        """test update method"""
        tu_std = Rectangle(1, 2)
        tu_all = Rectangle(2, 4, 0, 0, 99)

        tu_std.update()
        self.assertEqual(tu_std.__str__(), '[Rectangle] (1) 0/0 - 1/2')

        tu_std.update(77, 3, 6, 1, 1)
        self.assertEqual(tu_std.__str__(), '[Rectangle] (77) 1/1 - 3/6')

        tu_all.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(tu_all.__str__(), '[Rectangle] (89) 3/4 - 1/2')

    def test_to_dictionary(self):
        """test to dictionary method"""
        ttd_std = Rectangle(2, 3)
        ttd_all = Rectangle(3, 6, 1, 1, 99)

        expected_std = {'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0}
        expected_all = {'id': 99, 'width': 3, 'height': 6, 'x': 1, 'y': 1}

        self.assertDictEqual(ttd_std.to_dictionary(), expected_std)
        self.assertDictEqual(ttd_all.to_dictionary(), expected_all)
