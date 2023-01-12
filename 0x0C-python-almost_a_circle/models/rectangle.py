#!/usr/bin/python3
'''Defining the Base class'''


class Base:



    __nb_object = 0

    def __init__(self, width, height, x = 0, y = 0, id = None):
        self.width = width
        self.height = height
        self.x = x 
        self.y = y
        self.id = id
