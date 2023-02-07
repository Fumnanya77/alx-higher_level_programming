#!/usr/bin/python3
""" This module demonstrates loading objects `from` a `JSON` `file` """


import json


def load_from_json_file(filename):
    """ This `function` creates an object form a `JSON` `file`

    args:
        filename: This is the `JSON` `file` the object will be created from
    """
    with open(filename, 'r', encoding="utf-8") as fj:
        json_file_load = json.load(fj)
    return json_file_load
