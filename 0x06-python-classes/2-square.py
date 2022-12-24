#!/usr/bin/python3
'''Defining a class Square'''


class Square:
    '''A class Square with a private attribute size.
     The size attribute must be an integer'''
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(size)
