#!/usr/bin/python3
'''A module Square, defined by size'''


class Square:
    '''A Class called Square, defined by size'''
    
    def __init__(self, size=0):
        '''Initializes square. 
        Args: size (int); size of a square''''

        self.__size = size

    @property
    def size(self):
        '''The method sets the value of a square
        Returns: size (int)'''

        return self.__size

    @size.setter
    def size(size, value):
        '''Changes the value of size. 
        Args: value (int): new value of size'''
        if type(value) != int:
            raise TypeError("The size must be an integer")
        elif value < 0:
            raise ValueError("The size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Returns the area of a square. 
        Return: are'''

        return self.__size ** 2
