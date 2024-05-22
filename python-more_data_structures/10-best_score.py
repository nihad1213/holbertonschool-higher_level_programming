#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_val = max(a_dictionary.values())
        return max_val
    else:
        return None
