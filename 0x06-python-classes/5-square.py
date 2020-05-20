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
        """

        self.__size = size

    @property
    def size(self):
        """Get the private size value.
        Return:
          self._size: value of size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Set size into class object.
        Args:
          value: size to check
        Raises:
          ValueError: if size is lesser than 0.
          TypeError: if size is not an integer.
        """

        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Square Area method.
        Return:
          The Area of the square.
        """

        return self.__size ** 2

    def my_print(self):
        """Printing method.
           My_print generates an # composed square
        """
        if self.__size > 0:
            for X in range(self.__size):
                print("#" * self.__size)
        else:
            print()
