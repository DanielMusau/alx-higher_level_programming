#!/usr/bin/python3
""" Module contains class Square that inherits
from Rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square that inherits from Rectangle. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization of the square. """
        super().__init__(size, size, x, y)

    def __str__(self):
        """ Returns string representation of object. """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ Size getter. """
        return self.width

    @size.setter
    def size(self, value):
        """ Size setter. """
        self.width = value
        self.height = value
