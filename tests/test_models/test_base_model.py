#!/usr/bin/python3
"""
test_base_model module
tests the base_model module from the models package
"""
import unittest
from models.base_model import BaseModel
import re
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Tests the BaseModel class
    """

    def setUp(self):
        """ Sets up the initial conditions of each test case
        """
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_BaseModel(self):
        """ Tests the instantation of a BaseModel instance
        """
        self.assertIsInstance(self.b1, BaseModel)
        self.assertIsInstance(self.b2, BaseModel)
        self.assertIsInstance(self.b1.id, str)
        self.assertIsInstance(self.b2.id, str)
        self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)

    def test_str(self):
        """ Tests the method __str__ that returns the string representation
        of the BaseModel instance
        """
        str1 = str(self.b1)
        exp_str = "[BaseModel] ({}) {}".format(self.b1.id, self.b1.__dict__)
        self.assertEqual(exp_str, str1)
        pass

    def test_to_dict(self):
        """ Tests the to_dict method that returns dictionary of all the
        key/values of the BaseModel instance
        """
        dict1 = self.b1.to_dict()
        self.assertIsInstance(dict1, dict)
        self.assertEqual(dict1.get('__class__'), 'BaseModel')

        fmt_match = re.search(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$",
                              dict1['updated_at'])
        self.assertIsNotNone(fmt_match)
        fmt_match = re.search(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$",
                              dict1['created_at'])
        self.assertIsNotNone(format_match)
