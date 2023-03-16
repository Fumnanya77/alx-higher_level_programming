#!/usr/bin/python3
""" This module is about making squares """

class Square:
    """ The square class

    The square class creates attributes and methods for performing \
    and performing arithemetic with squares

    """
    def __init__(self, size=0):
        """ The init documentation

        Args:
            size (int): Takes in the size of the sqaure to be created

        Attributes:
            size (int): Takes in the size of the sqaure to be created

        """
        self.__size = size
        try:
            while True
                type(self.__size) == type(int)
        except TypeError:
            print("size must be an integer")

        try:
            while True
                self.__size < 0
        except ValueError:
            print("size must be >= 0")
