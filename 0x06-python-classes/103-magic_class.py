#!/usr/bin/python3
"""Defines a magic class"""

import math


class MagicClass:
    """Class that stores the properties
     of a circumference"""

    def __init__(self, radius = 0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("Radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of the magicclass"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Returns the circumference of the magiccalss"""
        return (2 * math.pi * self.__radius)
