#!/usr/bin/python3
"""
Module of Base Geometry
"""


class BaseGeometry:
    """
    BaseGeometery class hass started
    has one method area
    """
    def area(self):
        """
        raise expectation
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        that validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        instantiation
        args:
            width: rectangle side 1
            height: rectangle side 2
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        implements area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        returns a string representation of the object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
