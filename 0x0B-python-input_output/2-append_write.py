#!/usr/bin/python3
""" This module is about appending to an existing or non-existing `file`. """


def append_write(filename="UTF8", text=""):
    """ This appends to a `file`.

    This `function` should not overwrite an existing `file`, and should
    create a new `file` if not existing.

    args:
        filename: The `file` to be written to
        text: The `text` that would be written to the file
    """
    with open(filename, 'a', encoding="utf-8") as _file:
        file_append = _file.write(str(text))
    return file_append
