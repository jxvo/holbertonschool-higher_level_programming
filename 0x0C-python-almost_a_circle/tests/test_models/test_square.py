#!/usr/bin/python3
"""Test module for square model"""

import os
import unittest
import importlib
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square



class TestSquare(unittest.TestCase):
    """contains methods that test and sometimes break our Square class"""

    def set_up(self):
        importlib.reload(models)
