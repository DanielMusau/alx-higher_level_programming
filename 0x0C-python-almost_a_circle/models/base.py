#!/usr/bin/python3
""" Module contains the base of all other classes
in the project.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a JSON string representation of
        list_dictionaries. """
        res = "[]"
        if list_dictionaries == None:
            return res
        else:
            return json.dumps(list_dictionaries)
