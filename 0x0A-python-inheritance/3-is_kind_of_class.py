#!/usr/bin/python3
""" The module will contain function that return true if an object is an

    instance of a class or the class inherited from a specified class and false
    if otherwise
"""


def is_kind_of_class(obj, a_class):
    """ The functions that computes the instances """
    if isinstance(obj, a_class):
        return True
    else:
        return False
