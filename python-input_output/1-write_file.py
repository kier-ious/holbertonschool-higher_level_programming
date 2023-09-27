#!/usr/bin/python3
"""Write a func that writes a str to txt and returns # of chars"""


def write_file(filename="", text=""):
    """Reads txt file, prints to stdout"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
