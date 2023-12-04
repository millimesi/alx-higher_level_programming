#!/usr/bin/python3
"""
Module with function
"""


class MyList(list):
    """class that ihherited list clas"""
    def print_sorted(self):
        """ print sorted list
        """
        print(sorted(self))
