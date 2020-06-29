#!/usr/bin/python3
""" State module """

from .base_model import BaseModel


class State(BaseModel):
    """ State Attributes """

    name = ""

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(**kwargs)
