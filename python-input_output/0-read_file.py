#!/usr/bin/python3

def read_file(filename=""):
    """function read and print file"""
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
