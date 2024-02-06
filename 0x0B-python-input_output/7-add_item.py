#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys


from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

try:
    items_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    items_list = []

items_list.extend(sys.argv[1:])
save_to_json_file(items_list, "add_item.json")
