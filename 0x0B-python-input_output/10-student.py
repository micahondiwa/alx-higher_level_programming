#!/usr/bin/python3
"""Write a class Student that defines a student by"""


class Student:
    def __init__(self, first_name, last_name, age):
        """This function init the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names contained in
        this list must be retriev"""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for i in attrs:
            if i in self.__dict__ and type(i) is str:
                my_dict[i] = self.__dict__.get(i)

        return my_dict
