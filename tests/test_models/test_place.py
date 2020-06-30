#!/usr/bin/python3
""" Module for place test """

import unittest
from models.base_model import BaseModel
from models.place import Place


class test_place(unittest.TestCase):
    """ Test for place class """

    def test_place_inheritance(self):
        """ test for BaseModel Inheritance """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """ test for correct attributes """
        placeName = Place()
        placeList = dir(placeName)
        result = True
        checkList = [
            'city_id',
            'user_id',
            'name',
            'description',
            'number_rooms',
            'number_bathrooms',
            'max_guest',
            'price_by_night',
            'latitude',
            'longitude',
            'amenity_ids',
            'created_at',
            'updated_at',
            'id'
        ]
        for item in checkList:
            if item not in placeList:
                result = False
                break
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
