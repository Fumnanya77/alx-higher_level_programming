#!/usr/bin/python3
def no_c(my_string):
    my_string = my_string.translate({ord('C'): None})
    my_string = my_string.translate({ord('c'): None})
    return my_string[:len(my_string)]
