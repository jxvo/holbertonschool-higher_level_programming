#!/usr/bin/python3
"""Test module for rectangle model"""

import unittest
import io
import contextlib
import importlib
import models
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestSquare(unittest.TestCase):
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
        s_std = Square(5)
        s_kwa = Square(id=99, size=3)
        s_all = Square(5, 1, 1, 77)
        with self.assertRaises(TypeError):
            s_str = Square("two", 0, 0, "99")
            s_neg = Square(-1, -1, 0, -99)
            s_none = Rectangle(None)
            s_empty = Rectangle()

        self.assertEqual(s_std.id, 1)
        self.assertEqual(s_kwa.id, 99)
        self.assertEqual(s_all.id, 77)

    def test_str(self):
        """test rectangle's __str__ method"""

        tstr_std = Square(5)
        tstr_all = Square(3, 2, 2, 99)

        self.assertEqual(tstr_std.__str__(), '[Square] (1) 0/0 - 5')
        self.assertEqual(tstr_all.__str__(), '[Square] (99) 2/2 - 3')

    def test_area(self):
        """test area"""
        ta_std = Square(5)
        ta_all = Square(4, 0, 0, 99)
        ta_kwa = Square(id=77, size=3)

        self.assertEqual(ta_std.area(), 25)
        self.assertEqual(ta_all.area(), 16)
        self.assertEqual(ta_kwa.area(), 9)

    def test_display(self):
        """test display"""

        output = io.StringIO()

        td_std = Square(5)
        td_all = Square(5, 0, 1, 99)

        std_expected = "#####\n#####\n#####\n#####\n#####\n"
        all_expected = "\n#####\n#####\n#####\n#####\n#####\n"

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
        tu_std = Square(3)
        tu_all = Square(5, 0, 0, 99)

        tu_std.update()
        self.assertEqual(tu_std.__str__(), '[Square] (1) 0/0 - 3')

        tu_std.update(77, 7, 1, 1)
        self.assertEqual(tu_std.__str__(), '[Square] (77) 1/1 - 7')

        tu_all.update(**{ 'id': 89, 'size': 9, 'x': 3, 'y': 4 })
        self.assertEqual(tu_all.__str__(), '[Square] (89) 3/4 - 9')

    def test_to_dictionary(self):
        """test to dictionary method"""
        ttd_std = Square(5)
        ttd_all = Square(9, 1, 1, 99)

        expected_std = {'id': 1, 'size': 5, 'x': 0, 'y': 0}
        expected_all = {'id': 99, 'size': 9, 'x': 1, 'y': 1}

        self.assertDictEqual(ttd_std.to_dictionary(), expected_std)
        self.assertDictEqual(ttd_all.to_dictionary(), expected_all)
