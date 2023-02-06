#!/usr/bin/python3
""" The module will contain function that return true if an object is an

    instance of a class inherited directly or indirectly from a specified
    class and false if otherwise
"""


def inherits_from(obj, a_class):
    """ The functions that computes the instances """
    if issubclass(type(isinstance(issubclass(type(obj), a_class), a_class)), a_class):
        return True
    else:
        return False
