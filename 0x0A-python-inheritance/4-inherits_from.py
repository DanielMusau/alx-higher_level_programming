#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Fucntion that checks if object is an instance of a class
    that inherited from the specified class.
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
