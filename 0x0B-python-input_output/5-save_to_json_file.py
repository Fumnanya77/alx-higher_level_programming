#!/usr/bin/python3
""" This module saves to a `JSON` file """


import json
def save_to_json_file(my_obj, filename):
    """ This `function` saves an object to a `JSON` file

    args:
        my_obj: The `object` to be saved to the `JSON` file
        filename: The `JSON` file it will be saved on
    """
    with open(filename, 'w', encoding="utf-8") as fj:
        json_file = json.dump(my_obj, fj)
    return json_file
