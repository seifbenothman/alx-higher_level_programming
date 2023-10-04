#!/usr/bin/python3
def remove_char_at(str, n):
    modif = ""
    for x in range(len(str)):
        if x == n:
            continue
        else:
            modif += str[x]
      return (modif)
