#!/usr/bin/python3
"""module for out tests for state class"""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestState(unittest.TestCase):

    """class for tests for state """

    def setUp(self):
        """set it up"""
        pass

    def tearDown(self):
        """tear it down"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """start fresh with storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """is an instance what we like to see"""

        rat = State()
        self.assertEqual(str(type(rat)), "<class 'models.state.State'>")
        self.assertIsInstance(rat, State)
        self.assertTrue(issubclass(type(rat), BaseModel))

    def test_attr(self):
        """probably does nothing"""
        rat = State()
        self.assertTrue(rat.name == "")

if __name__ == "__main__":
    unittest.main()
