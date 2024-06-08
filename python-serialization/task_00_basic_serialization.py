#!/usr/bin/python3
"""Task"""


import json


def serialize_and_save_to_file(data, filename):
    """Def"""
    with open(filename, 'w') as f:
        json.dump(data, f)
    pass

def load_and_deserialize(filename):
    """Def"""
    with open(filename. r) as f:
        return json.load(f)
    pass
