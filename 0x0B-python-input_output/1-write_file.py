#!/usr/bin/python3
""" This module is about writimg to a `file`. """


def write_file(filename="UTF8", text=""):
    """ This writes to a `file`.

    This `function` should overwrite an existing `file`, and should create a
    new `file` if not existing.

    args:
        filename: The `file` to be written to
        text: The `text` that would be written to the file
    """
    with open(filename, 'w', encoding="utf-8") as _file:
        file_write = _file.write(str(text))
    return file_write
