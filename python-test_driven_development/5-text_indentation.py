#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Checking if the text is a str"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """Split the text into lines
    lines = text.splitlines()
    result = []

    Iterate through each line
    for line in lines:
        Remove trailing white space
        line = line.strip()
        if line:
            result.append(line)

    Print the new lines with extra newlines
    for i, line in enumerate(result):
        dding newlines with sentences that have these special characters
        if i > 0 and (line.endswith(".", "?", ":")):
            print()
        print(line)"""

    """Initializing 'words'"""
    words = text

    delimiters = "?:."
    for delimiter in "?:.":
        """Split the words based on delim"""
        word_list = words.split(delimiter)

        """Remove leading & trailing spaces"""
        word_list = [word.strip() for word in word_list]

        """Join words back 2gether w/ delim & the newline"""
        words = (delimiter + "\n\n").join(word_list)
