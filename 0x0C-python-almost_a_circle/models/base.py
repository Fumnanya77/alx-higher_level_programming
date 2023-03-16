#!/usr/bin/python3
""" The Base of other classes in this project """
def Base():
    __nb_objects = 0
    def __init__(self, id):
        if self.id != "None":
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
