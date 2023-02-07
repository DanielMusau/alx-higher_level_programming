#!/usr/bin/python3
"""Module contains a MyInt Class that inherits from
the int class. """


class MyInt(int):
    """ Class that inherits from int class."""

    def __eq__(self, other):
        """ Method that returns != check """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """ Method that returns == check """
        return int.__eq__(self, other)
