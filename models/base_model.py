#!/usr/bin/python3
""" module for base class """
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ BaseModel class- Main class """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ str print friendly version of repr """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Pub inst method """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Pub inst method """
        my_dict = {}
        for key, value in self.__dict__.items():
            my_dict[key] = value
        my_dict["__class__"] = type(self).__name__
        created = self.created_at
        updated = self.updated_at
        my_dict["created_at"] = created.isoformat()
        my_dict["updated_at"] = updated.isoformat()
        return my_dict        
