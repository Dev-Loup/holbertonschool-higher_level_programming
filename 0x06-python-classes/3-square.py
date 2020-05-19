#!/usr/bin/python3
""" Class Square creation module
    A Blueprint for squares
"""


class Square:
    """Set the class square"""

    def __init__(self, size=0):
        """Iniatiate Attributes for Square class.
        Args:
          size: integer with size of the square.
        Raises:
          ValueError: if size is lesser than 0.
          TypeError: if size is not an integer.
        """

        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Square Area method.
        Return:
          The Area of the square.
        """

        return self.__size ** 2
