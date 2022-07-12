#!/usr/bin/python3
"""Module consists of a class that defines a student"""


class Student:
    """Class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes the class and all its instances.
        Args:
            first_name: The first name of the student.
            last_name: the last name of the student.
            age: Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrievs a dictionary rep of
        a student instance."""
        n_dict = {}
        if type(attrs) == list:
            for i in attrs:
                if type(i) != str:
                    n_dict = self.__dict__
                    break
                n_dict[i] = getattr(self, i)
        else:
            n_dict = self.__dict__
        return (n_dict)

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance."""
        for i in json:
            self.__dict__[i] = json[i]
