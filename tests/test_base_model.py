#!/usr/bin/python3
""" Module for city test """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class test_BaseModel(unittest.TestCase):
    """ Test for BaseModel class """

    def test_attributes(self):
        """ test for correct attributes """
        base_modelName = BaseModel()
        base_modelList = dir(base_modelName)
        result = True
        checkList = [
            'created_at',
            'updated_at',
            'id'
        ]
        for item in checkList:
            if item not in base_modelList:
                result = False
                break
        self.assertTrue(result)

    def test__str__(self):
        """ test for __str__ repr """
        base_modelObj = BaseModel()
        typeObj = "[{}]".format(type(base_modelObj).__name__)
        base_id = "({})".format(base_modelObj.id)
        base_modelDict = "{}".format(base_modelObj.__dict__)
        strofbaseModel = str(base_modelObj)

        strobjList = strofbaseModel.split(" ")
        strtypeObj = strobjList.pop(0)
        stridObj = strobjList.pop(0)
        dictObjOnly = ' '.join(strobjList)

        self.assertEqual(typeObj, strtypeObj) 
        self.assertEqual(base_id, stridObj)
        self.assertEqual(base_modelDict, dictObjOnly)

    def test_save(self):
        """ test for save instance method """
        pass
        # base_modelObj = BaseModel()
        # base_modelObj.updated_at = datetime.now()
        # self.assertEqual(base_modelObj.updated_at, base_modelObj.save())

    def test_to_dict(self):
        """ test for to_dict instance method """
        base_modelObj = BaseModel()
        my_dict = {}
        for key, value in base_modelObj.__dict__.items():
            my_dict[key] = value
        my_dict["__class__"] = "BaseModel"
        created = base_modelObj.created_at
        updated = base_modelObj.updated_at
        my_dict["created_at"] = created.isoformat()
        my_dict["updated_at"] = updated.isoformat()
        to_dictObj = base_modelObj.to_dict()
        self.assertEqual(my_dict, to_dictObj)

if __name__ == "__main__":
    unittest.main()
