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
        self.__width = value

    @property
    def height(self):
        """ Height property getter. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height property setter. """
        self.__height = value

    @property
    def x(self):
        """ x property getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x property setter. """
        self.__x = value

    @property
    def y(self):
        """ y property getter. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Y property setter. """
        self.__y = value
