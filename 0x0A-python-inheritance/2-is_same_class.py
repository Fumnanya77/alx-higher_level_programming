#!/usr/bin/python3
""" The module will contain function that return true if an object is exactly

    the instance of a class
"""


def is_same_class(obj, a_class):
    """ The functions that computes the instances """
    if type(obj) == a_class:
        return True
    else:
        return False
