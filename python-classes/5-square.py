#!/usr/bin/python3
"""shows Square class"""


class Square:
    """It show cases a square"""
    def __init__(self, size=0):
        """set the square size
        Args:
            size (int, optional): the square size measure
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """The area of the square property is returned."""
        return self.__size ** 2

    @property
    def size(self):
        """obtain the square property"""
        return self.__size

    @size.setter
    def size(self, size):
        """set size property
        Args:
            size (int): represent the new size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """# displays the square area on stdout"""
        i = 0
        if self.__size == 0:
            print("")
        else:
            while i < self.__size:
                print("#" * self.__size)
                i += 1
