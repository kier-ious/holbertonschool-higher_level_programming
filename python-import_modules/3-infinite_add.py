#!/usr/bin/python3
import sys

def infinite_addition(arguments):
    total = sum(int(arg))
    for arg in arguments:
        print(total)

if __name__ == "__main__":
    args = sys.argv[1:]
    infinite_addition(args)
