#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Checking if the text is a str"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """Split the text into lines"""
    lines = text.splitlines()
    result = []

    """Iterate through each line"""
    for line in lines:
        """Remove trailing white space"""
        line = line.strip()
        if line:
            result.append(line)

    """Print the new lines with extra newlines"""
    for i, line in enumerate(result):
        """Adding newlines with sentences that have these special characters"""
        if i > 0 and (line.endswith(".", "?", ":")):
            print()
        print(line)
