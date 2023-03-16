#!/usr/bin/python3
""" This module is about adding two integers

    It should be explicit on what to add and not add.
"""


def add_integer(a, b=98):
    """ This function adds two floats or integers """

    if a or b:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        else:
            a = int(a)
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        else:
            b = int(b)
    else:
        raise TypeError("add_integer() missing 1 required argument: 'a'")
    return(a + b)
