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
