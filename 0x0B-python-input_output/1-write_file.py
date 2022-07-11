#!/usr/bin/python3
"""
This module contains a functions that writes a string to a text file.
"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file.

    Args:
        filename: file to be written to.
        text: Text to be written in file.
    """
    with open(filename, 'w', encoding='utf-8') as file_r:
        return file_r.write(text)
