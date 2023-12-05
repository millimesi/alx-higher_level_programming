#!/usr/bin/python3
'''
File handling project
'''

import json


def from_json_string(my_str):
    ''' function that deseralize a data structure'''
    return json.loads(my_str)
