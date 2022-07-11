#!/usr/bin/python3
"""
This module consists of a function that creates an Object from
a JSON file.
"""
import json


def load_from_json_file(filename):
    """function that creates an Object from aJSON file

    Args:
        filename: JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file_r:
        return json.load(file_r)
