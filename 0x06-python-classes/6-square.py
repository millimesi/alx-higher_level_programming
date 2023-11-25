#!/usr/bin/python3
''' Define square Class'''


class Square:
    """my square class.
    Atrributes:
    __size(int): size of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ initialization method
        args:
            size (int): size of the square
            position (int tuple): int tuple position
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if ((len(position) != 2) or type(position[1]) != int or
                type(position[0]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position"""
        if ((len(value) != 2) or type(value[1]) != int or
                type(value[0]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """returns the area of the square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
