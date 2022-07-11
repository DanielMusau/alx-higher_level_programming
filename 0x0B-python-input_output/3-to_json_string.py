#!/usr/bin/python3
"""
This module consists of a function that returns
the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON represemtation
    of an object.

        Args:
        my_obj: Object.
    """
    return json.dumps(my_obj)
