#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) < 123:
            i = chr(ord(i) - (97 - 65))
        print("{}".format(i), end="")
    print("")
