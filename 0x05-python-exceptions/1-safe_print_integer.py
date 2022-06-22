#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == int:
            return True
    except ValueError:
        return False
