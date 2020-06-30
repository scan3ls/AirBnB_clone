#!/usr/bin/python3
""" JSON Module """

import json


class FileStorage():
    """
        [de]serialized instances to and from a JSON file

        Attributes:
            __file_path: private str - path to JSON file
            __objects: private dict - store all objects
                       by <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return the dict __objects """
        return type(self).__objects

    def new(self, obj):
        """ sets in __objects the obj with key
            <obj class name>.id
        """

        key = type(obj).__name__ + "." + obj.id
        value = obj.to_dict()
        type(self).__objects[key] = value

    def save(self):
        """ serializes __objects to JSON file """

        with open(type(self).__file_path, 'w') as f:
            json.dump(type(self).__objects, f)

    def reload(self):
        """ deserialize the JSON file to __objects """
        try:
            with open(type(self).__file_path, 'r') as f:
                type(self).__objects = json.load(f)
        except:
            pass
