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

    def test_init_no_args(self):
        """init no args please"""
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
        msg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)


if __name__ == '__main__':
    unittest.main()
