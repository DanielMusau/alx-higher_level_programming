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
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width value.

        Returns:
            width of the rectangle


        """
        return self.__width

    @width.setter
    def width(self, value):
        """Validates the width value got earlier.

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if the width is less than zero


        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the height value.

        Returns:
            height of the rectangle.


        """
        return self.__height

    @height.setter
    def height(self, value):
        """Validates the height value got earlier.

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than zero.


        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
