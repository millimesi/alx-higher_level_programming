#!/usr/bin/python3
"""Module with look up function"""


def lookup(obj):
    """
    args:
        obj: object to be look up
    return:
        list of available attributes and methods of an object
    """

    return dir(obj)
