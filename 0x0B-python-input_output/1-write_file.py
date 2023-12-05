#!/usr/bin/python3
'''
File handling project
'''


def write_file(filename="", text=""):
    ''' function that writes a text file'''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
