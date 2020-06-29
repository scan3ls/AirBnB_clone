#!/usr/bin/python3
""" City module """

from .base_model import BaseModel


class City(BaseModel):
    """ City Attributes """

    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(**kwargs)
