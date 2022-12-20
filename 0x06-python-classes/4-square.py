#!/usr/bin/python3
class Square:
    """
    A Class called Square, defined by size
    """
    def __init__(self, size = 0);
        """
        The method that initalizes a sqauer object-an instance of a Square class.
        """
        if  not instance(size, int):
            raise TypeError("The size myst be an integer")
        elif size < 0:
            raise ValueError("The size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        The method returns the area of a square object.
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        The method returns the size of a square.
       """

    @size.setter
    def size(size, value):
        """
       The method that sets the value of the size of a Square.
        """
        if not isinstance(value, int):
            raise TypeError("The size must be an integer")
        elif value < 0:
            raise ValueError("The size must be >= 0")
        else:
            self.__size = value
