#!/usr/bin/python3
"""
This module contains a class that defines a Square.
"""


class Square:
    """ A class that defines a Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class and all its instances.

            Args:
                size (int): size of the square.
                position (int): position of the cursor.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the value of the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Checks if the value of size got earlier is valid.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets the value of the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Checks if the value of position got earlier is valid.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the character '#'
        """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
                for i in range(0, self.size):
                    for k in range(self.position[0]):
                        print(" ", end='')
                    for j in range(self.size):
                        print("#", end='')
                    print()
