#!/usr/bin/python3
"""
This module consists of a class that defines a student.
"""


class Student:
    """Class that defines a student.
    """
    def __init__(self, first_name, last_name, age):
        """Initializing the class and it's instances.

        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method that retrieves a dictionary.
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj

            n_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        n_list[satr] = obj[satr]
            return n_list

        return obj
