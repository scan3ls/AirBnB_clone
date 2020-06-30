#!/usr/bin/python3
""" Module for user test """

import unittest
from models.base_model import BaseModel
from models.user import User


class test_user(unittest.TestCase):
    """ Test for user class """

    def test_user_inheritance(self):
        """ test for BaseModel Inheritance """
        self.assertTrue(issubclass(User, BaseModel))

    def test_attributes(self):
        """ test for correct attributes """
        userName = User()
        userList = dir(userName)
        result = True
        checkList = [
            'email',
            'password',
            'first_name',
            'last_name',
            'created_at',
            'updated_at',
            'id'
        ]
        for item in checkList:
            if item not in userList:
                result = False
                break
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
