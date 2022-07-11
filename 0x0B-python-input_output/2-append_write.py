#!/usr/bin/python3
"""
This module consists of a function that appends
a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file.

    Args:
        filename: File to be modified.
        text: Text to be appended into file.
    """
    with open(filename, 'a', encoding='utf-8') as file_r:
        if not filename:
            file_r = open(filename, 'w', encoding='utf-8')
        return file_r.write(text)
