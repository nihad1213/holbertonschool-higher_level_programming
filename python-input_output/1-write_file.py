#!/usr/bin/python3
"""Python"""


def write_file(filename="", text=""):
    """Write ti a file"""
    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
