#!/usr/bin/python3
import sys

if __name__ == "__main__":
    add = 0
    for i in range(1, len(sys.argv)):
        add += int(sys.argv[1])
    print("{:d}".format(add))
