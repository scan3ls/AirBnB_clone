#!/usr/bin/python3
""" Module for amenity test """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """ Test for amenity class """

    def test_amenity_inheritance(self):
        """ test for BaseModel Inheritance """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attributes(self):
        """ test for correct attributes """
        amenityName = Amenity()
        amenityList = dir(amenityName)
        result = True
        checkList = [
            'name',
            'created_at',
            'updated_at',
            'id'
        ]
        for item in checkList:
            if item not in amenityList:
                result = False
                break
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
