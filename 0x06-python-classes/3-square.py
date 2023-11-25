#!/usr/bin/python3
''' Define Empty Class'''


class Square:
    """my square class.
    Atrributes:
    __size(int): size of the square
    """
    def __init__(self, size=0):
        """ initialization method
        args:
            size (int): size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
