#!/usr/bin/python3
"""Form module
"""


class Rectangle:
    """Class Rectangle
    Private instance attributes:
        width: defines base parameter
        height: defines height parameter
    """

    def __init__(self, width=0, height=0):
        """Attributes initiation
        Args:
            width: rectangle base
            Height: rectangle height
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
            TypeError: height must be an integer
            ValueError: height must be >= 0
        self.width = width
        self.height = height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width for private instance
        """

        return self.__width

    @property
    def height(self):
        """Get height for private instance
        """

        return self.__height

    @width.setter
    def width(self, value):
        """ set width value on class
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height value on class
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
