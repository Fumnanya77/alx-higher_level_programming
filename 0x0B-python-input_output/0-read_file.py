#!/usr/bin/python3
""" This module is about reading 4rm a specified `file`. """


def read_file(filename="UTF8"):
    """ This `function` reads a `file` using `with`to enable closing

    args:
        filename: The name of the `file` that would be read
    """
    with open(filename, 'r', encoding="utf-8") as _file:
        file_read = _file.read()
        print(file_read)
    return file_read
