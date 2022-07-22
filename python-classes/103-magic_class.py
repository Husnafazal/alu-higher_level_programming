#!/usr/bin/python3
"""Show a MagicClass complementing completely a bytecode provided by Holberton."""

import math


class MagicClass:
    """Showcase a circle."""

    def __init__(self, radius=0):
        """Prompt a MagicClass.
        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Reinstate the dimensions of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Reinstate the perimeter of the MagicClass."""
        return (2 * math.pi * self.__radius)
