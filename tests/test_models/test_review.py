#!/usr/bin/python3
""" Module for review test """

import unittest
from models.base_model import BaseModel
from models.review import Review


class test_review(unittest.TestCase):
    """ Test for review class """

    def test_review_inheritance(self):
        """ test for BaseModel Inheritance """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """ test for correct attributes """
        reviewName = Review()
        reviewList = dir(reviewName)
        result = True
        checkList = [
            'place_id',
            'user_id',
            'text',
            'created_at',
            'updated_at',
            'id'
        ]
        for item in checkList:
            if item not in reviewList:
                result = False
                break
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
