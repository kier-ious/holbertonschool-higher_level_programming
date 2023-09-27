#!/usr/bin/python3
"""Append a file"""


def append_file(filename="", text=""):
    """write str to txt file, returns #"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
