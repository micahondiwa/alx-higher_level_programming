#!/usr/bin/python3
'''Definig class Rectangle'''


class Rectangle:
    '''A class Rectangle with private attributes 
    width and height. Both width and height 
    must be integers'''
    def __init__(self, width, height):
        if not isinstance(width, height, int):
            raise TypeError('width and height must be an integer')
        elif width and height < 0:
            raise ValueError('height and width must be >= 0')
        else:
            self.__width = int(width)
            self.__height = int(height)
