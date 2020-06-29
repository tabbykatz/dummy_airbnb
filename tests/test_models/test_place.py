#!/usr/bin/python3
"""module for tests on Place class"""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid

class TestPlace(unittest.TestCase):

    """class containing tests for Place class"""

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
        """test that an instance is the right thing"""

        rat = Place()
        self.assertEqual(str(type(rat)), "<class 'models.place.Place'>")
        self.assertIsInstance(rat, Place)
        self.assertTrue(issubclass(type(rat), BaseModel))

    def test_attr(self):
        """check the attributes exist"""
        rat = Place()
        attrlist = ["city_id", "user_id", "name", "description", "number_rooms",
                "number_bathrooms", "max_guest", "price_by_night", "latitude",
               "longitude", "amenity_ids"]
        for item in attrlist:
            self.assertTrue("rat.{}".format(item))

if __name__ == "__main__":
    unittest.main()
