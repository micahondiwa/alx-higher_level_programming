#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list, and then save
   them to a file:
        *If the file doesnt exist, it should be created
"""
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    my_items = load_from_json_file(filename)

except FileNotFoundError:
    my_items = []
for i in range(1, len(argv)):
    my_items.append(argv[i])

save_to_json_file(my_items, filename)
