#!/usr/bin/python3
"""test module for city class"""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestCity(unittest.TestCase):

    """tests for ye olde City"""

    def setUp(self):
        """set it up"""
        pass

    def tearDown(self):
        """tear it all down"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """start fresh with storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """test creating an instance and what it is"""

        rat = City()
        self.assertEqual(str(type(rat)), "<class 'models.city.City'>")
        self.assertIsInstance(rat, City)
        self.assertTrue(issubclass(type(rat), BaseModel))

    def test_attributes(self):
        """test attributes of the city class"""
        rat = City()
        self.assertTrue(rat.state_id == "")
        self.assertTrue(rat.name == "")

if __name__ == "__main__":
    unittest.main()
