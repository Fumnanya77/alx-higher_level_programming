#!/usr/bin/python3
def max_integer(my_list=[]):
    temp = 0
    if len(my_list) == 0:
        temp = None
    for i in range(len(my_list)):
        if my_list[i] > temp:
            temp = my_list[i]
        elif my_list[i] < 0 and my_list[i+1] < 0 and temp <= 0:
            if my_list[i] < temp:
                temp = my_list[i]
        else:
            continue
    return temp
