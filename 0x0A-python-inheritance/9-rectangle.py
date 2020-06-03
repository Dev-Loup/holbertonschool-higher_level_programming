#!/usr/bin/python3
""" Class declaration module
    classes:
        Rectangle: Class made from baseGeometry
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class rectangle based on BaseGeometry
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Calculate rectangle area
            Return:
                Result of area
        """

        return self.__width * self.__height

    def __str__(self):
        """ Print Rectangle sizes
            Return:
                [Rectangle] <width>/<height>
        """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
