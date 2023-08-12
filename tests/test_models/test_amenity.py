#!/usr/bin/python3
"""
The test_amenity module tests the amenity module from the models package
"""
from unittest import TestCase
from models.amenity import Amenity


class TestAmenity(TestCase):
    """
    TestAmenity class tests the Amenity class
    """

    def setUp(self):
        """ Sets up the initial conditions for each test case
        """
        self.amenity1 = Amenity()

    def tearDown(self):
        """ Tears down test conditions after each test
        """
        del self.amenity1

    def test_Amenity(self):
        """ Tests the instantiation of an Amenity instance
        """
        self.amenity1
        self.assertEqual("", self.amenity1.name)
        self.assertNotIn('name', self.amenity1.to_dict())

        dict2 = {
                'id': 'cac66cd4-bd96-4161-b54a-a208e2d59534',
                'created_at': '2019-05-28T21:03:54.052298',
                'updated_at': '2019-05-28T21:03:54.052301',
                'name': 'Swimming Pool',
            }
        amenity2 = Amenity(**dict2)
        self.assertEqual(amenity2.to_dict()['name'], 'Swimming Pool')
