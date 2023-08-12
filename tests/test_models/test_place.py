#!/usr/bin/python3
"""
The test_place module tests the place module from the models package
"""
from unittest import TestCase
from models.place import Place


class TestPlace(TestCase):
    """
    TestPlace class tests the Place class
    """

    def setUp(self):
        """ Sets up the initial conditions for each test case
        """
        self.place1 = Place()

    def test_Place(self):
        """ Tests the instantiation of a Place instance
        """

        self.assertEqual("", self.place1.city_id)
        self.assertEqual("", self.place1.user_id)
        self.assertEqual("", self.place1.name)
        self.assertEqual("", self.place1.description)
        self.assertEqual(0, self.place1.number_rooms)
        self.assertEqual(0, self.place1.number_bathrooms)
        self.assertEqual(0, self.place1.max_guest)
        self.assertEqual(0, self.place1.price_by_night)
        self.assertEqual(0.0, self.place1.latitude)
        self.assertEqual(0.0, self.place1.longitude)
        self.assertIsInstance(self.place1.amenity_ids, list)

        dict2 = {
                'id': 'a208e2d59534',
                'created_at': '2023-11-21T03:03:54.052298',
                'updated_at': '2023-11-21T03:03:54.052301',
                'city_id': '3fb55af41bfba',
                'user_id': 'fb51b27ebcfb1',
                'name': 'Casa Shifidi',
                'number_rooms': 8,
                'number_bathrooms': 4,
                'price_by_night': 235.85
            }
        place2 = Place(**dict2)
        self.assertEqual('3fb55af41bfba', place2.city_id)
        self.assertEqual("fb51b27ebcfb1", place2.user_id)
        self.assertIsInstance(place2.number_rooms, int)
        self.assertIsInstance(place2.number_bathrooms, int)
        self.assertIsInstance(place2.price_by_night, float)
        self.assertNotIn('description', place2.to_dict())
        self.assertNotIn('latitude', place2.to_dict())
        self.assertNotIn('longitude', place2.to_dict())
