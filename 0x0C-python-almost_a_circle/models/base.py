#!/usr/bin/python3
""" Module contains the base of all other classes
in the project.
"""
import json


class Base:
    """ Base class. """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization. """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a JSON string representation of
        list_dictionaries. """
        res = "[]"
        if list_dictionaries == None:
            return res
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation to
        list_objs to a file. """
        filename = f'{cls.__name__}.json'
        res = []
        
        if list_objs == None:
            pass
        else:
            for i in range(len(list_objs)):
                res.append(list_objs[i].to_dictionary())

        text = cls.to_json_string(res)

        with open(filename, 'w', encoding='UTF-8') as f:
            return f.write(text)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string
        representation json_string. """
        res = []

        if not json_string:
            return res
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Class method that returns an instance with all
        attributes already set. """
        if cls.__name__ == "Rectangle":
            dummy = cls(12, 12)
        else:
            dummy = cls(12)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Class method that returns a list of instances. """
        filename = f'{cls.__name__}.json'
        
        if filename == None:
            return []
        
        with open(filename, 'r', encoding='UTF-8') as f:
            list_text = f.read()
                
        cls_list = cls.from_json_string(list_text)
        inst_list = []
        
        for index in range(len(cls_list)):
            inst_list.append(cls.create(**cls_list[index]))

        return inst_list
