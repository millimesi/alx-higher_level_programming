#!/usr/bin/python3
''' function that adds 2 integers
'''


def add_integer(a, b=98):
    """Accepts only float and integer arguments and add them
    args:
        a: num1
        b: num2
    return:
        a + b
    """

    if (type(a) not in [int, float]):
        raise TypeError("a must be an integer")
    if (type(b) not in [int, float]):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
