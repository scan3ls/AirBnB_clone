#!/usr/bin/python3
""" file storage test module """

import unittest
import json
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review


class test_FileStorage(unittest.TestCase):
    """ test class """

    def save_main(self):
        """ move main file to temp """
        # move main file
        try:
            os.rename("file.json", "tmp_jFile")
        except:
            pass

    def load_main(self):
        """ move main file from temp """
        try:
            os.rename("tmp_jFile", "file.json")
        except:
            pass

    def test_BuildFile(self):
        """ test file creation """

        # move main file
        self.save_main()

        base = BaseModel()
        base.save()
        try:
            f = open("file.json", 'r')
        except FileNotFoundError:
            print("File storage build failed")
            return
        f.close()
        os.remove("file.json")

        # restore main file
        self.load_main()

    def test_isjson(self):
        """ test if contents are json """

        # move main file
        self.save_main()

        # build json file
        base = BaseModel()
        base.save()

        with open("file.json", 'r') as f:
            string = json.load(f)
        self.assertTrue(string is not None)

        # destroy json file and move main file back
        os.remove("file.json")
        self.load_main()

    def test_attributes(self):
        """ verify class attributes """
        check_list = [
            "_FileStorage__file_path",
            "_FileStorage__objects"
        ]

        storage = FileStorage()
        dictionary = dir(storage)
        result = True

        for item in check_list:
            if item not in dictionary:
                result = False
                print("\t!!!{}!!!".format(item))
                break

        self.assertTrue(result)

    def test_functions(self):
        """ verify class functions """
        check_list = [
            "all",
            "new",
            "save",
            "reload"
        ]

        storage = FileStorage()
        dictionary = dir(storage)
        result = True

        for item in check_list:
            if item not in dictionary:
                result = False
                print("\t!!!{}!!!".format(item))
                break

        self.assertTrue(result)

    def test_basemodel(self):
        """ test basemodel json """
        self.build_obj("BaseModel")

    def build_obj(self, obj):
        """ Build obj and load to a temp json file """
        objects = {
            "BaseModel": BaseModel
        }

        self.save_main()

        new_obj = objects[obj]()
        new_obj.save()
        with open("file.json", 'r') as f: 
            string = f.read()
        os.remove("file.json")

        self.load_main()

if __name__ == "__main__":
    unittest.main()
