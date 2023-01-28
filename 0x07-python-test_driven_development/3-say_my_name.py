#!/usr/bin/python3
""" Module contains a function that
prints the first and last name of a user.
"""


def say_my_name(first_name, last_name=""):
    """ Function that prints name """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
