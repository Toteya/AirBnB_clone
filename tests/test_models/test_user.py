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
        pass

    def test_User(self):
        """ Tests the instantiation of a User instance
        """
        user1 = User()

        self.assertIsInstance(user1.id, str)
        self.assertIsNotNone(user1.created_at)
        self.assertIsNotNone(user1.updated_at)

        self.assertEqual("", user1.email)
        self.assertEqual("", user1.password)
        self.assertEqual("", user1.first_name)
        self.assertEqual("", user1.last_name)

        user2 = User(**user1.to_dict())
        self.assertEqual(user1.id, user2.id)

    def test_str(self):
        """ Tests the string representation of a User instance
        """
        pass

