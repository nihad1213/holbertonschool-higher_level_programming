#!/usr/bin/python3
"""
    SOAD - Aerials
"""


def say_my_name(first_name, last_name=""):
    """ say_my_name """
    if type(first_name) is not str:
        raise TypeError("first_name must be string")
    if type(last_name) is not str:
        raise TypeError("last_name must be string")
    print("My name is {:s} {:s}".format(first_name, last_name))
