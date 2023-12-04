#!/usr/bin/python3
"""
Module with function"""


def inherits_from(obj, a_class):
    """ check if an object has inherited form the class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
