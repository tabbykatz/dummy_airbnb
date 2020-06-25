#!/usr/bin/python3
"""unit tests module for our BaseModel Class"""

from models.base_model import BaseModel
from datetime import datetime
import uuid
import unittest

class TestBaseModel(unittest.TestCase):

    """tests for the BaseModel class"""

    def setUp(self):
        """to set it up"""
        pass

    def tearDown(self):
        """to tear it all down"""
        pass

    """Tests for instantiation"""
    def test_instance(self):
        """making a lab rat"""
        rat = BaseModel()
        self.assertEqual(str(type(rat)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(rat, BaseModel)
        self.assertTrue(issubclass(type(rat), BaseModel))

if __name__ == '__main__':
    unittest.main()
