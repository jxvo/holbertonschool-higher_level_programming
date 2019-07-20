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
        importlib.reload(models)

    def test_init(self):

    def test_create(self):

    def test_save_json(self):

    def test_load_json(self):

    def test_save_csv(self):

    def test_load_csv(self):

    def test_to_json_string(self):

    def test_from_json_string(self):

    def test_draw(self):
