#!/usr/bin/python3
class Square:
    """
    A Class Square thatis defined my size.
    """
    def __init__(self, size = 0):
        """
        The method that initializes the square object.
        """ 
        if not isinstance(size, int):
            raise TypeError("The size must be an integer")
        elif size < 0:
            raise ValueError("The size must be >= 0")
        else:
            self.__size = size 

    def area(self):
        """
        The method that returns the area of a square object
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        The method to return the size of a square object.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The method sets the size value of a square object
        """
        if not isinstance(size, int):
            raise TypeError("The size must be an integer")
        elif size < 0:
            raise ValueError("The value of size must be>= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        The method prints a square with # according to the sizevalue.
        """
        if not self.__size = value:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end ='')
                print()
