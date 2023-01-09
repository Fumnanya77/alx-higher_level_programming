#!/usr/bin/python3
"""python3 -c 'print(__import__("0-lookup").lookup.__doc__)'

    This fuction prints out the attributes and methods of an obect
"""

def lookup(obj):
    lup = print(dir(obj))
    return lup
