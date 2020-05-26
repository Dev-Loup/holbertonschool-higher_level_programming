#!/usr/bin/python3
"""Form module
"""


class Rectangle:
    """Class Rectangle
    Private instance attributes:
        width: defines base parameter
        height: defines height parameter
    Public instance attributes:
        number_of_instances: instance counter
    """

    number_of_instances = 0
    print_symbol = "#"

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
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates rectangle area
           Return:
            area calculation
        """

        return self.__height * self.__width

    def perimeter(self):
        """Calculates rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            perim = 0
        else:
            perim = (self.__height + self.__width) * 2
        return perim

    def __str__(self):
        """ set rectangle with #
        """
        draw = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for Y in range(self.__height):
            draw += (str(self.print_symbol) * self.__width)
            if Y < (self.__height - 1):
                draw += "\n"
        return draw

    def __repr__(self):
        """ Returns string representation
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Set a square
        """
        return cls(size, size)
