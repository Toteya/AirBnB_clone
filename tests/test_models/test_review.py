#!/usr/bin/python3
"""
The test_review module tests the review module from the models package
"""
from unittest import TestCase
from models.review import Review


class TestPlace(TestCase):
    """
    TestReview class tests the Review class
    """

    def setUp(self):
        """ Sets up the initial conditions for each test case
        """
        self.review1 = Review()

    def test_Review(self):
        """ Tests the instantiation of a Review instance
        """
        self.assertEqual("", self.review1.place_id)
        self.assertEqual("", self.review1.user_id)
        self.assertEqual("", self.review1.text)

        self.assertNotIn('place_id', self.review1.to_dict())
        self.assertNotIn('user_id', self.review1.to_dict())
        self.assertNotIn('text', self.review1.to_dict())

        dict2 = {
                'id': 'cace66cd4-bd96-4161-b54a-a208e2d59534',
                'created_at': '2022-06-28T21:03:54.052298',
                'updated_at': '2022-06-28T21:03:54.052301',
                'user_id': '59b3eb51bfba',
            }
        review2 = Review(**dict2)
        self.assertEqual(review2.to_dict()['user_id'], '59b3eb51bfba')
        self.assertNotIn('place_id', review2.to_dict())
        self.assertNotIn('text', review2.to_dict())
