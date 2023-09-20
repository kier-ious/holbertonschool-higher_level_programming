#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """Checking if the text is a str"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    space_flag = "non_space"

    """Iterate through each line"""
    for char in text:
        if space_flag == "non_space":
            if char == " ":
                """Skips consectutive spaces"""
                continue
            else:
                """Prints non_space char and changes flag"""
                print(char, end="")
                space_flag = "space"
        else:
            if char in (".", "?", ":"):
                """Prints special char w/ 2 \n"""
                print(f"{char}", end="\n\n")
                space_flag = "non_space"
            else:
                """Prints non special char"""
                print(f"{char}", end="")
