#!/usr/bin/python3
'''A class Square, defined by size'''


class Square:
    '''A Class called Square, defined by size'''
    def __init__(self, size=0):
        if  not instance(size, int):
            raise TypeError("The size myst be an integer")
        elif size < 0:
            raise ValueError("The size must be >= 0")
        else:
            self.__size = size

    '''The method returns the area of a square'''

    def area(self):
        return (self.__size ** 2)

    '''The method returns the size of a square'''
   @property
    def size(self):
    
    '''The method sets the value of a square'''
    @size.setter
    def size(size, value):
        if not isinstance(value, int):
            raise TypeError("The size must be an integer")
        elif value < 0:
            raise ValueError("The size must be >= 0")
        else:
            self.__size = value
