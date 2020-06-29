#!/usr/bin/python3
""" Review module """

from .base_model import BaseModel


class Review(BaseModel):
    """ Review Attributes """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ constructor """
        super().__init__(**kwargs)
