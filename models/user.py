#!/usr/bin/python3
""" User module """

from .base_model import BaseModel


class User(BaseModel):
    """ User Attributes """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(**kwargs)
