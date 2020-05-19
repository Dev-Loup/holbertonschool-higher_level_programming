#!/usr/bin/python3
""" Class Square creation with size attributes.
"""


class Square:
    """Class Square declaration based on size.
       Function requires to be provided with a correct size int.
    """
    def __init__(self, size):
        """initialize Square size.

        Args:
          size: the size of the square.
        """
        self.__size = size
