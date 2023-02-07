#!/usr/bin/python3
""" Module contains a function that adds
a new attribute to an object if it's possible.
"""


def add_attribute(obj_val, name, value):
    """ Function that adds a new attribute
    to an object. """
    if not hasattr(obj_val, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj_val, name, value)
