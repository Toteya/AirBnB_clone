#!/usr/bin/python3
"""
test_base_model module
tests the base_model module from the models package
"""
import unittest
from models.base_model import BaseModel
import re

class TestBaseModel(unittest.TestCase):
    """ Tests the BaseModel class
    """

    def setUp(self):
        """ Sets up the initial conditions of each test case
        """
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def test_BaseModel(self):
        """ Tests the instantiation of a BaseModel instance
        """
        self.assertIsInstance(self.b1, BaseModel)
        self.assertIsInstance(self.b2, BaseModel)
        # self.assertIsInstance(self.b1.id, str)
        # self.assertIsInstance(self.b2.id, str)
        # self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertIsInstance(self.b1.created_at, str)
        self.assertIsInstance(self.b1.updated_at, str)
        self.assertEqual(self.b1.created_at, self.b1.updated_at)

        format_match = re.search("^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$",
                                 self.b1.updated_at)
        format_match = re.search("^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$",
                                 self.b1.created_at)
        self.assertIsNotNone(format_match)

    def test_str(self):
        """ Tests the method __str__ that returns the string representation
        of the BaseModel instance
        """
        pass

    def test_to_dict(self):
        """ Tests the to_dict method that returns dictionary of all the
        key/values of the BaseModel instance
        """
        dict1 = self.b1.to_dict()
        self.assertIsInstance(dict1, dict)
        self.assertIs(dict1.get('__class__'), BaseModel)
