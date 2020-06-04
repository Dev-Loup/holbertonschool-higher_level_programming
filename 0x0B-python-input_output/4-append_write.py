#!/usr/bin/python3
""" Writing new files module
    Functions:
        write_file: write a file
"""


def write_file(filename="", text=""):
    """ Write a new file
        Args:
            filename: string containing the name or "" if
            not given.
            text: content of the file
        Return: number of chars written
    """

    with open(filename, 'w', encoding='utf8') as fl_opened:
        return fl_opened.write(text)
