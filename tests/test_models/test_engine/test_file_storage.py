#!/usr/bin/python3
"""
test_file_storage module
Tests the module file_storage
"""
from unittest import TestCase
from unittest.mock import mock_open, patch
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(TestCase):
    """
    Contain unittests for the FileStorage class
    """

    def setUp(self):
        """ Sets up the test initial conditions
        """
        storage._FileStorage__objects = {}

    def test_all(self):
        """ Tests the all() method that returns the private attribute
        __objects, a dictionary that store all objects
        """
        self.assertIsInstance(storage.all(), dict)
        self.assertEqual(0, len(storage.all()))
        bm1 = BaseModel()
        self.assertEqual(1, len(storage.all()))

    def test_new(self):
        """ Tests the new() method that sets in __objects an obj with
        the correct key based on the obj's class and its id
        """
        self.assertEqual(0, len(storage.all()))

        storage.new(BaseModel())
        self.assertEqual(1, len(storage.all()))
        storage.new(User())
        self.assertEqual(2, len(storage.all()))

        storage.new(None)
        self.assertEqual(2, len(storage.all()))

    def test_save(self):
        """ Tests the method that serializes __objects dictionary to a JSON
        file
        """
        bm1 = BaseModel()
        user1 = User()
        with patch('builtins.open', create=True) as my_mock:
            storage.save()
            my_mock.assert_called_once_with("file.json", "w", encoding="utf-8")

    def test_reload(self):
        """ Tests the method that deserializes a JSON file to the
        __objects dictionary
        """
        # Empty file
        m_open = mock_open(read_data=None)
        with patch('builtins.open', m_open):
            self.assertEqual(0, len(storage.all()))
            storage.reload()
            self.assertEqual(0, len(storage.all()))

        # File exists
        file_contents = "".join(['{"BaseModel.746522df25ff": ',
                                 '{"id": "746522df25ff", ',
                                 '"created_at": ',
                                 '"2023-08-13T10:52:58.645656", ',
                                 '"updated_at": ',
                                 '"2023-08-13T10:52:58.646607", ',
                                 ' "__class__": "BaseModel"}}'])
        m_open = mock_open(read_data=file_contents)
        with patch('builtins.open', m_open):
            self.assertEqual(0, len(storage.all()))
            storage.reload()
            self.assertEqual(1, len(storage.all()))
            self.assertIn('BaseModel.746522df25ff', storage.all())
            obj = storage.all()['BaseModel.746522df25ff']
            self.assertIsInstance(obj, BaseModel)
            self.assertNotIsInstance(obj, User)
