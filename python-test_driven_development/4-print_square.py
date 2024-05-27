#!/usr/bin/python3
"""
    Sagopa Kajmer - BPG(2003)
"""


def print_square(size):
    """Print squar"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("x" * size)
