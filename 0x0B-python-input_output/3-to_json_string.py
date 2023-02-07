#!/usr/bin/python3
""" `JSON` representation of objects """


import json
def to_json_string(my_obj):
    """ This shows the json string representsion of objects.

    args:
        my_obj: the object to be passed to json string
    """
    json_string_ = json.dumps(my_obj)
    return json_string_
