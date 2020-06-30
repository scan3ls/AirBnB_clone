#!/usr/bin/python3
""" Module for city test """

import unittest
from models.base_model import BaseModel
from models.city import City


class test_city(unittest.TestCase):
    """ Test for city class """

    def test_city_inheritance(self):
        """ test for BaseModel Inheritance """
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """ test for correct attributes """
        cityName = City()
        cityList = dir(cityName)
        result = True
        checkList = [
            'name',
            'state_id',
            'created_at',
            'updated_at',
            'id'
        ]
        for item in checkList:
            if item not in cityList:
                result = False
                break
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
