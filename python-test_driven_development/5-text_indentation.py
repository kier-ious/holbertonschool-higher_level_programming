#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Checking if the text is a str"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    print()
