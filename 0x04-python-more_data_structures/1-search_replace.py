#!/usr/bin/python3
def search_replace(my_list, search, replace):
    add = my_list.copy()
    for i in range(len(add)):
        if add[i] == search:
            add[i] = replace
    return add
