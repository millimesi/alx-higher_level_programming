#!/usr/bin/python3
""" Test my code using doctests"""


def square_area(side=0):
    """Finds the area a circle for the given radius
    >>> square_area()
    0
    >>> square_area(2)
    4
    >>> square_area("h")
    Traceback (most recent call last):
    TypeError: incorrect value
    """
    if type(side) not in [int, float]:
        raise TypeError("incorrect value")
    if side < 0:
        raise ValueError("side can not be negative")
    return side ** 2
