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

    def test_init_such_args(self):
        """such args. much wow."""
        pass

    def test_datetime_creation(self):
        """checking for datetime function"""
        rat = BaseModel()
        date = datetime.now()
        difference = rat.updated_at - rat.created_at
        self.assertTrue(abs(difference.total_seconds()) < 0.01)
        difference = rat.created_at - date
        self.assertTrue(abs(difference.total_seconds()) < 0.1)

    def test_ids_special(self):
        """test for unique ids"""
        rat = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(rat)), len(rat))



if __name__ == '__main__':
    unittest.main()
