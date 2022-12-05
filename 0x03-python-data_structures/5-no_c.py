#!/usr/bin/python3
def no_c(my_string):
#    for i in range(0, len(my_string)):
#if my_string[i] != 'c' or my_string[i] != 'C':
#        print(my_string[i])
#    new_string = [print(my_string[i]) for i in range(0, len(my_string))]
    my_string = my_string.translate({ord('C'):None})
    my_string = my_string.translate({ord('c'):None})
    return my_string[:len(my_string)]
