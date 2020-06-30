#!/usr/bin/python3
""" Module for state test """

import unittest
from models.base_model import BaseModel
from models.state import State


class test_state(unittest.TestCase):
    """ Test for state class """

    def test_state_inheritance(self):
        """ test for BaseModel Inheritance """
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """ test for correct attributes """
        stateName = State()
        stateList = dir(stateName)
        result = True
        checkList = [
            'name',
            'created_at',
            'updated_at',
            'id'
        ]
        for item in checkList:
            if item not in stateList:
                result = False
                break
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
