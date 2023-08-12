#!/usr/bin/python3
"""
The test_city module tests the city module from the models package
"""
from unittest import TestCase
from models.city import City


class TestCity(TestCase):
    """
    TestCity class tests the City class
    """

    def setUp(self):
        """ Sets up the initial conditions for each test case
        """
        self.city1 = City()

    def test_City(self):
        """ Tests the instantiation of a City instance
        """
        self.assertEqual("", self.city1.name)
        self.assertNotIn('state_id', self.city1.to_dict())
        self.assertNotIn('name', self.city1.to_dict())

        dict2 = {
                'id': 'cace66cd4-bd96-4161-b54a-a208e2d59534',
                'created_at': '2019-05-28T21:03:54.052298',
                'updated_at': '2019-05-28T21:03:54.052301',
                'name': 'Lubango',
            }
        city2 = City(**dict2)
        self.assertEqual(city2.to_dict()['name'], 'Lubango')
        self.assertNotIn('state_id', city2.to_dict())
