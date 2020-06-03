#!/usr/bin/python3
""" Module square morphing from
    rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class with Rectangle base
    """

    def __init__(self, size):
        """ Define the new Square
            Args:
                Size: length value
        """

        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)
