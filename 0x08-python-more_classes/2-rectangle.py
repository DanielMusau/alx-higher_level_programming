#!/usr/bin/python3
"""
This module consists of a class that defines a Rectangle.
"""


class Rectangle:
    """A class that defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """Initializes the class and it's instances.
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

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

    @property
    def height(self):
        """Gets the height value.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Validates the width value got earlier.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle.
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))
