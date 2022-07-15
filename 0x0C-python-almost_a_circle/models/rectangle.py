#!/usr/bin/python3
"""Module consists of a class Rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """class that inherits Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class instantiation."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("Width should be type int.")
        elif value < 0:
            raise ValueError("Width should be greater than zero")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("Height should be type int.")
        elif value < 0:
            raise ValueError("Height should be greater than zero")
        self.__height = value
    
    @property
    def x(self):
        """width getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x should be type int.")
        elif value < 0:
            raise ValueError("x should be greater than zero")
        self.__x = value
    
    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y should be type int.")
        elif value < 0:
            raise ValueError("y should be greater than zero")
        self.__y = value
