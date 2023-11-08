#!/usr/bin/python3
"""
Returns true if obj is instance of class that it inherits from or is subcls of
"""


def inherits_form(obj, a_class):
    """
    Return:
    true if obj is instance of class that it inherits from or is subcts of
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
