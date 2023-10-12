#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    add = {}
    for key, value in a_dictionary.items():
        add[key] = value * 2
    return add
