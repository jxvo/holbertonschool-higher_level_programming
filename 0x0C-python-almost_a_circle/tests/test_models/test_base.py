#!/usr/bin/python3
"""Test module for base model"""

import os
import unittest
import importlib
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestBase(unittest.TestCase):
    """contains methods that test and sometimes break our Base class"""

    def set_up(self):
        """reset all of our class modules"""
        importlib.reload(models.base)
        importlib.reload(models.rectangle)
        importlib.reload(models.square)

    def test_init(self):
        """test instantiation with id attritbute"""
        b_std = Base()
        b_none = Base(None)
        b_num = Base(99)
        """b_float = Base(float('inf'))
        b_str = Base("nine")
        b_list = Base([1, 2.5, "three"])
        """

        self.assertEqual(b_std.id, 1)
        self.assertEqual(b_none.id, 2)
        self.assertEqual(b_num.id, 99)

    def test_create(self):
        """test create method"""
        pass

    def test_save_json(self):
        """test save to JSON method"""
        tsj_std = [{"id": 12}]
        tsj_exp = [{"betty": 999, "holberton": 777}]
        tsj_empty = []
        tsj_none = None

        self.assertCountEqual(Base.to_json_string(tsj_std), '[{'id': 12}]')
        self.assertCountEqual(Base.to_json_string(tsj_exp),
                              '[{"betty": 999, "holberton": 777}]')
        self.assertCountEqual(Base.to_json_string(tsj_std), '[]')
        self.assertCountEqual(Base.to_json_string(tsj_std), '[]')

    def test_load_json(self):
        """test load from JSON method"""
        tlj_std = [{"id": 3}]
        tlj_exp = [{"betty": 999, "holberton": 777}]
        tlj_empty = []
        tlj_none = None

        self.assertEqual(Base.from_json_string(
            Base.to_json_string(tlj_std)), tlj_std)
        self.assertEqual(Base.from_json_string(
            Base.to_json_string(tlj_exp)), tlj_exp)
        self.assertEqual(Base.from_json_string(
            Base.to_json_string(tlj_empty)), tlj_empty)
        self.assertEqual(Base.from_json_string(
            Base.to_json_string(tlj_none)), tlj_none)

    """def test_save_csv(self):

    def test_load_csv(self):

    def test_to_json_string(self):

    def test_from_json_string(self):

    def test_draw(self):
"""
