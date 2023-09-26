#!/usr/bin/python3
"""Reading file, printing to stdout"""


def read_file(filename=""):
    """Reads txt file, prints to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
