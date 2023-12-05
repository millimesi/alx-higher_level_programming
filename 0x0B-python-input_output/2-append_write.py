#!/usr/bin/python3
'''
File handling project
'''


def append_write(filename="", text=""):
    ''' function that appends a text file'''
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
