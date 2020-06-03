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
        """instantion method
            Private class Attributes:
                width: base of Rectangle
                Height: height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
