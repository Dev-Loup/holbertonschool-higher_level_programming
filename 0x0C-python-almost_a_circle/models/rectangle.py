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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width from class
        """

        return self.__width

    @property
    def height(self):
        """ get height from class
        """

        return self.__height

    @property
    def x(self):
        """ get x from class
        """

        return self.__x

    @property
    def y(self):
        """ get y from class
        """

        return self.__y

    @width.setter
    def width(self, width):
        """ get width from class
            Args:
                width: value to set
        """

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """ get height from class
            Args:
                height: value to set
        """

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """ get x from class
            Args:
                x: value to set
        """

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
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

        return self.width * self.height

    def display(self):
        """ print the rectangle with #
            representation.
        """

        for line in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """ Print default definition
            Return: predefined string
        """

        return "[Rectangle]"\
               "({}) {}/{} - {}/{}".format(self.id,
                                           self.x,
                                           self.y,
                                           self.width,
                                           self.height)

    def display(self):
        """ Print a Rectangle with
            position management
            Args:
            self.x: X axis
            self.y: Y axis
            self.width: first size
            Self.height: second size
        """

        if self.y > 0:
            print("\n" * self.y, end="")
        for line in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """ update a class square with
            args o kwargs
            Args:
                *args: no keyworded args
                **kwargs: keyworded args
        """

        setter = ['id', 'width',
                  'height',
                  'x',
                  'y']
        if args:
            for counter, arg in enumerate(args):
                setattr(self, setter[counter], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary of
            the class
        """

        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
