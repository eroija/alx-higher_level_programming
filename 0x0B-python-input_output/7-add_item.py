#!/usr/bin/python3
"""
This script adds all arguments to a Python list
"""
import sys
import os


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = 'add_item.json'
length = len(sys.argv)

if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []


if length != 1:
    for i in range(1, length):
        my_list.append(sys.argv[i])

save_to_json_file(my_list, filename)
