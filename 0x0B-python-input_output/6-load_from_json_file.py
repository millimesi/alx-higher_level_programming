#!/usr/bin/python3
'''
File handling project
'''

import json


def load_from_json_file(filename):
    ''' function that load json from file text file'''
    with open(filename, "r+") as f:
        return json.load(f)
