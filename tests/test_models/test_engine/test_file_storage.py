#!/usr/bin/python3
"""
test_file_storage module
Tests the module file_storage
"""
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Contain unittests for the FileStorage class
    """

    def setUp(self):
        """ Sets up the test initial conditions
        """
        pass

    def test_all(self):
        """ Tests the all() method that returns the private attribute
        __objects, a dictionary that store all objects
        """
        pass
    
    def test_new(self):
        """ Tests the new() method that sets in __objects an obj with
        the correct key based on the obj's class and its id
        """
        pass
    
    def test_save(self):
        """ Tests the method that serializes __objects dictionary to a JSON
        file
        """
        pass

    def test_reload(self):
        """ Tests the method that deserializes a JSON file to the
        __objects dictionary
        """
