#!/usr/bin/python3
"""
The test_user module tests the user module from the models package
"""
from unittest import TestCase
from models.user import User


class TestUser(TestCase):
    """
    TestUser class tests the User class
    """

    def setUp(self):
        """ Sets up the initial conditions for each test case
        """
        self.user1 = User();

    def tearDown(self):
        """ Tears down tests conditions and objects after each test
        """
        del self.user1

    def test_User(self):
        """ Tests the instantiation of a User instance
        """
        self.assertIsInstance(self.user1.id, str)
        self.assertIsNotNone(self.user1.created_at)
        self.assertIsNotNone(self.user1.updated_at)

        self.assertEqual("", self.user1.email)
        self.assertEqual("", self.user1.password)
        self.assertEqual("", self.user1.first_name)
        self.assertEqual("", self.user1.last_name)

        dict2 = {
                'id': 'cac66cd4-bd96-4161-b54a-a208e2d59534',
                'created_at': '2019-05-28T21:03:54.052298',
                'updated_at': '2019-05-28T21:03:54.052301',
                'email': 'gigi@kmail.na',
                'first_name': 'Hagrid'
            }
        user2 = User(**dict2)
        self.assertEqual(user2.id, 'cac66cd4-bd96-4161-b54a-a208e2d59534')
        # self.assertEqual(user2.created_at, '2019-05-28T21:03:54.052298')
        # self.assertEqual(user2.updated_at, '2019-05-28T21:03:54.052301')
        self.assertEqual(user2.email, 'gigi@kmail.na')
        self.assertEqual(user2.first_name, 'Hagrid')
        self.assertEqual(user2.last_name, "")
        self.assertNotIn('last_name', user2.to_dict())

    def test_str(self):
        """ Tests the string representation of a User instance
        """
        pass
