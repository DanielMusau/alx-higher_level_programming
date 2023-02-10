#!/usr/bin/python3
""" Module contains class Rectangle that inherits
from Base. """
from models.base import Base


class Rectangle(Base):
    """ Class Rectangle that inherits from Base. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization. """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width property getter. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width property setter. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Height property getter. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height property setter. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ x property getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x property setter. """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y property getter. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y property setter. """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle. """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the rect with character #. """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print()
