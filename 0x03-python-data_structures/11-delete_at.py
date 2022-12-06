#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(len(my_list)):
        if idx < 0 or idx >= len(my_list):
            return my_list
        elif i == idx:
            del my_list[i]
    return my_list
