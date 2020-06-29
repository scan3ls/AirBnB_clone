#!/usr/bin/python3
""" Amenity module """

from .base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity Attributes """

    name = ""

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(**kwargs)
