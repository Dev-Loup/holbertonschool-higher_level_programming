#!/usr/bin/python3
""" Rectangle module
    Creates Rectangles
    Classes:
        Rectangle: set Rectangle parameters
"""

from models.base import Base


class Rectangle(Base):
    """ Rectangle class
        (arg) defines the argument treated
        Pub methods:
            set_(arg): setter & getter for
                attributes
            area(): returns area value
            display(): prints a rectangle draw with #
            update(): update class with args or kwargs
            to_dictionary(): returns a kwarg dictionary from instance
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Rectangle Class constructor
            Args:
                width: first size
                height: second size
                x: first position
                y: second position
                id: identification
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def set_width(self):
        """ get width from class
        """

        return self.__width

    @property
    def set_height(self):
        """ get height from class
        """

        return self.__height

    @property
    def set_x(self):
        """ get x from class
        """

        return self.__x

    @property
    def set_y(self):
        """ get y from class
        """

        return self.__y

    @set_width.setter
    def set_width(self, width):
        """ get width from class
            Args:
                width: value to set
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @set_height.setter
    def set_height(self, height):
        """ get height from class
            Args:
                height: value to set
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @set_x.setter
    def set_x(self, x):
        """ get x from class
            Args:
                x: value to set
        """

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @set_y.setter
    def set_y(self, y):
        """ get y from class
            Args:
                y: value to set
        """

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ calculates rectangle area
            Return: Area value
        """
        return self.__width * self.__height

    def display(self):
        """ print the rectangle with #
            representation.
        """

        for line in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """ Print default definition
            Return: predefined string
        """

        return "[Rectangle]"\
               "({}) {}/{} - {}/{}".format(self.id,
                                           self.__x,
                                           self.__y,
                                           self.__width,
                                           self.__height)

    def display(self):
        """ Print a Rectangle with
            position management
            Args:
            self.__x: X axis
            self.__y: Y axis
            self.__width: first size
            Self.__height: second size
        """
        if self.__y > 0:
            print("\n" * self.__y, end="")
        for line in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        setter = ['id', 'set_width',
                  'set_height',
                  'set_x',
                  'set_y']
        if args:
            for counter, arg in enumerate(args):
                setattr(self, setter[counter], arg)
        else:
            for key, value in kwargs.items():
                if key != 'id':
                    attr_key = "set_" + key
                else:
                    attr_key = key
                setattr(self, attr_key, value)

    def to_dictionary(self):
        """ Returns a dictionary of
            the class
        """

        return {'id': self.id,
                'width': self.set_width,
                'height': self.set_height,
                'x': self.set_x,
                'y': self.set_y}
