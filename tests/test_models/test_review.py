#!/usr/bin/python3
"""module for testing review class"""

import unittest
from datetime import datetime
import time
from models.review import Review
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestReview(unittest.TestCase):

    """class to write tests for review"""

    def setUp(self):
        """set it up, up, up"""
        pass

    def tearDown(self):
        """tear it down, down, down"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """start fresh with storage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """check that an instance is what we want it to be"""

        rat = Review()
        self.assertEqual(str(type(rat)), "<class 'models.review.Review'>")
        self.assertIsInstance(rat, Review)
        self.assertTrue(issubclass(type(rat), BaseModel))

    def test_attr(self):
        """check attribute existence"""
        rat = Review()
        self.assertTrue(rat.place_id == "")
        self.assertTrue(rat.user_id == "")
        self.assertTrue(rat.text == "")

if __name__ == "__main__":
    unittest.main()
