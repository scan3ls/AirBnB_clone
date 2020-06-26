#!/usr/bin/python3
""" module for base class """
from uuid import uuid4
from datetime import datetime
from .__init__ import storage


class BaseModel():
    """ BaseModel class- Main class """
    def __init__(self, *args, **kwargs):
        """ constructor """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs.items()) <= 0:
            storage.new(self)
            return

        for key, value in kwargs.items():
            if key == "__class__":
                continue
            if key == "created_at" or key == "updated_at":
                value = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)

    def __str__(self):
        """ str print friendly version of repr """
        return "[{}] ({}) {}"\
            .format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Pub inst method """
        self.updated_at = datetime.now()

        storage.new(self)
        storage.save()
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
