#!/usr/bin/python3
""" Module contains the base of all other classes
in the project.
"""


class Base:
    """ Base class. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization. """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
