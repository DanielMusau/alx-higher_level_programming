#!/usr/bin/python3
"""
This module consists of a class that defines a rectangle.
"""


class Rectangle:
    """A class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initializes the class and its instances.
            Args:
                height (int): height of the rectangle.
                width (int): width of the rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Gets the height value.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Validates the height value got earlier.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
    @property
    def width(self):
        """Gets the width value.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Validates the width value got earlier.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
