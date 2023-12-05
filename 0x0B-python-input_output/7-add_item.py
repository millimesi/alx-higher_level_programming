#!/usr/bin/python3
'''
File handling project
'''

import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__(
        "6-load_from_json_file"
        ).load_from_json_file

    try:
        arg_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        arg_list = []
    arg_list.extend(sys.argv[1:])
    save_to_json_file(arg_list, "add_item.json")
