#!/usr/bin/python3
"""
class
"""


def inherits_from(obj, a_class):
    """
    determine a class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
