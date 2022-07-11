#!/usr/bin/python3
"""
This module consists of a function that writes an
Object to a text file using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file
       using JSON representation.

    Args:
        my_obj: Object to written
        filename: file to written to.
    """
    with open(filename, 'w', encoding='utf-8') as file_r:
        json.dump(my_obj, file_r)
