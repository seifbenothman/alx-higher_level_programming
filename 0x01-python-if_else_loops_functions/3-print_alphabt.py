#!/usr/bin/python3
for gp in range(97, 123):
    if gp in [101, 113]:
        continue
    print("{}".format(chr(gp)), end="")
