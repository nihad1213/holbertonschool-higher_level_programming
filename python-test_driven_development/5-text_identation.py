#!/usr/bin/python3
"""
    Balabey - Sessiz geceler
"""
def text_indentation(text):
    """Function"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        words = (delimeter + "\n\n").join(
                [index.strip(" ") for index in words.split(delimeter)])

