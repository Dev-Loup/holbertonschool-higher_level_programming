#!/usr/bin/python3
""" Writing new files module
    Functions:
        append_write: write a file or append if exists
"""


def append_write(filename="", text=""):
    """ Write a new file or append info if exists
        Args:
            filename: string containing the name or "" if
            not given.
            text: content of the file
        Return: number of chars written
    """

    with open(filename, 'a', encoding="utf-8") as fl_opened:
        return fl_opened.write(text)
