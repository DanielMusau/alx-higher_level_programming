#!/usr/bin/python3
"""Module consists of a class Base"""


class Base:
    """Class name Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """classs instantiation."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
