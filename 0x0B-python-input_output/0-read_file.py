#!/usr/bin/python3
"""
This module consists of a function to read a file.
"""


def read_file(filename=""):
    """Functions that reads a text file (UTF*) and prints
       it to stdout.

       Args:
        filename: the file to be read.
    """
    with open(filename, 'r', encoding='utf-8') as file_r:
        print(file_r.read(), end='')
