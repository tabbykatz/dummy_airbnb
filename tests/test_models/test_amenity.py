#!/usr/bin/python3
"""tests module for Amenity class"""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestAmenity(unittest.TestCase):

    """a class full of tests for amenity"""

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
        """create an instance of this class?"""

        rat = Amenity()
        self.assertEqual(str(type(rat)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(rat, Amenity)
        self.assertTrue(issubclass(type(rat), BaseModel))

    def test_attributes(self):
        """ test existence of attributes"""
        rat = Amenity()
        #self.assertExists(rat.name)
if __name__ == "__main__":
    unittest.main()
