#!/usr/bin/python3
"""
This module contains a class that defines a Rectangle.
"""


class Rectangle:
    """A class that defines a Rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the class and all its instances.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get method that retrieves the width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width value after validating it.
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
        """Validates the height value got earlier.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """Returns the rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """Method to print the rectangle with the character # """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle
        else:
            for i in range(self.height):
                rectangle += ("#" * self.width) + "\n"

            return rectangle[:-1]

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method that prints a message when the instance is deleted """
        print("Bye rectangle...")
