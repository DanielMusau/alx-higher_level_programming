#!/usr/bin/python3
"""
This module contains a class that defines a Rectangle.
"""


class Rectangle:
    """A class that defines a Rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the class and all its instances.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that calculates the rectangle area """
        return self.width * self.height

    def perimeter(self):
        """Method that calculates the Rectangle perimeter. """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """Method that returns the Rectangle #"""
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"
        return rectangle[:-1]

    def __repr__(self):
        """Method that returns the string rep of the instance """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method that prints a message when the instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method that returns the bigger Rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
