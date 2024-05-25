#!/usr/bin/python3
"""SOAD - Jet Pilot"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initialization method"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Calculate the area of the square"""
        return self.__size ** 2
