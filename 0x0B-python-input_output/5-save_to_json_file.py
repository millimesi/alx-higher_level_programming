#!/usr/bin/python3
'''
File handling project
'''

import json


def save_to_json_file(my_obj, filename):
    ''' function that write json representation to text file'''
    with open(filename, "w") as f:
        json.dump(my_obj, f)
