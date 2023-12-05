#!/usr/bin/python3
'''
File handling project
'''


def read_file(filename=""):
    ''' function that reads a text file'''
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())
