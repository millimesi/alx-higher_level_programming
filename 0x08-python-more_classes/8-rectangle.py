#!/usr/bin/python3
""" rectangle module with its clas"""


class Rectangle:
    """Empty rectangle class
    attributes:
        width(int): width
        height(int): width
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height
        args:
            width(int): width
            height(int): width
        """

        self.__width = width
        self.__height = height
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """property getter of width"""

        return self.__width

    @width.setter
    def width(self, value):
        """property of width
        arges:
            value: value to width
        """

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property getter of height"""

        return self.__height

    @height.setter
    def height(self, value):
        """property of height
        arges:
            value: value to height
        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area of the rectangle """

        return self.__height * self.__width

    def perimeter(self):
        """ returns the area of the rectangle """

        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """  returns the biggest rectangle based on the area"""

        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            else:
                return rect_2

    def __str__(self):
        """ returns informal nice string"""

        hash = ""
        for i in range(self.__height):
            for j in range(self.__width):
                hash += str(self.print_symbol)
            if i != (self.__height - 1):
                hash += '\n'
        return hash

    def __repr__(self):
        """ returns a string representation of the object """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """deletes an instance"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
