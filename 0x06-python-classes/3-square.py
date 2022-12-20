#!/usr/bin/python3
class Square:
    """
    A calss Square, defined by the size attribute
    """" 
    def __init__(self, size = 0)
    """
    Initializing the Object in the Square class
    """
        if not isinstance(size, int):
            raise TypeError("The size of x must be an integer")
        elif size < 0:
            raise ValueError("The size of x must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        The area method calculates the area of a Square object
        """
        return (self.__size ** 2)
