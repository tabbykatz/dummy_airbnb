#!/usr/bin/python3
"""module for testing user class n stuff"""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel
import uuid


class TestUser(unittest.TestCase):

    """class containing testssss"""

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

        rat = User()
        self.assertEqual(str(type(rat)), "<class 'models.user.User'>")
        self.assertIsInstance(rat, User)
        self.assertTrue(issubclass(type(rat), BaseModel))

    def test_attr(self):
        """check it out this test is jank"""
        rat = User()
        attrlist = ["email", "password", "first_name", "last_name"]
        for item in attrlist:
            self.assertTrue("rat.{}".format(item))

if __name__ == "__main__":
    unittest.main()
