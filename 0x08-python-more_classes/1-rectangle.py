#!/usr/bin/python3
""" Creating an empty rectangle class """


class Rectangle(object):
    """ The class module """

    def __init__(self, width=0, height=0):
        """ Defining the rectangle.
            
		The attributes are width and rectangle

		Args:
            width(int): the size of the rectangle
			height(int): the other side of the shape

    """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) == False:
            raise TypeError("width must be an integer")
        else:
            self.__width = value
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) == False:
            raise TypeError("height must be an integer")
        else:
            self.__height = value
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
