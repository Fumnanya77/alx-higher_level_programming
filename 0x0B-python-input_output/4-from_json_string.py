#!/usr/bin/python3
""" Decode a `JSON` strong """


import json


def from_json_string(my_string):
    """ Decodong a `JSON` string

    args:
        my_string: the json string
    """
    json_obj = json.loads(my_string)
    return json_obj
