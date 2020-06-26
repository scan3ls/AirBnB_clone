#!/usr/bin/python3
""" initialize file storage """

from .engine import file_storage

storage = file_storage.FileStorage()

storage.reload()
