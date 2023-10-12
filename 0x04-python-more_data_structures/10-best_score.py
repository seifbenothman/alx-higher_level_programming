#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = 0
    s = ""
    for key, value in a_dictionary.items():
        if value > best:
            best = value
            s = key
    return s
