#!/usr/bin/python3
"""Holy Wars"""


import json

def load_from_json_file(filename):
    """Pantera - Walk"""
    with open(filename, 'r', encoding="utf-8") as file:
        object_o = json.load(file)
        return object_o
