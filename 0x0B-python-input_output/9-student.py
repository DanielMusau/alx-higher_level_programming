#!/usr/bin/python3
"""
This module consists of a class that defines a student.
"""


class Student:
    """Class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initialization of the class and all it's instances.

        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age: the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function that retrieves a dictionary rep of
            a student instance.
        """
        return self.__dict__.copy()
