#!/usr/bin/python3
"""Sepultura - Roots bloody roots"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Init"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
