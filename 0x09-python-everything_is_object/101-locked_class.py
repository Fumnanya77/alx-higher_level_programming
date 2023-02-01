#!/usr/bin/python3
"""Creating a locked class.

Creation of a class that restricts the creation of new instance attributes

"""


class LockedClass():
    """ The locked class"""
    __slots__ = ['first_name']

    def __init__(self):
        """ the instance method """
        first_name = ""
