#!/usr/bin/python3
"""
Module that adds all arguments to a Python list, and then
save them into a file.
"""
import sys
import os.path


file_save = __import__('5-save_to_json_file').save_to_json_file
file_load = __import__('6-load_from_json_file').load_from_json_file

my_list = []
if os.path.exists("add_item.json"):
    my_list = file_load("add_item.json")

for arg in sys.argv[1:]:
    my_list.append(arg)

file_save(my_list, "add_item.json")
