#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number) % 10
    print(f"{n}", end="")
    return n
