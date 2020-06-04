#!/usr/bin/python3
""" Printing files module
    Functions:
        read_file: read a given file and
        print it
"""


def read_file(filename=""):
    """ Read and send the file to the standard output
        filename: string containing the name or "" if
        not given.
    """

    with open(filename, encoding="utf-8") as fl_opened:
        fl_written = fl_opened.read()
        print(fl_written, end='')
