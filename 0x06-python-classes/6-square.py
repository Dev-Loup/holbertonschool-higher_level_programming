#!/usr/bin/python3
""" Class Square creation module
    A Blueprint for squares
"""


class Square:
    """Set the class square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiate Attributes for Square class.
        Args:
          size: integer with size of the square.
          position: tuple of square location
        """

        self.size = size
        self.position = position

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
        if self.size != 0:
            if self.position[1] is not 0:
                print("" * self.position[1])
            for X in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
        else:
            print()

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
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """Get position value.
        Return:
          gotten position
        """

        return self.__position

    @position.setter
    def position(self, value):
        """Set position value.
        Args:
          value: data of position
        """

        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int and type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value
