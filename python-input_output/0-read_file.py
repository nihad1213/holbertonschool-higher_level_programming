#!/usr/bin/python3
"""Python"""


def read_file(filename=""):
    """function read and print file"""
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
