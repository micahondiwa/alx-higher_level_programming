#!/usr/bin/python3
"""A module containing a square"""


class Square:
    """A square class"""

    def __init__(self, size=0):
        """initializes square
        Args:
            size (int): size of the square
        """

        self.size = size

    @property
    def size(self):
        """Gets value of size
        Returns:
            size (int)
        """

        return self.__size

    @size.setter
    def size(self, value):
        """ Change the value of size
        Args:
            value (int): new value of size
        """

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculates the area of a square
        Returns:
            area
        """

        return self.__size * self.__size

    def my_print(self):
        """Print a square"""

        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
