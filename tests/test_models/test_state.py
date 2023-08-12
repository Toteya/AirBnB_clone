#!/usr/bin/python3
"""
The test_state module tests the state module from the models package
"""
from unittest import TestCase
from models.state import State


class TestState(TestCase):
    """
    Tests tests the State class
    """

    def setUp(self):
        """ Sets up the initial conditions for each test case
        """
        self.state1 = State()

    def test_State(self):
        """ Tests the instantiation of a State instance
        """
        self.assertEqual("", self.state1.name)
        self.assertNotIn('name', self.state1.to_dict())

        dict2 = {
                'id': 'cace66cd4-bd96-4161-b54a-a208e2d59534',
                'created_at': '2022-06-28T21:03:54.052298',
                'updated_at': '2022-06-28T21:03:54.052301',
                'name': 'Angola',
            }
        state2 = State(**dict2)
        self.assertEqual(state2.to_dict()['name'], 'Angola')
