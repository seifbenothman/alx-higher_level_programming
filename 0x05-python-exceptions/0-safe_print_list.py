#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            count = count + 1
        except TypeError:
            break
    print("")
    return count
